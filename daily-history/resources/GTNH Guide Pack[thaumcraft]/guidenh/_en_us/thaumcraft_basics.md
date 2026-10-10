---
navigation:
  title: Thaumcraft Basics
  parent: ./index.md
  icon: 'Thaumcraft:ItemThaumometer'
  position: 90
---

# Thaumcraft Basics

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

In Thaumcraft, stones, trees, creatures and even machines can all be described through <Color color="#B7A0D6">aspects</Color>.<br>
Through observation and research, thaumaturges learn to understand these properties, then use wands, alchemy and infusion to turn that knowledge into useful tools and facilities.

Aura nodes in the world provide magical energy, while the aspects within items provide materials for alchemy. Delving into forbidden knowledge can also bring <Color color="#D5B77A">Warp</Color> upon the researcher.<br>
Together, these concepts form the world of Thaumcraft: **essentia, Warp, magical energy and aspects** are connected, but have different storage locations, sources and uses.<br>
Aspects appear repeatedly in item descriptions, research tables, wands, nodes and recipes. Understanding an aspect means considering both where it appears and which aspects it can combine to form.

## Aspects

**Aspects** describe an object's composition and properties. They can represent natural attributes such as air and earth, as well as concepts such as life, metal and order.<br>
Here, "composition" refers not only to the materials an object is made from, but also to its magical tendencies and meaning. Creatures, tools and magical items can therefore all be described using the same system.

The six primal aspects are <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air (Aer), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth (Terra), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Fire (Ignis), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Water (Aqua), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Order (Ordo) and <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" />Entropy (Perditio).
They form the foundation of the aspect system. Compound aspects are formed by combining two other aspects.<br>
For example, <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"victus"}' scale="0.75" />Life (Victus) is composed of Earth and Water.<br>

Compound aspects can themselves contain other compound aspects, creating a network of relationships that extends through multiple layers.<br>Connections in research notes follow these relationships. Understanding how aspects relate to one another helps explain both research connections and how alchemical materials provide essentia.

**The aspects contained in an item and the combinations that form an aspect are two different kinds of information.** The former tells you which aspects an item provides and in what amounts; the latter tells you which two aspects make up a compound aspect.<br>An item can contain several aspects in different amounts. Different items may provide the same aspect, so there are often several possible materials for producing a particular type of essentia.

Addons also expand the aspect system. When you encounter an unfamiliar aspect, its name, composition and presence in actual items are more useful than simply memorizing every icon.<br>**Discovering an aspect means you understand it; having research points for that aspect means you have a corresponding resource to spend on research.**

## The Thaumonomicon

<ItemLink id="Thaumcraft:ItemThaumonomicon" showIcon="left" />is the main source of knowledge in Thaumcraft.<br>It organizes research entries by topic and addon, recording lore, item uses, requirements and recipes. Completed research can be consulted at any time, while unfinished research shows the directions you can explore next.

Research in the book is not a collection of independent recipes. Connections between entries indicate prerequisites: a research may build on basic knowledge or require knowledge from several different areas.<br>Some entries also require specific scans, other conditions or discoveries related to Eldritch knowledge before they appear. **An entry being absent does not necessarily mean that its content is missing from the modpack.**

Research can be completed in different ways. Entries that require research notes involve studying a note at a research table, completing its aspect connections, then obtaining and reading the resulting discovery.<br>Other research unlocks directly by consuming the required research points. Both grant knowledge, but their resource costs and completion methods differ.

The Thaumonomicon reflects the player's research progress. Owning a book is the beginning of a thaumaturgical journey; unlocking research and obtaining items should be understood separately.

In GTNH, research progress is also closely connected to material processing, other magic mods and GT machines.<br>
The book is useful for understanding mechanics and research relationships, while actual recipes should also be checked against the current instance's NEI and quest book. Some descriptions retained from the original mod do not fully reflect GTNH's changes.

## Scanning, Research Points and Aspects

<ItemLink id="Thaumcraft:ItemThaumometer" showIcon="left" />is used to examine the aspects of items, blocks and creatures, and can also reveal aura nodes.<br>Scanning yields research points from an object's aspects, reveals which aspects it contains and sometimes provides clues to new research.

Some objects cannot yet be scanned because their aspects are not understood. Aspect knowledge follows composition relationships, so researchers must first understand the relevant basic and component aspects before they can understand more complex objects. This is why exploration and research support each other.

**Research points** are recorded for each player by aspect type. They are the resource used by the research table and some directly unlocked research. The amounts of <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air, <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth and other aspects shown in the research table<br>indicate the remaining research points for each aspect. Placing aspects in research notes costs research points; combining aspects to obtain points for a compound aspect also consumes points for its component aspects.

Aspect connections in research follow direct composition relationships. For example, Life is composed of Earth and Water, so Life is connected to both Earth and Water. **Understanding these relationships is knowledge; placing the aspects also requires research points.** Knowing an aspect without having its research points still prevents you from using it in research.

Scanning is an important source of research points, but repeatedly scanning the same kind of object cannot provide an unlimited supply. As research progresses, other ways to obtain research points or assist with research become available. The Vis stored in your wand and the essentia jars in your base do not directly determine your research point reserves.

## Vis: Magical Energy

<Color color="#B7A0D6">Vis</Color> is an important term for magical energy in Thaumcraft. Energy drawn from nodes is stored in wands as <Color color="#B7A0D6">Vis</Color>, mainly for arcane crafting, wand foci and similar uses. In Thaumcraft's lore, both <Color color="#B7A0D6">Vis</Color> and essentia are related to aspects separated from objects and purified. In practice, wand reserves, device power supplies and essentia containers need to be distinguished.

**Wands store Vis separately for each of the six primal aspects.** Each has its own current reserve and capacity. If a recipe requires Air and Order, having more Fire cannot make up for missing Order.

Wands both store and use magical energy. Wand caps, rods and related equipment can affect capacity or the <Color color="#B7A0D6">Vis</Color> cost of applicable operations. When reading a recipe, consider the required aspect types, their amounts and whether your current wand can meet those requirements.

## Vis Discounts

> [!NOTE]
> **Vis discounts** are a very important mechanic in GTNH. They reduce the <Color color="#B7A0D6">Vis</Color> consumed by applicable operations.

The actual Vis cost of the same recipe can be reduced by using different wands or equipment. Discounts do not change the required aspect types, however, and the same discount does not necessarily apply to every magical system. Vis discounts cannot solve insufficient essentia, missing crafting materials or locked research.<br>
In GTNH, crafting a wand with a higher Vis capacity often requires stacking discounts to meet the minimum requirements for crafting that wand.

## Aura Nodes

**Aura** is the magical energy present throughout the world, while **aura nodes** are concentrations of that energy. A node is more than a special object to scan: it contains particular aspect types and amounts, and is an important source of Vis for wands.

<ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" />provide magical sight that helps you locate aura nodes.

> [!NOTE]
> Previously scanned nodes can be looked up with the I key.

When examining a node, distinguish its aspect composition, reserves and condition. The aspects it provides determine which magical energy it can replenish, while their amounts indicate the scale of its reserves.<br>Its type and quality affect its properties and ability to supply energy. Most nodes replenish drained energy over time, but their recovery and uses are not all the same.

Aura nodes have six types and four quality states. The type determines a node's special effects, while its quality determines how quickly its aspects regenerate.<br>
The core's appearance helps identify its type; scanning the node with a Thaumometer also reveals the type's name.

<Column width="500" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_types.png" x="0" y="140" width="2170" height="440" displayWidth="500" wrap="inline" title="Aura Node Types" />
</Column>

| Type | Description | Core Appearance | Effects |
| --- | --- | --- | --- |
| Normal | The most common and ordinary type, with a stable core and no special effects. | White | None |
| Sinister | A relatively dangerous node type.<br>Usually generated alongside obsidian totems, Eldritch altars, barrows or elven altars. | Dark purple | Gradually changes biomes in a 25×25 area centered on itself to Eerie.<br>When a player enters within 24 blocks, it can spawn Furious Zombies in an 11×3×11 area in low light. |
| Pure | Usually generated inside Silverwood trees. | White,<br>turbine-like | Changes Tainted Land within its range to Magical Forest.<br>Those inside Silverwood trees can change any surrounding biome to Magical Forest. |
| Tainted | Naturally generated in Tainted Land. A non-Pure node in Tainted Land can also become Tainted over time. | Purple,<br>smoky | Changes biomes in a 15×15 area centered on itself to Tainted Land.<br>Also generates tainted growth on block surfaces within a 9×9×9 area. |
| Unstable | Similar to a Normal node, but its core constantly pulses. | White,<br>radiating | Every 5 seconds, has a 50% chance to convert one stored point of a primal aspect into an aspect orb and release it. |
| Hungry | The rarest and most dangerous node type, appearing very rarely through natural world generation. | White,<br>ring-shaped | Draws in and devours everything within 16 blocks, absorbing its aspects to increase the node's aspect capacity. |

<Column width="400" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_states.png" displayWidth="400" wrap="inline" title="Aura Nodes" />
</Column>

- **Normal (not displayed): regenerates one aspect point every 30 seconds.**
- **Bright: regenerates one aspect point every 20 seconds and appears more vivid than a Normal node.**
- **Pale: regenerates one aspect point every 45 seconds and appears dimmer than a Normal node.**
- **Fading: does not regenerate aspects, appears extremely dim and flickers constantly.**

**A node's reserves and a wand's reserves are independent.** Drawing energy transfers Vis provided by the node into the wand. Spending Vis from a wand does not mean that a node will automatically refill it. A node that provides only some aspects cannot supply all the energy required by every recipe on its own.

Nodes usually contain primal aspects, but may also contain compound aspects. Their icons describe their magical composition; they do not make nodes into research point stores or essentia jars. Finding, scanning and using nodes involve observation, research rewards and actual energy supply respectively.

> [!WARNING]
> Draining an aspect from a node to zero with a wand can damage the node or even remove that aspect. Exhausting every aspect can make the node disappear entirely. <Color color="#D5B77A">The ability to regenerate magical reserves does not mean that damage to the node will automatically heal.</Color> Consider the node protection abilities you have unlocked when assessing charging risks.

Further node research introduces uses such as moving and stabilizing nodes. Device power systems require attention to node output and the facilities that supply the energy, and are related to the Vis stored and consumed in wands.

Replenishing multiple aspects in a wand and establishing a power supply for fixed devices have different requirements. A node's composition, condition and unlocked uses should all be considered in relation to its intended purpose.

## Essentia

<Color color="#B7A0D6">Essentia</Color> consists of aspects separated and refined from items. It can be stored, transported and used through the appropriate containers and facilities.<br>It turns an item's magical properties into a production resource that can be managed centrally, and is an important requirement for alchemy, infusion and some magical devices.

The aspects contained in a material determine which essentia it can provide. An item with several aspects may yield several types of essentia, while a recipe usually needs only some of them.<br>Essentia production therefore involves more than material quantities: it also involves which aspects are needed, what additional output is produced and whether those products can be stored and used properly.

Essentia can belong to primal or compound aspects. Air, Life and Metal essentia are all resources classified by their corresponding aspects.<br>Wands store only the six primal aspects separately, while essentia systems handle a wider range of types. Their containers and supply methods also differ.

Storage and availability should also be distinguished. Having a type of essentia in your base means you own that resource; whether a device can access it still depends on the appropriate containers, transport facilities and supply conditions.

## Arcane Crafting, Alchemy and Infusion

After research is unlocked, crafting still follows the requirements of its particular system. These systems share the language of aspects, but differ in how they obtain magical energy, consume materials and receive resources. When reading a recipe, first identify which system it belongs to.

**Alchemy** focuses on transformations between items and aspects. A Crucible breaks down added items into their aspects; a suitable catalyst then combines with the aspects required by a recipe to produce the target item. Understanding alchemy therefore involves knowing what the materials provide, what the recipe consumes and how unused aspects are handled.

**Infusion** imbues a central item with the properties of other items and with essentia. The infusion altar, placement of ingredients and essentia supply together form the conditions for this process. A wand can be used to start it, but the required essentia must come from the appropriate sources.

Infusion also involves stability and risks during the process. Completing the recipe's research and apparently having all the materials does not guarantee a smooth craft.<br>Insufficient essentia or missing ingredients can stall crafting and increase the chance of unexpected events. Stability and supply conditions will be discussed further in the infusion guide.

## Warp and Forbidden Knowledge

**Warp** is an influence upon the researcher. Some Thaumcraft knowledge concerns forbidden and Eldritch subjects. Researching these subjects, as well as certain crafting activities or other actions, can change the researcher's mind and body. Warp is borne by the player.

The Thaumonomicon records both ordinary research and forbidden knowledge. Forbidden research carries corresponding warnings and purple effects, and learning it can increase Warp.<br>A research entry's prerequisites, benefits and forbidden knowledge warnings are therefore all relevant to understanding it.

The relationship between Warp and knowledge also works in the other direction: discovering and unlocking some Eldritch knowledge depends on the player's Warp state and related events.<br>Unusual events are not always purely negative; they can sometimes provide new insights. Forbidden research can cause Warp, while Warp can help a researcher encounter deeper knowledge, creating a connection between the two.

Warp can be divided into three types:

- Temporary Warp: can gradually fade.
- Sticky Warp: does not naturally fade like temporary Warp and requires appropriate methods to remove.
- Permanent Warp: does not naturally fade; dealing with it in NH depends on additional research and methods.

Warp can manifest as hallucinations, physical discomfort, unusual creatures or other events. Their severity depends on the player's Warp level.
Higher Warp brings more effects and causes Warp events to occur more frequently.

The **Warp Ward** buff can protect the player from Warp effects.

> [!WARNING]
> Warp Theory expands the range of Warp events in GTNH. High Warp can cause dangerous events that may damage your base.

## Warp and Environmental Pollution

Warp mainly describes effects upon the player, while **Flux** and **Taint** concern magical hazards in the environment.<br>Wasteful or abnormal magical processes can generate Flux, such as aspects left unused in a Crucible. Taint affects terrain, blocks and creatures. Contact with Flux can also cause adverse status effects that affect magic use.

## How the Concepts Relate

| Concept | Where It Is Recorded or Exists | Connections to Other Concepts |
| --- | --- | --- |
| Aspects | The magical properties of items and other objects, and composition relationships used in research | Provide a shared classification system for research, Vis and essentia |
| Research points | The player's research resources, recorded by aspect | Used for research; costs are not paid with wand Vis or stored essentia |
| Unlocked research | The player's knowledge progress, consulted through the Thaumonomicon | Grants knowledge and crafting access without also supplying materials or magical energy |
| Wand Vis | Magical energy stored separately in a wand for each of the six primal aspects | Can be drawn from nodes and used for arcane crafting, foci and similar purposes |
| Aura nodes | Concentrations of magical energy in the world | Provide energy for wands and, after further research, can also supply devices |
| Essentia | Appropriate containers and magical production facilities | Obtained from aspects in materials and used for alchemy, infusion and some devices |
| Warp | A state borne by the player | Can result from forbidden research and other actions, and is also connected to the discovery of some Eldritch knowledge |
| Flux and Taint | Environmental magical hazards and their related effects | Connected to magical production and the environment; dealing with them does not remove Warp |

These connections show that exploration, research and production in Thaumcraft are not three isolated systems. Exploration provides objects and clues, research explains aspects and unlocks their uses, nodes and materials provide actual magical resources, and facilities use those resources for crafting and automation.

</Column>