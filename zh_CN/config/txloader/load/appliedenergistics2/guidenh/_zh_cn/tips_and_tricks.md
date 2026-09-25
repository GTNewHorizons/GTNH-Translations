---
navigation:
  title: Tips and Tricks
  position: 20
---

# Tips and Tricks

A load of random little recommendations

* Remove Optifine.
* You can rotate and zoom into guidebook scenes that have the zoom and annotation hide/show buttons.
* Keep your network treelike and avoid loops.
* Keep full-block [devices](ae2_mechanics/devices.md) in groups of 8 or less unless you deeply understand how [channels](ae2_mechanics/channels.md) route through a network.
* Pick a wood and stick with it for all your [patterns](items_blocks/patterns.md). Enabling substitutions sometimes works, but using the same wood type everywhere greatly reduces hassle.
* Add an [energy cell](items_blocks/energy_cells.md) so that your network can handle power spikes.
* You can use water in the <ItemLink id="appliedenergistics2:tile.BlockCondenser" />.
* The best way to keep your network clean is to not put random mob loot like swords and armor in. Each unique combination of enchantment and durability is another [type](ae2_mechanics/bytes_and_types.md).
* An "item entering system" event must occur when returning the result of a [processing pattern](items_blocks/patterns.md), like through an <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:tile.BlockInterface" />, or an interface return slot. You cannot just pipe the result into a chest with a <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> on it.
* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> pushes complete recipe batches to an adjacent inventory. This is useful for making sure machines do not receive partial batches, but sometimes you want the ingredients to go to multiple places. You can achieve this using multiple interfaces or an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> as a [pipe subnet](tricks_example/pipe_subnet.md).
