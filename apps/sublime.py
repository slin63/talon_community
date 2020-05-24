from datetime import datetime

from talon.voice import Context, Key, press, Str
from ..utils import (
    parse_words_as_integer,
    repeat_function,
    optional_numerals,
    text,
    delay,
)

context = Context("Sublime", bundle="com.sublimetext.3")


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


def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    press("cmd-" + str(line_number))


def jump_screens(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number is None:
        return

    press("ctrl-" + str(line_number))


def jump_to_next_word_instance(m):
    press("cmd-d")


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


def comment_lines_function(m):
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
    press("cmd-/")


GOGURU = "goo"

context.keymap(
    {
        # Selecting text
        "select (lines | line)"
        + optional_numerals
        + "until"
        + optional_numerals: select_lines_function,
        "(day line)" + optional_numerals: [repeat_function(2, "ctrl-shift-k", True)],
        # Finding text
        "find over": Key("cmd-f"),
        "find next": jump_to_next_word_instance,
        # Navigation
        "(lie | buy)" + optional_numerals + "[over]": jump_to_line,
        "Go to line": Key("ctrl-g"),
        "line up" + optional_numerals: repeat_function(2, "alt-up"),
        "line down" + optional_numerals: repeat_function(2, "alt-down"),
        "(go to file|master) [<dgndictation>]": [Key("cmd-p"), text],
        "go to ( thing | think ) [<dgndictation>]": [Key("cmd-r"), text],
        "command [<dgndictation>]": [Key("cmd-shift-p"), text],
        # tabbing
        "screen alone": Key("alt-cmd-1"),
        "screen split": Key("alt-cmd-2"),
        "screen screen": Key("alt-k"),
        "next tab": Key("cmd-alt-right"),
        "last tab": Key("cmd-alt-left"),
        "new tab": Key("cmd-n"),
        "jay" + optional_numerals: jump_tabs,
        "screen" + optional_numerals: jump_screens,
        # Menu
        "save": Key("cmd+s"),
        "open": Key("cmd+o"),
        # editing
        "block": [" {", Key("enter")],
        "commy": Key("cmd-/"),
        "open workspace": Key("ctrl-alt-o"),
        "save workspace": Key("ctrl-alt-shift-s"),
        "fold": Key("cmd-alt-["),
        "unfold": Key("cmd-alt-]"),
        "drop cursor": Key("cmd-shift-alt-down"),
        "sub packages add": [Key("cmd-shift-p"), "package install", Key("enter")],
        "sub packages": [Key("cmd-shift-p"), "package "],
        "toggle sidebar": [Key("cmd-k"), Key("cmd-b")],
        "toggle console": Key("ctrl-`"),
        # Searching
        "set case": Key("alt-cmd-c"),
        "search tab": Key("shift-cmd-f"),
        "search this": [Key("cmd-c"), Key("cmd-f"), Key("cmd-v")],
        # SendCode
        "sub send": Key("cmd-enter"),
        # Sublime Merge
        "submerge": Key("cmd-alt-z"),
        # Opening finder
        "open finder": [Key("cmd-shift-p"), "finder open here", Key("enter")],
        # Insert debugging print
        "pie bug": Key("alt-x"),
        # goguru because we live in the middle ages
        GOGURU + "describe ": [Key("cmd-shift-p"), "describe", Key("enter")],
        GOGURU
        + "definition ": [Key("cmd-shift-p"), "jump to definition", Key("enter")],
        GOGURU + "referrences ": [Key("cmd-shift-p"), "referrers", Key("enter")],
        # Built in definition navigator
        "sub ref": Key("shift-f12"),
        "sub def": Key("alt-cmd-down"),
        # TODO 05/13@14:57:
        # Macro for TODO:
        "remind": [Key("cmd-/"), "TODO ", str(datetime.now().strftime("%m/%d")), ": ",],
    }
)
