import sys
from typing import Any

# Define ANSI codes to avoid using colorama (extra dependency)
ANSI_RED = r"[31m"
ANSI_RESET = r"[39m"

_verbose = False


def configure(verbose: bool = False):
    global _verbose
    _verbose = verbose


def get_int(prompt: str) -> int:
    n = ''
    while type(n) != int:
        try:
            n = int(input(prompt))
        except ValueError:
            if _verbose:
                sys.stderr.write(f"{ANSI_RED}Invalid input. Please enter a valid integer{ANSI_RESET}\n")
            continue

    return n


def get_float(prompt: str) -> float:
    f = ''
    while type(f) != float:
        try:
            f = float(input(prompt))
        except ValueError:
            if _verbose:
                sys.stderr.write(f"{ANSI_RED}Invalid input. Please enter a valid number.{ANSI_RESET}\n")
            continue

    return f


def get_these(element1: str, element2: str, prompt: str) -> str:
    t = None
    while t != element1.lower() and t != element2.lower():
        t = input(prompt).lower()
        if t not in {element1, element2} and _verbose:
            sys.stderr.write(f"{ANSI_RED}Invalid input. Please enter either {element1} or {element2}.{ANSI_RESET}\n")

    return t


def get(element, prompt):
    t = None
    while t != element:
        t = input(prompt)


def get_this(_type: type, prompt: str, args: tuple[Any] = None, kwargs: dict[str, Any] = None) -> Any:
    v = None
    if not args: args = ()
    if not kwargs: kwargs = dict()
    while True:
        t = input(prompt)
        try:
            v = _type(t, *args, **kwargs)
            break
        except Exception as _:
            if _verbose:
                sys.stderr.write(
                    f"{ANSI_RED}Invalid input. Please enter a valid value for {_type.__name__}.{ANSI_RESET}\n")
            continue

    return v
