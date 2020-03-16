from talon.voice import Context, Key, press, Str
from ..utils import (
    parse_words_as_integer,
    repeat_function,
    optional_numerals,
    text,
    camel_case,
)
from datetime import datetime

context = Context("VSCode", bundle="com.microsoft.VSCode")


def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press("ctrl-g")
    Str(str(line_number))(None)
    press("enter")


def select_suggestion(m):
    suggestion_number = parse_words_as_integer(m._words[1:])

    for i in range(0, suggestion_number - 1):
        press("down")

    press("tab")


def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    press("ctrl-" + str(line_number))


def jump_screens(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    for i in range(0, line_number):
        press("cmd-" + str(line_number))


def jump_to_next_word_instance(m):
    press("escape")
    press("cmd-f")
    Str(" ".join([str(s) for s in m.dgndictation[0]._words]))(None)
    press("return")


def select_lines_function(m):
    divider = 0
    for word in m._words:
        if str(word) == "until":
            break
        divider += 1
    line_number_from = int(str(parse_words_as_integer(m._words[2:divider])))
    line_number_until = int(str(parse_words_as_integer(m._words[divider + 1 :])))
    number_of_lines = line_number_until - line_number_from

    press("ctrl-g")
    Str(str(line_number_from))(None)
    press("enter")
    for i in range(0, number_of_lines + 1):
        press("shift-down")


context.keymap(
    {
        # Selecting text
        "select line"
        + optional_numerals
        + "until"
        + optional_numerals: select_lines_function,
        # Finding text
        "find next": Key("cmd-d"),
        # Clipboard
        "clone": Key("alt-shift-down"),
        # Navigation
        "definition": Key("f12"),
        "(pizza | lie)" + optional_numerals: jump_to_line,
        "Go to line": Key("cmd-g"),
        "line up" + optional_numerals: repeat_function(2, "alt-up"),
        "line down" + optional_numerals: repeat_function(2, "alt-down"),
        # Because tab9 sucks
        "tip": Key("tab"),
        "tip" + optional_numerals: select_suggestion,
        # Navigating Interface
        "explore tab": Key("shift-cmd-e"),
        "search tab": Key("shift-cmd-f"),
        "debug tab": Key("shift-cmd-d"),
        "source control tab": Key("shift-ctrl-g"),
        "command [<dgndictation>]": [Key("cmd-shift-p"), text],
        "extensions tab": Key("shift-cmd-x"),
        "go to file <dgndictation>": [Key("cmd-p"), text],
        "go to ( thing | think ) [<dgndictation>]": [Key("cmd-shift-o"), camel_case],
        "master [<dgndictation>]": [Key("cmd-p"), text],
        # Workspaces
        "workspaces": Key("cmd-f1"),
        "open workspace": [Key("ctrl-k"), Key("ctrl-w")],
        "save workspace": [Key("ctrl-k"), Key("shift-w")],
        # tabbing
        "stiffy": Key("cmd-alt-left"),
        "next tab": Key("cmd-alt-right"),
        "stippy": Key("cmd-alt-right"),
        "last tab": Key("cmd-alt-left"),
        "new tab": Key("cmd-n"),
        "jay" + optional_numerals: jump_tabs,
        "screen swap": Key("ctrl-1"),
        "screen alone": Key("ctrl-cmd-="),
        "screen split": Key("ctrl-cmd--"),
        "screen right": Key("ctrl-cmd-backspace"),
        "screen left": Key("ctrl-shift-cmd-backspace"),
        # Menu
        "save": Key("cmd+s"),
        "open": Key("cmd+o"),
        "toggle sidebar": Key("cmd-b"),
        "toggle panel": Key("cmd-j"),
        # Integrations
        "(merge | smerge | march)": Key("shift-alt-cmd-m"),
        # editing
        "bracken": [Key("cmd-shift-ctrl-right")],
        "die line" + optional_numerals: [repeat_function(2, "shift-cmd-k", True)],
        "comment": Key("cmd-/"),
        "(comment | comma) many"
        + optional_numerals: [
            repeat_function(2, "shift-down", True),
            Key("cmd-/"),
            Key("left"),
        ],
        "(select above | shift home)": Key("cmd-shift-up"),
        "(select below | shift end)": Key("cmd-shift-down"),
        "(drop cursor | cursor drop)": Key("alt-cmd-down"),
        "(drop cursor | cursor drop) up": Key("alt-cmd-up"),
        "fold all": [Key("cmd-k"), Key("cmd-0")],
        "fold": [Key("cmd-k"), Key("cmd-[")],
        "unfold all": [Key("cmd-k"), Key("cmd-j")],
        "unfold": [Key("cmd-k"), Key("cmd-]")],
        # various
        "remind": [
            Key("cmd-/"),
            "TODO (",
            str(datetime.now().strftime("%m/%d @ %H:%M")),
            "): ",
        ],
        "search all": Key("cmd-shift-f"),
        "(drop-down | drop)": Key("ctrl-space"),
    }
)
