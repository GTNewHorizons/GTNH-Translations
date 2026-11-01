---
item_ids:
  - Thaumcraft:blockMetalDevice:0
  - Thaumcraft:blockStoneDevice:0
  - Thaumcraft:blockMetalDevice:1
navigation:
  title: Alchemy and Essentia
  parent: ./index.md
  icon: 'Thaumcraft:blockMetalDevice:0'
  position: 60
---

# Alchemy and Essentia

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**Alchemy** uses the aspects in materials to transform them into magical materials, fuels, and items needed for research.<br>
As infusion and magical devices become available, these aspects can also be extracted as <Color color="#B7A0D6">essentia</Color>, forming a production system that stores, distributes, and supplies them on demand.

In GTNH, alchemy also contributes to the processing of technological materials. Transmutation, alchemical duplication, and related research provide material conversion recipes, while magical devices and addons expand the uses of essentia.<br>
Check NEI and the Thaumonomicon for individual recipes.

## Crucibles and Alchemy Recipes

The <ItemLink id="Thaumcraft:blockMetalDevice:0" showIcon="left" /> is the basic alchemy facility, created by using a wand on a placed Cauldron.<br>
It holds 1000 mB of water and requires a continuous heat source below it. Once the water boils and bubbles appear, it can dissolve ingredients and perform recipes.<br>
Water can be supplied through fluid pipes. Fire, lava, or <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" /> can provide heat.

Ingredients added to the Crucible contribute their aspects. Once the required aspects are present, adding the appropriate **catalyst** consumes those aspects and produces the result.<br>
Catalyst handling depends on research and recipe conditions. When a recipe cannot be performed, a catalyst containing aspects may also be dissolved.

- <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" /> provides light and can heat Crucibles and Thaumatoriums.
- <ItemLink id="Thaumcraft:ItemResource:0" showIcon="left" /> is an alchemical fuel that also speeds up essentia distillation in an Alchemical Furnace.
- <ItemLink id="Thaumcraft:ItemResource:2" showIcon="left" />, Balanced Shards, and other alchemical materials are widely used in later devices and magical items.

Each successful Crucible recipe consumes 50 mB of water. Any aspects left after crafting remain available for other recipes.<br>
Wearing <ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> reveals their types and amounts.

GTNH enables a fix for processing a whole stack of catalysts when water runs out, stopping further crafting once the water is depleted. When processing batches, keep track of the remaining aspects and research requirements to avoid dissolving catalysts.

## Leftover Aspects and Flux

Aspects in a Crucible degrade over time. Each degradation converts a compound aspect into one of its components, while primal aspects disappear.<br>

This process may generate <Color color="#B7A0D6">Flux</Color>.

When the Crucible contains more than 100 aspect points in total, losses and Flux spills become more frequent.
GTNH also enables additional degradation above 200 points, with the amount increasing as the excess grows.<br>
For large batches of the same item, a Thaumatorium makes consumption easier to control.

Choose ingredients with the requirements of related recipes in mind, using leftover aspects for another product. Calculate input quantities from the number of planned crafts to reduce residues left in the Crucible for long periods.

> [!WARNING]
> Sneak-right-clicking a Crucible with a wand empties its water and aspects, releasing Flux. Both the degradation of large surpluses and emptying the Crucible can pollute the surroundings. Leave space for Flux treatment in your alchemy area.

A <ItemLink id="Thaumcraft:blockStoneDevice:14" showIcon="left" /> removes nearby Flux Gas and Flux Goo, requires Aer energy, and can recover some essentia.<br>
Taint that has already spread requires suitable purification facilities.

## The Thaumatorium

After completing **Automated Alchemy** research, a structure made from one Crucible and two <ItemLink id="Thaumcraft:blockMetalDevice:9" showIcon="left" /> blocks can be activated with a wand to form a Thaumatorium.<br>
It suits repeated production of alchemical materials, drawing the quantities of essentia required by each recipe from external supplies.

- **Operating requirements:** It still needs a heat source below it, but requires no water.
- **Recipe selection:** Adding a catalyst lists the related recipes in the interface, where you can select an unlocked result.
- **Essentia supply:** Connect tubes or an Essentia Provider to a compatible port to supply the aspects requested by the current recipe.
- **Product output:** Products leave through the small opening on the upper front. An inventory placed in front of this opening can receive them directly.
- **Recipe memory:** It normally retains one active recipe. Each <ItemLink id="Thaumcraft:blockMetalDevice:12" showIcon="left" /> adds two more.

The Thaumatorium allows catalyst input, essentia supply, and product collection to connect separately to logistics systems. When several products share a catalyst, check which recipes are active, especially when using autocrafting.

## Essentia Distillation

An <ItemLink id="Thaumcraft:blockStoneDevice:0" showIcon="left" /> breaks items down into essentia, which the <ItemLink id="Thaumcraft:blockMetalDevice:1" showIcon="left" /> above it separates by aspect. Up to five alembics can be stacked on a single furnace.

- **Furnace buffer:** 50 points in total, shared by multiple aspects.
- **Alembic buffer:** 32 points each, holding one type of essentia at a time.
- **Ingredient input:** Feed items to be broken down through the sides of the furnace.
- **Fuel input:** Supply solid fuel from below. Alumentum speeds up distillation.

Items containing more aspects take longer to break down. If an item's total aspect content exceeds the furnace's remaining buffer space, the furnace cannot continue processing.<br>
Essentia left in the alembics can also block output, so continuous production requires a collection system.

Right-click an alembic with an essentia jar to collect essentia compatible with the jar's contents.<br>
A <ItemLink id="Thaumcraft:ItemEssence:0" showIcon="left" /> collects 8 points at a time and cannot be filled when the alembic contains fewer than 8 points.<br>
Automatic collection can use tubes, alchemy golems, or Thaumic Energistics' Essentia Import Buses.

## Choosing Essentia Ingredients

NEI's aspect source pages help you find ingredients. Consider aspect yield, byproducts, acquisition cost, and the ability to maintain a steady supply.

- **Main demand:** Compare the amount of the desired aspect per item and the time the furnace takes to process it.
- **Other aspects:** Provide storage or an outlet for the other essentia produced by the same ingredient. A full byproduct store can stop the entire production line.
- **Reliable sources:** Farms, tree farms, mob drops, and byproducts from existing processing lines suit continuous distillation.
- **Processed forms:** Different item forms of the same material may contain different aspects. Choose ingredients according to the processing facilities available.

For essentia such as <Color color="#B7A0D6">Magic (Praecantatio)</Color>, Metal (Metallum), or Life (Victus), find candidate ingredients by aspect, then compare their overall output. Once the essentia system is established, separate inputs for frequently used ingredients make it easier to replenish particular stocks.

## Jars, Labels, and Phials

A <ItemLink id="Thaumcraft:blockJar:0" showIcon="left" /> holds 64 points of one type of essentia and retains its contents when broken. Jars are useful for transport, preparing supplies for devices, and building smaller storage areas sorted by aspect.

A <ItemLink id="Thaumcraft:ItemResource:13" showIcon="left" /> locks a jar to a particular aspect. A label already assigned to an aspect can also be applied to an empty jar. Labels affect suction priority in tube systems:

- An unlabeled ordinary jar has 32 suction.
- A labeled ordinary jar has 64 suction until full, then stops drawing essentia.
- A <ItemLink id="Thaumcraft:blockJar:3" showIcon="left" /> continues accepting and destroying excess essentia after filling. When labeled, it has 48 suction until full, then drops to 32.

Void Jars provide an outlet for byproducts that remain in surplus over time. In tube networks, labeled ordinary jars will usually fill first. In AE storage systems, configure the Storage Bus priority and its option for using Void Jars.

Glass Phials and Phials of Essentia hold 8 points per filled phial, making them convenient for carrying and transferring small amounts. They are also used in some recipes and for assigning aspects to labels.

> [!WARNING]
> Sneak-right-clicking a jar or alembic with an empty hand clears its essentia. Clicking the labeled face of a jar removes the label; clicking another face may empty the jar. Excess essentia accepted by a Void Jar is also permanently lost.

## Essentia Tubes and Suction

An <ItemLink id="Thaumcraft:blockTube:0" showIcon="left" /> uses <Color color="#B7A0D6">suction</Color> to determine essentia flow. A receiving device's suction propagates through tubes toward the source, losing 1 point per ordinary tube segment. Essentia moves toward a compatible receiver with higher suction.

Each ordinary tube segment holds only one type of essentia at a time and responds to one suction type.<br>
When labeled jars for different aspects share a line, their requests can interfere with each other, causing stalled flow or venting. Filters and valves can limit the propagation of requests so that individual branches work as intended.

Common components for routing and control include:

- <ItemLink id="Thaumcraft:blockTube:3" showIcon="left" />: Once labeled, it only allows the selected essentia through.
- <ItemLink id="Thaumcraft:blockTube:1" showIcon="left" />: Opens and closes manually or through redstone, isolating branches that are temporarily unused.
- <ItemLink id="Thaumcraft:blockTube:6" showIcon="left" />: Restricts the direction of transfer, helping prevent backflow through branches.
- <ItemLink id="Thaumcraft:blockTube:5" showIcon="left" />: Halves propagated suction to adjust competition between branches.
- <ItemLink id="Thaumcraft:blockTube:4" showIcon="left" />: Temporarily stores 8 points in total across multiple essentia types. Its default suction is low; attaching Arcane Bellows increases it.

An <ItemLink id="Thaumcraft:ItemResonator" showIcon="left" /> reads the essentia type, amount, and suction in devices or tubes.<br>
When flow stops, inspect the source, tubes, and receiver to find where suction is interrupted or aspect requests conflict.

Dedicated lines for individual aspects are easier to keep stable. For systems handling multiple aspects, use buffers and controlled branches, or let Thaumic Energistics handle the main storage and distribution.

## Centrifuging and Other Transport Options

An <ItemLink id="Thaumcraft:blockTube:2" showIcon="left" /> receives compound essentia from below and outputs one of its component aspects from above.<br>
Each point of compound essentia consumed produces 1 point of a randomly chosen component, which may itself still be a compound aspect.

This lets existing compound essentia replenish more basic aspects. Connect an Essentia Buffer above the centrifuge, then route the two possible outputs into separate branches. Further decomposition requires multiple stages and suitable output handling.

- **Alchemy golems:** Transport essentia between sources and jars, serving storage areas spread across several locations. Check the golem research for range, assignments, and upgrades.
- <ItemLink id="Thaumcraft:blockMirror:6" showIcon="left" />: Linked pairs supply distant essentia to Runic Matrices and other devices that draw from nearby sources.
- <ItemLink id="Thaumcraft:blockTube:7" showIcon="left" />: Condenses essentia into Ethereal Essences for storage and transport as items.

## Thaumic Energistics and Essentia Autocrafting

Thaumic Energistics stores essentia in an ME network, using **Essentia Storage Cells** and an **Essentia Terminal** to manage stocks. Its common interfaces include:

- **Essentia Import Bus:** Imports essentia from alembics, jars, and other devices into the network.
- **Essentia Export Bus:** Supplies configured essentia types to external devices or containers.
- **Essentia Storage Bus:** Makes external essentia containers part of the network's inventory, bringing existing jar storage under unified management.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.essentia.provider" showIcon="left" />: Works with essentia tube connections, allowing Thaumatoriums and similar devices to obtain essentia from the network. It can also collect essentia from adjacent sources and has 8 suction.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.infusion.provider" showIcon="left" />: Supplies network essentia to Runic Matrices and other devices that draw from nearby sources.

The <ItemLink id="thaumicenergistics:thaumicenergistics.block.distillation.encoder" showIcon="left" /> encodes item distillation into essentia autocrafting patterns.<br>
Use an actual item and its aspect information when encoding, select the desired essentia outputs, and provide the pattern to the ME autocrafting system.<br>
The distillation line receives the ingredients and returns the extracted essentia to the network.

This enables on-demand production of missing essentia. Other aspects from the same ingredient still need to be collected. When regularly replenishing a commonly used aspect, provide storage or an outlet for byproducts that accumulate over time.

When connecting a Void Jar through an Essentia Storage Bus, enable the corresponding option in the bus interface and set a lower priority so normal storage receives essentia first.

## Increasing Essentia Production

As demand grows, you can upgrade extraction devices while keeping the existing storage and distribution system:

- <ItemLink id="thaumicbases:advAlchFurnace" showIcon="left" />: An upgrade to the ordinary Alchemical Furnace with faster processing. It still outputs through Arcane Alembics above it and can use bellows.
- <ItemLink id="Thaumcraft:blockAlchemyFurnace" showIcon="left" />: Requires research involving a Primordial Pearl, has a 500-point essentia buffer, and uses Ignis, Perditio, and Aqua Centi-Vis.<br>
Items enter through the opening at the top, and the lower ports output essentia. An Item Grate makes it easier to feed ingredients using item logistics.
- **Large Essentia Smeltery:** GT's large-scale extraction machine, requiring electricity and Centi-Vis. Essentia Output Hatches or ME Essentia Output Hatches connect it to downstream systems. Its structure and Diffusion Cells affect processing performance.

When increasing extraction speed, also check the throughput of alembics and essentia interfaces. If essentia remains in an extraction device's buffer for long periods, address output and storage first.

The Advanced Alchemical Furnace uses Ignis to maintain its temperature, consuming it even while idle. Perditio and Aqua are used during processing.<br>
For Centi-Vis sources, connections, and output, see [Wands, Vis and Nodes](./wands_vis_nodes.md).

## Common Problems

- **No output after adding ingredients to a Crucible:** Check whether the water is boiling, the research is complete, the catalyst matches, and the required aspects have degraded.
- **Catalysts dissolve:** Check the remaining aspects and research requirements. For batches, keep track of water and the number of successful crafts.
- **An Alchemical Furnace stops processing:** Check fuel, remaining buffer space, and whether the alembics have been emptied. An ingredient's total aspect content may also exceed the remaining buffer space.
- **One essentia type never flows:** Use an Essentia Resonator to inspect suction and aspect types, then check labels, filters, valves, and competing branches.
- **A Thaumatorium has catalysts but does not work:** Check the heat source, active recipes, and the supply path for each required aspect.
- **An essentia line stops periodically:** Check for full byproduct storage, available network storage space, and interface throughput.
- **AE contains essentia, but a device still lacks it:** Check whether the interface suits the target device, along with network power, channels, and configuration.

</Column>
