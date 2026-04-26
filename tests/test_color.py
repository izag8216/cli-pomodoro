"""Tests for color module."""

import pytest
from cli_pomodoro.color import ciede2000, find_closest_emoji, rgb_to_lab


def test_rgb_to_lab():
    """Test RGB to Lab conversion."""
    L, a, b = rgb_to_lab((255, 0, 0))
    assert L > 0
    assert a > 0


def test_ciede2000_same_color():
    """Test CIEDE2000 distance for identical colors."""
    distance = ciede2000((255, 0, 0), (255, 0, 0))
    assert distance == 0.0


def test_ciede2000_different_colors():
    """Test CIEDE2000 distance for different colors."""
    distance = ciede2000((255, 0, 0), (0, 0, 255))
    assert distance > 0


def test_find_closest_emoji():
    """Test finding closest emoji from palette."""
    palette = ["\U0001F3B2", "\U0001F308"]
    result = find_closest_emoji((100, 100, 100), palette)
    assert result in palette


def test_find_closest_emoji_empty_palette():
    """Test with empty palette returns fallback."""
    result = find_closest_emoji((100, 100, 100), [])
    assert result == "\u2588"
