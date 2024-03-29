"""

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  zope.configuration.config.ConfigurationExecutionError:\
  martian.error.GrokError: Multiple possible ways to render view <class\
  'grokcore.view.tests.base.view.eitherviewtemplateequalorrender.CavePainting'>.\
  It has both a 'render' method as well as an associated template.

"""

import grokcore.view as grok


class Mammoth(grok.Context):
    pass


class CavePainting(grok.View):
    template = grok.PageTemplate(filename='templates/cavepainting.pt')

    def render(self):
        return "Cool I have a render method."
