"""Tests for mosaic module."""

import os
import tempfile
from pathlib import Path

import pytest
from PIL import Image

from cli_pomodoro.mosaic import image_to_mosaic, mosaic_to_text


@pytest.fixture
def temp_image():
    """Create a temporary test image."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        img = Image.new("RGB", (100, 100), (255, 0, 0))
        img.save(f.name)
        yield f.name
    os.unlink(f.name)


def test_image_to_mosaic_png_output(temp_image):
    """Test mosaic generation to PNG."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        output = image_to_mosaic(temp_image, density=10, output_path=f.name)
        assert Path(output).exists()
        os.unlink(output)


def test_image_to_mosaic_text_output(temp_image):
    """Test mosaic generation to text."""
    result = image_to_mosaic(temp_image, density=10)
    assert isinstance(result, str)
    assert "\n" in result


def test_mosaic_to_text(temp_image):
    """Test text output with width parameter."""
    result = mosaic_to_text(temp_image, density=10, width=30)
    assert isinstance(result, str)


def test_mosaic_tiny_image():
    """Test that tiny images raise error."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        img = Image.new("RGB", (5, 5), (255, 0, 0))
        img.save(f.name)
        with pytest.raises(ValueError, match="too small"):
            image_to_mosaic(f.name, density=10)
        os.unlink(f.name)
