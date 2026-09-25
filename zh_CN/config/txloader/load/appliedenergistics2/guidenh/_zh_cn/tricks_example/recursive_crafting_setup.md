---
navigation:
  parent: ../tricks_example_index.md
  title: Recursive Crafting
  icon: witchery:ingredient:130
---

# Recursive Crafting Setup

As mentioned in [Autocrafting](../ae2_mechanics/autocrafting.md), the autocrafting planner cannot handle a recipe whose primary output is also an input. For example, it cannot handle the recipe that duplicates <ItemLink id="witchery:ingredient:130" />.

One solution is to use an <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> as a [pattern](../items_blocks/patterns.md).

The standard level emitter can then be used to start a small setup that crafts continuously. This section uses a setup that duplicates <ItemImage id="witchery:ingredient:130" /><ItemLink id="witchery:ingredient:130" /> as an example.

<RecipeFor id="witchery:ingredient:130" />

***

<GameScene zoom="6" width="350" interactive={true}>
  <ImportStructure src="../assets/structures/recursive_recipe_setup.snbt" />
  <IsometricCamera yaw="15" pitch="30" />
  <DiamondAnnotation pos="3.5 0.5 1.5" color="#00ff00">
    To the main network
  </DiamondAnnotation>
  <BlockAnnotation pos="2 0 1">
    (1) Interface: configure it to store the extra materials required: magma cream, blaze powder, and a Small Pile of Nether Star Dust.
    <Row>
      <ItemImage id="minecraft:magma_cream" scale="2" />
      <ItemImage id="minecraft:blaze_powder" scale="2" />
      <ItemImage id="gregtech:gt.metaitem.01:506" scale="2" />
    </Row>
  </BlockAnnotation>
  <BlockAnnotation pos="0 0 0">
    (5) Molecular Assembler: contains the pattern for duplicating <ItemLink id="witchery:ingredient:130" />.
    <Row><RecipeFor id="witchery:ingredient:130" /></Row>
    One ingredient must be placed in it manually when setting it up.
  </BlockAnnotation>
  <BoxAnnotation min="1.3 1 1.3" max="1.7 1.3 1.7">
    (2) Standard level emitter: configure it for “<ItemLink id="witchery:ingredient:130" />” and set it to “emit a redstone signal to craft the item”.
    <Row>
      <ItemImage id="witchery:ingredient:130" scale="2" />
      <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />
    </Row>
  </BoxAnnotation>
  <BoxAnnotation min="1.7 0 1" max="2 1 2">
    (3) Import bus #1: filter it to the items stored in the interface. Install a redstone card. Set the redstone mode to “active with a redstone signal”.
    <Row>
      <ItemImage id="minecraft:magma_cream" scale="2" />
      <ItemImage id="minecraft:blaze_powder" scale="2" />
      <ItemImage id="gregtech:gt.metaitem.01:506" scale="2" />
      <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" />
    </Row>
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1">
    (6) Import bus #2: default configuration.
  </BoxAnnotation>
  <BoxAnnotation min="0 1 0" max="1 1.3 1">
    (4) Storage bus #1: priority higher than the other storage bus. This is very important.
  </BoxAnnotation>
  <BoxAnnotation min="2 0 0.7" max="3 1 1">
    (7) Storage bus #2: filter “<ItemLink id="witchery:ingredient:130" />”. Its priority is lower than the other storage bus.
    <Row>
      <ItemImage id="witchery:ingredient:130" scale="2" />
    </Row>
  </BoxAnnotation>
</GameScene>

## Configuration

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) Configure it to store the extra materials required: magma cream, blaze powder, and a Small Pile of Nether Star Dust.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (2) Configure it for “<ItemLink id="witchery:ingredient:130" />” and set it to “emit a redstone signal to craft the item”.
* The first <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (3) is set to filter the items stored in the interface. Install a redstone card and set the redstone mode to “active with a redstone signal”.
* The priority of the first <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (4) must be *higher* than that of the second storage bus. See [Priority](../ae2_mechanics/import_export_storage.md#storage-priority).
* The <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> (5) contains the pattern for duplicating <ItemLink id="witchery:ingredient:130" /> and one manually inserted <ItemLink id="witchery:ingredient:130" />.

  *Pattern*
  <RecipeFor id="witchery:ingredient:130" />

* The second <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (6) uses the default configuration.
* The second <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (7) is filtered to “<ItemLink id="witchery:ingredient:130" />”. Its [priority](../ae2_mechanics/import_export_storage.md#storage-priority) is *lower* than that of the first storage bus.

## How It Works

1. Because it contains an <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> and is set to “emit a redstone signal to craft the item”, the <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> acts as a [pattern](../items_blocks/patterns.md). “<ItemLink id="witchery:ingredient:130" />” appears in the [terminal](../items_blocks/terminals.md) as an item that can be [autocrafted](../ae2_mechanics/autocrafting.md).
2. When a crafting request is received from a player or the system, the standard level emitter turns on.
3. The first <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> is activated by the standard level emitter and extracts the materials from the <ItemLink id="appliedenergistics2:tile.BlockInterface" />.
4. The only <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> in the network that can store these materials is the one on the assembler.
5. The <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> receives the materials (with one <ItemLink id="witchery:ingredient:130" /> already inside), starts crafting, and produces two <ItemLink id="witchery:ingredient:130" />.
6. The second <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> extracts one <ItemLink id="witchery:ingredient:130" />.
7. The first storage bus has the higher priority, so <ItemLink id="witchery:ingredient:130" /> returns to the assembler.
8. The second <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> extracts one <ItemLink id="witchery:ingredient:130" />.
9. The assembler can no longer accept <ItemLink id="witchery:ingredient:130" />, so the second <ItemLink id="witchery:ingredient:130" /> enters the lower-priority storage bus and is sent to the interface.
10. The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (which is not configured to store <ItemLink id="witchery:ingredient:130" />) sends it back to the network.
