---
navigation:
  parent: /items_blocks_index.md
  title: ME Fluid Interface
  icon: ae2fc:fluid_interface
item_ids:
  - ae2fc:fluid_interface
categories:
- devices
---

# ME Dual Fluid Interface

<Row gap="20">
<BlockImage id="ae2fc:fluid_interface" scale="4" />
<ItemImage id="ae2fc:part_fluid_interface" scale="4" />
<ItemImage id="ae2fc:part_fluid_p2p_interface" scale="4" />
</Row>

*"Mysterious power from AE2FC"*

An interface behaves like a small chest or fluid tank. Its configured slots can automatically be filled from or emptied
into [network storage](../ae2_mechanics/import_export_storage.md). It can process up to nine item groups per tick, and can
therefore provide fast input and output when paired with high-speed pipes.

It can store up to nine different fluids at once, unlike a normal tank that stores only one, while also storing items.
When disconnected from a network it continues to work as a normal container.

## Internal Operation

The interface is effectively a composite device containing multiple high-speed <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />
and <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> buses, plus multiple <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> level emitters:

<GameScene width="450" height="200" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_internals.snbt" />
  <BoxAnnotation color="#dddddd" min="2.3 0.3 1.3" max="9.7 1 1.7">Level emitters controlling stored quantities</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 4 1.3" max="9.7 4.7 1.7">Level emitters controlling stored quantities</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 1.3 1.3" max="9.7 2 1.7">High-speed import bus array, one item group per tick</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 3 1.3" max="9.7 3.7 1.7">High-speed export bus array, one item group per tick</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2 2 1" max="10 3 2">Nine independent storage slots</BoxAnnotation>
  <IsometricCamera yaw="15" pitch="15" />
</GameScene>

## Special Interactions

* Attaching an <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> to an unconfigured interface makes the storage bus
  access all [storage](../ae2_mechanics/import_export_storage.md) on the interface's network, as though it were attached to
  the network itself. Configuring any item in the interface disables this behavior.

<GameScene width="200" height="150" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_storage.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

* An unconfigured interface on a [subnetwork](../ae2_mechanics/subnetworks.md) lets a connected ME interface push directly
  into the subnetwork's storage, skipping the interface slots and waiting for available space before sending the next batch.

<GameScene width="320" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/fluid_interface_storage.snbt" />
  <BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">Interface (must be the flat variant)</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">Storage bus array</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">Target machines (multiple machines or input faces)</BoxAnnotation>
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Variants

Interfaces have a normal block form and a flat [cable subpart](../ae2_mechanics/cables_subparts.md):

* **Normal interface:** accepts and outputs items on every side and provides network connections on every side.
* **Flat interface:** can be placed densely on a cable, accepts and outputs only on its front, and does not provide a
  network connection on its front.

The two forms can be converted in a crafting grid.

## Settings

* The nine slots at the top define the item or fluid quantities to maintain.
* Right-click a fluid container, such as a bucket, to set a fluid filter.
* Click the wrench beside a slot to set its target quantity.

## Upgrade Support

The interface supports these [upgrade cards](upgrade_cards.md):

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> enables fuzzy matching (by damage value or ignoring NBT).
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> enables autocrafting requests, extracting stored items first
  and triggering [autocrafting](../ae2_mechanics/autocrafting.md) when storage is insufficient.

## Priority

Click the wrench in the top-right corner of the GUI to set priority. Higher-priority interfaces receive items first.

## Recipes

<Recipe id="ae2fc:fluid_interface" />

<RecipeFor id="ae2fc:part_fluid_interface" />

