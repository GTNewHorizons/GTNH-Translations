---
navigation:
  parent: ../tricks_example_index.md
  title: Interface Autostocking
  icon: appliedenergistics2:tile.BlockInterface
---

# Interface Autostocking

One might ask "How do I keep a certain amount of various items in stock, crafting more as needed?"

One solution is use of an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> and <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> to automatically request new items
from your network's [autocrafting](../ae2_mechanics/autocrafting.md). This setup is more suited to maintaining a small quantity of a wide
variety of items.

This demonstration setup is cut short so it isn't too wide, it is likely most optimal to use 4 <ItemLink id="appliedenergistics2:tile.BlockInterface" />s and 4 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />s,
to use all 8 [channels](../ae2_mechanics/channels.md) in a regular [cable](../items_blocks/cables.md).

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/interface_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
  (1) Interfaces: Set to keep the desired items in themselves. They have Crafting Cards.
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
  (2) Storage Busses: "Input/Output Mode" set to "Extract Only".
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  To Main Network
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

* The <ItemLink id="appliedenergistics2:tile.BlockInterface" />s (1) are set to keep the desired items in themselves, by clicking the desired item into their
   top slots or dragging into the top slots from NEI, then clicking on the wrench icon above the slots to set the amount. They have <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />s.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />s (2) are set such that "Input/Output Mode" is set to "Extract Only".

## How It Works

1. If an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> cannot retrieve enough of a configured item from [network storage](../ae2_mechanics/import_export_storage.md),
   (and it has a <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />), it will request that the network's [autocrafting](../ae2_mechanics/autocrafting.md) craft more of that item.
2. The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />s allow the network to access the contents of the interfaces.
