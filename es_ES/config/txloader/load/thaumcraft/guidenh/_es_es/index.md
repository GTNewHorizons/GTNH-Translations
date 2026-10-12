---
item_ids:
  - Thaumcraft:ItemThaumonomicon
navigation:
  title: Thaumcraft
  icon: 'Thaumcraft:ItemThaumonomicon'
  position: 40
---

# Thaumcraft

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/infusion_altar.snbt" />
</GameScene>

**Thaumcraft 4** (TC4) is one of GTNH's main magic mods and the first magic mod you encounter.

Starting with scanning and research, you gradually learn about the aspects contained in items and creatures. Through alchemy and infusion, you can create wands, magical tools, equipment and automation systems.

In NH, Thaumcraft is closely connected to technology materials, the Twilight Forest and other magic mods. As your research progresses, you can explore Botania and Blood Magic, connect magical systems to AE, or use magic to maintain GT machines.

This page provides an overview of Thaumcraft's world, basic concepts and NH-specific changes, focusing on the uses of magical facilities and the differences between <Color color="#B7A0D6">research points, Vis and essentia</Color>.

<br clear="all" />

## The World of Thaumcraft

- **Everything has aspects.** In Thaumcraft, objects have more than an appearance and a purpose: they also contain <Color color="#B7A0D6">aspects</Color> that you can observe and study. Fire, water, order, life and metal can all be described through aspects. Combining aspects produces more complex properties; understanding these relationships is fundamental to research and alchemy.

- **Knowledge becomes infrastructure.** The world also contains <Color color="#B7A0D6">aura nodes</Color> that gather magical energy. Wands can draw Vis from nodes for arcane crafting and wand foci. Essentia extracted from items is used for alchemy, infusion and some magical devices. As your knowledge and facilities improve, you move from manual research and crafting to essentia storage, logistics and automated production.

- **Exploration has consequences.** Processing magical materials can pollute the surrounding environment, while learning forbidden knowledge can give the player Warp. When researching a new ability, learn about its uses, costs and effects together.

## The Thaumonomicon

The <ItemLink id="Thaumcraft:ItemThaumonomicon" showIcon="left" /> is your main source of knowledge about Thaumcraft, containing research explanations, research notes and unlocked recipes. Its research entries provide the operating instructions for individual devices.

The book has separate tabs for different topics and addons. Research has prerequisites, and some entries only appear after specific scans or other conditions are met. **An entry being absent does not necessarily mean it does not exist.**

| Content in the Book | Information Provided |
| --- | --- |
| Research icons and connections | Prerequisites between research entries and hints about unlocking them |
| <Color color="#B7A0D6">Research notes</Color> | Research solved at a Research Table, primarily through aspect connections |
| Research that costs research points | The aspect types and research points required to unlock it |
| Completed research | Device uses, operating instructions and recipes |
| <Color color="#D5B77A">Forbidden knowledge markers</Color> | Purple effects and the associated warnings indicate that learning this research may cause Warp |

Completed research must be read to unlock its content. **Research unlocks and material requirements are independent:** seeing a recipe in the book does not mean your technology and magical facilities can already produce it.

## Aspects, Research Points, Vis and Essentia

These concepts often use the same aspect icons, but serve different purposes. When you see an icon, first check whether it appears at a Research Table, in a wand or in an essentia container.

| Concept | Meaning | Main Uses |
| --- | --- | --- |
| <Color color="#B7A0D6">Aspects</Color> | Properties that describe items, creatures and magical phenomena | Understanding research combinations and identifying which essentia an item can provide |
| <Color color="#B7A0D6">Research points</Color> | Research resources accumulated by the player, tracked separately for each aspect | Connecting research notes, combining aspects and unlocking some research |
| <Color color="#B7A0D6">Vis</Color> | Magical energy stored in a wand, tracked separately for each primal aspect | Crafting at an Arcane Worktable, using wand foci and similar operations |
| <Color color="#B7A0D6">Essentia</Color> | Aspects extracted from items that can be stored and transported | Alchemy, infusion and some magical devices |

## Aspects and Research Points

The six <Color color="#B7A0D6">primal aspects</Color> are <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air (Aer), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth (Terra), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Fire (Ignis), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Water (Aqua), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Order (Ordo) and <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" />Entropy (Perditio). Compound aspects are formed from two other aspects; NH's addons also expand the aspect system.

Scanning items, creatures and other targets can reveal aspects and grant research points. Some targets require you to know their component aspects before they can be scanned. Combining aspects at a Research Table can also help you discover new compound aspects. If you lack research points, you need to replenish your research resources; charging a wand will not solve that problem.

## Vis and Essentia

Vis in a wand is tracked separately for the six primal aspects. Check the stored amount of each aspect required by an arcane recipe; having one aspect fully charged cannot make up for a shortage of another.

Essentia is usually extracted from items using an Alchemical Furnace or similar facilities, then collected in jars or other containers. A recipe requiring compound aspects such as metal or life is often asking for the corresponding essentia rather than Vis in a wand.

Aer Vis required by an Arcane Worktable and Metallum essentia required by infusion come from a wand and an essentia supply system, respectively. **Research points, wand Vis and essentia in jars cannot replace each other.**

## Nodes and Sources of Magical Energy

**Aura nodes** are concentrations of magical energy in the world. Observation tools reveal their aspects, and wands can draw Vis from them. Most nodes gradually regenerate their energy, so finding and managing nodes is an important part of early magical power supply.

Nodes have different types, qualities and aspect compositions. Once you understand them, you can research ways to move, preserve and modify them, using what you find while exploring to supply your base's magical facilities.

> [!WARNING]
> When drawing energy from a node with an early wand, avoid casually draining an aspect to zero. <Color color="#D5B77A">Draining a node completely</Color> can damage it and affect its ability to provide energy later. First learn what protections your wand and completed research offer.

Later, you will also encounter <Color color="#B7A0D6">Centi-Vis</Color>: modified nodes can supply compatible devices with this form of energy. Storing Vis in a wand and building a Centi-Vis supply network are two forms of power supply that you need to understand separately.

## Vis Costs and Discounts

<Color color="#B7A0D6">Wand capacity</Color> determines how much Vis of each primal aspect the wand can store, while <Color color="#B7A0D6">Vis discounts</Color> reduce the energy actually consumed by an operation. Wand caps and some equipment provide discounts. For more demanding recipes, consider both wand capacity and the discounts available to you.

For example, suppose an arcane recipe has a base requirement of 100 Vis of one aspect, with a total applicable discount of 20%. The actual requirement becomes 80 Vis of that aspect. This allows a wand with a capacity of 80 to satisfy a recipe that originally required 100, but the wand's capacity remains 80.

| Problem | What to Check |
| --- | --- |
| The wand has enough capacity but lacks stored energy | Replenish every type of Vis required by the recipe |
| A fully charged wand still cannot meet the recipe's requirements | Upgrade the wand or increase the discounts applicable to that craft |
| You have equipment with discounts but still cannot craft | Check the actual requirements, whether the equipment is worn and the stored amount of each aspect |
| Infusion lacks essentia | Prepare an essentia supply; Vis discounts cannot replace essentia ingredients |

## Flux, Taint and Warp

Environmental problems and effects on the player need to be understood separately.

| Concept | Main Target | What to Know |
| --- | --- | --- |
| <Color color="#D5B77A">Flux</Color> | The surrounding environment | Improper magical processing can release pollution; watch your alchemy facilities and their surroundings |
| <Color color="#D5B77A">Taint</Color> | Terrain, blocks and creatures | An environmental hazard that needs dedicated treatment; investigate its source and control methods when you find it |
| <Color color="#D5B77A">Warp</Color> | The player | Forbidden research and some actions cause Warp, which can trigger related events |

Cleaning up environmental pollution does not remove the player's Warp, and dealing with Warp does not replace treating a tainted area. Look for forbidden knowledge warnings when reading new research, and consider pollution control when preparing new alchemy facilities.

> [!WARNING]
> Warp Theory adds more Warp events in NH. <Color color="#D5B77A">High Warp</Color> can trigger dangerous events that damage your base. Before pursuing forbidden research, learn about these events and how to respond, and make suitable arrangements for valuable facilities and items.

## NH-Specific Changes and Mod Integration

NH makes many changes to Thaumcraft's material progression, research and user experience, mainly in the following areas.

| Topic | What to Watch For in NH |
| --- | --- |
| Wand materials | The usual wand progression involves Twilight Forest boss materials; check current recipes and material sources before crafting |
| Wand upgrades | Capacity and Vis discounts need to develop together; after completing the relevant research, you can also replace wand rods and caps |
| Recipe lookup | Use the Thaumonomicon for research and operating instructions, and NEI to check current recipes; the quest book explicitly directs you to NEI for some wand recipes |
| Scanning conveniences | You can scan items in your inventory; scanning an entire chest still requires the corresponding research |
| Research and aspect assistance | Aspect Recipe Index and similar features help you find aspect sources, combinations and related recipes |
| Magical automation | Golems, Automagy and related content provide logistics and automation facilities; Thaumic Energistics connects essentia storage and supply to AE |
| Technology and magic integration | Addons such as EMT provide tools and devices; GT also has facilities such as the Research Completer and Vis Maintenance Hatch |
| Other magic paths | Botania and Blood Magic also have connections to Thaumcraft research and materials |

Magic offers movement and building tools, equipment and enchantments, durability repair, material processing, and item and essentia automation. Choose a research direction based on your current needs, then follow its prerequisites to develop the facilities you need.

## Topics

This category organizes guides by topic, with each topic page directly under Thaumcraft. The guides focus on an overview of mechanics, facility uses, resource relationships and NH-specific changes. The Thaumonomicon and NEI provide detailed operating instructions and recipes.

| Chapter | Main Content |
| --- | --- |
| [Thaumcraft Basics](./thaumcraft_basics.md) | The Thaumonomicon, aspects, nodes, Warp, Vis, Vis discounts and an overview of the world |
| Aspects, Scanning and Research | The aspect system, scanning conditions, research points, research notes and prerequisites |
| Wands, Vis and Nodes | Wand properties, uses of foci, node types, Vis and Centi-Vis supply |
| Alchemy and Essentia | Crucibles and alchemy devices, essentia production and distribution, pollution control |
| Infusion Crafting | Altar components, recipe resources, stability and integration with other devices |
| Golems and Automation | Golem functions, cores and upgrades, work areas and logistics uses |
| Warp and Eldritch Knowledge | Sources of Warp, ways to deal with it, Eldritch research and exploration |
| Thaumic Tinkerer | Enchanting, repairs, infused crops, devices and KAMI content |
| Addons and GT Integration | Thaumic Energistics, other addon facilities, and GT's magical devices and material connections |

</Column>