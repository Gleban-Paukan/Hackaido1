from art import tprint

from rich.console import Console

beauty_output = Console()


def welcome():
    tprint("Hackaido")
    beauty_output.print('Enter text to rewrite (double enter in end of file):', style='bold underline green')
    text = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break;
        text += line
    beauty_output.print("Now print emotion:", style='bold underline blue')
    emotion = input()
    return [text, emotion]
