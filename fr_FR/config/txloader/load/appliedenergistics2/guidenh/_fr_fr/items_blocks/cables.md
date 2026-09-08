---
navigation:
  parent: /items_blocks_index.md
  title: Cables
  icon: appliedenergistics2:item.ItemMultiPart:36
categories:
- network infrastructure
item_id: "appliedenergistics2:item.ItemMultiPart 0-16,20-36,40-56,60-76,520-536"
---

# Cables

<GameScene zoom="3" showBackground={false}>
  <ImportStructure src="../assets/structures/cables.snbt" />
  <IsometricCamera yaw="135" pitch="30" />
</GameScene>

While adjacent ME machines can also create an ME network, cables are still the primary way to extend an ME network over large areas.

Differently colored cables can prevent adjacent cables from connecting to each other, making the distribution of [channels](../ae2_mechanics/channels.md) more efficient. They also affect the color of terminals connected to them, so terminals will not always appear purple. Fluix cables can connect to cables of all colors.

**Note that channels and cable colors are unrelated.**

## An Important Note

**If you are new to AE2 and are not yet familiar with channels, use smart cables and dense cables wherever possible. They display the path of channels through the network, making it easier to understand how channels behave.**

## Another Note

**Channels are not item/fluid/energy/other types of pipes.** Channels have no internal storage, and ME interfaces and machines do not "input" items into channels. The only thing channels do is connect AE2 [devices](../ae2_mechanics/devices.md) into a network.

## Glass Cable

<ItemImage id="appliedenergistics2:item.ItemMultiPart:16" scale="4" />

<ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> is the simplest cable, capable of transmitting energy and up to 8 [channels](../ae2_mechanics/channels.md). It comes in 17 colors, with Fluix as the default, and can be dyed into the corresponding color using any of the 16 dyes.

To craft a dyed cable, surround a dye with 8 cables in the crafting grid. The colors of the cables used for crafting do not need to match, but they must be the same type of cable, such as glass or smart cable. Cables in the world can also be dyed using any Forge-compatible paintbrush.

Any dyed cable can be placed in a crafting table to remove its dye.

Cables can be wrapped with Fluix Crystals to create <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" />, and can also be crafted into <ItemLink id="appliedenergistics2:item.ItemMultiPart:56" /> to better observe the behavior of [channels](../ae2_mechanics/channels.md).

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:16" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:11" />

---

## Covered Cable

<ItemImage id="appliedenergistics2:item.ItemMultiPart:36" scale="4" />

Compared to <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" />, covered cables do not provide any additional gameplay functionality. However, they can be used as practical decoration if you prefer their appearance.

Covered cables can be dyed in the same way as <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" />. Four <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" /> can be crafted into <ItemLink id="appliedenergistics2:item.ItemMultiPart:536" />.

<Recipe id="appliedenergistics2:item.ItemMultiPart:36" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:31" />

---

## Dense Cable

<ItemImage id="appliedenergistics2:item.ItemMultiPart:536" scale="4" />

High-capacity cables can transmit 32 channels instead of the 8 channels of regular cables. However, dense cables do not support buses. You must first step down from a dense cable to a smaller cable, such as <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> or <ItemLink id="appliedenergistics2:item.ItemMultiPart:56" />, before placing buses or panels on it.

Dense cables slightly modify the "shortest path" behavior of channels: channels will first take the shortest path to a dense cable, and then take the shortest path through that dense cable to the controller.

<Recipe id="appliedenergistics2:item.ItemMultiPart:536" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:531" />

---

## Smart Cable

<Row>

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

</Row>

Although they look similar to <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" />, smart cables can display channel usage and provide diagnostic functionality. Channels are displayed as colored lines on the black stripes of the cable, making it easier to understand channel usage in the network. On regular smart cables, the first four channels are displayed as lines matching the cable color, while the last four are white. On dense cables, each line represents 4 channels.

On a network with an <ItemLink id="appliedenergistics2:tile.BlockController" />, the lines on the cable exactly match the actual paths of the channels.

Smart cables on ad-hoc networks instead display the total number of channels used by the entire network, rather than the number of channels passing through the cable itself.

Smart cables can be dyed in the same way as <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" />.

<Recipe id="appliedenergistics2:item.ItemMultiPart:56" />

<Recipe id="appliedenergistics2:item.ItemMultiPart:76" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:71" />