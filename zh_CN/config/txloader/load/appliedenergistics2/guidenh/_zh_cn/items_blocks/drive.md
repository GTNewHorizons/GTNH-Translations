---
navigation:
  parent: /items_blocks_index.md
  title: ME Drive
  icon: appliedenergistics2:tile.BlockDrive
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockDrive
---

# ME Drive

<ItemImage id="appliedenergistics2:tile.BlockDrive" scale="4" />

The ME Drive is a [device](../ae2_mechanics/devices.md) for holding [storage cells](storage_cells.md). Cells inside
the drive count as [network storage](../ae2_mechanics/import_export_storage.md), and it has ten slots for individual cells.

Cells can be inserted or extracted with any logistics method, such as hoppers or AE2 buses.

The drive can be rotated with a <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" />.

## Cell Status LEDs

The LEDs on cells in the drive show their current status:

| Color | Status |
| :--- | :--- |
| Green | Empty |
| Blue | Contains items |
| Orange | [Types](../ae2_mechanics/bytes_and_types.md) are full; no new types can be added |
| Red | [Bytes](../ae2_mechanics/bytes_and_types.md) are full; no new items can be added |
| Black | No power or the drive has no [channel](../ae2_mechanics/channels.md) |

## Priority

Click the wrench in the top-right corner of the GUI to set a priority. Items entering the network prefer the highest
priority storage location. If two locations have the same priority, the one that already contains the item is preferred.
Partitioned cells from the [Cell Workbench](cell_workbench.md) count as already containing their partitioned items when
priorities are equal. Items leaving storage are extracted from the lowest-priority location first. This fills high-priority
storage while emptying low-priority storage during normal import and export.

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockDrive" />


