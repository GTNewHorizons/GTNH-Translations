---
navigation:
  parent: /items_blocks_index.md
  title: ME Annihilation Plane
  icon: appliedenergistics2:item.ItemMultiPart:300
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:300
- appliedenergistics2:item.ItemMultiPart:301
---

# ME Annihilation Plane

<GameScene zoom="8" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/annihilation_plane.snbt" />
</GameScene>

The Annihilation Plane can break blocks and pick up items. It inserts items into [network storage](../ae2_mechanics/import_export_storage.md), working similarly to an <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />. Under normal circumstances, it actively picks up items near the target position after breaking a block. For items that directly collide with the plane, it only picks up items within the collision range on the surface of the plane.

The Annihilation Plane can only break blocks that meet certain conditions. For example, it cannot break air, fluids, bedrock, end portals, end portal frames, or command blocks. The block must also have non-negative hardness and pass the mining permission check.

An <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> and tools enchanted with this enchantment behave the same way, but the energy cost is 16 times that of the Annihilation Plane.

The Annihilation Plane is a [cable subpart](../ae2_mechanics/cables_subparts.md).

**REMEMBER TO ENABLE FAKE PLAYERS IN YOUR CHUNK CLAIM**

## Filtering

The Annihilation Plane will only break a block or pick up an item if the drops or items can be stored in its network. This means to filter one, *you must restrict what can be stored on its network*, most likely by putting it on a [subnetwork](../ae2_mechanics/subnetworks.md). An <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> or [partitioning](cell_workbench.md) the [cells](storage_cells.md) can achieve this.

<GameScene width="300" height="200" zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
    Filter the drops from the target block.
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
    Partition the storage for the drops.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

The Annihilation Plane filters *by item drops*. Therefore, if you want to break only <ItemLink id="etfuturum:amethyst_cluster_2:6" />, the plane must be enchanted with silk touch. Unfully grown amethyst buds drop nothing, and the network can always store "nothing", so a normal Annihilation Plane will keep breaking them.

## Recipe

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:300" />
