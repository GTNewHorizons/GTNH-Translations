---
item_ids:
  - gregtech:gt.blockmachines:236
  - gregtech:gt.blockmachines:237
quest_ids:
  - AAAAAAAAAAAAAAAAAAAAGA==
  - XABK1llCToa6KKcF5Z69GA==
navigation:
  title: Coke Oven
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:236
  position: -1
---
# Coke Oven
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:236" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" /> is a Stone tier multiblock substituting fuel for a more efficient fuel like Log to Charcoal or Coal to Coal Coke, while producing Creosote Oil as a byproduct, which is also useful for fuel or lubricant sources.

The Coke Oven is superseded by the [<ItemLink id="gregtech:gt.blockmachines:15546" showIcon="left" />](./pyrolyse_oven.md) and [<ItemLink id="Railcraft:machine.alpha:12" showIcon="left">Advanced Coke Oven</ItemLink>](./advanced_coke_oven.md) in MV.

| Property | Details |
| --- | --- |
| Unlock Tier | Stone |
| Structure Size (LxWxH) | 3x3x3 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces 10 gibbl/s pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:236" />

<RecipesFor id="gregtech:gt.blockcasings12" />

Optional: If you want automation, you can use <ItemLink id="gregtech:gt.blockmachines:237" showIcon="left" />.

<RecipesFor id="gregtech:gt.blockmachines:237" handlerBlacklist="bq_quest" />

A Coke Oven with three Coke Oven Hatches requires 114 <ItemLink id="dreamcraft:CokeOvenBrick" showIcon="left" />, 54 iron, and 18 bronze to build. The bricks cost 190 sand, 114 clay, and 38 uses of the <ItemLink id="dreamcraft:WoodenBrickForm" showIcon="left" />.  
If you plan to build multiple Coke Ovens (and most players do, to meet the initial fuel demand), it will help to stockpile plenty of these materials.

### Structure

The coke oven can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" /> | 1, Front center, 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings12" showIcon="left" /> | 0-25, Empty center 3x3x3 cube shape |
| <ItemLink id="gregtech:gt.blockmachines:237" showIcon="left" /> | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings12" showIcon="left" /> |

### Wallsharing

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/coke_oven_wallshare.snbt" />
</GameScene>

Coke Ovens may wallshare each of their sides to save on coke oven bricks and coke oven hatches.  
Wallsharing them saves a significant amount of resources and reduces the number of hatches required - which can be a significant early boost.

The example on the right shows 6 Coke Ovens wallsharing each other, with sharing <ItemLink id="gregtech:gt.blockmachines:237" showIcon="left" /> to reduce costs for crafting Hatches, and ease of automation.

## Usage

The Coke Oven is primarily used to burn logs into charcoal, but can also be used to refine coal into coal coke which has twice the burn time and can smelt iron into steel 33% faster in the [<ItemLink id="gregtech:gt.blockmachines:140" showIcon="left" />](./bricked_blast_furnace.md).  
Cactus coke and sugar coke are very similar renewable alternatives but they are not nearly as energy dense.  
Check NEI to see all recipes that the Coke Oven processes.

### Creosote Oil
<ItemLink id="NotEnoughItems:neiFluidDisplay:68" showIcon="left" /> is a byproduct of nearly all Coke Oven recipes.  
Extract creosote oil manually with buckets, fluid cells, seared tanks, and super tanks or automatically with fluid pipes attached to a <ItemLink id="gregtech:gt.blockmachines:237" showIcon="left" />.

Creosote oil can be used as fuel in a variety of places including vanilla furnaces, the [<ItemLink id="Railcraft:machine.beta:5" showIcon="left" >Railcraft Boiler</ItemLink>](./railcraft_boiler.md), and the [<ItemLink id="gregtech:gt.blockmachines:15529" showIcon="left">Large Boiler</ItemLink>](./large_boiler.md).  
It can also be used to craft torches very efficiently and make lubricant in a distillery, brewery, or [<ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" />](./distillation_tower.md).

The Coke Oven automatically stops processing when there is no more room for creosote oil or charcoal/coke. Therefore, it needs to be emptied every so often to continue working. This can be done manually or automatically--see the following section for a guide on the latter. Creosote oil can also be immediately voided by breaking and replacing the controller.

### Coke Oven Hatch
The <ItemLink id="gregtech:gt.blockmachines:237" showIcon="left" /> is required for automating the Coke Oven. The coke oven hatch does not have its own internal inventory and therefore does not drop items or void fluids when broken--only the controller does that.

The Coke Oven Hatch functions in one of three available modes: input, output (items), and output (fluids). Switch modes by right-clicking the hatch with a screwdriver and rotate the hatch by right-clicking it with a wrench.

Coke oven hatches cannot auto-pull from adjacent inventories but they can auto-push, which means a hopper or [conveyor module](/misc/covers.md#conveyor-module) is all that is really required.

### Troubleshooting
1. **Multiblock does not form.** The structure is not built correctly, most likely because a block is occupying the mandatory air at the very center of the structure. The Coke Oven must be hollow to form.

1. **Does not run, or stops suddenly.** The outputs are full or inputs are missing. The Coke Oven automatically stops processing if there is nowhere for the outputs to go.

1. **The conveyor module is not pulling any logs into the Coke Ovens.** The conveyor module is likely on an item pipe and therefore needs to be set to IMPORT because it is not attached to the chest or barrel that the logs are probably stored in.

## References
- [GTNH Wiki : Coke Oven](https://wiki.gtnewhorizons.com/wiki/Coke_Oven)