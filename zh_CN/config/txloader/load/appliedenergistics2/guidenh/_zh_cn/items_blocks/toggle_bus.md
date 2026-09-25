---
navigation:
  parent: /items_blocks_index.md
  title: ME Toggle Bus
  icon: appliedenergistics2:item.ItemMultiPart:80
categories:
- network infrastructure
item_ids:
- appliedenergistics2:item.ItemMultiPart:80
- appliedenergistics2:item.ItemMultiPart:100
---

# The Toggle Bus

<GameScene zoom="8" showBackground={false}>
  <ImportStructure src="../assets/structures/toggle_bus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

A cable subpart that can toggle its connection state using redstone, allowing a section of an [ME Network](../ae2_mechanics/me_network_connections.md) to be disconnected. The inverted variant provides the opposite behavior. Toggling can cause the network to reboot and recalculate connected devices.

## Recipes

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:80" />
<RecipeFor id="appliedenergistics2:item.ItemMultiPart:100" />


