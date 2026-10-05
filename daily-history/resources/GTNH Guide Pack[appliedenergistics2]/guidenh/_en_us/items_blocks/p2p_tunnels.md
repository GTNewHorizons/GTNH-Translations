---
navigation:
  parent: /items_blocks_index.md
  title: P2P Tunnels
  icon: appliedenergistics2:item.ItemMultiPart:460
categories:
- devices
---

# Point-to-Point Tunnels

P2P tunnel usage and behavior are described in [AE2 Mechanics - P2P Tunnels](../ae2_mechanics/p2p_tunnels.md).

<Row>
<ItemImage id="appliedenergistics2:item.ItemMultiPart:460" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:461" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:462" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:463" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:466" scale="4" />
</Row>
<Row>
<ItemImage id="appliedenergistics2:item.ItemMultiPart:467" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:468" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:470" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:471" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:472" scale="4" />
</Row>

P2P tunnels transfer items, fluids, redstone signals, energy, light, and [channels](../ae2_mechanics/channels.md) through a network without directly interacting with it. Each variant transports one type of thing. They act like portals connecting two block faces at a distance, with defined input and output ends rather than a bidirectional connection.

![Portal](../assets/images/p2p_portal.png)

For example, a hopper facing an Item P2P tunnel behaves as if it were connected directly to the barrel on the other end. Two barrels next to each other do not transfer items through the tunnel.

<GameScene width="300" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_hopper_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene width="300" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_barrel_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Types And Attunement

<GameScene width="400" zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

Only ME P2P tunnels are directly craftable. Right-click any P2P tunnel with the appropriate item to attune it:

- ME P2P: any [cable](cables.md)
- Redstone P2P: a redstone component
- Item P2P: a chest or hopper
- Fluid P2P: an iron bucket or glass bottle
- Energy P2P: an energy container
- Light P2P: a torch or glowstone

ME P2P channels cannot pass through another ME P2P tunnel. Energy P2P tunnels effectively tax 2.5% of transported FE/E through their own [energy](../ae2_mechanics/energy.md) consumption.

## Common Uses

ME P2P tunnels are commonly used to transport many [channels](../ae2_mechanics/channels.md) efficiently. Eight input tunnels can take 256 (8 x 32) channels from a controller and eight output tunnels can deliver them elsewhere, while each end consumes only one channel. Because the tunnels can be placed on a dedicated [subnetwork](../ae2_mechanics/subnetworks.md), they need not consume channels on the main network.

<GameScene width="350" height="300" zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/structures/p2p_compact_channels.snbt" />
  <IsometricCamera yaw="120" pitch="30" />
</GameScene>

## Nesting

ME P2P channels cannot pass through other ME P2P tunnels, so they cannot be nested indefinitely. Other tunnel types can pass through ME P2P tunnels; for example, a redstone P2P tunnel in the same arrangement can still work.

<GameScene width="350" height="300" zoom="3" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_nesting.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

## Linking

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_linking_frequency.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Use a <ItemLink id="appliedenergistics2:item.ToolMemoryCard" /> to link P2P tunnels. The connection frequency is shown as a 2x2 color array on the back of each tunnel.

- Shift-right-click a tunnel to generate a new frequency.
- Right-click to paste settings, an upgrade card, or a frequency.

The tunnel shift-right-clicked is the input; the tunnel right-clicked is the output. Multiple outputs are allowed, but ME P2P channels are divided between them instead of being copied to every output.

## Recipe

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:460" />

# P2P Tunnels
For the usage and behavior of P2P Tunnels, see [AE2 Mechanics - P2P Tunnels](../ae2_mechanics/p2p_tunnels.md).
