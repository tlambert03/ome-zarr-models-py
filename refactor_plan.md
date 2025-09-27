# OME-Zarr Models Refactor Plan

## Objective
Replace BaseOMEAttrs subclasses in ome_zarr_models with corresponding pure models from yaozarrs.

## Model Mapping Analysis

### V05 Models to Replace
| ome_zarr_models (BaseOMEAttrs) | yaozarrs equivalent | Notes |
|-------------------------------|---------------------|-------|
| `ImageAttrs` (v05/image.py:21) | `Image` (v05/_image.py:325) | Direct 1:1 mapping |
| `LabelsAttrs` (v05/labels.py:78) | `LabelsGroup` (v05/_label.py:76) | Direct mapping for labels container |
| `WellAttrs` (v05/well.py:10) | `Well` (v05/_well.py:31) | Direct 1:1 mapping |
| `HCSAttrs` (v05/hcs.py:17) | `Plate` (v05/_plate.py:142) | HCS uses Plate model |
| `ImageLabelAttrs` (v05/image_label.py:16) | `ImageLabel` (v05/_label.py:55) | Direct 1:1 mapping |

### V06 Models to Replace
| ome_zarr_models (BaseOMEAttrs) | yaozarrs equivalent | Notes |
|-------------------------------|---------------------|-------|
| `ImageAttrs` (_v06/image.py:21) | `Image` (v05/_image.py:325) + version override | Use v05 model with version="0.6" |
| `LabelsAttrs` (_v06/labels.py:78) | `LabelsGroup` (v05/_label.py:76) + version override | Use v05 model |
| `WellAttrs` (_v06/well.py:10) | `Well` (v05/_well.py:31) + version override | Use v05 model |
| `HCSAttrs` (_v06/hcs.py:17) | `Plate` (v05/_plate.py:142) + version override | Use v05 model |
| `ImageLabelAttrs` (_v06/image_label.py:16) | `ImageLabel` (v05/_label.py:55) + version override | Use v05 model |

### V04 Models
No BaseOMEAttrs subclasses found in v04 - different architecture, no changes needed.

## Refactor Strategy

### Phase 1: V05 Models
1. **ImageAttrs → Image**
   - File: `src/ome_zarr_models/v05/image.py`
   - Replace: `class ImageAttrs(BaseOMEAttrs):`
   - With: `from yaozarrs.v05 import Image as ImageAttrs`
   - Remove the class definition

2. **LabelsAttrs → LabelsGroup**
   - File: `src/ome_zarr_models/v05/labels.py`
   - Replace: `class LabelsAttrs(BaseOMEAttrs):`
   - With: `from yaozarrs.v05 import LabelsGroup as LabelsAttrs`
   - Remove the class definition

3. **WellAttrs → Well**
   - File: `src/ome_zarr_models/v05/well.py`
   - Replace: `class WellAttrs(BaseOMEAttrs):`
   - With: `from yaozarrs.v05 import Well as WellAttrs`
   - Remove the class definition

4. **HCSAttrs → Plate**
   - File: `src/ome_zarr_models/v05/hcs.py`
   - Replace: `class HCSAttrs(BaseOMEAttrs):`
   - With: `from yaozarrs.v05 import Plate as HCSAttrs`
   - Remove the class definition

5. **ImageLabelAttrs → ImageLabel**
   - File: `src/ome_zarr_models/v05/image_label.py`
   - Replace: `class ImageLabelAttrs(BaseOMEAttrs):`
   - With: `from yaozarrs.v05 import ImageLabel as ImageLabelAttrs`
   - Remove the class definition

### Phase 2: V06 Models
For v06, we'll need to create wrapper classes or modify the yaozarrs models to support version="0.6":

1. **Create V06 wrapper models** (if needed)
   - Copy yaozarrs v05 models but with `version: Literal["0.6"]`
   - Or find a way to parameterize the version in yaozarrs models

2. **Replace v06 BaseOMEAttrs subclasses** with the same pattern as v05

### Phase 3: Testing and Validation
1. Run tests after each file change
2. Ensure all imports are correct
3. Verify that the API remains the same from the outside
4. Check that serialization/deserialization works correctly

## Implementation Order
1. Start with v05/image.py (simplest case)
2. Move to v05/well.py
3. Then v05/image_label.py
4. Handle v05/labels.py (might be more complex due to validation logic)
5. Handle v05/hcs.py (might be more complex due to plate logic)
6. Address v06 models (decide on strategy first)
7. Run full test suite
8. Code review

## Potential Issues to Watch For
1. **Import dependencies**: Some files may import the old models
2. **Type annotations**: Ensure type hints remain correct
3. **Validation logic**: Some BaseOMEAttrs may have custom validation
4. **Version handling**: v06 models need special handling since yaozarrs only has v04/v05
5. **Backwards compatibility**: External API should remain the same

## Testing Strategy
- Run `uv run pytest` after each model replacement
- Focus on integration tests that use the models
- Verify JSON serialization/deserialization still works
- Check that zarr-python integration still works correctly

## Success Criteria
- All tests pass
- External API remains unchanged
- Models are now "pure" (don't require zarr-python for validation)
- Can validate JSON documents directly without zarr-python