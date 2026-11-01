---
item_ids:
  - ThaumicTinkerer:enchanter
  - ThaumicTinkerer:repairer
  - ThaumicTinkerer:spellCloth
  - ThaumicTinkerer:kamiResource:0
  - ThaumicTinkerer:ichorPickGem
  - ThaumicTinkerer:ichorclothChestGem
navigation:
  title: Thaumic Tinkerer
  parent: ./index.md
  icon: 'ThaumicTinkerer:enchanter'
  position: 20
---

# Thaumic Tinkerer

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**Thaumic Tinkerer (TT)** adds customizable enchanting, durability repair, block transport, infused crops, and a wide range of functional devices to Thaumcraft.<br>
Later, <Color color="#B7A0D6">KAMI</Color> research builds on Ichor to provide Ichorcloth armor, Ichorium tools, teleportation devices, and more.

Its content supports equipment upgrades, material production, and base construction. The Osmotic Enchanter and Thaumic Restorer fit into existing equipment and essentia systems;<br>
infused crops are bred through aspect combinations, while KAMI makes further use of void materials, Osmiridium, and higher wand Vis capacity.

NH rewrites many research prerequisites and recipes, so check current materials in NEI. This page focuses on device mechanics, uses, and NH-specific changes.

## Osmotic Enchanter

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/osmotic_enchanter.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

The <ItemLink id="ThaumicTinkerer:enchanter" showIcon="left" /> is a powerful enchanting table added by TT.<br>
It lets you choose the enchantments and levels to apply to equipment, using Vis from a wand.<br>
Different enchantments require different primal aspects, and the costs rise quickly at higher levels.

**Surrounding pillars**

The enchanter requires **6 nearby pillars**. Their bases must be at the same height as the enchanter and within **4 blocks** along both the X and Z axes.<br>
Each pillar consists of **2–12 <ItemLink id="Thaumcraft:blockCosmeticSolid:0" showIcon="left" />** stacked vertically, topped with <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" />.

The scene shows a layout with two totems per pillar.<br>
Other positions meeting the range and height requirements also work; the pillars do not require a fixed hexagonal layout.

**Items and power supply**

- The item must be **unenchanted** and have the item type and enchantability required by the chosen enchantment.
- The interface only offers registered enchantments that apply to the item and whose research requirements are met. Restrictions such as the incompatibility between Silk Touch and Fortune still apply.
- The wand's caps must have a base Vis consumption modifier of **100% or less**. Iron and copper caps do not qualify; staves are also not accepted.
- Vis is absorbed gradually during processing, so the total requirement can exceed the wand's current reserves. If it runs short, remove the wand, recharge it, and return it to continue supplying Vis.
- The item is locked while the enchanter is working, preventing removal or changes to the selected enchantments. Invalid pillars interrupt the process.

The Osmotic Enchanter is made through infusion, with an ordinary Enchanting Table as the central ingredient and Obsidian Totems, Thaumium Plates, and Spellbinding Cloth around it.<br>
The recipe has an instability of **12**, and the research adds **3 Warp**.

**Spellbinding Cloth**

Combining <ItemLink id="ThaumicTinkerer:spellCloth" showIcon="left" /> with an item in a crafting recipe removes its enchantments, allowing you to redesign the combination.

> [!WARNING]
> Spellbinding Cloth removes the item's existing enchantments. Before using it on equipment with rare enchantments or effects that are difficult to obtain again, check which ones you intend to keep.

## Useful Enchantments

Thaumic Tinkerer's enchantment research appears in its research tab. Complete the corresponding research to select these enchantments in the Osmotic Enchanter.<br>
They affect mining, combat, or movement, so choose them according to the equipment's intended use.

**Mining and harvesting**

- **Tunnel**: Increases mining speed when repeatedly digging in a straight line, making it useful for tunnels.
- **Shatter**: Increases mining speed against blocks with high hardness.
- **Disintegrate**: Provides very high mining speed against ordinary blocks suited to the tool, such as stone, dirt, and netherrack. It reduces effectiveness against other targets and doubles durability consumption.
- **Flaming Touch**: Specializes in fast mining of wooden blocks, reducing effectiveness against other targets and also doubling durability consumption.

**Combat and movement**

- **Vampirism**: Converts part of the damage dealt by an attack into healing for the wielder.
- **Quick Draw**: Speeds up drawing a bow.
- **Ascent Boost**: Applied to leggings to increase jump height.
- **Slow Fall**: Applied to boots to reduce falling speed and fall damage; sneaking temporarily disables the effect.

Other combat enchantments include Dispersed Strikes, Focused Strikes, Final Strike, Valiance, Pounce, and Shockwave. Their research entries describe their effects and applicable equipment.<br>
Mining enchantments with high durability consumption pair well with repair facilities or unbreakable Ichorium tools.

## Durability Repair and Status Protection

**Thaumic Restorer**

The <ItemLink id="ThaumicTinkerer:repairer" showIcon="left" /> repairs inserted items using <Color color="#B7A0D6">Instrumentum essentia</Color>. Each point of Instrumentum restores **8 durability**.

Supply essentia through the restorer's connection face, using tubes connected to your Instrumentum stock. Goggles of Revealing show the remaining damage, and the restorer emits a redstone signal while repairing.

Automation can insert damaged items and extract them once repairs are complete, supporting a cycle of equipment collection, repair, and resupply.<br>
It accepts items according to their repairability; **Tinkers' Construct tools cannot be repaired**.

See [Alchemy and Essentia](./alchemy_essentia.md) for essentia storage and distribution.

**Talisman of Remedium**

When worn and enabled, the <ItemLink id="ThaumicTinkerer:cleansingTalisman" showIcon="left" /> absorbs several negative status effects, consuming its durability to remove them. It can also handle some Warp-related effects, at a high durability cost.

**Wand Focus: Mending**

The <ItemLink id="ThaumicTinkerer:focusHeal" showIcon="left" /> consumes wand Vis during continuous use to slowly heal the caster. It is useful for recovering between fights and requires reserves of the relevant Vis.

## Transport, Collection, and Device Interfaces

**Wand Focus: Dislocation**

The <ItemLink id="ThaumicTinkerer:focusDislocation" showIcon="left" /> picks up a block, stores it, and places it elsewhere. Containers, furnaces, and some mob spawners can also be moved. Vis is charged when picking up the block; placing it back costs no additional Vis.

Blocks with tile entities cost **5 times** as much Vis as ordinary blocks, while mob spawners cost **20 times** as much.<br>
The focus cannot move certain blocks, including aura nodes, some AE blocks, bundled conduits, reinforced essentia jars, and other special devices.

**Transvector Interface and Dislocator**

- A <ItemLink id="ThaumicTinkerer:interface" showIcon="left" /> bound to a target block extends its item, fluid, and other interfaces.<br>
Bind it with a <ItemLink id="ThaumicTinkerer:connector" showIcon="left" />, within a range of **4 blocks**. It shares the target's corresponding capabilities, providing additional connection points around a device.
<br>
- A <ItemLink id="ThaumicTinkerer:dislocator" showIcon="left" /> swaps the block in front of it with the bound location when triggered by redstone, also moving entities at those positions.<br>
Its binding range is **16 blocks**, and its facing can be adjusted with a wand.

**Attractors and automated tool use**

- The <ItemLink id="ThaumicTinkerer:magnet" showIcon="left" /> affects dropped items, while the Corporeal Attractor affects living creatures. Blue mode attracts and red mode repels;<br>
the range is half the redstone signal strength, up to **7.5 blocks**. The Corporeal Attractor also uses Soul Molds to filter creature types and distinguish adults from babies.
<br>
- The <ItemLink id="ThaumicTinkerer:animationTablet" showIcon="left" /> performs left-click or right-click actions with the inserted tool or item, either continuously or under redstone control.<br>
Tool type and durability also affect its work when harvesting, placing blocks, or performing other automated actions.

These devices supplement existing logistics and redstone controls. See [Magic Automation](./magic_automation.md) for more on collection, inventory monitoring, and production support.

## Lighting, Movement, and Portable Devices

**Lighting and darkening**

<ItemLink id="ThaumicTinkerer:brightNitor" showIcon="left" /> illuminates the area around its carrier even while stored in the inventory, making it useful in caves and areas without fixed lighting.

<ItemLink id="ThaumicTinkerer:gaseousLightItem" showIcon="left" /> and <ItemLink id="ThaumicTinkerer:gaseousShadowItem" showIcon="left" /> release spreading gases that respectively light up or darken the surrounding area.

The <ItemLink id="ThaumicTinkerer:gasRemover" showIcon="left" /> dissipates both types of nearby gas, allowing you to change an area that has already been prepared.

**Movement and storage**

- The <ItemLink id="ThaumicTinkerer:focusFlight" showIcon="left" /> consumes Vis to lift the caster into the air, providing short-distance movement and a way over obstacles.
- The <ItemLink id="ThaumicTinkerer:focusEnderChest" showIcon="left" /> provides remote access to Ender storage. With EnderStorage integration, it can also be bound to an Ender Chest's color combination.
- When worn and enabled, the <ItemLink id="ThaumicTinkerer:xpTalisman" showIcon="left" /> collects nearby experience orbs. Glass bottles in the inventory can be used to convert stored experience into Bottles o' Enchanting for storage and transfer.
- The <ItemLink id="ThaumicTinkerer:revealingHelm" showIcon="left" /> combines Thaumium helmet protection with the observation abilities of Goggles of Revealing, retaining head protection while using those abilities.

## Elemental Fire

Thaumic Tinkerer's six elemental fires are involved in environmental transformation and later Infused Seeds research.

- <ItemLink id="ThaumicTinkerer:fireFire" showIcon="left" />: Converts some ordinary blocks into their Nether counterparts, such as stone into netherrack.
- <ItemLink id="ThaumicTinkerer:fireWater" showIcon="left" />: Transforms terrain toward water, ice, and snow, including some Nether terrain.
- <ItemLink id="ThaumicTinkerer:fireAir" showIcon="left" />: Converts some blocks into desert counterparts.
- <ItemLink id="ThaumicTinkerer:fireEarth" showIcon="left" />: Turns stone, cobblestone, and other blocks into dirt, with additional transformations such as gravel into clay.
- <ItemLink id="ThaumicTinkerer:fireOrder" showIcon="left" />: Has no usable block transformation results in the current version, but its research remains a prerequisite for Infused Seeds.
- <ItemLink id="ThaumicTinkerer:fireChaos" showIcon="left" />: Removes the magic from other elemental fires, turning them back into ordinary fire.

> [!WARNING]
> NH allows elemental fire to spread and transform blocks by default. Control its area of effect and avoid releasing it near bases, farms, wooden buildings, or important facilities. Ordinary fire left by Perditio Imbued Fire can also continue burning.

## Infused Crops

<ItemLink id='ThaumicTinkerer:infusedSeeds:0:{mainAspect:{Aspects:[{key:"aer",amount:1}]},aspectTendencies:{Aspects:[]}}' showIcon="left" /> carry a main aspect and primal aspect tendencies. Each main aspect has a different loot pool; aspect combinations allow you to breed crops that produce particular materials.

Infused Seeds research requires all six elemental fire research entries. The six primal seeds are made through infusion, using Wheat Seeds as the central ingredient and **4 crystal clusters of the corresponding aspect**.<br>
Each recipe requires **32 Messis, 32 Meto, and 16 essentia of the corresponding primal aspect**, with an instability of **4**. Compound aspect seeds are obtained through further breeding.

Seeds can be planted on ordinary farmland, converting it into Infused Farmland. Growth requires at least **light level 9**. Harvesting mature crops produces seeds and the corresponding loot, and leaves aspect residue in the soil.

A mature crop leaves its main aspect in the farmland below when harvested. Farmland holds up to **20 points** of residue in total; excess residue causes some aspects to be reduced at random.

When a mature crop is harvested, its main aspect may combine with an aspect in the soil, turning the dropped seed into a new compound aspect seed.<br>
For example, <Color color="#B7A0D6">Aer + Ignis = Lux</Color>. Growing Ignis crops in soil with accumulated Aer residue can yield Lux seeds when harvested. Following further aspect combinations leads to more complex main aspects.

**Primal aspect tendencies**

Tendencies affect growth, yield, and mutation. A crop can have at most **50 tendency points** in total; excess points cause some tendencies to be reduced at random.

| Tendency | Main Effect |
| --- | --- |
| Aqua | Speeds up growth |
| Terra | Increases soil residue left after harvesting a mature crop |
| Ignis | Improves the chance of producing compound aspect seeds |
| Ordo | Increases the number of loot rolls |
| Perditio | Increases seed drops |
| Aer | Speeds up the acquisition of tendencies from adjacent crops |

Compound aspect crops can acquire the corresponding tendency from adjacent primal crops, up to **5 points** per tendency through this method. Adjacent compound crops also transfer tendencies between themselves; higher values require further breeding through this exchange.

**Loot and NEI**

Thaumic Tinkerer provides NEI loot lookup for Infused Seeds, showing the possible outputs and their probabilities for a given aspect crop. These probabilities come from its loot pool, while Ordo tendency also affects the number of loot rolls per harvest.

- Crops of the **four natural elements** produce the corresponding Imbued Grain, which can be used in alchemy to make Aer, Ignis, Aqua, and Terra potions.
- **Ordo and Perditio** crops produce glass and sand, respectively.
- The **Cognitio** loot pool includes paper, books, bookshelves, and Knowledge Fragments.
- The **Alienis** loot pool includes Ender Pearls, Eyes of Ender, and Void Seeds.
- Other compound aspects have their own loot pools. Look up a target item's recipes in NEI to find a suitable main aspect to breed.

For long-term harvesting, preserve the seeds and their tendencies, soil residue, and growing locations, assigning suitable planting areas to breeding and production.

## Unlocking KAMI Research

The main entry point to <Color color="#B7A0D6">KAMI</Color> is **Ichor** research. Its prerequisites cover the main Thaumcraft categories and relevant Thaumic Tinkerer research. Completing them opens the way to Ichorcloth, Ichorium, and their advanced devices.

Unlocking Ichor research is demanding and often leaves the researcher with 300+ Warp, so prepare suitable Warp protection.

Check the prerequisites of the Ichor recipe in `NEI` to see what remains locked and identify hidden prerequisites. The quest book also highlights easily missed research such as the Thaumium Crowbar and Cursed Spirit's Blade.

## Ichor, Ichorcloth, and Ichorium

**Dimensional shards**

<ItemLink id="ThaumicTinkerer:kamiResource:6" showIcon="left" /> and <ItemLink id="ThaumicTinkerer:kamiResource:7" showIcon="left" /> are important ingredients for Ichor.

- Zombie Pigmen killed by a player in the **Nether** have a **1/16** chance to drop a Nether Shard.
- Endermen killed by a player in the **End** have a **1/32** chance to drop an Ender Shard.
- NH also provides infusion recipes for dimensional shards, using various Forbidden Magic shards, infused shards, and the corresponding central ingredients. Beekeeping offers another route for a continuous supply.

The drops require the corresponding dimension and a player kill; account for these conditions when designing a mob supply.<br>
An `EEC` processing the corresponding mobs in their required dimension also produces shards.

**Ichor**

<ItemLink id="ThaumicTinkerer:kamiResource:0" showIcon="left" /> is made by infusing a Nether Star.

The recipe uses one Nether Star as the central ingredient, surrounded by a Flawless Diamond, Nether Shard, Eye of Ender, and Ender Shard, producing **2 Ichor**.<br>
Its essentia requirements are **32 Humanus, 32 Lux, 64 Spiritus, 16 Alienis, and 16 Ordo**, with an instability of **10**. Ichor research itself adds **5 Warp**.

**Ichorcloth and Ichorium**

- <ItemLink id="ThaumicTinkerer:kamiResource:1" showIcon="left" /> combines Ichor, Enchanted Fabric, Void Metal Foil, Osmiridium Foil, and Flawless Diamonds. It is a main material for Ichorcloth Robes and their awakened upgrades.
- **Ichorium** combines Ichor, void metal, Osmiridium, and Flawless Diamonds. GT's Ichorium ingots and material forms are used to make plates, screws, rings, and various tool components.

Both arcane crafting recipes require **125 Vis of each of the six primal aspects**. Wand capacity and Vis discounts affect which recipes you can actually craft. See [Wands, Vis and Nodes](./wands_vis_nodes.md) for the relevant equipment and discount sources.

**Ichorium wand components**

The <ItemLink id="ThaumicTinkerer:kamiResource:4" showIcon="left" /> provides a **30%** Vis discount for all primal aspects. The <ItemLink id="ThaumicTinkerer:kamiResource:5" showIcon="left" /> gives a wand a capacity of **1000 Vis per primal aspect**.

This path supports large arcane recipes and sustained focus use. The caps, core, and finished wand each require their corresponding research and crafting.

## Ichorcloth Armor and Awakening

Ordinary Ichorcloth armor consists of the <ItemLink id="ThaumicTinkerer:ichorclothHelm" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorclothChest" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorclothLegs" showIcon="left" />, and <ItemLink id="ThaumicTinkerer:ichorclothBoots" showIcon="left" />.<br>
These pieces do not lose durability. Infusion can awaken them to grant additional movement, protection, and observation abilities.

- <ItemLink id="ThaumicTinkerer:ichorclothHelmGem" showIcon="left" />: Provides revealing abilities, underwater breathing, clear underwater vision, and continued health regeneration while hungry.
- <ItemLink id="ThaumicTinkerer:ichorclothChestGem" showIcon="left" />: Provides sustained flight, fall protection, and protection against ordinary projectiles.
- <ItemLink id="ThaumicTinkerer:ichorclothLegsGem" showIcon="left" />: Provides fire protection and converts incoming fire damage into healing.
- <ItemLink id="ThaumicTinkerer:ichorclothBootsGem" showIcon="left" />: Improves movement, jumping, and reach across gaps, allows automatic stepping up one-block rises, and provides Haste and fall protection.

Awakened armor effects are controlled by the **Toggle Awakened Armor** keybinding, which defaults to `U`.<br>
NH disables the awakened leggings' automatic light placement by default, while retaining the awakened boots' ability to turn dirt beneath the wearer into grass.

Awakening recipes use advanced gems, Ichorium components, and other magical devices, with high instability.<br>
Once material production is established, a stable Infusion Altar and sufficient essentia reserves are needed. See [Infusion Crafting](./infusion_crafting.md) for altar supply and stability.

## Ichorium Tools and the Bedrock Dimension

The <ItemLink id="ThaumicTinkerer:ichorPick" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorShovel" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorAxe" showIcon="left" />, and <ItemLink id="ThaumicTinkerer:ichorSword" showIcon="left" /> do not lose durability and can be awakened further.

Sneak-right-click to switch an awakened tool's working mode:

- <ItemLink id="ThaumicTinkerer:ichorPickGem" showIcon="left" />: Single-block, **5×5 area**, and **10-block line** mining, with the ability to break bedrock.
- <ItemLink id="ThaumicTinkerer:ichorShovelGem" showIcon="left" />: Single-block, **5×5 area**, and vertical column mining of the same block type.
- <ItemLink id="ThaumicTinkerer:ichorAxeGem" showIcon="left" />: Single-block, **5×5 area**, and whole-tree chopping.
- <ItemLink id="ThaumicTinkerer:ichorSwordGem" showIcon="left" />: Single-target attacks, area attacks against nearby creatures of the same type, and a mode that grants Soul Hearts.

> [!WARNING]
> Area and line mining affect several blocks at once. Before using awakened tools near your base or devices, check the current mode and direction to avoid breaking blocks you intend to keep.

**Bedrock Dimension**

The Awakened Ichorium Pickaxe's bedrock-breaking ability also provides access to the **Bedrock Dimension**. Mining bedrock at **Y=0–4** in the Overworld while sneaking creates an entrance. Inside, you can continue mining bedrock and the vertical ore veins within it.

This dimension provides a special mining space. GTNH adjusts its ore content; conventional miners first need room to work, so plan a suitable means of clearing bedrock.

The quest book warns that leaving may place you on the nearby surface or inside blocks. Prepare return methods, mining tools, and location records before entering to reduce problems caused by changing entry and exit points.

## KAMI Building and Teleportation Devices

**Storing and placing large quantities of blocks**

- Once bound to a block type, the <ItemLink id="ThaumicTinkerer:blockTalisman" showIcon="left" /> absorbs matching blocks from the inventory beyond one stack, leaving a stack available for use. It stores over 2 billion blocks of one type and can deposit them into containers or place them in the world.
- The <ItemLink id="ThaumicTinkerer:placementMirror" showIcon="left" /> previews and places blocks in a selected area. Materials can come from the inventory or Black Hole Rings holding the required block.
- <ItemLink id="ThaumicTinkerer:protoclay" showIcon="left" /> switches between the holder's Awakened Ichorium tools to use a suitable tool for the current target.
- The <ItemLink id="ThaumicTinkerer:ichorPouch" showIcon="left" /> provides a large portable inventory while retaining the functions of a Focus Pouch. NH prevents its use in Witchery's dream dimension.

**Celestial Gateways and Recall**

A <ItemLink id="ThaumicTinkerer:warpGate" showIcon="left" /> uses a <ItemLink id="ThaumicTinkerer:skyPearl" showIcon="left" /> to record another gateway's position. Each gateway holds **10 destinations**, connecting bases, mining sites, and other frequently used locations.

Bind a Celestial Pearl to a destination gateway and insert it into the departure gateway to create a one-way connection. A return route requires a pearl configured at each end. The gateway's interface can also restrict connections from other gateways.

The <ItemLink id="ThaumicTinkerer:focusRecall" showIcon="left" /> uses a bound Celestial Pearl in the hotbar and consumes Vis to teleport the caster to its destination, extending a fixed teleportation network into a portable way home.

</Column>
