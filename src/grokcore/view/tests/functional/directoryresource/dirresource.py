"""
A directory resource defined without an explicit name direective is available
through the dotted name of the module in which the directoryresource is
defined::

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open(
  ...     'http://localhost/@@/'
  ...     'grokcore.view.tests.functional.directoryresource.fixture.resource/file.txt')
  >>> bprint(browser.contents)
  Foo resource file's content.

Directoryresource registrations can be differentiated based on layers (and
skins)::

  >>> browser.open(
  ...     'http://localhost/++skin++another/@@/'
  ...     'grokcore.view.tests.functional.directoryresource.fixture.resource/file.txt')
  >>> bprint(browser.contents)
  Anotherfoo resource file's content.

This resource is only available on the particular layer::

  >>> browser.open(
  ...     'http://localhost/++skin++another/@@/'
  ...     'grokcore.view.tests.functional.directoryresource.fixture.resource/'
  ...     'anotherfile.txt')
  >>> bprint(browser.contents)
  Anotherfoo resource anotherfile's content.

  >>> browser.handleErrors = True
  >>> browser.open(
  ...     'http://localhost/@@/'
  ...     'grokcore.view.tests.functional.directoryresource.fixture.resource/'
  ...     'anotherfile.txt')
  Traceback (most recent call last):
  ...
  urllib.error.HTTPError: HTTP Error 404: Not Found

Directoryresources can be registered under an explicit name::

  >>> browser.handleErrors = False
  >>> browser.open('http://localhost/@@/fropple/file.txt')
  >>> bprint(browser.contents)
  Bar resource file's content.

Subdirectories are published as directoryresources recusively::

  >>> browser.open('http://localhost/@@/fropple/baz/file.txt')
  >>> bprint(browser.contents)
  Baz resource file's content.

A relative path to a directory with resources::

  >>> browser.open('http://localhost/@@/frepple/file.txt')
  >>> bprint(browser.contents)
  Baz resource file's content.

An absolute path to a directory with resources::

  >>> browser.open('http://localhost/@@/frupple/file.txt')
  >>> bprint(browser.contents)
  Baz resource file's content.

"""  # noqa: E501 line too long
