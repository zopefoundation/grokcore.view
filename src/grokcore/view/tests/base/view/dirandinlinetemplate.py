"""
If multiple templates can be found, one in the module and one in the
template directory, there is an error:

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  zope.configuration.config.ConfigurationExecutionError:\
  martian.error.GrokError: Conflicting\
  templates found for name 'cavepainting': the inline template in\
  module 'grokcore.view.tests.base.view.dirandinlinetemplate' conflicts\
  with the file template in directory\
  '...dirandinlinetemplate_templates'

"""
import grokcore.view as grok


class Mammoth(grok.Context):
    pass


class CavePainting(grok.View):
    pass


cavepainting = grok.PageTemplate("nothing")
