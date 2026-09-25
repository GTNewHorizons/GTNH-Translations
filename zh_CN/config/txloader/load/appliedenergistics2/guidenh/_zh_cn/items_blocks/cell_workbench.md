---
navigation:
  parent: /items_blocks_index.md
  title: Cell Workbench
  icon: appliedenergistics2:tile.BlockCellWorkbench
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockCellWorkbench
---

# Cell Workbench

<ItemImage id="appliedenergistics2:tile.BlockCellWorkbench" scale="4" />

The Cell Workbench can be used to configure [storage cells](storage_cells.md) and <ItemLink id="appliedenergistics2:item.ItemViewCell" />.

You can install [upgrade cards](upgrade_cards.md) into cells, or configure "partitions" to restrict the types of items the cell can store.

If you do not have the required item or fluid, you can drag it from NEI to place it into the filter slot.

Using a fluid container, such as an iron bucket or fluid tank, while pressing <Color id="YELLOW"><KeyBind id="key.container_interaction.desc" /></Color> will set the fluid as the filter instead of the iron bucket or tank item.

## Settings

The Cell Workbench has several buttons in the top-left and top-right. Some buttons are displayed only for cells that support the corresponding feature:

* **Clear**: Clears all partition settings in the workbench.
* **Partition Storage**: Automatically fills the partition slots based on the items currently stored in the cell.
* **Copy Mode**: Determines whether the workbench's partition settings are retained when the cell is removed. They are cleared by default. When retention is enabled, the same partition settings can be copied to other cells. If the new cell already has partition settings, the cell's own settings take priority.
* **Fuzzy Comparison**: Available when a <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" showIcon="left" linksTo="../items_blocks/upgrade_cards.md#Fuzzy Card"/> is installed. Adjusts how partitions perform fuzzy matching.
* **Ore Dictionary Filter**: Available when a <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" showIcon="left" linksTo="../items_blocks/upgrade_cards.md#Ore Dictionary Filter Card"/> is installed. Allows ore dictionary names to be entered for filtering. When enabled, the normal partition slots are hidden, and it takes priority over fuzzy mode.
* **Cell Restriction**: Click to open the restriction settings GUI:
  * **Maximum Item Count**: Limits the total number of items stored in the cell, rather than limiting each item type separately.
  * **Maximum Item Types**: Limits the number of different item types the cell can store.

  Entering `0` disables the corresponding restriction. Restriction values cannot exceed the cell's own capacity or maximum number of item types. Click the reset button to clear both restrictions.

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockCellWorkbench" />
