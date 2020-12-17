"""

  >>> grok.testing.grok(__name__)

  >>> cave = Cave()
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> from zope.component import getMultiAdapter

  >>> view = getMultiAdapter((cave, request), name='piepmatz')
  >>> print(view())
  <p>Piep! Piep!</p>

"""

import grokcore.view as grok


class Cave(grok.Context):
    pass


class Piepmatz(grok.View):
    pass  # template in zpt_templates/piepmatz.pt
