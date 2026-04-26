"""CLI entry point for cli-pomodoro."""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console

from . import __version__
from .banner import copy_to_clipboard, generate_banner
from .mosaic import image_to_mosaic, mosaic_to_text
from .palettes import list_palettes

console = Console()


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """cli-pomodoro: Emoji art generator CLI tool.

    Create emoji mosaics from images or generate emoji text banners.
    """
    pass


@cli.command()
@click.argument("image", type=click.Path(exists=True))
@click.option("--density", "-d", type=click.IntRange(1, 100), default=30, help="Grid cell count per row (1-100)")
@click.option("--palette", "-p", type=click.Choice(list_palettes()), default="apple", help="Emoji palette")
@click.option("--format", "-f", type=click.Choice(["png", "text"]), default="png", help="Output format")
@click.option("--width", "-w", type=int, default=60, help="Character width for text output")
@click.option("--copy", is_flag=True, help="Copy output to clipboard")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def mosaic(
    image: str,
    density: int,
    palette: str,
    format: str,
    width: int,
    copy: bool,
    output: Optional[str],
) -> None:
    """Convert an image to an emoji mosaic."""
    console.print(f"[dim]Processing {image}...[/dim]")

    try:
        if format == "text":
            result = mosaic_to_text(image, density=density, palette_name=palette, width=width)
            if copy:
                copy_to_clipboard(result)
                console.print("[green]Copied to clipboard![/green]")
            console.print(result)
        else:
            out_path = output or image.replace(Path(image).suffix, "_emoji.png")
            image_to_mosaic(image, density=density, palette_name=palette, output_path=out_path)
            console.print(f"[green]Saved to {out_path}[/green]")
            if copy:
                console.print("[dim]Use --format text --copy for clipboard[/dim]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


@cli.command()
@click.argument("text", type=str)
@click.option("--style", "-s", type=click.Choice(["block", "rainbow", "shadow"]), default="block", help="Banner style")
@click.option("--copy", is_flag=True, help="Copy output to clipboard")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--font-size", type=int, default=48, help="Font size for PNG output")
def banner(
    text: str,
    style: str,
    copy: bool,
    output: Optional[str],
    font_size: int,
) -> None:
    """Generate an emoji banner from text."""
    try:
        result = generate_banner(text, style=style, output_path=output, font_size=font_size)
        if output:
            console.print(f"[green]Saved to {output}[/green]")
        else:
            if copy:
                copy_to_clipboard(result)
                console.print("[green]Copied to clipboard![/green]")
            console.print(result)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    cli()
