---
navigation:
  parent: /items_blocks_index.md
  title: ME Fluid Import Bus
  icon: ae2fc:part_fluid_import
categories:
- devices
item_ids:
- ae2fc:part_fluid_import
---

# ME Fluid Import Bus

<ItemImage id="ae2fc:part_fluid_import" scale="4" />

*"Mysterious power from AE2FC"*

The import bus extracts items and fluids from an adjacent container (and additional material types when supported by an
addon) and stores them in [network storage](../ae2_mechanics/import_export_storage.md).

To reduce latency, the bus enters a low-frequency sleep mode when it has not imported anything recently. Importing an item
wakes it and returns it to full speed, performing four operations per second.

It is a [cable subpart](../ae2_mechanics/cables_subparts.md).

## Filter Settings

By default, all accessible items are imported. Adding an item to a filter slot enables whitelist mode and permits only that
item. Items can be dragged from NEI into a filter slot even when you do not own them. Right-click a fluid container, such as
a bucket or tank, to set a fluid filter instead of filtering the container item.

## Upgrade Support

The bus supports these [upgrade cards](upgrade_cards.md):

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> increases the number of filter slots.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> increases the amount transferred per operation.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> changes the filter to a blacklist.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> adds redstone control (high, low, or pulse activation).

## Transfer Rate

| Speed cards | Amount per operation |
| :--- | :--- |
| 0 | 1 |
| 1 | 8 |
| 2 | 32 |
| 3 | 64 |
| 4 | 96 |

## Recipe

<RecipeFor id="ae2fc:part_fluid_import" />


