"""
For reference, see the [plate section of the OME-Zarr specification](https://ngff.openmicroscopy.org/0.5/index.html#plate-md).
"""

from yaozarrs.v05 import Acquisition, Column, Row
from yaozarrs.v05 import PlateDef as Plate
from yaozarrs.v05 import PlateWell as WellInPlate

__all__ = [
    "Acquisition",
    "Column",
    "Plate",
    "Row",
    "WellInPlate",
]
