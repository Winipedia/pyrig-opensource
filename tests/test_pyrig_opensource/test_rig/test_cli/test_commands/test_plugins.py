"""Test module."""

import pyrig
import pyrig_codecov
import pyrig_codeql
import pyrig_fixtures
import pyrig_openssf
import pyrig_public
import pytest

from pyrig_opensource.rig.cli.commands.plugins import plugins, show_plugins


def test_show_plugins(capsys: pytest.CaptureFixture[str]) -> None:
    """Test function."""
    assert show_plugins() is None

    captured = capsys.readouterr()
    out, err = captured.out, captured.err
    assert out.splitlines() == [str(plugin) for plugin in plugins()]
    assert err == ""


def test_plugins() -> None:
    """Test function."""
    assert plugins() == (
        pyrig,
        pyrig_codecov,
        pyrig_codeql,
        pyrig_fixtures,
        pyrig_openssf,
        pyrig_public,
    )
