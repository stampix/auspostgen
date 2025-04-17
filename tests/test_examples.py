"""Tests for the example barcodes from the original repository."""

import os

from auspostgen import build_barcode, write_barcode_to_image_file


def test_example_barcode37(tmp_path):
    """Test generation of version 37 barcode."""
    output_path = tmp_path / "my-barcode37.png"

    # Generate the barcode
    barcode = build_barcode("11", "59564391")
    write_barcode_to_image_file(barcode, str(output_path))

    # Verify the file was created and has content
    assert output_path.exists()
    assert os.path.getsize(output_path) > 0


def test_example_barcode52(tmp_path):
    """Test generation of version 52 barcode."""
    output_path = tmp_path / "my-barcode52.png"

    # Generate the barcode
    barcode = build_barcode("59", "59564391", "11ABA")
    write_barcode_to_image_file(barcode, str(output_path))

    # Verify the file was created and has content
    assert output_path.exists()
    assert os.path.getsize(output_path) > 0


def test_example_barcode67(tmp_path):
    """Test generation of version 67 barcode."""
    output_path = tmp_path / "my-barcode67.png"

    # Generate the barcode
    barcode = build_barcode("62", "59564391", "11ABA11ABA")
    write_barcode_to_image_file(barcode, str(output_path))

    # Verify the file was created and has content
    assert output_path.exists()
    assert os.path.getsize(output_path) > 0
