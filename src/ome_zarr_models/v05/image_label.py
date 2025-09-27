from typing import ClassVar, Self

# Import needed for pydantic type resolution
import pydantic_zarr  # noqa: F401
import zarr
from pydantic import ConfigDict, Field

from ome_zarr_models.v05.base import BaseGroupv05
from ome_zarr_models.v05.image import Image
from yaozarrs.v05 import Image as ImageAttrs
from yaozarrs.v05 import ImageLabel as Label

__all__ = ["ImageLabel", "ImageLabelAttrs"]


class ImageLabelAttrs(ImageAttrs):
    """
    Attributes for an image label object.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(validate_by_name=True)

    image_label: Label | None = Field(alias="image-label", default=None)


class ImageLabel(BaseGroupv05[ImageLabelAttrs]):
    """
    An OME-Zarr image label dataset.
    """

    @classmethod
    def from_zarr(cls, group: zarr.Group) -> Self:  # type: ignore[override]
        """
        Create an instance of an OME-Zarr image from a `zarr.Group`.

        Parameters
        ----------
        group : zarr.Group
            A Zarr group that has valid OME-Zarr image label metadata.
        """
        # Use Image.from_zarr() to validate multiscale metadata
        image = Image.from_zarr(group)
        return cls(attributes=image.attributes.model_dump(), members=image.members)
