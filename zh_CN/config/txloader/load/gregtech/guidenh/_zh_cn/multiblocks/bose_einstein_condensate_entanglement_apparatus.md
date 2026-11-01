---
item_ids:
  - gregtech:gt.blockmachines:15754
quest_ids:
  - So7OhYd8SVO3_Jl370cogA==
navigation:
  title: Bose-Einstein Condensate Entanglement Apparatus
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15754
  position: -11001
---
# Bose-Einstein Condensate Entanglement Apparatus
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15754" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left" /> is a UIV tier multiblock for converting fluids into entangled condensate in the [BEC Line](./bose_einstein_condensate_line.md)--similar to an input hatch. 

The Entanglement Apparatus does not overclock but it has unlimited parallels to process as much as possible based on the amount of power provided.  
Multi-amp and laser energy hatches are supported for serious throughput and the Entanglement Apparatus can even entangle different fluids simultaneously but the processing time is always going to be the max duration of the active recipes.  
The EU quota in recipes is simply the required EU/t for each additional parallel but actual consumed EU/t per parallel is only 5% of that value.

| Property | Details |
| --- | --- |
| Unlock Tier | UIV |
| Structure Size (LxWxH) | 34x19x19 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:15754" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

### Structure

The Entanglement Apparatus has no tiered components. 

The Entanglement Apparatus can be rotated or flipped.

Multi-amp and laser energy hatches are supported for serious throughput. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left" /> | 1, Front center, 10th layer |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 236 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 232 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 216 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 184 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 136-158 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 148 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 101 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> around controller |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> around controller |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1, Back center |

### Wallsharing

The Entanglement Apparatus may wallshare each of its sides to save few blocks, but since Entanglement Apparatus can scale its processing indefinitely with unlimited parallel, and ability to run multiple recipes at once, more than one is generally not built.

## Usage

The Entanglement Apparatus or BEC Generator is the first step in the [BEC Line](./bose_einstein_condensate_line.md) and converts fluids into entangled condensate at the cost of power. The Entanglement Apparatus does not overclock but it has unlimited parallels to process as much as possible based on the amount of power provided.

Insert fluid through an input hatch on the front of the structure.  
The Entanglement Apparatus can entangle different fluids simultaneously but the processing time is always going to be the max duration of the active recipes.  
For example, if molten neutronium (20 ticks) and molten spacetime (60 ticks) are both present and there is enough power to support both of them, then the processing time will be 60 ticks because that is the maximum of the two. If there is not enough power to support both, then priority follows standard multiblock order with colored hatches, location, etc.

The entangled condensate is outputted through the <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> on the back of the structure and stored in [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Containment Fields</ItemLink>](./bose_einstein_condensate_containment_field.md) until the [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) pulls it into [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Nodes</ItemLink>](./bose_einstein_condensate_teleportation_node.md) for recipes. The challenge, however, is that the Entanglement Apparatus does not check if there is enough space available for the condensate before it begins processing. It could unintentionally overflow the network's storage and void the condensate if not careful. The solution is using a <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> on the Containment Field to temporarily disable the Entanglement Apparatus if levels ever get too high, or dynamically adjusting the field strength of the Containment Field with OpenComputers.

If multiple Containment Fields are available on the same network, then the condensate from the Entanglement Apparatus is split proportional to their total field strength. For example, if one Containment Field has a 150,000 field strength and another has a 50,000 field strength, then the former receives 75% of the condensate and the latter receives only 25% of the condensate.

### Recipes

Every recipe consists of a single input fluid, an EU quota for entanglement, and a fixed duration.  
The quota is the required EU/t per parallel but the actual consumed EU/t per parallel is only 5% of that value.  
For example, neutronium has a quota of 7,864,320 EU which means every 7,864,320 EU/t in throughput grants an additional parallel but each one only ever consumes 393,216 EU/t.  
The durations are very long to encourage passive condensate production, and then later filtering for the correct ones with a [<ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left">Maxwell Gate</ItemLink>](./bose_einstein_condensate_maxwell_gate.md).

| Entangled Condensate | per Parallel | Duration | Power |||
| --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | ^^ | Required per Parallel || Consumed per Parallel |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:941" showIcon="left">Neutronium</ItemLink> | 144 L | 30 s | 7,864,320 EU/t | 1A UEV | 393,216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:942" showIcon="left">Cosmic Neutronium</ItemLink> | 144 L | 30 s | 7,864,320 EU/t | 1A UEV | 393,216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:943" showIcon="left">Bedrockium</ItemLink> | 144 L | 30 s | 7,864,320 EU/t | 1A UEV | 393,216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:944" showIcon="left">Chromatic Glass</ItemLink> | 144 L | 30 s | 31,457,280 EU/t | 1A UIV | 1,572,864 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:945" showIcon="left">Celestial Tungsten</ItemLink> | 144 L | 30 s | 31,457,280 EU/t | 1A UIV | 1,572,864 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:946" showIcon="left">Infinity</ItemLink> | 144 L | 30 s | 125,829,120 EU/t | 1A UMV | 6,291,456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:949" showIcon="left">Dimensionally Shifted Superfluid</ItemLink> | 1,000 L | 60 s | 125,829,120 EU/t | 1A UMV | 6,291,456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:950" showIcon="left">Lossless Phonon Transfer Medium</ItemLink> | 1,000 L | 90 s | 125,829,120 EU/t | 1A UMV | 6,291,456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:951" showIcon="left">Degenerate Quark Gluon Plasma</ItemLink> | 1,000 L | 120 s | 125,829,120 EU/t | 1A UMV | 6,291,456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:947" showIcon="left">Hypogen</ItemLink> | 144 L | 60 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:948" showIcon="left">Transcendent Metal</ItemLink> | 144 L | 60 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:952" showIcon="left">Spacetime</ItemLink> | 144 L | 120 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:953" showIcon="left">Tachyon Rich Temporal Fluid</ItemLink> | 144 L | 120 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:954" showIcon="left">Spatially Enlarged Fluid</ItemLink> | 144 L | 120 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:955" showIcon="left">Boundless Cosmic Solder</ItemLink> | 1,000 L | 120 s | 503,316,480 EU/t | 1A UXV | 25,165,824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:956" showIcon="left">MHDCSM</ItemLink> | 144 L | 180 s | 2,013,265,920 EU/t | 1A MAX | 100,663,296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:957" showIcon="left">Magmatter</ItemLink> | 144 L | 180 s | 2,013,265,920 EU/t | 1A MAX | 100,663,296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:958" showIcon="left">Universium</ItemLink> | 144 L | 180 s | 2,013,265,920 EU/t | 1A MAX | 100,663,296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:959" showIcon="left">Eternity</ItemLink> | 144 L | 180 s | 2,013,265,920 EU/t | 1A MAX | 100,663,296 EU/t |
{: widths="220,60,60, 120, 40, 120"}


## References
- [GTNH Wiki : Bose-Einstein Condensate Entanglement Apparatus](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Entanglement_Apparatus)
