---
navigation:
  parent: /items_blocks_index.md
  title: Charger
  icon: appliedenergistics2:tile.BlockCharger
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockCharger
---

# Charger

<ItemImage id="appliedenergistics2:tile.BlockCharger" scale="4" />

The Charger can charge the tools it supports and <ItemLink id="gregtech:gt.metaitem.01:8516" />.

It must be supplied with power from its top or bottom. Both AE2 [cables](cables.md) and energy cables from other mods can be used. The Charger accepts both AE2 energy (AE) and Forge Energy (FE). Items can be inserted and extracted from all sides. Only completed products are extracted, so no filtering is required. The <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> can be used to rotate it for automation.

<ItemImage id="gregtech:gt.metaitem.01:8516" /><ItemLink id="gregtech:gt.metaitem.01:8516" /> can be charged into <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:1" />, or <ItemLink id="minecraft:compass" showIcon="left"/> can be transformed into <ItemLink id="appliedenergistics2:tile.BlockSkyCompass" showIcon="left"/>.

~~Placing an <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:46" /> on the top or bottom and right-clicking it with a hand crank allows items to be charged manually.~~

## Simple Automation

As shown below, the Charger's ability to rotate allows it to be semi-automated in the following way:

<GameScene zoom="4" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockCharger" />