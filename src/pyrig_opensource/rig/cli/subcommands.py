"""Project-specific CLI commands.

Functions defined directly in this module are registered as top-level CLI
commands. Module-level `typer.Typer` instances are registered as command
groups, with each group's name derived from the kebab-case form of the
variable name.
"""


def plugins() -> None:
    """List the pyrig plugins bundled together by this plugin.

    Prints one plugin per line, each shown as its module object's `str()`
    (e.g. `<module 'pyrig' from '...'>`). Useful for confirming which plugins
    were pulled in by installing this package.
    """
    from pyrig_opensource.rig.cli.commands.plugins import show_plugins  # noqa: PLC0415

    show_plugins()
