---
navigation:
  parent: /items_blocks_index.md
  title: ME Fluid Export Bus
  icon: ae2fc:part_fluid_export
categories:
- devices
item_ids:
- ae2fc:part_fluid_export
---

# ME Fluid Export Bus

<ItemImage id="ae2fc:part_fluid_export" scale="4" />

*"Mysterious power from AE2FC"*

This device extracts items and fluids (and additional material types when supported by an addon) from [network
storage](../ae2_mechanics/import_export_storage.md) and pushes them into the attached container.

To reduce overhead, the bus enters a low-frequency sleep mode when it has been inactive recently. After a successful
export it returns to full speed, performing four operations per second.

It is a [cable subpart](../ae2_mechanics/cables_subparts.md).

## Filter Settings

By default, nothing is exported. Adding an item to a filter slot creates a whitelist and permits only the selected item.
Items and fluids can be dragged directly from NEI into a filter slot, even when you do not currently have them.
Right-click a fluid container, such as a bucket or tank, to set a fluid filter rather than filtering the container itself.

## Upgrade Support

The bus supports these [upgrade cards](upgrade_cards.md):

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> increases the number of filter slots.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> increases the amount transferred per operation.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> changes the filter to a blacklist.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> requests [autocrafting](../ae2_mechanics/autocrafting.md), with options to use stored items first or always craft new ones.
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

<RecipeFor id="ae2fc:part_fluid_export" />


