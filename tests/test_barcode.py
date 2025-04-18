"""Tests for the barcode generation functionality."""

import os
from pathlib import Path

from src import build_barcode, write_barcode_to_image_file


def test_barcode_generation(tmp_path: Path) -> None:
    """Test that we can generate a barcode image."""
    output_path = tmp_path / "test_barcode.png"

    # Generate the barcode
    # write_image(str(output_path), "12345678901234567890", version=37)
    barcode = build_barcode(
        fcc_value="11",  # Standard letter
        dpid_value=12345678,  # 8-digit DPID
        customer_value=None,  # No customer value
    )

    # Write the barcode to an image file
    write_barcode_to_image_file(barcode, str(output_path))

    # Verify the file was created and has content
    assert output_path.exists()
    assert os.path.getsize(output_path) > 0
