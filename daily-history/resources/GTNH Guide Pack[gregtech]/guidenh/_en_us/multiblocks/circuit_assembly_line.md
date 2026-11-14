---
item_ids:
  - gregtech:gt.blockmachines:12735
  - bartworks:gt.bwMetaGeneratedItem0:2
  - bartworks:gt.bwMetaGeneratedItem0:3
  - bartworks:gt.bwMetaGeneratedItem0:4
  - bartworks:gt.bwMetaGeneratedItem0:5
  - bartworks:gt.bwMetaGeneratedItem0:6
  - bartworks:gt.bwMetaGeneratedItem0:7
  - bartworks:gt.bwMetaGeneratedItem0:8
  - bartworks:gt.bwMetaGeneratedItem0:9
  - bartworks:gt.bwMetaGeneratedItem0:11
  - bartworks:gt.bwMetaGeneratedItem0:12
  - bartworks:gt.bwMetaGeneratedItem0:13
  - bartworks:gt.bwMetaGeneratedItem0:14
  - bartworks:gt.bwMetaGeneratedItem0:15
  - bartworks:gt.bwMetaGeneratedItem0:16
  - bartworks:gt.bwMetaGeneratedItem0:17
  - bartworks:gt.bwMetaGeneratedItem0:18
  - bartworks:gt.bwMetaGeneratedItem0:19
  - bartworks:gt.bwMetaGeneratedItem0:20
  - bartworks:gt.bwMetaGeneratedItem0:21
  - bartworks:gt.bwMetaGeneratedItem0:22
  - bartworks:gt.bwMetaGeneratedItem0:23
  - bartworks:gt.bwMetaGeneratedItem0:24
  - bartworks:gt.bwMetaGeneratedItem0:25
  - bartworks:gt.bwMetaGeneratedItem0:26
  - bartworks:gt.bwMetaGeneratedItem0:27
  - bartworks:gt.bwMetaGeneratedItem0:28
  - bartworks:gt.bwMetaGeneratedItem0:29
  - bartworks:gt.bwMetaGeneratedItem0:30
  - bartworks:gt.bwMetaGeneratedItem0:31
  - bartworks:gt.bwMetaGeneratedItem0:32
  - bartworks:gt.bwMetaGeneratedItem0:33
  - bartworks:gt.bwMetaGeneratedItem0:34
  - bartworks:gt.bwMetaGeneratedItem0:35
  - bartworks:gt.bwMetaGeneratedItem0:36
  - bartworks:gt.bwMetaGeneratedItem0:37
  - bartworks:gt.bwMetaGeneratedItem0:38
  - bartworks:gt.bwMetaGeneratedItem0:39
  - bartworks:gt.bwMetaGeneratedItem0:40
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKKQ==
  - AAAAAAAAAAAAAAAAAAAKKA==
  - AAAAAAAAAAAAAAAAAAAKLQ==
  - AAAAAAAAAAAAAAAAAAAKLA==
  - AAAAAAAAAAAAAAAAAAAKKw==
  - AAAAAAAAAAAAAAAAAAAKLg==
  - AAAAAAAAAAAAAAAAAAAKKg==
navigation:
  title: Circuit Assembly Line
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:12735
  position: -6001
---
# Circuit Assembly Line
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12735" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:12735" showIcon="left" />(CAL) is an LuV tier multiblock specialized in circuit assembling. 

The CAL is a direct upgrade from the singleblock circuit assembler because it runs perfect overclocks and bulk recipes that are 1/6th the average cost for crystal, wetware, bioware, and optical circuits. However, the CAL is built as a series of slices similar to the regular [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) and inputs must be inserted in the exact order in which they appear in NEI. 

The CAL must also be permanently imprinted with a specific circuit type which means it cannot process anything other than that; there is no universal setup and there are no data sticks/hatches. 

The CAL has an alternate circuit assembler mode which allows it to craft normal circuit assembler recipes without inserting inputs in a specific order or across the different slices, although it can only process $$\text{Energy Hatch Tier}-1$$ tier recipes.

The CAL is superseded by the [<ItemLink id="gregtech:gt.blockmachines:9500" showIcon="left" />](./nanochip_assembly_complex.md) in UEV.

| Property | Details |
| --- | --- |
| Unlock Tier | LuV |
| Structure Size (LxWxH) | 3x2-7x3 |
| Power | Regular |
| Overclocks | Perfect |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting

<RecipesFor id="gregtech:gt.blockmachines:12735" handlerId="gt.recipe.fakeAssemblylineProcess"  />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gregtech:gt.blockcasings2" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="gregtech:gt.blockcasings2:5" />

### Structure
The CAL is built as a series of slices with an input bus at the bottom center of each one.  
Each slice can only have 1 type of item when the CAL operates in Circuit Assembly Line mode. For this reason, the CAL needs as many slices as the recipe has item types to process a CAL recipe.  
For example, the crystal processor has six solid inputs and therefore needs seven slices to craft (the last is for the output bus).

If the CAL operates in Circuit Assembler mode, this restriction does not apply, but the CAL needs to be **at least 5 slices long to operate**.

The CAL can be rotated or flipped. The slice with the controller is always the front and therefore the location of the first input. 

The glass only needs to be EV+ and has no effect on the operation of the machine. 

Multi-amp and laser energy hatches are not supported and there can only be **ONE** regular energy hatch. Unlike the regular Assembly Line, the output bus must be on the bottom center of the last slice. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass and the projector stack size to specify the length of the machine, up to the maximum of seven blocks long.

#### Base Structure (Minimum requirements)
| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:12735" showIcon="left" /> | 1, First slice, 3rd layer |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 4, Both sides of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 4, 3rd layer |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-3, Both sides of 1st layer |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 2, Center of 2nd layer |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1, Any 3rd layer Casing |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Any 1st layer side casings |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1, Center of 1st layer |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Any 1st layer side casings |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1, Center of 1st layer, on last slice |

#### Each Additional Slice

<GameScene interactive={true} wrap="square" align="right" width="170" height="130">
  <Block id="gregtech:gt.blockmachines:71" />
  <Block id="gregtech:gt.blockcasings2" x="-1"/>
  <Block id="gregtech:gt.blockcasings2" x="1"/>
  <Block id="gregtech:gt.blockcasings2:5" y="1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="-1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="1" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="-1" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="1" />
</GameScene>

Each additional slice (1 length) requires these blocks:

| Component | Quantity and placement |
| --- | --- |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 2, Both sides of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 3, 3rd layer |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-2, Both sides of 1st layer |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 1, Center of 2nd layer |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1, Center of 1st layer |

Note that the <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus must be moved to the last slice when you extend CAL slices.

### Wallsharing
<GameScene interactive={true} wrap="square" align="right" width="220" height="200" rotateY="315" rotateX="30" >
  <ImportStructure src="/assets/structures/cal_wallshare.snbt" />
</GameScene>

CALs may wallshare each of their sides to save on casings, glass, and buses/hatches. 

Every recipe (except mainframe recipes) consumes 0.5A of power or less, which means one energy hatch can be shared between four CALs at the same time. Mainframe recipes consume nearly 1A of power, so check the amperage when sharing the same energy hatch. 

Right-click ME buses/hatches with wire cutters to allow connections from any side and wallshare up to eight machines simultaneously. The example on the right shows four CALs wallshared with connected ME input buses/hatches, but another set of four can be built directly on top without any additional buses/hatches.

## Usage
The Circuit Assembly Line can operate in 2 modes: Circuit Assembly Line and Circuit Assembler.

### Circuit Assembler Mode
In Circuit Assembler mode, the CAL works as a normal [Circuit Assembler](/singleblock/circuit_assembler.md).  
It doesn't have any speed benefit compared to the singleblock; however, the CAL can process [<ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left">Cleanroom</ItemLink>](./cleanroom.md) recipes, perform perfect overclocks, and run higher tier recipes just by upgrading its hatch, without building new singleblock machines. 

In Circuit Assembler mode, only $$\text{Hatch Tier} - 1$$ recipes can be processed, so at least one singleblock machine is ultimately required to progress through the tiers (similar to [<ItemLink id="gregtech:gt.blockmachines:32018" showIcon="left" />](./precise_auto_assembler_mt_3662.md) - neither supports tier skipping).

You can use Input Separation<FloatingImage src="gregtech:textures/gui/overlay_button/input_separation_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> to make a single CAL process multiple recipes with different programmed circuits.  
This makes Circuit Assembler mode suitable for assembling multiple AE2 storage components, OpenComputer components, Forestry Electron Tubes for bees/trees, and even some of the GT data components like <ItemLink id="gregtech:gt.metaitem.01:32708" showIcon="left" />.

### Circuit Assembly Line Mode
In Circuit Assembly Line mode, the CAL works similarly to the [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md). To process CAL recipes, all items must be inserted in the exact order in which they appear in NEI.

The CAL must also be permanently imprinted with a specific circuit type which means it cannot process anything other than that; there is no universal setup and there are no data sticks/hatches. Rebuilding the machine will not reset its imprinted behavior, either.  
Insert a Circuit Imprint into the controller to imprint a CAL, alternatively you may craft an imprinted controller with a blank controller and a Circuit Imprint.

Different variants of the same circuit tier (e.g. <ItemLink id="gregtech:gt.metaitem.03:32087" showIcon="left" /> and <ItemLink id="gregtech:gt.metaitem.03:32096" showIcon="left" />) are not the same and require different imprints. But it is fine to use the same imprinted CAL with different recipes - for example, the Quantum Supercomputer's SMD diode recipe and Advanced SMD diode recipe can be processed in the same CAL.


Crafting circuit imprints requires a few rare materials, listed below.

> [!NOTE]
> Press <KeyBind action="nei.options.keys.recipe.recipe" /> to check each item's obtainable sources and recipes.

<br>{/* To add gap between callout and list - without this callout will stick to the list below */}

1. <ItemLink id="bartworks:gt.bwMetaGeneratedgem:35" showIcon="left" scale="0.7" /> : Material to craft <ItemLink id="bartworks:gt.bwMetaGeneratedgemExquisite:35" showIcon="left" /> and <ItemLink id="bartworks:gt.bwMetaGenerateddust:36" showIcon="left" />.  
  Most commonly obtained through Blood Magic meteors using <ItemLink id="gregtech:gt.blockmachines:406" showIcon="left" /> as a catalyst, or by smelting quartzite and amethyst together in an [<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />](./electric_blast_furnace.md) to make flawed gems. The flawed gems' quality can be increased using [<ItemImage id="gregtech:gt.blockmachines:594" noTooltip />EV+ Laser Engravers](/singleblock/laser_engraver.md) or [<ItemLink id="gregtech:gt.blockmachines:1001" showIcon="left" />](./implosion_compressor.md) - just note that you also need the dust version to create Magneto Resonatic Dust.
1. <ItemLink id="bartworks:gt.bwMetaGenerateddust:4" showIcon="left" /> : Material to craft <ItemLink id="bartworks:gt.bwMetaGenerateddust:36" showIcon="left" />.  
  <ItemLink id="bartworks:gt.bwMetaGeneratedgemFlawed:4" showIcon="left" /> can be obtained by smelting <ItemLink id="bartworks:gt.bwMetaGenerateddust:3" showIcon="left" /> with <ItemLink id="bartworks:gt.bwMetaGenerateddust:6" showIcon="left" /> in an [<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />](./electric_blast_furnace.md). Yttrium Oxide is not consumed in this process.  
1. <ItemLink id="gregtech:gt.metaitem.01:2059" showIcon="left" /> : Material to craft <ItemLink id="bartworks:gt.bwMetaGenerateddust:36" showIcon="left" />.  
  <ItemLink id="gregtech:gt.metaitem.01:9059" showIcon="left" /> can be obtained by smelting crushed lead ore in an [<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />](./electric_blast_furnace.md). You can also get the dust directly by electrolyzing <ItemLink id="miscutils:itemDustAlburnite" showIcon="left" />, which can be obtained from the cerite ore vein in the [<ItemLink id="gtneioreplugin:blockDimensionDisplay_Eg" showIcon="left" />](/dimensions/toxic_overglades.md) dimension.

## References
- [GTNH Wiki : Circuit Assembly Line](https://wiki.gtnewhorizons.com/wiki/Circuit_Assembly_Line)