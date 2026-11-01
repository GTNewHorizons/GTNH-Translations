---
item_ids:
  - Thaumcraft:ItemEldritchObject:0
  - Thaumcraft:ItemEldritchObject:2
  - Thaumcraft:ItemEldritchObject:3
  - Thaumcraft:ItemSanityChecker
  - Thaumcraft:ItemSanitySoap
  - Thaumcraft:ItemBathSalts
  - WarpTheory:item.warptheory.paper
  - WarpTheory:item.warptheory.cleanser
navigation:
  title: Warp and Eldritch Knowledge
  parent: ./index.md
  icon: 'Thaumcraft:ItemEldritchObject:0'
  position: 30
---

# Warp and Eldritch Knowledge

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Eldritch knowledge explores the world's deepest secrets, but often leads its students astray.<br>
Delving into forbidden research gradually builds up <Color color="#B7A0D6">Warp</Color>.<br>
The whispers, hallucinations, and physical changes it brings can also lead to discoveries in <Color color="#B7A0D6">Eldritch Studies</Color>.

Eldritch Studies covers void metal, primal energy, and exploration of the Outer Lands, connecting to the Advanced Alchemical Furnace, the Staff Core of the Primal, and later KAMI research.
GTNH's **Warp Theory** expands Warp events and provides ways to deal with permanent Warp.

## Sources and Types of Warp

Research marked with purple forbidden knowledge warnings in the Thaumonomicon is a major source of Warp.<br>
Crafting certain items, eating some foods, and using magical tools can also add Warp; look for the relevant markings in research entries and item tooltips.

| Type | Properties | Treatment |
| --- | --- | --- |
| **Temporary Warp** | Gradually fades during Warp checks | Wait, or remove it with items such as Sanitizing Soap |
| **Sticky Warp** | Does not fade naturally; also called normal Warp | Sanitizing Soap has a chance to reduce it; cleansing items from addons can also remove it |
| **Permanent Warp** | Ordinary Sanitizing Soap cannot remove it | In NH, items such as Pure Tears and Purification Talismans can remove it |

Equipment with the **Warping** property also adds Warp to event calculations.<br>
This contribution comes from items currently worn or held and disappears when they are unequipped; cleansing items do not remove the property from the equipment itself.

**Checking your Warp**

GTNH's IGI overlay can display Warp directly. You can also check it with the following items:

- <ItemLink id="WarpTheory:item.warptheory.paper" showIcon="left" />: Shows the exact amounts of permanent, sticky, and temporary Warp in chat when used. Color changes, burning, and other reactions also indicate the danger level.
- <ItemLink id="Thaumcraft:ItemSanityChecker" showIcon="left" />: Displays a Warp bar while held. Dark purple represents permanent Warp, light purple represents sticky Warp, and pink represents temporary Warp. The bar is full at a combined total of 100; use litmus paper to check higher values.

## Warp Events and the Timer

Thaumcraft's own Warp events include Unnatural Hunger, Sun Scorned, blurred vision, increased Vis costs, and Eldritch Guardians appearing in dense fog. Some whispers also grant research points or new discoveries.

- **Vis drained from your wand**, affecting subsequent crafting and combat.
- **Inventory items swapped or shuffled**, along with random teleportation and unusual movement.
- **Poison, Wither, Blindness**, and other effects, or the appearance of Firebats and hostile creatures.
- Events that cause lasting damage, such as **countdown explosions, nearby block decay, and spawning a Wither**.

Events are triggered by random checks. The available events also depend on Warp strength, the timer, and configuration.<br>
The table below lists some event thresholds in NH's default configuration. The **effective strength** used to select an event depends on current Warp and the timer, and equipment such as faceplates can reduce it.

| Effective Strength Threshold | Additional Risk |
| --- | --- |
| 50 | Draining Vis from your wand |
| 125 | Swapping inventory items |
| 130 | Random teleportation |
| 150 | Shuffling inventory items |
| 160 | Countdown explosion |
| 180 | Nearby block decay |
| 200 | Spawning a Wither |

Block decay affects blocks, plants, and leaves that the event can transform; countdown explosions and Withers can cause further damage to nearby facilities.<br>
Where you stay while accumulating Warp also determines how much these events can damage.

**Event decay in 2.9**

After you stop gaining new Warp, events gradually weaken; ordinary random events stop once the timer runs out.<br>
**Gaining Warp again reactivates the timer.** Forbidden research, related crafting, and other sources can all end this quiet period.<br>
Equipment with the Warping property affects event strength but **does not reset the timer**. Existing sticky and permanent Warp remains after events stop.

> [!WARNING]
> High Warp events can cause explosions, damage terrain, or spawn a Wither near the player. Stay away from important machines, storage, and other players' facilities when gaining large amounts of Warp, waiting for Eldritch discoveries, or using cleansing items with backlash.

## Warp Ward and Symptom Relief

<Color color="#B7A0D6">Warp Ward</Color> prevents ordinary Warp events for its duration. Your existing Warp remains, making it useful for suppressing events while crafting, exploring, or going about daily activities.

**Purifying Bath Salts and the Arcane Spa**

Throwing <ItemLink id="Thaumcraft:ItemBathSalts" showIcon="left" /> into water creates Purifying Fluid. Bathing in it grants Warp Ward; higher permanent Warp shortens the protection.

An <ItemLink id="Thaumcraft:blockStoneDevice:12" showIcon="left" /> uses water and Purifying Bath Salts to replenish Purifying Fluid in the area above it, providing a convenient way to renew protection at your base.

Botania's <ItemLink id='Botania:brewFlask:0:{brewKey:"warpWard"}' showIcon="left" /> also provides Warp Ward. Each dose from a regular flask grants 10 minutes of protection.

An equipped <ItemLink id="WarpTheory:item.warptheory.portableshower" showIcon="left" /> reapplies Warp Ward when it expires, making it useful when regularly wearing equipment with the Warping property.

<ItemLink id="thaumicbases:rosehipSyrup" showIcon="left" /> reduces the level of effects such as blurred vision, Unnatural Hunger, and Vis Exhaustion, removing them when they are already at the lowest level. It also treats some ordinary negative potion effects.

## Reducing and Removing Warp

**Sanitizing Soap**

Finishing the use animation of <ItemLink id="Thaumcraft:ItemSanitySoap" showIcon="left" /> removes all temporary Warp and has a chance to reduce sticky Warp by 1.

- The base chance is **33%**.
- Warp Ward adds **25 percentage points**.
- Standing in Purifying Fluid adds another **25 percentage points**, for **83%** when both conditions are met.

Keep using the soap until the animation finishes. Using it in Purifying Fluid saves materials when removing large amounts of sticky Warp.

**Thaumic Insurgence soaps**

Thaumic Insurgence provides additional cleansing options:

- <ItemLink id="thaumicinsurgence:item.ItemSanitySoapAlpha" showIcon="left" /> (α soap): Also removes temporary Warp and has a chance to reduce sticky Warp by 1, with a higher base chance of 50%. Warp Ward and Purifying Fluid raise this to 100%.

- <ItemLink id="thaumicinsurgence:item.ItemSanitySoapBeta" showIcon="left" />: On success, converts **1 permanent Warp into 2 sticky Warp**, which can then be removed with ordinary or α soap. The base chance is 10%, with Warp Ward and Purifying Fluid each adding 15 percentage points. Failure adds 2 temporary Warp.

**Impure Tear**

<ItemLink id="WarpTheory:item.warptheory.cleanserminor" showIcon="left" /> removes 5 Warp when your combined permanent, sticky, and temporary Warp is **at least 50**.<br>
It removes temporary Warp first, then sticky Warp, then permanent Warp. It can lower high Warp, but cannot continue cleansing once the total falls below the threshold. Its research requires Eldritch Epiphany, Arcane Litmus Paper, and other prerequisites.

**Pure Tear**

<ItemLink id="WarpTheory:item.warptheory.cleanser" showIcon="left" /> removes all accumulated temporary, sticky, and permanent Warp at once.<br>
Its powerful effect places its research behind Eldritch Revelation, Ichor, and other prerequisites, with demanding material requirements.

The **Purge Your Warp** quest offers another way to obtain a Pure Tear. Check its required submissions and rewards even if you have not completed the corresponding research.

> [!WARNING]
> A Pure Tear queues a series of backlash events based on your Warp before cleansing. **Warp Ward cannot prevent this backlash.** After using it, stay away from your base until the concentrated events have finished.

**Purification Talisman**

An equipped <ItemLink id="WarpTheory:item.warptheory.amulet" showIcon="left" /> periodically attempts to reduce Warp, gradually removing permanent Warp as well. It is suitable for ongoing cleansing.

The cleansing process still queues ordinary Warp events. Warp Ward delays these events, which may resume after the protection ends; choose a suitable place to stay while cleansing.

## Discovering Eldritch Research

The two Eldritch discoveries come from random checks during Thaumcraft Warp events. They use the **sum of the player's permanent and sticky Warp**:

- **Eldritch Epiphany**: Can unlock when the total is **greater than 25**, revealing the Eldritch tab in the Thaumonomicon and opening research paths such as void metal and the Sanity Checker.
- **Eldritch Revelation**: Can unlock when the total is **greater than 50**. It is a prerequisite for Opening the Eye and some advanced Eldritch research.

Temporary Warp and equipment Warp do not count toward these thresholds. Reaching the required amount still leaves you waiting for a random check, so the time required varies.

**Warp Ward prevents this check.** If you regularly wear a Portable Shower or maintain another source of protection, remove it and wait in an area prepared for Warp events.<br>
You can reduce your Warp after receiving the discoveries; unlocked research remains available.

## Crimson Cult and Opening the Eye

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_obelisk.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Ordinary Eldritch Obelisk

</Column>

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/crimson_cult_obelisk.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Crimson Cult Obelisk

</Column>

</Column>

While exploring, you may discover two kinds of Eldritch Obelisks. Crimson Clerics and Crimson Knights can be found near Crimson Cult obelisks, and defeating them can yield <ItemLink id="Thaumcraft:ItemEldritchObject:1" showIcon="left" />.<br>

Scanning the relevant enemies helps reveal research clues. Hold the book and right-click to read it, unlocking **Crimson Cult**.<br>
Crimson Knights fight in melee, while Crimson Clerics use ranged magic.

(Crimson Clerics do not attack unprovoked. Leaving some clerics alive allows Crimson Knights to keep spawning, greatly increasing your opportunities to obtain <ItemLink id="Thaumcraft:ItemEldritchObject:1" showIcon="left" />.)

Eldritch Guardians may also appear around the ritual area. These sites are useful sources of Crimson Rites, Eldritch Eyes, and related scans.

After completing **Crimson Cult** and **Eldritch Revelation**, you can research **Opening the Eye** to gain access to the Outer Lands.

The ritual requires an intact naturally generated Eldritch Obelisk of either kind, with its Eldritch Altar at the base and Sinister Node above preserved.<br>
Insert **4 <ItemLink id="Thaumcraft:ItemEldritchObject:0" showIcon="left" />** into the altar, then right-click it with a wand to open an Eldritch Portal.<br>
The ritual has a base requirement of **100 Vis of each of the six primal aspects**. **Arcane crafting Vis discounts apply.**

Eldritch Eyes can drop from Eldritch Guardians or be made through infusion after completing Opening the Eye research.<br>
The node above the altar participates in opening the portal; bottling or converting it affects the ritual.

Gadomancy provides the **Gate of the Voidwalkers**, an artificial entrance built using a Node Manipulator and a Redirection Focus.<br>
It also requires Eldritch Eyes and wand Vis. The corresponding research shows its structure.

> [!WARNING]
> The Gate of the Voidwalkers allows only one entity to pass through, after which the entrance disappears. Prepare another means of returning, or be ready to complete the Outer Lands challenge before leaving.

## Exploring the Outer Lands

<Color color="#B7A0D6">The Outer Lands</Color> is a separate maze built from Ancient Stone. Corridors connect rooms containing enemies, Ancient Urns, research clues, and boss areas. An expedition usually involves finding a key room, obtaining a Runed Tablet, opening a boss room, and returning with a Primordial Pearl.

Entering through an Eldritch Portal grants **The Outer Lands** research. Special blocks and glyphs reveal further research clues; obtaining a pearl opens additional Eldritch and addon research paths in the Thaumonomicon.

**The maze and research clues**

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_key_room.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Key Room

</Column>

</Column>

- <ItemLink id="Thaumcraft:blockEldritch:5" showIcon="left" /> and <ItemLink id="Thaumcraft:blockCosmeticSolid:11" showIcon="left" />: Scan these after entering the Outer Lands to discover **Revelations in the Outer Lands** and learn more about the maze.
- **Libraries and other special rooms**: Their layouts differ from ordinary corridors and contain special blocks and loot related to research.
- **Ancient Urns**: Found in corridors and rooms, they release loot when broken. Higher-quality urns may also appear around boss rooms.
- **Key rooms**: A Runed Tablet floats above the central stone pedestal, guarded by Eldritch Guardians. These rooms are the source of naturally generated tablets.
- **Boss room entrances**: An Ancient Locking Mechanism requires a Runed Tablet to activate.

Enemies in the maze include Eldritch Guardians, Shambling Husks, and Eldritch Crabs. Narrow corridors affect ranged attacks and movement; dense fog, negative effects, and branching paths can also slow exploration.

The Outer Lands restricts common forms of creative flight and Thaumcraft levitation, so changes in elevation along the corridors matter.<br>
Marking the entrance, explored branches, and boss rooms helps you find your way back.

## Runed Tablets and Ancient Locking Mechanisms

A <ItemLink id="Thaumcraft:ItemEldritchObject:2" showIcon="left" /> is the key to opening an Outer Lands boss room.<br>
Naturally generated tablets appear at the center of dedicated key rooms. Search the maze to find one, then bring it to a boss room entrance.

After completing Opening the Eye, you can research **Runed Tablet** and craft tablets through infusion. The research itself adds 5 Warp, and the recipe has an instability of **10**.

The main ingredients include:

- <ItemLink id="DraconicEvolution:infoTablet" showIcon="left" /> as the central ingredient.
- **2 Eldritch Eyes** and **4 Void Seeds**.
- <ItemLink id="ThaumicExploration:pureZombieBrain" showIcon="left" />.
- <ItemLink id="Automagy:crystalBrain:3" showIcon="left" />.

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_boss_door.snbt" />
  <IsometricCamera yaw="90" pitch="0" />
</GameScene>

<Column width="120" align="center" gap="0">

Boss Room Door

</Column>

</Column>

The essentia requirements are **128 Praecantatio, 64 Alienis, 64 Cognitio, 32 Iter, 32 Tenebrae, and 32 Vacuos**.<br>
Crafted tablets are useful once you have the materials and essentia supply, reducing the time spent searching for a key room on each expedition.

**Use and consumption**

Right-clicking the locking mechanism with a tablet consumes **1 tablet**. After a brief charging period, the mechanism transforms the room and creates its challenge.

Each mechanism can only be activated once. After obtaining more tablets, look for unopened boss rooms in new mazes.<br>
Outer Lands challenges include an Eldritch Construct, an Eldritch Warden, the Crimson Cult, and Taint. The room type is determined by world generation.

## Boss Challenges in the Outer Lands

**Eldritch Construct**

The construct has two combat forms. An attack that would defeat its initial body causes it to shed its head and enter a headless form, continuing the fight.<br>
Losing its head also causes an explosion. Defeat the transformed body to obtain a Primordial Pearl.

This transformation interrupts the pace of combat; watch for the explosion and subsequent attacks when fighting at close range.

**Eldritch Warden**

The warden primarily attacks with ranged Eldritch projectiles and can apply Wither, Weakness, and other effects.<br>
It appears with additional absorption health. Depleting this shield triggers a frenzy, briefly making it invulnerable and creating a force field.

Leave enough room to dodge its projectiles and force field. Defeating the warden yields a Primordial Pearl and a Rare Treasure Bag.

**Crimson Cult**

The Crimson Portal at the center of the room continually spawns Crimson Knights and Clerics, followed by a Crimson Praetor. The praetor restores the health of nearby cultists; dealing with it first makes the remaining enemies easier to clear.

The portal has strong health regeneration before the praetor appears. **The Primordial Pearl in this room drops from the Crimson Portal**, which must be defeated. The praetor also drops a Rare Treasure Bag.

**Taint**

These rooms contain tainted terrain and several tentacles, including Giant Taintacles. Their attacks and the tainted environment interfere with movement, so consider your footing and attacks from other tentacles while clearing them.

The last Giant Taintacle defeated drops a Primordial Pearl. Defeating just one may leave other Giant Taintacles in the room.

Maintain Warp Ward during an Outer Lands expedition to reduce additional Warp events during combat. After completing the challenge, use the return portal to leave.

### Void Metal and Primal Energy

**Void metal**

After Eldritch Epiphany and Thaumium research, you can research void metal. <ItemLink id="Thaumcraft:ItemResource:17" showIcon="left" /> is used to make <ItemLink id="Thaumcraft:ItemResource:16" showIcon="left" />, and is also required for Eldritch Eyes, Runed Tablets, and various addon devices.

Void metal opens several paths:

- **Void metal tools and armor**: Some tools and equipment repair their own durability and have the Warping property.
- **Void metal wand caps**: Reduce wand Vis costs and support further wand upgrades.
- **Advanced essentia storage**: Expands storage capacity for individual aspects, supporting larger alchemy and infusion recipes.
- **Void Thaumaturge Robes**: Combine protection, Vis discounts, and abilities such as those of the Goggles of Revealing.
- **Addon material paths**: Research into Shadowmetal, Shadow Fortress equipment, and Primordial equipment continues to build on void metal discoveries.

**Primal energy and the Staff Core of the Primal**

<ItemLink id="Thaumcraft:ItemResource:15" showIcon="left" /> is an important ingredient in Eldritch crafting, used for Eldritch Eyes, the Primal Crusher, and several advanced magical recipes.

**Wand Focus: Primal** fires powerful orbs of primal energy that can damage the surrounding environment. Both the focus and its orbs are part of the scanning prerequisites for the Staff Core of the Primal.<br>
The staff core builds on research into several elemental staff cores. See [Wands, Vis and Nodes](./wands_vis_nodes.md) for its capacity, charging, and prerequisites.

## Primordial Pearls and Their Research Uses

A <ItemLink id="Thaumcraft:ItemEldritchObject:3" showIcon="left" /> is an important reward from the Outer Lands and a key material for developing more advanced Eldritch devices.<br>
Scanning it reveals **Primordial Pearl** research, connecting to the Advanced Alchemical Furnace, Primal Crusher, Primordial Node Manipulation, and several addon research paths.

**Advanced Alchemical Furnace**

The Advanced Alchemical Furnace increases the buffer and processing capacity of essentia extraction, using Ignis, Perditio, and Aqua Centi-Vis.<br>
Its research also requires knowledge of Essentia Distillation and Centi-Vis power. Once the constructs and furnace are ready, it can connect to existing essentia storage and logistics to meet the demands of large infusion recipes.

See [Alchemy and Essentia](./alchemy_essentia.md) for its components, inputs, outputs, and power supply.

**Primal Crusher**

The <ItemLink id="Thaumcraft:ItemPrimalCrusher" showIcon="left" /> combines abilities from the Shovel of the Earthmover, Pickaxe of the Core, and void metal tools. It mines earth and stone in a **3×3** area and has a chance to turn eligible ores into Native Clusters.<br>
It repairs its own durability, making it useful for large excavations as well as combat.

**Primordial Gauntlet and addon devices**

Witching Gadgets' <ItemLink id="WitchingGadgets:item.WG_PrimordialGlove" showIcon="left" /> holds an aura node and uses it to recharge socketed Infused Gems. Its sockets stabilize the gems, allowing their abilities to be reused after recharging.

Pearls are also used for advanced rings, Primordial equipment, and content from addons such as Thaumic Horizons and Tainted Magic.<br>
These paths consume substantial amounts of essentia and advanced materials. A steady pearl supply allows you to develop production devices, tools, and protection separately.

### Primordial Node Manipulation

**Primordial Node Manipulation** research provides a way to modify ordinary aura nodes with pearls. Using a Primordial Pearl on a node consumes the pearl and changes the node's base aspect amounts, with a chance to improve its quality.

- The base amounts of **existing primal aspects** may increase or decrease.
- **Missing primal aspects** have a chance to be added.
- The base amounts of **compound aspects** may decrease.
- Nodes of **Fading, Pale, or Normal quality** have a chance to improve.

A pearl can react with a node even before this research is completed; completing it improves the chances of some favorable changes. With an established pearl supply, it offers another way to modify nodes, taking both random outcomes and pearl costs into account.

See [Wands, Vis and Nodes](./wands_vis_nodes.md) for custom nodes, Node Manipulators, and Energized Nodes.

## Obtaining a Steady Supply of Primordial Pearls

**Primordial Berry**

CropsNH's **Primordial Berry** produces pearls when harvested at maturity. Plant a Primordial Pearl in Crop Sticks as the seed to establish the first crop.

- Primordial Berry cannot be obtained through crossbreeding, spread naturally, or be bred with other plants.
- Improving its stats requires devices such as the **Crop Gene Extractor and Crop Synthesizer**.
- Its preferred biome tags include **End and Magical**. At least one suitable biome tag or sufficient biome humidity is needed to prevent crop sickness.
- It has a long growth cycle and needs a stable growing environment with suitable acceleration.

**Reassembling pearl fragments**

GTNH also provides a <ItemLink id="dreamcraft:PrimordialPearlFragment" showIcon="left" /> route: processing a Primordial Pearl in a Forge Hammer produces **3 fragments**. The corresponding Witching Gadgets research and infusion recipe then turn each fragment back into a pearl.

The reassembly research requires Primordial Pearl and Ichor-related prerequisites. Its recipe consumes Eldritch Eyes, Ichor materials, Aurora Blocks, and large amounts of essentia, with an instability of **20**.<br>
This route turns one pearl into several, making it suitable once you have a complete Ichor material supply and infusion infrastructure.

## Pearl Revitalization and the Extremely Primordial Pearl

**Pearl Revitalization in Witching Gadgets**

Some Witching Gadgets recipes for Primordial equipment draw the energy from a pearl, leaving a <ItemLink id="WitchingGadgets:item.WG_Material:12" showIcon="left" />.<br>
After completing **Pearl Revitalization** research, infusion can restore it to a Primordial Pearl.

The recipe uses one shard of each of the six primal aspects and a <ItemLink id="Thaumcraft:blockCrystal:6" showIcon="left" />. It requires **64 essentia of each primal aspect** and **384 Praecantatio**, with an instability of **10**.<br>
When making Primordial Gauntlets, weapons, and armor, these leftover pearls can be returned to your material supply.

**Extremely Primordial Pearl**

The <ItemLink id="Avaritia:big_pearl" showIcon="left" /> comes from Avaritia's integration with Thaumcraft, unlocked after Primordial Pearl research.<br>
Its infusion uses one ordinary Primordial Pearl as the central ingredient and **7 more** around it, consuming **8 pearls** in total.

This infusion has an instability of **12** and requires 64 essentia each of the six primal aspects, Alienis, and Praecantatio, plus 32 Terminus. Producing it in quantity requires the corresponding essentia reserves and altar stability.

When used as a catalyst in later recipes, the Extremely Primordial Pearl can be retained. It is used for the Akashic Record and several Infinity equipment recipes. It does not stack; recipes requiring several pearls at once need that many separate pearls.

## Further Protection: Primordial Armor

**Primordial Armor** consists of <ItemLink id="WitchingGadgets:item.WG_PrimordialHelm" showIcon="left" />, <ItemLink id="WitchingGadgets:item.WG_PrimordialChest" showIcon="left" />, <ItemLink id="WitchingGadgets:item.WG_PrimordialLegs" showIcon="left" />, and <ItemLink id="WitchingGadgets:item.WG_PrimordialBoots" showIcon="left" />.<br>
Its material path uses Shadow Fortress equipment, void metal, and pearls, making it worth considering when developing advanced magical protection.

Each piece can be independently tuned to a **primal affinity** by sneak-right-clicking while holding it. Several pieces tuned to the same aspect also meet the item counts required by some abilities.

- **Aer affinity**: Reflects projectiles; at least two Aer-tuned pieces provide creative flight.
- **Terra affinity**: Grants regeneration when injured, while the boots also provide knockback resistance.
- **Ignis affinity**: Extinguishes you automatically and reduces fire and explosion damage; the helm can provide Night Vision.
- **Aqua affinity**: Removes several negative effects; the helm can provide Water Breathing and underwater Night Vision.
- **Ordo affinity**: Provides regeneration and reduces the level and duration of Thaumcraft's Warp-related negative status effects.
- **Perditio affinity**: Applies Blindness and Slowness to attackers when you are hit.

The Primordial Helm also reduces the effective strength of Warp Theory events. When wearing it regularly, combine it with protection such as a Portable Shower to manage the Warp contributed by your equipment.

</Column>
