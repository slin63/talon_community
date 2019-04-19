from talon.voice import Context, Key

from ..utils import is_filetype, snake_text, caps_text

PREFIX = " "
ctx = Context("spotify", bundle="com.spotify.client")


ctx.keymap(
    {
        PREFIX + " back": Key("cmd-left"),
        PREFIX + " next": Key("cmd-right"),
        PREFIX + " play": Key("space"),
        PREFIX + " more": Key("cmd-up"),
        PREFIX + " less": Key("cmd-down"),
    }
)
