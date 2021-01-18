

from grokcore import view as grok


class Cave(grok.Context):
    pass


class StaticResource(grok.DirectoryResource):
    grok.name('grokcore.view.tests.functional'
              '.static.notemplates_nooverridestatic.original')
    grok.path('static')


class CaveView(grok.View):
    grok.context(Cave)

    def render(self):
        return self.static['resource.css']()
