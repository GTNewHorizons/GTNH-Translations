---
navigation:
  parent: /items_blocks_index.md
  title: ME-IO Port
  icon: appliedenergistics2:tile.BlockIOPort
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockIOPort
---

# ME I/O Port

<BlockImage id="appliedenergistics2:tile.BlockIOPort"/>

The I/O Port rapidly fills or empties [storage cells](storage_cells.md) from [network storage](../ae2_mechanics/import_export_storage.md). It can be rotated with a <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" />.

## Settings

* Move the cell to the output slot when it is empty, full, or when the operation completes.
* Install <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> for redstone conditions.
* The center arrow selects transfer direction: cell to network storage, or network storage to cell.

## Upgrades

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> increases the amount moved per operation.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> adds high, low, and pulse redstone control.

In a cold state it operates every 5 ticks, then every tick while hot. Each operation transfers 256 x 2^n items, where n is the number of acceleration cards.

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockIOPort" />

