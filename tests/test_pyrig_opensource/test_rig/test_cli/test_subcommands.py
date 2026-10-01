"""Test module."""

from collections.abc import Callable, Iterable
from types import FunctionType

from pyrig_opensource.rig.cli.commands.plugins import show_plugins
from pyrig_opensource.rig.cli.subcommands import plugins


def test_plugins(
    command_works: Callable[[FunctionType], bool],
    command_calls_function: Callable[[FunctionType, FunctionType, Iterable[str]], bool],
) -> None:
    """Test function."""
    assert command_works(plugins)
    assert command_calls_function(plugins, show_plugins, [])
