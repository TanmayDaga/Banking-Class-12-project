import sys
import time

Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
Reset = "\u001b[0m"

Bold = "\u001b[1m"
Underline = "\u001b[4m"


def __printWithCode(text: str, code: str) -> None:
    print(f"{code}{text}{Reset}",end="")


def printRed(text: str) -> None: __printWithCode(text, Red)


def printGreen(text: str) -> None: __printWithCode(text, Green)


def printYellow(text: str) -> None: __printWithCode(text, Yellow)


def printBlue(text: str) -> None: __printWithCode(text, Blue)


def printMagenta(text: str) -> None: __printWithCode(text, Magenta)


def printCyan(text: str) -> None: __printWithCode(text, Cyan)


def printBold(text: str) -> None: __printWithCode(text, Bold)


def printUnderLine(text: str) -> None: __printWithCode(text, Underline)


