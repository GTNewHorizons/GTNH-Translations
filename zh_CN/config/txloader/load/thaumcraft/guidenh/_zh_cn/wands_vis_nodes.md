---
item_ids:
  - Thaumcraft:WandCasting
  - Thaumcraft:blockStoneDevice:11
navigation:
  title: Wands, Vis and Nodes
  parent: ./index.md
  icon: 'Thaumcraft:WandCasting'
  position: 70
---

# Wands, Vis and Nodes

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**<ItemImage id='Thaumcraft:WandCasting:0:{rod:"wood",cap:"iron"}' /> Wands** store and use <Color color="#B7A0D6">Vis</Color> in Thaumcraft, enabling arcane crafting, activating magical facilities, and using wand foci.<br>As research progresses, you need to improve wand capacity, Vis discounts, and your energy supply to support new recipes and facilities.

In GTNH, wand crafting also requires **Twilight Forest trophies and technological materials**.<br>
More advanced wands offer greater capacity, so upgrading involves both obtaining new materials and reducing the Vis needed to craft the next wand.

This page covers wand properties and crafting requirements, along with energy sources such as nodes, aspect orbs, and Centi-Vis. For aspects and research points, see [Thaumcraft Basics](./thaumcraft_basics.md).

## Wand Components and Uses

Wands consist of a **rod or staff core** and **caps**. The rod mainly determines Vis capacity, while the caps mainly determine the cost modifier. Some addon components also provide automatic recharging or energy conversion.

<Color color="#B7A0D6">Capacity is counted separately for each of the six primal aspects.</Color> A capacity of "50 Vis" means that up to 50 Vis of each primal aspect can be stored.

| Type | Arcane Crafting | Wand Foci | Main Features |
| --- | --- | --- | --- |
| Wand | Yes | Yes | Suitable for crafting, interacting with facilities, and using foci |
| Sceptre | Yes | No | With the same ordinary rod, capacity increases by 50%, with an additional 10 percentage point reduction in Vis cost |
| Staff | No | Yes | Uses a staff core, usually with greater capacity, for foci and facility interactions |

A sceptre's extra capacity and discount make it suitable for keeping in an Arcane Worktable.<br>
Staves offer greater capacity but cannot be used for arcane crafting.

Staff capacity depends on the specific core. For example, a Greatwood Staff Core holds 125 Vis, a Silverwood Staff Core holds 250 Vis, and the six elemental staff cores hold 175 Vis.

**Wand foci** provide active abilities such as mining, combat, and movement; a staff core is the component that determines the staff's capacity.<br>
## Wand Crafting Requirements

In GTNH, crafting a wand also requires screws and Twilight Forest boss trophies, with the materials determined by the component's recipe tier.

| Recipe Tier | Screw Material | Boss Trophy | Typical Acquisition Stage |
| --- | --- | --- | --- |
| 0 (LV) | Aluminium | <ItemLink id="TwilightForest:item.nagaScale" showIcon="left" /> | LV |
| 1 (MV) | Stainless Steel | <ItemLink id="dreamcraft:LichBone" showIcon="left" /> | MV |
| 2 (HV) | Energetic Alloy | <ItemLink id="dreamcraft:LichBone" showIcon="left" /> | MV |
| 3 (EV) | Vibrant Alloy | <ItemLink id="TwilightForest:item.fieryBlood" showIcon="left" /> | HV |
| 4 (IV) | Tungstensteel | <ItemLink id="TwilightForest:item.fieryTears" showIcon="left" /> | EV |
| 5 (LuV) | Enderium (TE) | <ItemLink id="TwilightForest:item.carminite" showIcon="left" /> | EV |
| 6 (ZPM) | Oriharukon | <ItemLink id="TwilightForest:item.carminite" showIcon="left" /> | EV |
| 7 (UV) | Osmiridium | <ItemLink id="dreamcraft:SnowQueenBlood" showIcon="left" /> | IV |

The standard recipes for ordinary Wooden, Greatwood, the six elemental, and Silverwood rods use tier 0, 1, 2, and 3 materials respectively. These tiers group wand recipes; some materials from higher tiers can be obtained earlier, without reaching the voltage stage of the same name.

The assembly Vis cost of an ordinary wand is **the rod's base cost + the rod's cap cost increment × the cap's assembly coefficient**, with the same amount required for each primal aspect. Sceptres additionally apply the rod's sceptre multiplier.<br>
For example, Greatwood uses 20 + 5 × the cap coefficient. Gold caps have a coefficient of 2, so assembling a wand requires 30 Vis of each aspect, while the corresponding sceptre requires 60 Vis of each. Check NEI for material quantities and addon rod parameters.

## Vis Discounts and Advanced Wands

<Color color="#B7A0D6">Vis discounts</Color> are important for crafting advanced wands.

- Caps | Determine the wand's base cost modifier; some caps only provide discounts for particular aspects
- Equipment and baubles | Provide Vis discounts for the relevant aspects when worn in the appropriate slots
- Sceptres | Reduce costs by another 10 percentage points in addition to cap and equipment effects

Among basic equipment, <ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> provide a 5% discount, <ItemLink id="Thaumcraft:ItemChestplateRobe" showIcon="left" /> and <ItemLink id="Thaumcraft:ItemLeggingsRobe" showIcon="left" /> each provide 2%, and <ItemLink id="Thaumcraft:ItemBootsRobe" showIcon="left" /> provide 1%. Together, the four pieces provide 10%.

<ItemLink id="WitchingGadgets:item.WG_AdvancedRobeChest" showIcon="left" /> and <ItemLink id="WitchingGadgets:item.WG_AdvancedRobeLegs" showIcon="left" /> provide 5% and 4% respectively, further reducing crafting costs.

In general, the actual cost is **recipe requirement × (cap cost modifier − equipment discount − sceptre discount)**, with a minimum modifier of 0.1. Equipment and sceptre effects subtract percentage points.

A practical example is a Gold Capped Greatwood Sceptre, whose base assembly cost is 60 Vis of each primal aspect.<br>
A Gold Capped Greatwood Wand holds 50 Vis. Even with the basic four-piece set's 10% discount, crafting the sceptre requires 54 Vis, exceeding that capacity.<br>
A cheaper combination using the same rod, or additional discounts, can overcome this requirement.

Thaumic Machina's **Vis Channels** augmentation first multiplies the cap cost modifier by 0.9, before applying equipment and sceptre discounts.<br>
For example, Thaumium caps' 90% modifier becomes 81%, or 61% with the basic four-piece set and a sceptre.

## Wand Caps

| Registry Name | Cap | Assembly Coefficient | Base Vis Cost | Features |
| --- | --- | --- | --- | --- |
| terrasteel | <ItemLink id="ForbiddenMagic:WandCaps:2" showIcon="left" /> | 1 | 180% | — |
| iron | <ItemLink id="Thaumcraft:WandCap:0" showIcon="left" /> | 0 | 110% | Node Preserver does not apply |
| copper | <ItemLink id="Thaumcraft:WandCap:3" showIcon="left" /> | 1 | 110% | Order and Entropy cost 100% |
| gold | <ItemLink id="Thaumcraft:WandCap:1" showIcon="left" /> | 2 | 100% | — |
| silver | <ItemLink id="Thaumcraft:WandCap:4" showIcon="left" /> | 3 | 100% | Air, Earth, Fire, and Water cost 95% |
| SOJOURNER | <ItemLink id="ThaumicExploration:sojournerCap" showIcon="left" /> | 5 | 95% | Passively draws Vis from nearby nodes while held |
| MECHANIST | <ItemLink id="ThaumicExploration:mechanistCap" showIcon="left" /> | 5 | 95% | Increases the rate of drawing Vis from nodes |
| cloth | <ItemLink id="TaintedMagic:ItemWandCap:1" showIcon="left" /> | 3 | 95% | — |
| thaumium | <ItemLink id="Thaumcraft:WandCap:2" showIcon="left" /> | 5 | 90% | — |
| manasteel | <ItemLink id="ForbiddenMagic:WandCaps:3" showIcon="left" /> | 6 | 85% | Reduces Mana conversion costs when paired with Livingwood or Dreamwood rods |
| vinteum | <ItemLink id="ForbiddenMagic:WandCaps:1" showIcon="left" /> | 5 | 90% | — |
| alchemical | <ItemLink id="ForbiddenMagic:WandCaps:0" showIcon="left" /> | 6 | 90% | Water costs 80%; reduces LP conversion costs with Blood or Blood Infused Wooden rods; wand attacks inflict Weakness |
| shadowcloth | <ItemLink id="TaintedMagic:ItemWandCap:3" showIcon="left" /> | 5 | 85% | — |
| thauminite | <ItemLink id="thaumicbases:resource:2" showIcon="left" /> | 6 | 85% | — |
| blood_iron | <ItemLink id="BloodArsenal:wand_caps:0" showIcon="left" /> | 6 | 85% | Water costs 80%; further reduces LP conversion costs with Blood Infused Wooden rods |
| void | <ItemLink id="Thaumcraft:WandCap:7" showIcon="left" /> | 7 | 80% | — |
| elementium | <ItemLink id="ForbiddenMagic:WandCaps:5" showIcon="left" /> | 7 | 70% | Reduces Mana conversion costs when paired with Livingwood or Dreamwood rods |
| crimsoncloth | <ItemLink id="TaintedMagic:ItemWandCap:2" showIcon="left" /> | 6 | 80% | — |
| shadowmetal | <ItemLink id="TaintedMagic:ItemWandCap:0" showIcon="left" /> | 8 | 70% | — |
| ICHOR | <ItemLink id="ThaumicTinkerer:kamiResource:4" showIcon="left" /> | 8 | 70% | — |

Version 2.9 buffed some Forbidden Magic wand components. See "Wand Component Buffs" under "New in 2.9" for the related changes.

### Component Replacement and Wand Augmentation

Salis Arcana adds research for **replacing caps and rods or staff cores**, with the corresponding recipes available in NEI. Replacement consumes the new component and destroys the old one, with the same Vis requirement as directly assembling the target wand.<br>
Permanent augmentations are retained, and replacing sceptre components also saves the Primal Charm required to craft a new sceptre. Replacement cannot change a wand, sceptre, or staff into another type.<br>
Wand augmentations are installed through infusion. Each augmentation can be installed once per wand, and different augmentations can coexist.

- Charge Buffer: increases capacity by 25%
- Vis Channels: multiplies the caps' Vis cost by 0.9, before equipment and sceptre discounts
- Contact Discharge: melee attacks with the wand consume Vis to deal magical damage that bypasses ordinary armor

## Sources of Vis

| Source or Facility | What It Provides | Characteristics |
| --- | --- | --- |
| Drawing directly from ordinary aura nodes | Primal aspect Vis stored in the node | Easy to use, but limited by the node's aspects, reserves, and regeneration rate |
| Aspect orbs | Vis of the corresponding primal aspect | A wand in the hotbar can absorb nearby orbs if it has room for that aspect |
| Primal Shrooms | Aspect orbs released when mature plants are harvested | A renewable supplementary source with random aspect output |
| Special rods or staff cores | Automatic recharging or conversion specified by the component | May only replenish one aspect or recharge to a low reserve level |
| Wand Recharge Pedestal | Draws Vis from nearby nodes to recharge a wand | Suitable for base charging; using compound aspects requires an additional device |
| Energized nodes and Centi-Vis networks | Continuous Centi-Vis output | Powers fixed devices and can recharge wands through appropriate charging facilities |
| Essentia Dynamo | Converts essentia into Centi-Vis | Requires a supply network, charging facilities, and a continuous supply of the relevant materials |

Hungry nodes, Ethereal Shards, and Empowering bees offer ways to cultivate or customize nodes for a lasting energy supply.

## Vishrooms, Primal Shrooms, and Aspect Orbs

<ItemLink id="Thaumcraft:blockCustomPlant:5" showIcon="left" /> is Thaumcraft's Vishroom and an ingredient for <ItemLink id="thaumicbases:ashroom" showIcon="left" />. **Primal Shrooms are the plants that release Vis orbs when harvested at maturity.**

The Primal Shroom alchemy recipe uses a Vishroom as its catalyst, along with <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" /> Entropy and <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"messis"}' scale="0.75" /> Crop aspects.<br>
Check NEI and the corresponding research for quantities. Breaking a mature plant with left-click drops the plant itself and 8–20 orbs of random primal aspects, each providing 1 Vis. The plant can then be replanted.

Primal Shrooms take time to grow, need a full supporting block below, and require a light level of at least 9 above.<br>
They cannot be harvested with right-click, and breaking them before maturity does not provide the same Vis yield. Growing and harvesting them provides a repeatable source of Vis.

Creatures can also leave aspect orbs when they die, which are absorbed by a wand in the hotbar with room for the corresponding aspect.

Ordinary elemental rods generally recharge only one aspect, and only to a small fraction of their capacity.<br>
Botania integration rods can convert Mana into Vis, provided their charging requirements are met and Mana is available.

## Observing Nodes and Reading Their Reserves

**Aura nodes** are concentrations of magical energy in the world. They can be scanned and used as a source of Vis for wands. Observing through a <ItemLink id="Thaumcraft:ItemThaumometer" showIcon="left" /> or wearing <ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> makes nodes easier to identify.

When examining a node, consider four kinds of information:

| Information | What It Determines |
| --- | --- |
| Aspect composition | Which primal aspects it can supply directly, and whether it contains compound aspects for other uses |
| Current reserves | How much Vis is available to draw immediately |
| Base capacity | The amount its normal regeneration can restore, which also affects energized node output |
| Type and quality | Special behavior, regeneration speed, and performance after conversion |

NH's node records help manage previously scanned nodes and can be opened with the I key by default.

### Node Types

Nodes have six main types. Type describes special behavior rather than a ranking; nodes of the same type can have different qualities and aspect compositions.

<Column width="500" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_types.png" x="0" y="140" width="2170" height="440" displayWidth="500" wrap="inline" title="Aura Node Types" />
</Column>

| Type | Core Appearance | Properties and Considerations |
| --- | --- | --- |
| Normal | White, with a stable core | The most common ordinary node, with no additional type effects |
| Sinister | Dark purple | Often associated with obsidian totems and Eldritch structures; changes nearby biomes and may spawn dangerous creatures |
| Pure | White vortex | Often found in Silverwood trees; can turn nearby biomes into Magical Forest, helping contain Taint |
| Tainted | Purple haze | Associated with Tainted Land; spreads Taint and its related hazards |
| Unstable | White, with a constantly pulsing core | Releases aspect orbs and loses Vis, making it unsuitable as a stable long-term energy source |
| Hungry | White ring | Draws in and devours nearby entities and items, and destroys blocks; its capacity can be cultivated by feeding it items with aspects |

> [!WARNING]
> Hungry nodes devour items, harm players, and affect nearby blocks. Valuable items, drops, and production facilities can be lost. Cultivate and modify them in a separate, protected area.

## Node Quality and Natural Regeneration

Node quality can be Normal, Bright, Pale, or Fading. Quality describes regeneration and is independent of type; a Pure node can also be Bright.

<Column width="400" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_states.png" displayWidth="400" wrap="inline" title="Aura Node Quality" />
</Column>

| Quality | Natural Regeneration | Appearance |
| --- | --- | --- |
| Normal | A regeneration event roughly every 30 seconds | No additional quality name |
| Bright | A regeneration event roughly every 20 seconds | More vivid than a Normal node |
| Pale | A regeneration event roughly every 45 seconds | Dimmer |
| Fading | Does not naturally regenerate Vis | Very dim and constantly flickering |

### Drawing from Nodes and Node Preserver

Wands can directly draw primal aspects from nodes, but cannot store compound aspects directly. A node containing only compound aspects requires another method of use.

**Advanced Node Tapping** and **Master Node Tapping** increase the drawing rate to twice and three times the normal rate respectively.<br>
These improve transfer speed, without increasing the node's natural regeneration rate or aspect capacity.

**Node Preserver** leaves at least 1 point of each aspect during normal drawing, reducing the risk of damage from draining the node.<br>
There are exceptions: sneaking bypasses protection, and low-end wands with ordinary Wooden rods or Iron caps cannot rely on it.

> [!WARNING]
> Draining an aspect to zero can remove that aspect or damage the node's quality. Exhausting every aspect can also make the node disappear.

## Moving, Stabilizing, and Cultivating Nodes

**Nodes in jars** provide a way to move nodes. Jarring risks damage, and jarred nodes do not naturally regenerate Vis, so they cannot serve as portable batteries to draw from at any time.

Before jarring, consider the node's current condition and the research explaining how to seal and release it. Once moved to your base, nearby node interactions and hazardous node types also need attention.

- <ItemLink id="Thaumcraft:blockStoneDevice:9" showIcon="left" />: prevents the stabilized node and other nodes from drawing Vis from each other, halves natural regeneration, and gradually repairs certain adverse conditions
- <ItemLink id="Thaumcraft:blockStoneDevice:10" showIcon="left" />: protects the node from being drained while allowing it to draw Vis from less stable neighbors; greatly suppresses natural regeneration and is better suited to planned node cultivation

Node Stabilizers sit below the node. **Applying redstone to a stabilizer disables it**, unlike the Node Transducer above the node, which requires redstone to activate.

Larger nodes can draw Vis from smaller neighbors, while Hungry nodes can grow by absorbing the aspects of consumed items.<br>
Cultivation requires time and suitable conditions; placing any two nodes close together will not necessarily merge them. Node quality, stabilizers, and the aspects in items affect whether a method suits the intended use.

## Node Manipulators and Quality Repair

<ItemLink id="thaumicbases:nodeManipulator" showIcon="left" /> and **Node Manipulator Foci** provide ways to actively modify nodes.<br>
Different foci have different effects, described by their respective research.

| Manipulator Focus | Use |
| --- | --- |
| <ItemLink id="thaumicbases:nodeFoci:8" showIcon="left" /> | Repairs Fading and Pale quality, and can also address the Unstable type |
| <ItemLink id="thaumicbases:nodeFoci:0" showIcon="left" /> | Raises Normal quality to Bright |
| <ItemLink id="thaumicbases:nodeFoci:7" showIcon="left" /> | Replenishes missing Vis and improves recharging |
| <ItemLink id="thaumicbases:nodeFoci:2" showIcon="left" /> | Has a chance to restore some Vis after consumption, without increasing capacity |

The manipulator sits directly above the node and operates through its installed focus. In the current implementation, the stabilizing focus takes about 5 minutes to repair Fading quality to Pale, and about 10 minutes to repair Pale to Normal.<br>
The brightening focus takes about 20 minutes to turn Normal quality into Bright. These times assume the node remains loaded and the game runs at normal speed.

Improving quality increases regeneration and can improve subsequent energized node output, but does not add aspect types or increase base capacity.

The Node Manipulator and Node Transducer both occupy the position above the node, so quality adjustment and later conversion are separate stages.

### Changing Base Aspects and Random Node Modification

To change a node's base aspects, you can also use <ItemLink id="gadomancy:BlockNodeManipulator:5" showIcon="left" />. Unlike the previous manipulator, it **randomly changes aspect composition, base amounts, quality, or type**.

| Possible Modification | Changes |
| --- | --- |
| Split compound aspects | Transfers a compound aspect's base amount to its component aspects |
| Combine aspects | Changes the base composition to form compound aspects |
| Add aspects | Adds missing primal aspects |
| Change quality | Quality may improve or deteriorate |
| Change type | Can produce another type, including the additional Growing type |

Each modification requires **at least 70 Vis of each primal aspect to be supplied cumulatively** to the manipulator, paid by the wand or staff placed inside.

Changing base aspects can help nodes with unsuitable compositions, but random modifications can also have negative results.<br>
To obtain an energy source with all six aspects, compare the materials, time, and risks of artificial node customization, node bees, and quality adjustment.

> [!WARNING]
> Random modifications by the Node Manipulator can lower quality or change the node's type. Assess these risks before using it on a node.

### Ethereal Shards and Artificial Nodes

<ItemLink id="ThaumicHorizons:synthNode" showIcon="left" /> is an artificial Vis container.<br>
Unlike natural nodes, **its aspect types and capacities can be set using materials, but it does not regenerate Vis on its own** and requires an external Centi-Vis supply.

<ItemLink id="Thaumcraft:ItemWispEssence" showIcon="left" /> increases its capacity. Each Ethereal Essence adds 4 points to the capacity of its aspect, without filling the added capacity.

Compound aspects can also be added to the shard. Charging them requires the supply network to provide their component primal aspects; an incomplete supply cannot fully charge the compound aspect.

**Ethereal Shards can also be used to customize ordinary nodes.** Once charged with Centi-Vis, a shard can be sealed into a jarred node and released as an ordinary aura node. This turns a composition defined by materials into a node that can regenerate naturally or undergo further modification.

This method needs an existing Centi-Vis source for the initial charge, such as an energized node or <ItemLink id="ThaumicHorizons:essentiaDynamo" showIcon="left" />.<br>
An Essentia Dynamo consumes essentia to produce Centi-Vis, while a dynamo that consumes wand Vis transfers energy.

### Empowering Bees and Node Cultivation

Empowering bees bring beekeeping into magical energy production. Effects operate within the hive's effective working area, influenced by territory genes and hive multipliers; check the effect gene the bee has actually inherited.

- Empowering: randomly increases an aspect's base capacity and current reserves, and may add new aspects
- Rejuvenating: refills existing Vis without increasing capacity through this effect
- Nexus: improves quality progressively from Fading to Bright, and can also address the Unstable type

Empowering bees select aspects randomly, while Nexus bees' quality improvements can complement capacity growth to improve later energy output.<br>
Bee effects must reach the target node, and cultivation requires continued operation.<br>
Jarred nodes can be cultivated this way, but artificial containers such as Ethereal Shards are excluded. A customized node must first be converted through jarring before node bees can affect it.

Industrial Apiary acceleration can greatly change cultivation speed. See the Forestry content for beekeeping mechanics, genetics, and acceleration requirements; this page focuses on their effects on nodes.

### Energized Nodes and Centi-Vis

**Energized nodes** change node use from storing Vis for gradual drawing to continuously producing <Color color="#B7A0D6">Centi-Vis (CV)</Color>.<br>
1 CV equals 0.01 Vis, and the node's displayed output indicates how much CV it supplies per game tick.

<ItemLink id="Thaumcraft:blockStoneDevice:11" showIcon="left" /> performs the conversion. A stabilizer below the node must operate throughout the process, while the transducer above the node is activated by redstone. Both facilities must remain in their required operating states after conversion.

**Conversion uses the node's base aspect amounts.** Compound aspects can also contribute to primal aspect output, so a node containing compound aspects is not necessarily worse than one containing only primal aspects.

Output does not increase in direct proportion to the node's reserves. Aspects are first broken down into primal aspects. For each primal aspect, the largest contribution from different sources is used rather than adding them together. The quality multiplier is then applied and the result rounded down, followed by taking the square root and rounding down again.

For example, a Normal-quality node contains 100 Fire and 100 Energy. Energy breaks down into Fire and Order, so the effective Fire amount remains 100 rather than 200, yielding 10 CV/t each of Fire and Order.<br>
Adding all the displayed aspect amounts together therefore does not give the correct output.

The quality multipliers for Bright, Normal, Pale, and Fading are 1.2, 1, 0.8, and 0.5 respectively, applied before taking the square root. Larger nodes generally provide more Centi-Vis.

**Energized nodes cannot be drawn from directly with a wand and do not regenerate like ordinary nodes.** They supply energy through Vis Relays and the relevant devices. Output remains limited separately for each of the six aspects, so high total output cannot compensate for a missing aspect.

> [!WARNING]
> Disabling or breaking the stabilizer below an energized node causes an explosion and Flux pollution. To dismantle the setup, first remove the **transducer's** redstone signal while keeping the stabilizer active. Wait until the node has completely returned to its ordinary form before removing the facilities. The restored node is drained and still risks damage, so avoid repeated switching.

### Centi-Vis Networks and Automatic Wand Charging

<ItemLink id="Thaumcraft:blockMetalDevice:14" showIcon="left" /> transmits Centi-Vis. Connections between nodes and relays require a distance of no more than 8 blocks and a clear line of sight. Relays can connect to other relays to extend the supply to devices around the base.

The network uses a tree structure: each relay has one upstream source and can supply multiple downstream devices. Distance, connections, and available output for each aspect determine whether a device receives energy.

| Charging Facility | Use |
| --- | --- |
| <ItemLink id="Thaumcraft:blockStoneDevice:5" showIcon="left" /> | Automatically charges a placed wand using nearby ordinary nodes; GTNH also enables charging from the Centi-Vis network |
| <ItemLink id="Thaumcraft:blockStoneDevice:8" showIcon="left" /> | Allows the pedestal to use compound aspects from ordinary nodes, with conversion losses |
| <ItemLink id="Thaumcraft:blockMetalDevice:2" showIcon="left" /> | Sits above an Arcane Worktable and uses Centi-Vis to recharge the wand inside |

Wand Recharge Pedestals and worktable Charging Relays make node energy available for everyday crafting at the base.<br>
For sustained use, consider node output, network connections, wand capacity, and crafting costs together.

## Common Problems

| Symptom | What to Check |
| --- | --- |
| Caps and rod are ready, but the wand cannot be crafted | Check research, Twilight Forest trophies, screw materials, and the actual Vis cost |
| The wand is full but cannot craft an advanced wand | Compare each aspect's actual requirement with capacity; check cap, equipment, and sceptre discounts |
| Vis costs remain higher than expected despite discount equipment | Iron caps impose a cost penalty, and different caps can use different modifiers for different aspects |
| A staff has high capacity but cannot be used in the worktable | Staves do not support arcane crafting; use a wand or sceptre |
| A node has Vis, but the wand cannot draw it | Check for compound aspects, a jarred node, or an already energized node |
| A node regenerates very slowly | Check quality, stabilizer effects, and nearby nodes; Fading quality does not regenerate naturally |
| A node is drained despite Node Preserver research | Check for sneaking or low-quality components such as ordinary Wooden rods or Iron caps |
| Planted Vishrooms do not produce Vis orbs | Vishrooms are an ingredient; harvest mature Primal Shrooms and let a wand with available capacity absorb the orbs |
| An Ethereal Shard has capacity, but the wand cannot draw Vis | Capacity is not the current reserve; provide the complete Centi-Vis supply first |
| An artificial node is smaller than expected after jarring | Jarring uses the amounts currently charged; check actual reserves before sealing |
| A node cultivated by Empowering bees has unbalanced aspects | The effect increases aspects randomly; high total capacity does not ensure all six required aspects are present |
| The original supply method stops working after node conversion | Energized nodes use Centi-Vis networks and cannot be drawn from directly with a wand |
| Centi-Vis devices work intermittently | Check network connections, loaded chunks, aspect output, and competing consumption from other devices |

</Column>
