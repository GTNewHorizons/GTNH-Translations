---
navigation:
  parent: /items_blocks_index.md
  title: Inscriber
  icon: appliedenergistics2:tile.BlockInscriber
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockInscriber
---

# Inscriber

<ItemImage id="appliedenergistics2:tile.BlockInscriber" scale="4" />

The inscriber presses circuit boards and [processors](processors.md) using [presses](presses.md), and can also crush several items into dust. It accepts AE2 energy (AE) and Fabric/Forge Energy (E/FE). In sided mode, items inserted from different sides enter different slots; use a <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> to rotate it. It can also push results to adjacent inventories.

The input buffer size is adjustable. Use a small buffer when feeding many inscribers from one inventory so materials are distributed more evenly.

The four circuit presses craft [processors](processors.md):

<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="4" />
</Row>

The name press can name items like an anvil, which is useful for labeling things in a <ItemLink id="appliedenergistics2:item.ItemMultiPart:500" />.

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:21" scale="4" />

## Settings

* Sided mode routes input and extraction by side. In non-sided mode, an internal filter chooses the target slot, but the top and bottom slots cannot be extracted.
* Results can be pushed to adjacent inventories.
* The input buffer can be large for manual feeding or small for large parallel setups.

## GUI And Sidedness

In sided mode, the side used for insertion or extraction selects the slot.

![Inscriber GUI](../assets/images/inscriber_gui.png) ![Inscriber sides](../assets/images/inscriber_sides.png)

A. **Top input** is accessed from the top (items can be inserted and extracted).

B. **Center input** is accessed from the left, right, front, and rear (items can be inserted but not extracted).

C. **Bottom input** is accessed from the bottom (items can be inserted and extracted).

D. **Output** is extracted from the left, right, front, and rear (items can be extracted but not inserted).

## Simple Automation

Sidedness and rotation allow semi-automated setups:

<GameScene width="350" height="220" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/inscriber_hopper_automation.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Alternatively, pipe items into and out of the inscriber in non-sided mode.

## Upgrades

The inscriber supports <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> (the acceleration card).

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockInscriber" />


