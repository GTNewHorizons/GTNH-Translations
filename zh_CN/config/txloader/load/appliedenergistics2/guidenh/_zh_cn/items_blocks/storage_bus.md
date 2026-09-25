---
navigation:
  parent: /items_blocks_index.md
  title: ME Storage Bus
  icon: appliedenergistics2:item.ItemMultiPart:220
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:220
- ae2fc:part_fluid_storage_bus
- thaumicenergistics:part.base:2
---

# Storage Bus

<Row gap="20">
<ItemImage id="appliedenergistics2:item.ItemMultiPart:220" scale="4" />
<ItemImage id="ae2fc:part_fluid_storage_bus" scale="4" />
<ItemImage id="thaumicenergistics:part.base:2" scale="4" />
</Row>

The storage bus turns the adjacent inventory into [network storage](../ae2_mechanics/import_export_storage.md). The network can see its contents and insert or extract items to satisfy [devices](../ae2_mechanics/devices.md).

By putting one or more storage buses on a [subnetwork](../ae2_mechanics/subnetworks.md) as its only storage, the buses can also act as sources or destinations for item transfer (see [Pipe Subnet](../tricks_example/pipe_subnet.md)). Large optimized inventories such as drawers are fine, but unoptimized inventories with many slots can hurt performance.

Storage buses are [cable subparts](../ae2_mechanics/cables_subparts.md).

## Filtering

By default, the bus stores everything. Items placed in filter slots form a whitelist. Items and fluids can be dragged into filters from NEI, and right-clicking with a fluid container sets the fluid rather than the container item.

## Priority

Click the wrench in the top-right of the GUI to set priority. Items enter the highest-priority storage first. For equal priorities, a storage that already contains the item is preferred; filtered storages count as already containing their filtered items. Extraction starts at the lowest priority.

## Settings

* The bus can be partitioned to the current contents of the adjacent inventory.
* You can choose whether items that the bus cannot extract remain visible to the network (for example, the middle input slot of an <ItemLink id="appliedenergistics2:tile.BlockInscriber" />).
* Filtering can apply to insertion and extraction, or insertion only.
* The bus can be bidirectional, insert-only, or extract-only.

## Upgrades

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> increases filter slots.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> enables fuzzy matching and NBT-ignoring filters.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> switches the whitelist to a blacklist.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" /> filters by ore-dictionary name.

## Recipe

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:220" />


