from ome_zarr_models.common.image_label_types import (
    RGBA,
    # Color,
    # LabelBase,
    # Property,
    # Source,
    # Uint8,
)
from yaozarrs.v05 import ImageLabel as LabelBase
from yaozarrs.v05 import Label
from yaozarrs.v05 import LabelColor as Color
from yaozarrs.v05 import LabelProperty as Property
from yaozarrs.v05 import LabelSource as Source
from yaozarrs.v05._label import Uint8

__all__ = ["RGBA", "Color", "Label", "LabelBase", "Property", "Source", "Uint8"]


# class Label(LabelBase):
#     """
#     Metadata for a single image-label.
#     """

#     version: Literal["0.5"] | None = None
