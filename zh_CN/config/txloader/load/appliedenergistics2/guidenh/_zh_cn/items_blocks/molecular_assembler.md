---
navigation:
  parent: /items_blocks_index.md
  title: Molecular Assembler
  icon: appliedenergistics2:tile.BlockMolecularAssembler
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockMolecularAssembler
---

# Molecular Assembler

<ItemImage id="appliedenergistics2:tile.BlockMolecularAssembler" scale="8" />

The molecular assembler takes item inputs and performs the operation defined by an adjacent <ItemLink id="appliedenergistics2:tile.BlockInterface" /> or by an inserted <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" />, <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />, or <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" />. It pushes results to adjacent inventories.

The assembler below contains a pattern for “1 oak log = 4 oak planks”. Feed oak logs into the upper hopper and it will craft, then eject oak planks into the lower hopper.

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Main Use

The main use of a molecular assembler is next to an <ItemLink id="appliedenergistics2:tile.BlockInterface" />. An interface sends the relevant pattern and ingredients to adjacent assemblers. Because assemblers automatically eject results to adjacent inventories (the interface return slot), an assembler next to an interface is sufficient to automate crafting patterns.

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Upgrades

The molecular assembler supports <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> (the acceleration card).

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockMolecularAssembler" />


