# Import needed for pydantic type resolution
import pydantic_zarr  # noqa: F401

from ome_zarr_models.v05.base import BaseGroupv05
from yaozarrs.v05 import Well as WellAttrs

__all__ = ["Well", "WellAttrs"]


class Well(BaseGroupv05[WellAttrs]):
    """
    An OME-Zarr well dataset.
    """
