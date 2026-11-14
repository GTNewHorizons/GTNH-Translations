---
item_ids:
  - gregtech:gt.blockmachines:9403
  - gregtech:gt.metaitem.01:30554
  - NotEnoughItems:neiFluidDisplay:390
quest_ids:
  - mMCFuGqxQTuuLnJgEldztA==
navigation:
  title: Clarifier Purification Unit
  parent: ./water_line.md
  icon: gregtech:gt.blockmachines:9403
  position: -6001
---
# Clarifier Purification Unit
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9403" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:9403" showIcon="left" /> (CPU) is an LuV tier multiblock used for the first step of the [Water Line](./water_line.md).

The CPU processes ordinary water into Grade 1 Water. It requires no Energy/Maintenance Hatches to run because it receives power directly from the [<ItemLink id="gregtech:gt.blockmachines:9402" showIcon="left" />](./water_purification_plant.md) once linked with a data stick, and it can be managed by the Purification Plant, like the rest of the Water Line multiblocks. 


| Property | Details |
| --- | --- |
| Unlock Tier | LuV |
| Structure Size (LxWxH) | 11x11x4 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:9403" handlerId="gt.recipe.fakeAssemblylineProcess" />

<RecipesFor id="gregtech:gt.blockcasings9:5" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

<RecipesFor id="gregtech:gt.blockframes:84" />

<RecipesFor id="gregtech:gt.blockframes:335" />

<RecipesFor id="gregtech:gt.blockcasings8:1" />

### Structure
The CPU cannot be rotated or flipped.

The water is spawned for free once formed and therefore does NOT need to be placed manually. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:9403" showIcon="left" /> | 1, Front center, 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings9:5" showIcon="left" /> | 123-128 |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | 21 |
| <ItemLink id="gregtech:gt.blockframes:84" showIcon="left" /> | 12 |
| <ItemLink id="gregtech:gt.blockframes:335" showIcon="left" /> | 12 |
| <ItemLink id="gregtech:gt.blockcasings8:1" showIcon="left" /> | 3, Center of 2nd-4th layer |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace 2nd layer <ItemLink id="gregtech:gt.blockcasings9:5" showIcon="left" /> except edges or center of side |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Can replace 2nd layer <ItemLink id="gregtech:gt.blockcasings9:5" showIcon="left" /> except edges or center of side |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Can replace 2nd layer <ItemLink id="gregtech:gt.blockcasings9:5" showIcon="left" /> except edges or center of side |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1+, Can replace 2nd layer <ItemLink id="gregtech:gt.blockcasings9:5" showIcon="left" /> except edges or center of side |

### Wallshare

There is no need to wallshare the CPU, since it can run an almost infinite number of parallels if sufficient power is supplied.

## Usage
<RecipeFor id="NotEnoughItems:neiFluidDisplay:390" wrap="square" align="right" />

The CPU is the first step of [Water Line](./water_line.md) processing. As you can see in the recipe next to it, the CPU filters normal water into Grade 1 Water, with a fixed success chance of 70%. 

You can increase the success chance to 85% by feeding Grade 1 Water back into it, as the [Water Line Guide](./water_line.md#shared-mechanics) describes. This is the only way to increase the success rate.

The CPU also requires an <ItemLink id="gregtech:gt.metaitem.03:32233" showIcon="left" /> to run, and has a 20% chance of consuming that filter on each cycle, so you need to passively produce filters to run the CPU continuously.

Like other Water Line multiblocks, the CPU can process recipes in parallel without any structural upgrades. Set how many parallels the CPU should run by clicking the "Open parallel configuration window"<FloatingImage src="gregtech:textures/gui/overlay_button/batch_mode_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> button. The filter's consumption probability is not affected by parallel.

> [!WARNING]
> The CPU cannot change its void mode, and **all excess items and fluids will be voided**. Make sure the CPU's maximum output doesn't exceed the output hatch's capacity. 

## References
- [GTNH Wiki : Clarifier Purification Unit](https://wiki.gtnewhorizons.com/wiki/Clarifier_Purification_Unit)