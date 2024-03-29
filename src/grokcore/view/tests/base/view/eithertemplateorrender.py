"""
Only one, either a template, or render() can be specified:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  zope.configuration.config.ConfigurationExecutionError:\
  martian.error.GrokError: Multiple possible ways to render view\
  <class 'grokcore.view.tests.base.view.eithertemplateorrender.CavePainting'>.\
  It has both a 'render' method as well as an associated template.
"""
import grokcore.view as grok


class Mammoth(grok.Context):
    pass


class CavePainting(grok.View):
    def render(self):
        pass


cavepainting = grok.PageTemplate("nothing")
