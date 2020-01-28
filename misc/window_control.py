from os import system

from talon.voice import Context, Key, press
from ..utils import parse_words_as_integer

ctx = Context("window_control")


def jump_tab(m):
    tab_number = parse_words_as_integer(m._words[1:])
    if tab_number is not None and tab_number > 0 and tab_number < 9:
        press("cmd-%s" % tab_number)


ctx.keymap(
    {
        # tab control
        "(open | new) tab": Key("cmd-t"),
        "die chai": Key("cmd-w"),
        "(pie | close) tab": Key("cmd-w"),
        "([switch] tab (right | next) | goneck)": Key("cmd-shift-]"),
        "([switch] tab (left | previous | preev) | gopreev)": Key("cmd-shift-["),
        "jay (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8)": jump_tab,
        "[switch] tab (end | rightmost)": Key("cmd-9"),
        "reopen tab": Key("cmd-shift-t"),
        # zooming
        "zoom in": Key("cmd-="),
        "zoom out": Key("cmd--"),
        "zoom normal": Key("cmd-0"),
        # window control
        "(open | new) window": Key("cmd-n"),
        "swaggy left half": Key("alt-cmd-left"),
        "swaggy right half": Key("alt-cmd-right"),
        "swaggy left": Key("ctrl-alt-cmd-left"),
        "swaggy right": Key("ctrl-alt-cmd-right"),
        "swaggy ( full | all )": Key("alt-cmd-f"),
        "window close": Key("cmd-shift-w"),
        "" "([switch] window (next | right) | pop)": Key("cmd-`"),
        "([switch] window (left | previous | preev) )": Key("cmd-shift-`"),
        "[switch] space (right | next)": Key("ctrl-right"),
        "[switch] space (left | previous | preev)": Key("ctrl-left"),
        "(minimise window | curtail)": Key("cmd-m"),
        "show app windows": Key("ctrl-down"),
        "force quit over": Key("cmd-q"),
        # application navigation
        "[open] launcher": Key("cmd-space"),
        "([switch] app (next | right) | swick)": Key("cmd-tab"),
        "[switch] app (left | previous | preev)": Key("cmd-shift-tab"),
        "[open] mission control": lambda m: system("open -a 'Mission Control'"),
    }
)
