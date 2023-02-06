"""
Make sure that only interfaces extending IBrowserRequest can be
registered as a skin:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  martian.error.GrokError: The grok.skin() directive is used on interface\
  'grokcore.view.tests.base.skin.notonlayer.NotALayer'. However,\
  'grokcore.view.tests.base.skin.notonlayer.NotALayer' does not extend\
  IRequest which is required for interfaces that are used as\
  layers and are to be registered as a skin.
"""
from zope.interface import Interface

import grokcore.view as grok


class NotALayer(Interface):
    grok.skin('not a layer')
