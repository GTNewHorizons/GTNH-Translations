---
navigation:
  parent: /items_blocks_index.md
  title: Pattern
  icon: appliedenergistics2:item.ItemMultiMaterial:52
  position: 410
categories:
- tools
item_ids:
- appliedenergistics2:item.ItemMultiMaterial:52
---

# Patterns

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:52" scale="4" />

Patterns are made in an <ItemLink id="appliedenergistics2:item.ItemMultiPart:340" /> from blank patterns. They can be
placed in <ItemLink id="appliedenergistics2:tile.BlockInterface" />s and <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />s.

There are several types of pattern for different processing methods:

*   <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" />s encode crafting-table recipes. They can be placed directly
    in a <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> to craft the result when ingredients are inserted,
    but their main use is in an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> next to a molecular assembler.
    ME Interfaces send the pattern and its ingredients to adjacent assemblers, which automatically eject their results.

*   <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />s are processing patterns and provide the most
    flexibility. They only state that, if an ME Interface sends the listed inputs to adjacent inventories, the ME network
    will receive the listed outputs at some point. The machine or process between the inputs and outputs does not matter.

The source also registers <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" />, a processing-pattern variant used
only by tunnel-pattern setups.

Multiple interfaces with identical patterns work in parallel. A pattern can also represent a whole batch, such as
8 cobblestone = 8 stone instead of 1 cobblestone = 1 stone, so the interface sends eight inputs per operation.

This fork also adds the <ItemLink id="appliedenergistics2:item.ItemMultiPart:473" />. Place a pair facing each other on
separate ME networks, then use a Certus Quartz Wrench on a repeater to switch it between **Provider** and **Accessor**
mode. The Provider mirrors the crafting patterns and craftable items from the network in front of it, allowing the other
network to use them for autocrafting. Both repeaters must be connected to powered ME networks.

## Recipes

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:52" />
