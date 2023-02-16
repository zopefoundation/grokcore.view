"""
Views have a method that can be used to construct URLs:

  >>> from zope.site.folder import Folder
  >>> herd = Folder()
  >>> getRootFolder()['herd'] = herd
  >>> manfred = Mammoth()
  >>> herd['manfred'] = manfred

The views in this test implement self.url():

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/herd/manfred/index")
  >>> print(browser.contents)
  http://localhost/herd/manfred/index
  >>> browser.open("http://localhost/herd/manfred/another")
  >>> print(browser.contents)
  http://localhost/herd/manfred/another
  >>> browser.open("http://localhost/herd/manfred/yetanother")
  >>> print(browser.contents)
  http://localhost/herd/manfred/yetanother

We get the views manually so we can do a greater variety of url() calls:

  >>> from zope import component
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> index_view = component.getMultiAdapter((manfred, request), name='index')
  >>> index_view.url()
  'http://127.0.0.1/herd/manfred/index'
  >>> another_view = component.getMultiAdapter((manfred, request),
  ...                                              name='another')
  >>> another_view.url()
  'http://127.0.0.1/herd/manfred/another'
  >>> yet_another_view = component.getMultiAdapter((manfred, request),
  ...                                              name='yetanother')
  >>> yet_another_view.url()
  'http://127.0.0.1/herd/manfred/yetanother'

Now let's get a URL for a specific object:

  >>> index_view.url(manfred)
  'http://127.0.0.1/herd/manfred'

This works with any other view too (as they share the same request):

  >>> another_view.url(manfred)
  'http://127.0.0.1/herd/manfred'

This shows that the default argument is the view itself:

  >>> another_view.url(another_view)
  'http://127.0.0.1/herd/manfred/another'

We can get the URL for any object in content-space:

  >>> another_view.url(herd)
  'http://127.0.0.1/herd'

We can also pass a name along with this, to generate a URL to a
particular view on the object:

  >>> another_view.url(herd, 'something')
  'http://127.0.0.1/herd/something'

It's also possible to just pass in a name. In this case, a URL to that
view on the context object will be constructed:

  >>> another_view.url('yet_another_view')
  'http://127.0.0.1/herd/manfred/yet_another_view'

The url() method supports a data argument which is converted to a CGI
type query string. If any of the values are of type unicode it's
converted to a string assuming the encoding is UTF-8.

There is some object/name/data resolution code available that provides
the magic to make mixing of positional arguments and keyword arguments
work.

This is the key word argument signature::

  >>> index_view.url(herd, '@@sample_view', data=dict(age=28))
  'http://127.0.0.1/herd/@@sample_view?age=28'
  >>> index_view.url(herd, data=dict(age=28))
  'http://127.0.0.1/herd?age=28'
  >>> index_view.url('@@sample_view', data=dict(age=28))
  'http://127.0.0.1/herd/manfred/@@sample_view?age=28'
  >>> index_view.url(data=dict(age=28))
  'http://127.0.0.1/herd/manfred/index?age=28'

There is no problem putting one of the 'reserved' arguments inside the data
argument or explicitely supplying 'None':

  >>> index_view.url(herd, None, data=dict(name="Peter"))
  'http://127.0.0.1/herd?name=Peter'

Since order in dictionairies is arbitrary we'll test the presence of multiple
keywords by using find()

  >>> url = index_view.url('sample_view', data=dict(a=1, b=2, c=3))
  >>> url.find('a=1') > -1
  True
  >>> url.find('b=2') > -1
  True
  >>> url.find('c=3') > -1
  True

It works properly in the face of non-ascii characters in URLs:

  >>> last_path = 'árgh'
  >>> url = another_view.url(herd, last_path)
  >>> url
  'http://127.0.0.1/herd/%C3%A1rgh'
  >>> from urllib.parse import unquote
  >>> expected = 'http://127.0.0.1/herd/árgh'
  >>> u_unquoted = unquote(url)
  >>> u_unquoted == expected
  True

Some combinations of arguments just don't make sense:

  >>> another_view.url('foo', 'bar')
  Traceback (most recent call last):
    ...
  TypeError: url() takes either obj argument, obj, string arguments, or string\
  argument
  >>> another_view.url('foo', herd)
  Traceback (most recent call last):
    ...
  TypeError: url() takes either obj argument, obj, string arguments, or string\
  argument
  >>> another_view.url(herd, 'bar', data='baz')
  Traceback (most recent call last):
    ...
  TypeError: url() data argument must be a dict.

Since we're relying on urllib to do the CGI parameter encoding it's quite
smart but fails on unicode objects but url() is programmed to automatically
convert unicode to UTF-8 on the fly.

  >>> index_view.url(data={'name':u'Andr\xe9'})
  'http://127.0.0.1/herd/manfred/index?name=Andr%C3%A9'

As we're relying on urllib to do the url encoding, it also converts values that
are lists to repeated key value pairs such that key=[1,2] becomes key=1&key=2

  >>> index_view.url(data={'key':[1,2]})
  'http://127.0.0.1/herd/manfred/index?key=1&key=2'

We also make sure the values in the list that are unicode instances are encoded
properly:

  >>> result = index_view.url(data={'key':[u'\xe9',2]})
  >>> print(result)
  http://127.0.0.1/herd/manfred/index?key=%C3%A9&key=2

  >>> from urllib.parse import parse_qs
  >>> expected = 'é'
  >>> result = parse_qs(result.split('?')[1])['key'][0]
  >>> result == expected
  True

Zope magic!! Here we test casting parameters in the CGI query string:

  >>> result = index_view.url('multiplier', data={'age:int':1})
  >>> result
  'http://127.0.0.1/herd/manfred/multiplier?age%3Aint=1'

  >>> browser.open(result)
  >>> browser.contents
  '2'
  >>> browser.open('http://127.0.0.1/herd/manfred/multiplier?age=1')
  >>> browser.contents
  '11'

It is possible to compute URLs for specific skin names.

First show how a view registered for a view, will by default compute URLs
for that skin:

  >>> browser.open('http://127.0.0.1/++skin++urltesting/herd/manfred/@@test')
  >>> browser.contents
  "I'm on a url testing skin:
  http://127.0.0.1/++skin++urltesting/herd/manfred/test"

We get the views manually so we can do a greater variety of url() calls:

  >>> from zope.publisher.browser import applySkin
  >>> request = TestRequest()
  >>> applySkin(request, URLTestingSkin)
  >>> # Shifting names normally happens during URL traversal.
  >>> request._traversed_names = ['++skin++urltesting']
  >>> request.shiftNameToApplication()
  >>> index_view = component.getMultiAdapter((manfred, request), name='test')
  >>> index_view.url()
  'http://127.0.0.1/++skin++urltesting/herd/manfred/test'

Explicitely remove the skin part:

  >>> index_view.url(skin=None)
  'http://127.0.0.1/herd/manfred/test'

Use another skin:

  >>> index_view.url(skin=AnotherURLTestingSkin)
  'http://127.0.0.1/++skin++anotherurltesting/herd/manfred/test'

When providing a skin **name**, it will be injected in the URLs:

  >>> index_view.url(skin='foobar')
  'http://127.0.0.1/++skin++foobar/herd/manfred/test'

"""

from zope.container.contained import Contained

import grokcore.view as grok


class Mammoth(Contained):
    pass


grok.context(Mammoth)


class Index(grok.View):
    def render(self):
        return self.url()


class Another(grok.View):
    def render(self):
        return self.url()


class YetAnother(grok.View):
    pass


class Multiplier(grok.View):
    def update(self, age=0):
        self.age = age

    def render(self):
        return str(self.age * 2)


yetanother = grok.PageTemplate('<p tal:replace="view/url" />')


class URLTestingSkin(grok.IBrowserRequest):
    grok.skin('urltesting')


class AnotherURLTestingSkin(grok.IBrowserRequest):
    grok.skin('anotherurltesting')


class URLTestingViewOnASkin(grok.View):
    grok.layer(URLTestingSkin)
    grok.name('test')

    def render(self):
        return f"I'm on a url testing skin: {self.url()}"
