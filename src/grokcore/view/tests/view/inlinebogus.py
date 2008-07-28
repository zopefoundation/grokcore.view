# -*- coding: latin-1 -*-
"""
We do not accept bogus inline template such as ones that contain
encoded strings:

  >>> import grokcore.view
  >>> grokcore.view.PageTemplate('''
  ... <html>
  ... <body><h1 tal:content="string:Mammoth Cave Painting"/>
  ... <p>���</p>
  ... </body>
  ... </html>''')
  Traceback (most recent call last):
    ...
  ValueError: Invalid page template. Page templates must be unicode or ASCII.
"""