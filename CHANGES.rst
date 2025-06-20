Changes
=======

5.1 (unreleased)
----------------

- Nothing changed yet.


5.0 (2025-06-18)
----------------

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


4.1 (2025-06-04)
----------------

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


4.0 (2023-02-16)
----------------

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


3.2 (2022-02-16)
----------------

- Add support for Python 3.7, 3.8, 3.9, and 3.10.

- Drop support for Python 3.4.

- Update the tests to ``martian >= 1.5``, thus requiring at least that version.


3.1 (2018-06-13)
----------------

- Added AfterTraversalEvent which is fired after all traversal is done.


3.0.3 (2018-01-12)
------------------

- Rearrange tests such that Travis CI can pick up all functional tests too.

3.0.2 (2018-01-05)
------------------

- Additional test fixes.

3.0.1 (2018-01-05)
------------------

- Additional test fixes.

3.0 (2018-01-03)
----------------

- In the template directory grokker, ignore directories and files
  without extensions.

- Drop support of Python 2.6.

- Claim support for Python 3.4, 3.5, and 3.6.

2.10.2 (2016-02-02)
-------------------

- Update tests.


2.10.1 (2014-07-29)
-------------------

- Fix broken MANIFEST.in


2.10 (2014-07-29)
-----------------

- Add an helper ``render_provider`` to look up and render a given
  content provider.


2.9 (2014-05-15)
----------------

- Make possible to disable the template warning with the help of the
  ``GROK_DISABLE_TEMPLATE_WARNING`` environment variable.

- The ``skin`` option of ``grokcore.view.util.url`` now accepts
  strings that will be used as skin name as possible alternative to a
  skin interface.

- The ``skin`` directive can now be used on interfaces that inherits
  only from ``IRequest`` instead of ``IBrowserRequest``.

2.8 (2012-12-11)
----------------

- Add a ``skin=[skin component]`` argument to the ``grokcore.view.util.url()``
  function and ``grokcore.view.components.View.url`` method. This allows for
  computing URLs on a specific skin. Note that it is not verified whether
  the computed URL actually exist on the specified skin.

2.7 (2012-05-01)
----------------

- Use the component registration api in grokcore.component.

- Improve error message when a templatedir() directive points to a non-
  existent directory. (fix launchpad issue 680528).

- Improve error message when a template is required for a component
  but cannot be found (Fix Launchpad issue #225855, #242698).

- Fix how the static resource are found. Instead of using as name the
  package name where the component is defined, using as name the
  package where the template for the component is defined, or the base
  component. This is done by setting an attribute ``__static_name__``
  on the component that specify which resource directory should be
  used. This fix missing resources when you extend the component and
  don't redefined the template.

2.6.1 (2011-06-28)
------------------

- Fix bug where zope.browserpage was not correctly declared as a dependency.

2.6 (2011-06-28)
----------------

- Add the ContentProvider component.

2.5 (2011-04-04)
----------------

- Fix a test that relied on older zope.testbrowser behaviour.

2.4 (2011-03-01)
----------------

- grok.View component can optionally use the ``grok.provides`` directive,
  specifying an interface that the component provides (instead of the
  zope.interface.Interface that views by default provide).

- Add a new ZCML directive, ``ignoreTemplates`` that let you configure which
  template filename pattern should be ignored by the template registry. The
  pattern attribute of the directive accepts regular expresssion that will be
  matched against the (template) file extension.

- Use the zope configuration action ordering feature to have templates
  registered for all packages and modules, before trying to associate the
  templates. Checking for unassociated templates is done very very late in the
  configuration action order.

- Inherited grok.template() information is looked up against the module of
  the view class that uses the grok.template() directive. This allows for
  subclassing view components that use the grok.template() directive from other
  packages.

2.3 (2011-01-04)
----------------

- Removed the static directory grokker in order to make way for using
  fanstatic.

2.2 (2010-12-16)
----------------

- Factor out a base template grokker that associate templates for
  viewish components.

- Merge support for a global template registry that removes
  unnecessary warnings about unassociated templates in "shared"
  template directories.

2.1 (2010-11-03)
----------------

- Use an update martian and grokcore.component.

- The custom zope publication has now moved from the grok package to
  grokcore.view. The registration of the publication is optional, and is used
  by grok and the grokcore.json package.

- The util function `make_checker` has been moved from the `grok`
  package to ``grokcore.view``.

2.0 (2010-11-01)
----------------

- The `view` directive has been moved from ``grokcore.viewlet`` to
  ``grokcore.view``.

- The `IGrokSecurityView` has been moved from ``grok`` to
  ``grokcore.view``.

- Fix the url() function to behave properly while passed an empty data dict.

- Fix the url() method to accept the "status" and "trusted" arguments, passed
  on to the redirect method on the response object.

- ``grokcore.view`` no longer depends on ``zope.app.testing`` and
  related packages. Instead we now use ``zope.app.wsgi.testlayer`` to
  run functional tests.

- Made package comply to zope.org repository policy.

- Fixed launchpad bug #395061 : removed the default_fallback_to_name
  function. It can be imported from ``grokcore.security`` if needed.

- ``grokcore.view`` no longer depends on ``zope.app.zcmlfiles``. We
  removed all the extra dependencies and fixed one test that used
  ``zope.app.rotterdam`` and ``zope.app.basicskin``.

- Back-ported the changes of the 1.13 branch related to the directory
  resource registration, using the latest ztk packages.

- Factor out generally useful methods and properties for view-ish
  components into components.ViewSupport mixin.

- Works with new Martian (0.13) and grokcore.component 2.1.

- Test fix: support windows paths.

- Warnings are now emitted as log messages with level
  `logging.WARNING` to a logger named ``grokcore.view`` with level
  `logging.ERROR`.

  That means that by default no warnings are emitted anymore (while
  errors will still appear).

  To get the warnings back, reduce the level of logger
  ``grokcore.view`` to `logging.WARNING` or lower. This can be done in
  Python or via a logging conf file, for instance in the .ini files of
  regular grokprojects. See the Python standard lib `logging` module
  for details.

1.12.1 (2009-09-17)
-------------------

- A compatibility fix to support ``grokcore.viewlet``.

1.12 (2009-09-17)
-----------------

- Use 1.0b1 versions.cfg in Grok's release info instead of a local
  copy; a local copy for all grokcore packages is just too hard to
  maintain.

- Revert the splitting CodeView/View. The original reasons for the
  split have been obsoleted by the recent martain developments
  regarding inheritted module level directives. At the same time the
  split up components proved cumbersome to use and a too big a change
  between the 1.0a and 1.0b releases of Grok.

  View components will now again behave like it did up until the latest alpha
  release of Grok.

  ``CodeView`` is still available as a backwards compatibility alias
  for ``View``. Please update all references to ``CodeView`` to
  ``View``.

- Fix the template registry and grokker for views to let View and
  other components using View as base class to be associated with a
  template directly by setting it as 'template' attribute on the view
  class. Example::

    class MyView(grokcore.view.View):

        template = grokcore.view.PageTemplate('<p>hello</p>')

  This isn't exactly *officially* supported but enough people depend
  on it and have documented it so that we don't want to just break it.

1.11 (2009-09-15)
-----------------

- The response attribute needs to be available in CodeView as well.

1.10 (2009-09-14)
-----------------

- Up the version requirement for grokcore.security to 1.2.

- Bring versions.cfg in line with current grok versions.cfg.


1.9 (2009-07-04)
----------------

- Fix needed for grokcore.formlib: allow a base_method'ed render() on view.
  This allows grokcore.formlib to have a render() in addition to a template.

- Reverted change to checkTemplates: for some formlib edge cases it detects
  the right templates again.


1.8 (2009-07-04)
----------------

- Add validator to templatedir directive to disallow path separator.

- Splitted CodeView out of View.  View only uses templates, CodeView only uses
  a render() method.  So views that have a render method must subclass from
  CodeView instead of View (that should be the only change needed).

- Add grok.View permissions to functional tests (requires grokcore.security 1.1)


1.7 (2009-05-19)
----------------

- Revert dependency from zope.container back to zope.app.container.


1.6 (2009-04-28)
----------------

- Simplify the DirectoryResource and DirectoryResourceFactory
  implementations by making better use of the hook points provided by
  zope.app.publisher.browser.directoryresource.

1.5 (2009-04-10)
----------------

- Don't register a 'static' resource directory if the 'static' directory does
  not exist.

- Make it possible to instantiate an ungrokked view by being slightly more
  defensive in __init__. This makes it easier to write unit tests.

1.4 (2009-04-08)
----------------

* Page template reloading now also works for macros. Fixes
  https://bugs.launchpad.net/grok/+bug/162261.

* Use zope.container instead of zope.app.container.

* Ignore '<tpl>.cache' files when looking up template files in a
  template dir. Fix bug https://bugs.launchpad.net/grok/+bug/332747

1.3 (2009-01-28)
----------------

* Adapt tests to work also from eggs not only source checkouts by
  avoiding `src` in directory comparisons.

* Fix the factory for subdirectories of the DirectoryResource implementation
  by using hooks in zope.app.publisher.browser.directoryresource.

* Update APIs interfaces to include the new ``path`` directive and
  new ``DirectoryResource`` component.

1.2 (2008-10-16)
----------------

* Expose the ``DirectoryResource`` class as a component for registering
  directories as resources. This is accompanied by the ``path`` directive that
  is used to point to the directory holding resources by way of an relative (to
  the module) or absolute path. ``DirectoryResource`` components can be
  differentiated by name and layer.

1.1 (2008-09-22)
----------------

* ``meta.py`` module containing the grokkers has been split in a
  package with separate modules for the view, template, skin and
  static resources grokkers. This allows applications to use only
  grokkers they need (and maybe redefine others).

1.0 (2006-08-07)
----------------

* Created ``grokcore.view`` in July 2008 by factoring security-related
  components, grokkers and directives out of Grok.
