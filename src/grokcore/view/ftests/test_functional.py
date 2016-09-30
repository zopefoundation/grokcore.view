import doctest
import os.path
import re
import unittest
from pkg_resources import resource_listdir

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi
from zope.testing import renormalizing
import grokcore.view


class Layer(
    zope.testbrowser.wsgi.TestBrowserLayer,
    zope.app.wsgi.testlayer.BrowserLayer):
    pass

layer = Layer(grokcore.view)


checker = renormalizing.RENormalizing([
    # Accommodate to exception wrapping in newer versions of mechanize
    (re.compile(r'httperror_seek_wrapper:', re.M), 'HTTPError:'),
    ])


def suiteFromPackage(name):
    files = resource_listdir(__name__, name)
    suite = unittest.TestSuite()
    getRootFolder = layer.getRootFolder
    globs = dict(http=zope.app.wsgi.testlayer.http,
                 getRootFolder=getRootFolder)
    optionflags = (
        renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2 +
        doctest.ELLIPSIS +
        doctest.NORMALIZE_WHITESPACE +
        doctest.REPORT_NDIFF)

    for filename in files:
        if filename == '__init__.py':
            continue

        test = None
        if filename.endswith('.py'):
            dottedname = 'grokcore.view.ftests.%s.%s' % (name, filename[:-3])
            test = doctest.DocTestSuite(
                dottedname,
                checker=checker,
                extraglobs=globs,
                optionflags=optionflags)
            test.layer = layer
        elif filename.endswith('.txt'):
            test = doctest.DocFileSuite(
                os.path.join(name, filename),
                optionflags=optionflags,
                globs=globs)
            test.layer = layer
        if test is not None:
            suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in [
            'contentprovider',
            'directoryresource',
            'static',
            'url',
            'view']:
        suite.addTest(suiteFromPackage(name))
    return suite
