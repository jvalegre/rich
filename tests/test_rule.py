import io

import pytest

from rich.console import Console
from rich.rule import Rule
from rich.text import Text


def test_rule():
    console = Console(width=16, file=io.StringIO(), force_terminal=True)
    console.rule()
    console.rule("foo")
    console.rule(Text("foo", style="bold"))
    console.rule("foobarbazeggfoobarbazegg")
    expected = "\x1b[38;5;10m────────────────\x1b[0m\n\x1b[38;5;10m───── \x1b[0mfoo\x1b[38;5;10m ──────\x1b[0m\n\x1b[38;5;10m───── \x1b[0m\x1b[1mfoo\x1b[0m\x1b[38;5;10m ──────\x1b[0m\n\x1b[38;5;10m─ \x1b[0mfoobarbazegg\x1b[38;5;10m ─\x1b[0m\n"
    assert console.file.getvalue() == expected


def test_repr():
    rule = Rule("foo")
    assert isinstance(repr(rule), str)


def test_error():
    with pytest.raises(ValueError):
        Rule(character="bar")
