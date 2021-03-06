from talon.voice import Context, ContextGroup
from talon.engine import engine
from talon_plugins import speech
from talon import app, tap, ui
from .. import utils


sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

dictation_group = ContextGroup("dictation")
dictation = Context("dictation", group=dictation_group)
dictation_group.load()
dictation_group.disable()


class VoiceType:
    SLEEPING = 1
    TALON = 2
    DRAGON = 3
    DICTATION = 4


spaghetti = {
    1: "💤 Sleeping...",
    2: "✅ Awake!",
    3: "💬 Dragon mode",
    4: "DICTATION",
}

voice_type = VoiceType.TALON
last_voice_type = VoiceType.TALON


def set_voice_type(type):
    global voice_type, last_voice_type
    if voice_type != VoiceType.SLEEPING:
        last_voice_type = voice_type
    voice_type = type

    talon_enabled = type == VoiceType.TALON
    dragon_enabled = type == VoiceType.DRAGON
    dictation_enabled = type == VoiceType.DICTATION

    global speech
    speech.set_enabled(talon_enabled)

    global dictation_group
    if not dictation_enabled:
        dictation_group.disable()

    global engine
    if dragon_enabled:
        engine.mimic("wake up".split())
    else:
        engine.mimic("go to sleep".split())

    if dictation_enabled:
        # Without postponing this "go to sleep" will be printed
        dictation_group.enable()

    if voice_type != VoiceType.SLEEPING:
        return app.notify(body=spaghetti[type], sound=True)
    return app.notify(body=spaghetti[type], sound=False)


sleepy.keymap(
    {
        "talon sleep": lambda m: set_voice_type(VoiceType.SLEEPING),
        "talon wake": lambda m: set_voice_type(last_voice_type),
        "dragon mode": lambda m: set_voice_type(VoiceType.DRAGON),
        # "dictation mode": lambda m: set_voice_type(VoiceType.DICTATION),
        "talon mode": lambda m: set_voice_type(VoiceType.TALON),
    }
)
sleep_group.load()


def sleep_hotkey(typ, e):
    global voice_type
    if e == "ctrl-alt-cmd-,":
        set_voice_type(VoiceType.SLEEPING)
    elif e == "ctrl-alt-cmd-.":
        set_voice_type(VoiceType.TALON)
    # elif e == "ctrl-alt-cmd-/":
    #     # set_voice_type(VoiceType.SLEEPING)
    #     set_voice_type(VoiceType.DRAGON)

    return True


tap.register(tap.HOOK | tap.KEY, sleep_hotkey)
