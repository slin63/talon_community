# https://github.com/JonathanNickerson/talon_voice_user_scripts

import time

import talon.clip as clip
from talon.voice import Key, press, Str, Context
from ..utils import (
    parse_words,
    join_words,
    is_not_terminal,
    numeral_list,
    extract_num_from_m,
    optional_numerals,
    repeat_function,
)

ctx = Context("generic_editor", func=is_not_terminal)
# ctx.set_list("n", numeral_list)


def find_next(m):
    press("cmd-f")
    Str(str(m.dgndictation[0]._words[0]))(None)
    press("escape")


def find_previous(m):
    press("left")
    press("cmd-f")
    Str(str(m.dgndictation[0]._words[0]))(None)
    press("cmd-shift-g")
    press("escape")


# jcooper-korg from talon slack
def select_text_to_left_of_cursor(m):
    words = parse_words(m)
    if not words:
        return
    old = clip.get()
    key = join_words(words).lower()
    press("shift-home", wait=2000)
    press("cmd-c", wait=2000)
    press("right", wait=2000)
    text_left = clip.get()
    clip.set(old)
    result = text_left.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, len(text_left) - result):
        press("left", wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right")


# jcooper-korg from talon slack
def select_text_to_right_of_cursor(m):
    words = parse_words(m)
    if not words:
        return
    key = join_words(words).lower()
    old = clip.get()
    press("shift-end", wait=2000)
    press("cmd-c", wait=2000)
    press("left", wait=2000)
    text_right = clip.get()
    clip.set(old)
    result = text_right.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, result):
        press("right", wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right")


alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789_"


def big_word_neck(m):
    return word_neck(m, valid_characters=set(alphanumeric) | set("/\\-_.>=<"))


def word_neck(m, valid_characters=alphanumeric):
    word_index = extract_num_from_m(m, 1)

    old = clip.get()
    press("shift-right", wait=2000)
    press("cmd-c", wait=2000)
    press("shift-left", wait=2000)
    current_highlight = clip.get()
    if len(current_highlight) > 1:
        press("right", wait=2000)
    press("shift-end", wait=2000)
    time.sleep(0.25)
    press("cmd-c", wait=2000)
    press("left", wait=2000)
    time.sleep(0.25)
    text_right = clip.get().lower()
    clip.set(old)

    is_word = [character in valid_characters for character in text_right]
    word_count = 1
    i = 0
    while i < (len(is_word) - 1) and not is_word[i]:
        i += 1

    # print("a start", i)

    while i < (len(is_word) - 1) and word_count < word_index:
        # print(i, is_word[i], word_count, word_index)
        if not is_word[i] and is_word[i + 1]:
            word_count += 1
        i += 1
    # warning: this is a hack, sorry
    # print("i", i)
    if i == 1 and is_word[0]:
        i = 0
    start_position = i
    # print(text_right[start_position:])
    while i < len(is_word) and is_word[i]:
        i += 1
    end_position = i

    # print(start_position, end_position)
    # cursor over to the found word
    for i in range(0, start_position):
        press("right", wait=0)
    # now select the word
    for i in range(0, end_position - start_position):
        press("shift-right")


def big_word_prev(m):
    return word_prev(m, valid_characters=set(alphanumeric) | set("/\\-_.>=<"))


def word_prev(m, valid_characters=alphanumeric):
    word_index = extract_num_from_m(m, 1)

    old = clip.get()
    press("shift-right", wait=2000)
    press("cmd-c", wait=2000)
    press("shift-left", wait=2000)
    current_highlight = clip.get()
    if len(current_highlight) > 1:
        press("left", wait=2000)
    press("shift-home", wait=2000)
    time.sleep(0.25)
    press("cmd-c", wait=2000)
    press("right", wait=2000)
    time.sleep(0.25)
    text_right = clip.get().lower()
    clip.set(old)

    text_right = list(reversed(text_right))

    is_word = [character in valid_characters for character in text_right]
    word_count = 1
    i = 0
    while i < (len(is_word) - 1) and not is_word[i]:
        i += 1

    while i < (len(is_word) - 1) and word_count < word_index:
        # print(i, is_word[i], word_count, word_index)
        if not is_word[i] and is_word[i + 1]:
            word_count += 1
        i += 1
    start_position = i
    # print(text_right[start_position:])
    while i < len(is_word) and is_word[i]:
        i += 1
    end_position = i

    # print(start_position, end_position, text_right[start_position:end_position])
    # cursor over to the found word
    for i in range(0, start_position):
        press("left", wait=0)
    # now select the word
    for i in range(0, end_position - start_position):
        press("shift-left")


ctx.keymap(
    {
        # meta
        "(save it | sage | sage it)": Key("cmd-s"),
        # "(undo it | rabbi)": Key("cmd-z"),
        "undo " + optional_numerals: repeat_function(1, "cmd-z"),
        "redo " + optional_numerals: repeat_function(1, "cmd-shift-z"),
        # "(redo it | rabbit)": Key("cmd-shift-z"),
        # clipboard
        "(snatch)": Key("cmd-x"),
        "(stish)": Key("cmd-c"),
        "(spark)": Key("cmd-v"),
        "(spark mat)": Key("cmd-alt-shift-v"),
        "copy all": [Key("cmd-a"), Key("cmd-c")],
        "paste all": [Key("cmd-a"), Key("cmd-v")],
        # motions
        "(go word left | fame )": Key("alt-left"),
        "(go word right | fish )": Key("alt-right"),
        "(go line start | lefty)": Key("cmd-left"),
        "(go line end | ricky)": Key("cmd-right"),
        # deleting
        "(delete around this | slurp)": Key("backspace delete"),
        # "(delete word left | )": Key("shift-cmd-left delete"),
        "(delete line left | snip left )": Key("shift-cmd-left delete"),
        "(delete line right | snip right )": Key("shift-cmd-right delete"),
        "(delete line)"
        + optional_numerals: [
            "byebye",
            repeat_function(
                2,
                "cmd-right shift-cmd-left shift-cmd-left backspace backspace down",
                True,
            ),
        ],
        # selecting
        "(copy this)": Key("alt-right shift-alt-left cmd-c"),
        # "(select this word | word this)": Key("alt-right shift-alt-left"),
        "(select this line | shackle)": Key("cmd-right shift-cmd-left"),
        # "(select above | shift home)": Key("shift-home"),
        # "(select below | shift end)": Key("shift-end"),
        "(select above | shift home)": Key("cmd-shift-up"),
        "(select below | shift end)": Key("cmd-shift-down"),
        "(select up )": Key("shift-up"),
        "(select down )": Key("shift-down"),
        "unindent": Key("shift-up cmd-shift-right backspace"),
        "(select all)": Key("cmd-a"),
        "(select left )": Key("shift-left"),
        "(select right )": Key("shift-right"),
        # "(select word number {generic_editor.n}* below | wordneck {generic_editor.n}*)": word_neck,
        "(select word left | scram)": Key("alt-shift-left"),
        "(select word right | scrash)": Key("alt-shift-right"),
        "(fishy)": Key("alt-shift-right delete"),
        "(famie)": Key("alt-shift-left delete"),
        "(select line left | lecksy)": Key("cmd-shift-left"),
        "(select line right | ricksy)": Key("cmd-shift-right"),
    }
)
