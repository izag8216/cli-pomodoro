"""Basic usage example for cli-pomodoro."""

from cli_pomodoro.mosaic import image_to_mosaic
from cli_pomodoro.banner import generate_banner, text_to_fullwidth


def main():
    print("cli-pomodoro demo")
    print("=================\n")

    print("Fullwidth text conversion:")
    print(text_to_fullwidth("HELLO WORLD"))
    print()

    print("Banner generation:")
    print(generate_banner("EMOJI", style="block"))


if __name__ == "__main__":
    main()
