"""

  >>> grok.testing.grok(__name__)

  >>> from zope.interface.verify import verifyObject
  >>> from grokcore.view.interfaces import IGrokView

We should find the ``cavepainting`` view for a mammoth:

  >>> manfred = Mammoth()
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> from zope import component
  >>> view = component.getMultiAdapter((manfred, request), name='cavepainting')
  >>> print view()
  A cave painting of a mammoth

  >>> view.context is manfred
  True
  >>> view.request is request
  True
  >>> verifyObject(IGrokView, view)
  True

"""

import grokcore.view as grok

class Mammoth(grok.Context):
    pass

class CavePainting(grok.View):
    template = grok.PageTemplate(filename='view_templates/cavepainting.pt')
