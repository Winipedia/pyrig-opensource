"""Backend implementation for the `plugins` CLI command.

Declares the fixed set of pyrig plugins this package bundles together, and
prints them to let users confirm what got installed.
"""

from types import ModuleType

import pyrig
import pyrig_codecov
import pyrig_codeql
import pyrig_fixtures
import pyrig_public
import pyrig_pypi
import typer


def show_plugins() -> None:
    """Print every plugin bundled by this plugin, one per line.

    Each line is the `str()` of the plugin's module object, e.g.
    `<module 'pyrig' from '...'>`.
    """
    for plugin in plugins():
        typer.echo(plugin)


def plugins() -> tuple[ModuleType, ...]:
    """Return every pyrig plugin bundled together by this plugin.

    Returns:
        Tuple of the imported plugin modules, in dependency order.

    Note:
        This list is maintained by hand, not discovered automatically. Keep
        it in sync with this package's own runtime dependencies.
    """
    return (
        pyrig,
        pyrig_codecov,
        pyrig_codeql,
        pyrig_fixtures,
        pyrig_public,
        pyrig_pypi,
    )
