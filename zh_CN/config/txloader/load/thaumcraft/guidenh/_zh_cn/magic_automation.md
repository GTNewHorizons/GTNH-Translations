---
item_ids:
  - Automagy:blockTally
  - Automagy:blockThirstyTank
  - Thaumcraft:blockMirror:0
navigation:
  title: Magic Automation
  parent: ./index.md
  icon: 'Automagy:blockTally'
  position: 40
---

# Magic Automation

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Thaumcraft and **Automagy** provide facilities for item collection, inventory monitoring, transport over long distances, and fluid supply.<br>
They can connect to existing pipes, ME networks, and redstone controls to handle particular parts of a production system.

Their main uses involve <Color color="#B7A0D6">collection and distribution, inventory conditions, spatial transport, and production support</Color>.

## Item Collection and Distribution

**Collecting dropped items**

A <ItemLink id="Thaumcraft:blockChestHungry" showIcon="left" /> absorbs dropped items that touch it. Placed where a device ejects items, it collects products into an inventory for existing logistics to extract.

**Taking items from adjacent inventories**

A <ItemLink id="Automagy:blockGreedyChest" showIcon="left" /> watches for items added to neighboring inventories and transfers a portion into itself according to its settings.<br>
Its default share is 50%. Open its settings with a wand to select extraction directions and operating modes.

- **Proportional distribution:** Take a chosen share of inputs to an adjacent inventory, dividing one source between different uses.
- **Maintaining stock:** Take items according to a target quantity, keeping a fixed supply for a branch of the production line.
- **Taking surplus:** Leave the required stock in an adjacent inventory and take the amount above the threshold.
- **Item filtering:** Use a <ItemLink id="Automagy:enchantedPaper:1" showIcon="left" /> or <ItemLink id="Automagy:enchantedPaper:2" showIcon="left" /> to select which items participate in distribution.

A Greedy Chest will not take items from a hopper directly beneath it. Transfers between two Greedy Chests also depend on their direction settings.<br>
When using one beside a machine's recipe buffer, configure directions and filters first to avoid diverting required ingredients.

**Preserving item samples**

A <ItemLink id="Automagy:blockTenaciousChest" showIcon="left" /> preserves samples of each item type, preventing automation that follows its extraction rules from removing them all.<br>
It attempts to split one item into a separate stack so the remaining stock can continue to be extracted. Players can still remove the reserved items manually.

This container suits seeds, saplings, and sorting samples. Once configured, logistics can continuously extract surplus stock while preserving samples needed to restart production or identify items.

## Mirrors and Transport over Long Distances

Linked pairs of <ItemLink id="Thaumcraft:blockMirror:0" showIcon="left" /> blocks transfer items over long distances and even between dimensions. Items can be thrown into a mirror or inserted through logistics. The receiving end needs an inventory or item collection device to handle the output.

Standard Magic Mirrors link in pairs. When removed, they retain their previous pairing information and can also be linked to a new target. After moving a mirror, check its receiving location and collection facilities.

Large amounts of continuous traffic build up strain on the mirrors, reducing output speed. This strain fades over time, and Ordo essentia can also help remove it.<br>
When multiple production lines share a collection point, account for both mirror throughput and the receiving end's processing capacity.

**Sending items home while traveling**

A <ItemLink id="Thaumcraft:HandMirror" showIcon="left" /> can be carried with you. Once bound to a fixed Magic Mirror, its interface sends items back to that location.<br>
It is useful for sending items to the base while exploring, gathering resources, or moving supplies. Existing collection and sorting systems can receive them at the base.

**Combining multiple sources**

A <ItemLink id="Automagy:blockMirrorAlt:0" showIcon="left" /> only accepts inputs. Use a <ItemLink id="Automagy:crystalEye" showIcon="left" /> to select a Magic Mirror that is already paired, connecting the device to that mirror transport channel.

Multiple Melding Mirrors can send items from different locations to a shared collection point, serving scattered farms, processing devices, and distant gathering sites. The target Magic Mirror must retain a valid pairing, and the output end needs continuous item collection.

> [!WARNING]
> Mirror outputs may produce dropped items. The receiving end's collection facilities, storage capacity, and output speed should handle the actual throughput to prevent items from remaining on the ground and despawning. Confirm the receiving location before sending valuable materials through mirrors.

## Inventory Monitoring and Automatic Control

**Signals based on item quantities**

A <ItemLink id="Automagy:blockTally" showIcon="left" /> reads items in a target inventory and outputs a redstone signal according to conditions set by a Runic Whitelist or Blacklist. It faces the inventory being checked and outputs the signal in the opposite direction.

Connect the result to a production device's redstone control to replenish low stocks, stop at a target quantity, or trigger another device once a set of materials is ready.

Tally Boxes can also use lenses to change what they detect:

- <ItemLink id="Automagy:tallyLens:1" showIcon="left" />: Detects loose items at the target location, allowing checks for a backlog at a collection point.
- <ItemLink id="Automagy:tallyLens:2" showIcon="left" />: Checks the target block's possible drops, including ordinary and Silk Touch results, allowing the presence of a particular block to become a trigger condition.

**Reading inventories remotely**

A <ItemLink id="Automagy:blockRemoteComparator" showIcon="left" /> uses a Crystalline Eye to bind to a target and reads the comparator state of an inventory or compatible block within 20 blocks. This lets detection devices sit near the control wiring, leaving the inventory's sides available for logistics connections.

Placed above a Tally Box, a Remote Comparator passes information about items in a distant inventory to the box for evaluation. Tally Boxes and Remote Comparators can also relay target information through a chain, carrying inventory conditions to more distant control points.

**Detecting entity counts**

A <ItemLink id="Automagy:blockEntitySignal" showIcon="left" /> detects entities of a selected type within range, with their number affecting signal strength.<br>
Use an <ItemLink id="Automagy:crystalEntityEye" showIcon="left" /> to select the target type. Adult or baby animals can be selected separately, making the device useful for breeding, slaughter, and other facilities controlled by entity counts.

The maximum detection area is 11×11×11. Solid blocks around the device change the detection directions and area: blocking one face limits detection in that direction and extends it toward the opposite side. Glass, water, and similar blocks do not obstruct detection in the same way.<br>
When placing it near animal pens, check its coverage against the walls.

**Timed activation**

A <ItemLink id="Automagy:blockHourglassMagic" showIcon="left" /> provides repeatable timing and redstone output.<br>
It can produce pulses when timing ends, continuous signals while timing, alternating output, and brief interruptions. Input signals can also start, reset, or stop the timer.

A Magic Hourglass provides timing for intermittent supply, periodic collection, or device activation. After adjusting its timing and modes with a wand, combine it with inventory conditions to decide when a device may operate.

**Redcrystal wiring**

<ItemLink id="Automagy:blockRedcrystal" showIcon="left" /> can be attached to different block faces and connect around corners. A wand adjusts connections to neighboring redcrystal, helping route controls around compact installations.

- <ItemLink id="Automagy:blockRedcrystalAmp" showIcon="left" />: Amplifies an incoming signal and outputs it in a selected direction.
- <ItemLink id="Automagy:blockRedcrystalDim" showIcon="left" />: Limits the maximum output signal strength.
- <ItemLink id="Automagy:blockRedcrystalDense" showIcon="left" />: Passes only signals that meet the chosen minimum strength.
- <ItemLink id="Automagy:blockRedcrystalRes" showIcon="left" />: When two crystals face each other, they transmit signals through space along a straight line, up to 15 blocks apart.
- <ItemLink id="Automagy:blockRedcrystalMerc" showIcon="left" />: Transmits redstone signals through paired Magic Mirrors. Bind each end to its corresponding mirror and place it within 8 blocks of that mirror.

Mercurial Redcrystal can send inventory conditions from the receiving end back to distant production lines, coordinating supply and collection through mirror logistics.

## Fluid Collection and Supply

A <ItemLink id="Automagy:blockThirstyTank" showIcon="left" /> has a default capacity of 16,000 mB. It collects and stores one fluid type and can connect to fluid pipes. It absorbs connected liquids that can be collected with a bucket, finding sources through connected regions of the same liquid.

GTNH's default configuration preserves adjacent water sources, allowing a tank beside a source to draw water continuously. The current configuration also lets exposed tanks collect rainwater. For other fluids, position the tank according to the pool's connectivity.

**Adding functions with glyphs**

Each of a Thirsty Tank's six faces can hold one glyph. The chosen face matters for directional functions. Capacity, speed, and disposal effects can be configured as needed.

- <ItemLink id="Automagy:glyph:3" showIcon="left" />: Outputs fluid to the container in that face's direction.
- <ItemLink id="Automagy:glyph:4" showIcon="left" />: Takes fluid from the container in that face's direction.
- <ItemLink id="Automagy:glyph:5" showIcon="left" />: Performs active collection only while receiving a redstone signal.
- <ItemLink id="Automagy:glyph:6" showIcon="left" />: Retains some fluid to prevent the tank from being completely emptied.
- <ItemLink id="Automagy:glyph:7" showIcon="left" />: Increases collection frequency. Multiple glyphs of this type increase it further.
- <ItemLink id="Automagy:glyph:8" showIcon="left" />: Adds 16,000 mB of capacity per glyph.

Glyphs of Siphoning and Envy supply fluid between adjacent containers. A Glyph of Temperance can connect to inventory monitoring or production controls. To maintain a fixed fluid type, a Glyph of Preservation leaves a reserve that keeps the tank bound to that type.

> [!WARNING]
> A <ItemLink id="Automagy:glyph:1" showIcon="left" /> accepts and destroys fluid beyond the tank's capacity, while a <ItemLink id="Automagy:glyph:2" showIcon="left" /> continuously destroys fluid inside it. When arranging fluid recovery or byproduct handling, ensure fluids you need to preserve do not enter tanks configured for disposal.

**Automatic milking**

With a <ItemLink id="Automagy:glyph:9" showIcon="left" /> installed, the tank searches for cows in the glyph's direction and collects milk, stopping its usual collection of surrounding liquids. Cows must be inside the relevant detection area, and the tank needs space for the output and a way to extract it.

In NH, each cow has a milking cooldown of 2000 game ticks, or about 100 seconds at normal speed. The cooldown is stored on the cow, so multiple tanks sharing one cow are subject to the same limit. Glyphs of the Guzzler increase search frequency; sustained output also depends on the number of cows available to milk in rotation.

## Production Support

**Accelerating crop growth**

A <ItemLink id="Thaumcraft:blockMetalDevice:8" showIcon="left" /> uses Plant (Herba) essentia to accelerate plants within its effective light coverage. It supports farms of ordinary crops such as wheat, carrots, and potatoes, with harvesting and collection handled by existing devices.

Position it so the light covers the planted area and maintain a supply of Herba.

**Animal breeding**

A <ItemLink id="Thaumcraft:blockMetalDevice:13" showIcon="left" /> consumes Life (Victus) essentia to put eligible animals within range into breeding mode. Once eight or more animals of a species are present, the lamp stops encouraging that species to breed.

Combine it with a Signum Entia and existing animal harvesting devices so breeding, population control, and product processing each handle one part of the system. Baby animals within range also count toward the limit, so pen layout and downstream processing speed affect continuous production.

**Directional mining**

An <ItemLink id="Thaumcraft:blockWoodenDevice:5" showIcon="left" /> is installed above or below an <ItemLink id="Thaumcraft:blockWoodenDevice:4" showIcon="left" />. With a <ItemLink id="Thaumcraft:FocusExcavation" showIcon="left" /> and pickaxe inserted, redstone controls mining in the selected direction.

Enchantments on the focus and pickaxe affect performance, while pickaxe durability affects how long operation can continue. Products leave through the base's output port or enter an inventory placed there. After changing direction, check the mining path and output position.

Entropy (Perditio) essentia or the corresponding Centi-Vis increases drilling speed. Arrange the direction, tools, and collection facilities around the area to be mined, with Centi-Vis supplied by an existing node network.

### Additional Golem Uses

Golems can supplement transport, harvesting, and item interactions between devices. Their installed core determines their work. Use a <ItemLink id="Thaumcraft:GolemBell" showIcon="left" /> to bind inventories, locations, and work targets.

- **Alchemy cores** transport essentia between alembics, jars, and compatible devices.
- **Harvest cores** handle compatible mature crops, using suitable upgrades to replant. Collection devices can gather the drops.
- **Use cores** simulate clicks with an item or an empty hand, serving targets that support these interactions.

When using a golem, choose its core, material, and upgrades for the task and leave a path to its targets. Once devices handle collection, distribution, and inventory control, golems can handle the remaining interactions.

</Column>
