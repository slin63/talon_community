from talon.voice import Context, Key, press, Str
from ..utils import parse_words_as_integer, repeat_function, optional_numerals, text, delay

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

context.keymap(
    {
        # Selecting text
        "select (lines | line)"
        + optional_numerals
        + "until"
        + optional_numerals: select_lines_function,
        "(die line)" + optional_numerals: [repeat_function(2, "ctrl-shift-k", True)],
        "(comment | comma) many" + optional_numerals: [
            repeat_function(2, "shift-down", True),
            Key("cmd-/"),
            Key("left"),
        ],

        "(select) many" + optional_numerals: [
            repeat_function(2, "shift-down", True),
        ],

        # Finding text
        "find over": Key("cmd-f"),
        "find next": jump_to_next_word_instance,
        # # Clipboard
        # "clone": Key("alt-shift-down"),
        # Navigation
        "(lay | line | lie)"  + optional_numerals + "[over]": jump_to_line,
        "Go to line": Key("ctrl-g"),
        "gogo": [Key('cmd-shift-g'), delay(.1), Key('enter')],
        "line up" + optional_numerals: repeat_function(2, "alt-up"),
        "line down" + optional_numerals: repeat_function(2, "alt-down"),
        # # Navigating Interface
        # "explore tab": Key("shift-cmd-e"),
        "search tab": Key("shift-cmd-f"),
        # "debug tab": Key("shift-cmd-d"),
        # "source control tab": Key("shift-ctrl-g"),
        # "extensions tab": Key("shift-cmd-x"),
        "go to file <dgndictation>": [Key("cmd-p"), text],
        "go to ( thing | think ) [<dgndictation>]": [Key("cmd-r"), text],
        "master": Key("cmd-p"),
        "command": Key("cmd-shift-p"),
        # "tab clean": [Key("cmd-shift-p"), Str("file: close all"), Key("enter")],
        # tabbing
        "screen alone": Key("alt-cmd-1"),
        "hello adrian": "hello hello hello",

        "screen split": Key("alt-cmd-2"),
        "search this": [Key('cmd-c'), Key('cmd-f'), Key('cmd-v')],
        "screen screen": Key("alt-k"),
        # "stiffy": Key("cmd-alt-left"),
        "next tab": Key("cmd-alt-right"),
        # "stippy": Key("cmd-alt-right"),
        "last tab": Key("cmd-alt-left"),
        "new tab": Key("cmd-n"),
        "jay" + optional_numerals: jump_tabs,
        "screen" + optional_numerals: jump_screens,
        # Menu
        "save": Key("cmd+s"),
        "open": Key("cmd+o"),
        # editing
        "comment": [Key("cmd-/")],
        "help": Key("ctrl-space"),
        "open workspace": Key("ctrl-alt-o"),
        # "bracken": [Key("cmd-shift-ctrl-right")],
        # various
        # "search all": Key("cmd-shift-f"),
        # "(drop-down | drop)": Key("ctrl-space"),
        # view
        # ""
        'fold': Key('cmd-alt-['),
        'unfold': Key('cmd-alt-]'),
        'bookmark': Key('ctrl-shift-r')
    }
)
