"""Tests for banner module."""

import os
import tempfile
from pathlib import Path

import pytest

from cli_pomodoro.banner import generate_banner, text_to_fullwidth


def test_text_to_fullwidth():
    """Test ASCII to fullwidth conversion."""
    result = text_to_fullwidth("ABC")
    assert len(result) > 0


def test_text_to_fullwidth_numbers():
    """Test number conversion."""
    result = text_to_fullwidth("123")
    assert len(result) > 0


def test_generate_banner_block():
    """Test block style banner."""
    result = generate_banner("HELLO", style="block")
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_banner_png_output():
    """Test banner PNG output."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        output = generate_banner("HELLO", style="block", output_path=f.name)
        assert Path(output).exists()
        os.unlink(output)


def test_generate_banner_styles():
    """Test all banner styles."""
    for style in ["block", "rainbow", "shadow"]:
        result = generate_banner("TEST", style=style)
        assert isinstance(result, str)
