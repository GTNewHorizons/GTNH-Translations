---
navigation:
  parent: /items_blocks_index.md
  title: ME Controller
  icon: appliedenergistics2:tile.BlockController
categories:
- network infrastructure
item_ids:
- appliedenergistics2:tile.BlockController
- appliedenergistics2:tile.BlockCreativeEnergyController
---

# Controller

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockController" meta="1" nbt='{inv:{},proxy:{p:0,g:6L,k:-1L},orientation_up:"UP",id:"BlockController",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />
  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyController" meta="1" nbt='{inv:{},proxy:{p:0,g:11L,k:-1L},orientation_up:"UP",id:"BlockCreativeEnergyController",orientation_forward:"EAST",internalCurrentPower:"9.22337203685477E14d"}' scale="4" />
</Row>

The controller is the routing hub of an [ME network](../ae2_mechanics/me_network_connections.md). Without one, the network is ad-hoc and supports at most eight channel-using [devices](../ae2_mechanics/devices.md). A network cannot contain multiple controller groups. Each controller face provides 32 [channels](../ae2_mechanics/channels.md).

Each controller block consumes 6 AE/t and stores 8000 AE, so large networks may need additional energy storage. See [Energy](../ae2_mechanics/energy.md).

Controllers are multiblocks with a free-form shape within these rules:

1. All controller blocks on one network must be connected.
2. The controller must fit within 7x7x7 blocks.
3. Controller blocks may be adjacent along at most one axis; violating this disables the controller.

<GameScene width="400" height="200" zoom="2" showBackground={false}>
  <ImportStructure src="../assets/structures/controllers.snbt" />
  <IsometricCamera yaw="195" pitch="25" />
</GameScene>

When powered and valid, the controller glows and cycles colors. Right-clicking it opens the same GUI as a <ItemLink id="appliedenergistics2:item.ToolNetworkTool" />.

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockController" />


