---
item_ids:
  - gregtech:gt.blockmachines:15756
quest_ids:
  - KV1vw68JTb-KiHQzBEPzBw==
navigation:
  title: Bose-Einstein Condensate Observation Array
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15756
  position: -11001
---
# Bose-Einstein Condensate Observation Array

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15756" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left" /> is a UIV tier multiblock for supplying power, condensate, and nanites to any connected [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Nodes</ItemLink>](./bose_einstein_condensate_teleportation_node.md) in the [BEC Line](./bose_einstein_condensate_line.md). 

The Observation Array is really just a large router rather than an assembler because it does not process any recipes or hold condensate itself. It only ever stores nanites locally for IO Nodes to read from and transfers condensate from the [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Containment Fields</ItemLink>](./bose_einstein_condensate_containment_field.md) to IO Nodes upon request. 

Up to 16 IO Nodes may connect to the same Observation Array via line-of-sight connector hatches, but it is not recommended to run different recipes at the same time because that could introduce penalties and potentially void outputs. IO Nodes do not have their own energy hatches so their individual power costs are summed together and covered by the Observation Array, which supports multi-amp and laser energy hatches for serious throughput.

BEC recipes appear as [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) recipes in NEI but there is no strict item or condensate order to follow. Instead, they have a certain number of equal-length steps equivalent to their number of solid inputs. The steps are not exactly hard stops but each one requests a specific nanite tier or better to run and exceeding the requested tier significantly reduces the IO Node's processing speed.  
The nanites are never actually consumed but they do need to be rapidly swapped out of the Observation Array to perfectly match the requested nanite at all times.  
The nanite order is constant per recipe but varies between recipes so any automation method needs to be highly precise and flexible.

| Property | Details |
| --- | --- |
| Unlock Tier | UIV |
| Structure Size (LxWxH) | 61x31x31 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting

<RecipesFor id="gregtech:gt.blockmachines:15756" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Structure

The Observation Array has no tiered components, and can be rotated or flipped.

Each <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> must face directly into one on an [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) for them to link, but there is no cabling inbetween and they can be up to 128 blocks apart if necessary. 

Multi-amp and laser energy hatches are supported for serious throughput. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

The <ItemLink id="gregtech:gt.blockmachines:9415" showIcon="left" /> is effectively an input bus exclusively for nanites and can hold up to 2,147,483,647 at once.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left" /> | 1, Front center, 16th layer |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 1700 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 1515 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 1444-1458 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 838 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 790 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 664 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 560 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 464 |
| <ItemLink id="gregtech:gt.blockmachines:9415" showIcon="left" /> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> | 1+, Can replace <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> in the center of each ring's edge |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1-2, Replaces the <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> on the center part at the left or right end of the machine |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |

### Wallsharing

Using a wallshare saves a small number of casings, but in return you lose 4 [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) connections (8 in total since there are 2 observation arrays), and the condensate hatches cannot be shared.

## Usage

The Observation Array works as a router that provides power, condensate, and nanites to connected [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Nodes</ItemLink>](./bose_einstein_condensate_teleportation_node.md). Up to 16 IO Nodes can be connected to the Observation Array.  
Despite it being listed as an assembler, think of the Observation Array as a large router and the IO Node as the assembler since the latter actually processes the recipes.

> [!NOTE]
> Check [BEC Line](./bose_einstein_condensate_line.md) for how the BEC line operates overall and what the Observation Array performs in BEC Line. This guide covers Observation Array specific information only.

### Condensate

The Observation Array does not hold any condensate itself unlike [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Containment Fields</ItemLink>](./bose_einstein_condensate_containment_field.md), only ever transfers it from the Containment Field to the IO Node upon request.

Any condensate in the network that is not requested by the current recipe is considered a contaminant or slowdown. Each contaminant significantly reduces the processing speed of the IO node and if there are ever more than three contaminants in the network at once then the recipe immediately fails and voids.  
Condensate supplied to an IO Node is no longer considered in the network and therefore does not affect other IO Nodes processing other recipes on the same Observation Array. However, it is still recommended to process only one recipe at a time to avoid these penalties altogether.

### Nanites

<LineChart 
  wrap="square" align="right"
  categories="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
  xAxisLabel="Nanite Count"
>
  <Series name="Δ=0, no unmatched contaminants" data="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20" />
  <Series name="Δ=3, no unmatched contaminants" data="0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2" />
  <Series name="Δ=0, 2 unmatched contaminants" data="0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6" />
  <Series name="Δ=3, 2 unmatched contaminants" data="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0" />
</LineChart>

Recipes are processed in sequential, equal-length steps equivalent to its number of solid inputs.  
For example, the <ItemLink id="gregtech:gt.metaitem.03:32310" /> is processed in five steps that are each 1/5th of the total overall duration because it has five solid inputs in its recipe. 

The steps are not exactly hard stops but each one requests a specific nanite tier or better to run and exceeding the requested tier significantly reduces the IO Node's processing speed, as seen in the following equations and graphs. 

<Latex formula="\Delta = \text{Nanite Tier Provided} - \text{Nanite Tier Requested}" scale="0.8" />
<Latex formula="d = \text{Max}(1 + \text{Unrequested Contaminant}, \text{Speed Divisor})" scale="0.8" />
<Latex formula="+\text{Progress Ticks/t} = \Biggl\lfloor \frac{\text{Min}(30720, \text{ Nanites Available})}{\text{Active Parallels} \times 2^\Delta \times d } \Biggl\rfloor" scale="0.8" />

It is possible to skip steps or complete entire recipes in one tick if there are enough nanites available at once, but there is a hard cap of 30,720 nanites.

Below table shows each nanite's tiers.
| Tier | Nanite |
| --- | --- |
| 1 | <ItemLink id="gregtech:gt.metaitem.03:4010" showIcon="left" >Carbon</ItemLink>/<ItemLink id="gregtech:gt.metaitem.03:4811" showIcon="left" >Glowstone</ItemLink> |
| 2 | <ItemLink id="gregtech:gt.metaitem.03:4054" showIcon="left" >Silver</ItemLink>/<ItemLink id="gregtech:gt.metaitem.03:4129" showIcon="left" >Neutronium</ItemLink> |
| 3 | <ItemLink id="gregtech:gt.metaitem.03:4086" showIcon="left" >Gold</ItemLink> |
| 4 | <ItemLink id="gregtech:gt.metaitem.03:4581" showIcon="left" >Transcendent Metal</ItemLink> |
| 5 | <ItemLink id="gregtech:gt.metaitem.03:4147" showIcon="left" >Six-Phased Copper</ItemLink> |
| 6 | <ItemLink id="gregtech:gt.metaitem.03:4585" showIcon="left" >White Dwarf Matter</ItemLink> |
| 7 | <ItemLink id="gregtech:gt.metaitem.03:4586" showIcon="left" >Black Dwarf Matter</ItemLink> |
| 8 | <ItemLink id="gregtech:gt.metaitem.03:4139" showIcon="left" >Universium</ItemLink> |
| 9 | <ItemLink id="gregtech:gt.metaitem.03:4141" showIcon="left" >Eternity</ItemLink> |
| 10 | <ItemLink id="gregtech:gt.metaitem.03:4143" showIcon="left" >Magmatter</ItemLink> |
{: widths="30" width="220"}

### Recipes

You can check recipes with nanite required for each step in [BEC Line Guide - Recipes](./bose_einstein_condensate_line.md#recipes).

## References
- [GTNH Wiki : Bose-Einstein Condensate Observation Array](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Observation_Array)
