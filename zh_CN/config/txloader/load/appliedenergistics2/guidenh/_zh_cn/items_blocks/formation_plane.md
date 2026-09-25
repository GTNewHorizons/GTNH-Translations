---
navigation:
  parent: /items_blocks_index.md
  title: ME Formation Plane
  icon: appliedenergistics2:item.ItemMultiPart:320
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:320
---

# Formation Plane

<Row gap="20">
<ItemImage id="appliedenergistics2:item.ItemMultiPart:320" scale="4" />
<ItemImage id="ae2fc:part_fluid_formation_plane" scale="4" />
</Row>

The formation plane places blocks and drops items. It works like an insert-only <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />, placing or dropping items when [devices](../ae2_mechanics/devices.md) insert them into [network storage](../ae2_mechanics/import_export_storage.md), such as an <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> or <ItemLink id="appliedenergistics2:tile.BlockInterface" />.

<GameScene width="350" height="220" zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

This device uses the same mechanics as storage buses in [pipe subnet](../tricks_example/pipe_subnet.md) setups and can replace them when you want to place blocks or drop items instead of transporting them.

They are [cable subparts](../ae2_mechanics/cables_subparts.md).

**Enable fake players in your chunk claim.**

## Filtering

By default, the plane places or drops anything. Items in filter slots form a whitelist. Items and fluids can be dragged from NEI; right-clicking with a fluid container selects the fluid.

## Priority

Click the wrench in the top-right of the GUI to set priority. Items entering the network start at the highest-priority storage.

## Settings

* The plane can place blocks in-world or drop items.

## Upgrades

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> increases filter slots.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> enables fuzzy matching and NBT-ignoring filters.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> switches whitelist filtering to a blacklist.

## Recipe

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:320" />

