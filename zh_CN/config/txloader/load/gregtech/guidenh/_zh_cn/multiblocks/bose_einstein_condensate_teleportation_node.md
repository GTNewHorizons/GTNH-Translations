---
item_ids:
  - gregtech:gt.blockmachines:15757
quest_ids:
  - 52NvoXdXSuCp2hCvV_otBA==
navigation:
  title: Bose-Einstein Condensate Teleportation Node
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15757
  position: -11001
---
# Bose-Einstein Condensate Teleportation Node

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15757" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">Bose-Einstein Condensate Teleportation Node (IO Node)</ItemLink> is a UIV tier multiblock for inserting and extracting items in the [BEC Line](./bose_einstein_condensate_line.md)--similar to an input/output bus. However, in practice the items never actually leave the IO Node and recipes are processed locally instead of in the [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md); the IO Node is technically the assembler and the Observation Array is really just a large router for power, condensate, and nanites. 

Up to 16 IO Nodes may connect to the same Observation Array via line-of-sight connector hatches, but it is not recommended to run different recipes at the same time because that could introduce penalties and potentially void outputs. 

Optionally, use a <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> to read the tier of the current required nanite or <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> to pause the machine.

| Property | Details |
| --- | --- |
| Unlock Tier | UIV |
| Structure Size (LxWxH) | 13x7x23 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

> [!NOTE]
> IO Nodes work with Observation Array, so most of the mechanic explanation is written in there.
> 
> This guide only informs you about IO Node's structure, construction, hatches for automation, and OpenComputers integration.
>
> Please check [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) and [BEC Line](./bose_einstein_condensate_line.md) guide for overall mechanics and detailed recipes.

## Crafting and Construction
### Crafting

<RecipesFor id="gregtech:gt.blockmachines:15757" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Structure

The IO Node has no tiered components, and can be rotated or flipped.

The <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> must face directly into one on the [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) for them to link, but there is no cabling inbetween and they can be up to 128 blocks apart if necessary. Just make sure there are no opaque blocks in between.

There is no maintenance hatch or even an energy hatch because the IO Node receives all its power from the Observation Array. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left" /> | 1, Front center, 12th layer |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 94 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 88 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 56 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 18-48 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 44 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 44 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 32 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 20 |
| <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> | 1, Back center casing |
| <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |

### Wallsharing

Bose-Einstein Condensate Teleportation Node can wallshare, although it is useless since multiple IO Nodes' positions are usually gapped by [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) and its hatch position.

## Usage

The IO Node has 2 specialized hatches that can help automation: <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> and <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" />.

<!-- This contents are from BEC line guide - should update both if there are any changes -->
- <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> : emits a redstone signal if the set condition inside its GUI is true.  
  There is a comparison operator and a threshold value for the tier of the current requested nanite.
- <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> : can pause the machine either immediately or upon transitioning to a new input step/nanite when it receives a redstone signal.  
  Pausing the machine halts all recipe progress and prevents condensate from being inserted, but the IO Node can still read the nanite(s) in the Observation Array, still updates any nanite detector hatches, and still consumes power.

### OpenComputers Integration
The IO Node is automatable with OpenComputers and has a few additional functions/methods compared to standard GregTech multiblocks, as seen below. These can be used to dynamically change the speed divisor and gather information about the nanites, condensates, and current recipe.
```lua
-- List all available methods for the IO Node
local component = require('component')
local bec_io_node = component.bec_io_node

for k,v in pairs(bec_io_node) do print(k,v) end

-- Returns the requested nanite tier as a table {name, tier}
bec_io_node.getRequiredTier()

-- Returns the provided nanite tier as a table {name, tier}
bec_io_node.getProvidedTier()

-- Returns the provided nanite amount as a number
bec_io_node.getAvailableNanites()

-- Returns the current types and amounts of condensate required as a table
bec_io_node.getRequiredCondensate()

-- Returns the current types and amounts of condensate consumed as a table
bec_io_node.getConsumedCondensate()

-- Returns all recipe steps as a table. Each step has a nanite (table), start tick (number), end tick (number), and index (number)
bec_io_node.getRecipeSteps()

-- Returns the amount of slowdowns currently applied as a number
bec_io_node.getSlowdowns()

-- Returns the speed divisor of the IO Node as a number
bec_io_node.getManualSlowdown()

-- Sets the speed divisor of the IO Node from a number
bec_io_node.setSpeedDivisor(divisor)
```

## References
- [GTNH Wiki: Bose-Einstein Condensate Teleportation Node](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Teleportation_Node)
