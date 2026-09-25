---
navigation:
  parent: /items_blocks_index.md
  title: ME Interface
  icon: appliedenergistics2:tile.BlockInterface
item_ids:
  - appliedenergistics2:tile.BlockInterface
  - ae2fc:fluid_interface
categories:
- devices
---

# ME Interface

<Row gap="20">
<BlockImage id="appliedenergistics2:tile.BlockInterface" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:440" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:471" scale="4" />
</Row>

An interface acts as a small chest and fluid tank. It inserts and extracts from [network storage](../ae2_mechanics/import_export_storage.md) according to the stock levels configured in its slots. It attempts to complete transfers in one game tick, up to nine item stacks per tick, making it a fast input/output method.

Unlike most fluid tanks, an interface can store up to nine fluid types as well as items. It is effectively a chest or multi-fluid tank with additional network behavior; disconnecting it from a network disables that behavior. This makes interfaces useful when a small amount of many different things must be stored.

## How An Interface Works Internally

An interface is essentially a chest/tank with <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />, and <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> attached.

<GameScene width="450" height="200" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_internals.snbt" />
  <BoxAnnotation color="#dddddd" min="2.3 0.3 1.3" max="9.7 1 1.7">Level emitters control the stocking quantity</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 4 1.3" max="9.7 4.7 1.7">Level emitters control the stocking quantity</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 1.3 1.3" max="9.7 2 1.7">Import buses transfer one stack per game tick</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 3 1.3" max="9.7 3.7 1.7">Export buses transfer one stack per game tick</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2 2 1" max="10 3 2">Nine independent internal slots</BoxAnnotation>
  <IsometricCamera yaw="15" pitch="15" />
</GameScene>

## Special Interactions

Connecting a <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> to an unconfigured interface exposes the entire [network storage](../ae2_mechanics/import_export_storage.md) of the interface's network to the storage-bus network. The interface network behaves like one large chest. Setting an item in an interface request slot disables this behavior.

An interface connected to another interface can form a [subnetwork](../ae2_mechanics/subnetworks.md): when the source interface has no request, it skips its own inventory and sends items directly to storage on the destination subnetwork, waiting if that storage cannot accept the next batch.

## Variants

Interfaces have normal and flat/[subpart](../ae2_mechanics/cables_subparts.md) variants. Normal interfaces output and receive on all sides and provide network connections. Flat interfaces are cable subparts, so several can share one cable; they can exchange items with their own storage but do not provide a network connection. The two forms can be converted in a crafting grid.

## Settings

The top row configures items to keep in stock. Items can be placed directly or dragged from NEI; click the wrench above a populated slot to set its amount. Right-click with a fluid container to set the fluid as a filter instead of the container item. A slot configured for stocking will not accept other items.

## Upgrades

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> enables fuzzy matching and NBT-ignoring filters.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> lets the interface request missing ingredients from the [autocrafting](../ae2_mechanics/autocrafting.md) system.

## Priority

Click the wrench in the top-right of the GUI to set priority. Higher-priority interfaces obtain items before lower-priority interfaces.

## Recipe

<Row>
<Recipe id="appliedenergistics2:tile.BlockInterface" />
<RecipeFor id="appliedenergistics2:item.ItemMultiPart:440" />
</Row>

