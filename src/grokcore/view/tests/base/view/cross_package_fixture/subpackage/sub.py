import grokcore.view as grok
from grokcore.view.tests.base.view.cross_package_fixture.zbase import BaseView


class SubView(BaseView):
    pass


class SubViewOverrideTemplate(BaseView):
    grok.template('subtemplate')
