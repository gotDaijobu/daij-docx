# encoding: utf-8

"""
Provides objects that can characterize image streams as to content type and
size, as a required step in including them in a document.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from daijdocx.image.bmp import Bmp
from daijdocx.image.gif import Gif
from daijdocx.image.jpeg import Exif, Jfif
from daijdocx.image.png import Png
from daijdocx.image.tiff import Tiff
from daijdocx.image.emf import Emf

SIGNATURES = (
    # class, offset, signature_bytes
    (Png,  0, b'\x89PNG\x0D\x0A\x1A\x0A'),
    (Jfif, 6, b'JFIF'),
    (Exif, 6, b'Exif'),
    (Gif,  0, b'GIF87a'),
    (Gif,  0, b'GIF89a'),
    (Tiff, 0, b'MM\x00*'),  # big-endian (Motorola) TIFF
    (Tiff, 0, b'II*\x00'),  # little-endian (Intel) TIFF
    (Bmp,  0, b'BM'),
    (Emf,  40, b' EMF')
)
