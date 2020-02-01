#!/usr/bin/env python3
from typing import List

from pytest import fixture

from object_colors import Color


@fixture
def color() -> Color:
    populated = Color()
    populated.populate_colors()
    return populated


@fixture
def color_str(color: Color, str_: str) -> Color:
    return color.green.get(str_)


@fixture
def str_() -> str:
    return "Cc: My Business <me@mybusiness.com>;"


@fixture
def marked(red: str, reset: str) -> str:
    return f"{red}Cc:{reset} My Business <me@mybusiness.com>;"


@fixture
def marked_color(green: str, red: str, reset: str) -> str:
    return f"{green}{red}Cc:{green} My Business <me@mybusiness.com>;{reset}"


@fixture
def marked_second(red: str, reset: str) -> str:
    return f"Cc: {red}My{reset} Business <me@mybusiness.com>;"


@fixture
def marked_second_color(green: str, red: str, reset: str) -> str:
    return f"{green}Cc: {red}My{green} Business <me@mybusiness.com>;{reset}"


@fixture
def all_cs(red: str, reset: str) -> str:
    return (
        f"{red}C{reset}{red}c{reset}{red}:{reset} My "
        f"Business <me@mybusiness.{red}c{reset}om>;"
    )


@fixture
def dupe_marked_color(green: str, red: str, reset: str) -> str:
    """do dupe fixture but with ignore"""
    return (
        f"{green}This is a string that says {red}one{green} several times. "
        f"It says {red}one{green} in this sentence. And {red}one{green} in "
        f"this sentence. This sentence also has {red}one{green} in it. Lastly "
        f"this sentence will also say {red}one{green}{reset}"
    )


@fixture
def dupe_marked(green: str, red: str, reset: str) -> str:
    """do dupe fixture but with ignore"""
    return (
        f"This is a string that says {red}one{reset} several times. It says "
        f"{red}one{reset} in this sentence. And {red}one{reset} in this "
        f"sentence. This sentence also has {red}one{reset} in it. Lastly this "
        f"sentence will also say {red}one{reset}"
    )


@fixture
def all_cs_color(red: str, green: str, reset: str) -> str:
    return (
        f"{green}{red}C{green}{red}c{green}{red}:{green} My "
        f"Business <me@mybusiness.{red}c{green}om>;{reset}"
    )


@fixture
def all_cs_no_caps(red: str, reset: str) -> str:
    return (
        f"C{red}c{reset}{red}:{reset} My "
        f"Business <me@mybusiness.{red}c{reset}om>;"
    )


@fixture
def all_cs_no_caps_color(red: str, green: str, reset: str) -> str:
    return (
        f"{green}C{red}c{green}{red}:{green} My "
        f"Business <me@mybusiness.{red}c{green}om>;{reset}"
    )


@fixture
def exact_idx(red: str, reset: str) -> str:
    return (
        f"{red}C{reset}{red}c{reset}: My Business "
        f"<me@mybusiness.{red}c{reset}om>;"
    )


@fixture
def exact_idx_color(green: str, red: str, reset: str) -> str:
    return (
        f"{green}{red}C{green}{red}c{green}: My Business "
        f"<me@mybusiness.{red}c{green}om>;{reset}"
    )


@fixture
def dupes() -> str:
    return (
        "This is a string that says one several times. It says one in this "
        "sentence. And one in this sentence. This sentence also has one in "
        "it. Lastly this sentence will also say one"
    )


@fixture
def colored_dupes() -> str:
    return (
        "\u001b[0;32;40mThis is a string that says one several times. It says "
        "one in this sentence. And one in this sentence. This sentence also "
        "has one in it. Lastly this sentence will also say one\u001b[0;0m"
    )


@fixture
def scatter_cs(green: str, red: str, reset: str) -> str:
    return (
        f"{red}C{reset}{red}c{reset}{red}:{reset} My Business "
        f"<me@mybusiness.{red}c{reset}om>;"
    )


@fixture
def scatter_cs_color(green: str, red: str, reset: str) -> str:
    return (
        f"{green}{red}C{green}{red}c{green}{red}:{green} My Business "
        f"<me@mybusiness.{red}c{green}om>;{reset}"
    )


@fixture
def scatter_cs_exact(green: str, red: str, reset: str) -> str:
    return f"C{red}c{reset}: My Business <me@mybusiness.{red}c" f"{reset}om>;"


@fixture
def scatter_cs_exact_color(green: str, red: str, reset: str) -> str:
    return (
        f"{green}C{red}c{green}: My Business "
        f"<me@mybusiness.{red}c{green}om>;{reset}"
    )


@fixture
def spaced_words(green: str, red: str, reset: str) -> str:
    return f"{red}Cc:{reset} My {red}Business{reset} <me@mybusiness.com>;"


@fixture
def spaced_words_color(green: str, red: str, reset: str) -> str:
    return (
        f"{green}{red}Cc:{green} My {red}Business{green} "
        f"<me@mybusiness.com>;{reset}"
    )


@fixture
def green() -> str:
    return "\u001b[0;32;40m"


@fixture
def red() -> str:
    return "\u001b[0;31;40m"


@fixture
def reset() -> str:
    return "\u001b[0;0m"


@fixture
def color_keys(color: Color, str_: str) -> str:
    return color.red.get_key(str_, "c", ignore_case=True, scatter=True)


@fixture
def attrs() -> List[str]:
    return [
        "get",
        "set",
        "get",
        "get_key",
        "print",
        "print_key",
        "pop",
        "multicolor",
        "populate_colors"
    ]


@fixture
def colors():
    return [
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "purple",
        "cyan",
        "white",
    ]


@fixture
def instances(colors) -> List[str]:
    return ["text", "effect", "background", "bold"] + colors


@fixture
def for_multiple_colors():
    return "Testing for multiple colors"
