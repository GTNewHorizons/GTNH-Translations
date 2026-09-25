---
navigation:
  parent: ../tricks_example_index.md
  title: Level Emitter Autostocking
  icon: appliedenergistics2:item.ItemMultiPart:280
---

# Level Emitter Autostocking

One might ask "How do I keep a certain amount of an item in stock, crafting more as needed?"

One solution is use of an <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />, and <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> to automatically request new items
from your network's [autocrafting](../ae2_mechanics/autocrafting.md). This setup is for maintaining a large quantity of one item.

You can of course make your network craft continuously, by omitting the level emitter and redstone card.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
  (1) Export Bus: Filtered to the desired item. Has a Redstone Card and Crafting Card. Redstone mode set to
  "Active with signal", Crafting behavior set to "Do not use stocked items".
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
  (2) Level Emitter: Configured with the desired item and quantity, set to "Emit when levels are below limit".
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
  (3) Interface: In its default configuration.
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  To Main Network
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> (1) is filtered to the desired item. It has a redstone card and a crafting card.
  The "Redstone Mode" is set to "Active with signal", The "Crafting Behavior" is set to "Do not use stocked items".
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (2) is configured with the desired item and quantity, and set to "Emit when levels are below limit".
* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (3) is in its default configuration.

## How It Works

1. If the amount of the desired item in [network storage](../ae2_mechanics/import_export_storage.md) is below the quantity specified in the
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />, it will emit a redstone signal.
2. Upon receiving a redstone signal (and due to the <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> and being set to not use stocked items),
   the <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> will request that the network's [autocrafting](../ae2_mechanics/autocrafting.md) craft
   more of the desired item, then export it.
3. Upon having an item pushed into it (and not being configured to have anything in its internal inventory), the <ItemLink id="appliedenergistics2:tile.BlockInterface" /> will push that item into network storage.
