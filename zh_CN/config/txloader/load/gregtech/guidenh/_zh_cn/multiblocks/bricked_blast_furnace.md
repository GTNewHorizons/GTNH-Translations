---
item_ids:
  - gregtech:gt.blockmachines:140
quest_ids:
  - AAAAAAAAAAAAAAAAAAAAQQ==
  - AAAAAAAAAAAAAAAAAAAATA==
  - AAAAAAAAAAAAAAAAAAACuQ==
  - AAAAAAAAAAAAAAAAAAACug==
navigation:
  title: Bricked Blast Furnace
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:140
  position: -501
---
# Bricked Blast Furnace
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:140" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:140" showIcon="left">Bricked Blast Furnace (BBF)</ItemLink> is a Steam tier multiblock for smelting iron into steel. 

Crafting the necessary firebricks requires gathering gypsum dust from basaltic mineral sand veins and calcite dust from lapis veins, among other things. 

Players commonly run 4-8 BBFs continuously to keep up with the high demand for steel in the early game. 

The BBF is superseded by the [<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />](./electric_blast_furnace.md), but it may be useful to keep some around for cheap and easy steel production while the EBF smelts other materials.

| Property | Details |
| --- | --- |
| Unlock Tier | Steam |
| Structure Size (LxWxH) | 3x3x4 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces 200 gibbl/s pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:140" />

<Row>
<RecipesFor id="gregtech:gt.blockcasings4:15" handlerId="codechicken.nei.recipe.ShapedRecipeHandler" input="dreamcraft:clayBucketConcrete" />
<RecipesFor id="gregtech:gt.blockcasings4:15" handlerId="gt.recipe.assembler" input="NotEnoughItems:neiFluidDisplay:224" />
</Row>

### Structure
The BBF consists of a controller block and several layers of firebrick around a hollow interior. 

There are no buses/hatches since all items are inserted and extracted manually from the controller. 

Unlike other multiblocks, there is no warning message or error when unformed - The only way to tell if the BBF is formed is by starting a recipe; the controller lights up and smoke is released out of the top of the structure. 

BBF cannot be rotated - The chimney must point upward.

Use the extended tooltip and NEI structure preview to learn more about its structure requirements in-game, and the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure in the world.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:140" showIcon="left" /> | 1, Front center, 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings4:15" showIcon="left" /> | 32, Everywhere except the controller and the hollow center of 2nd-4th layers |

### Wallsharing
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/bbf_wallshare.snbt" />
</GameScene>

BBFs may wallshare each of their sides to save on firebricks. This is extremely valuable in the early game because firebricks are very expensive and time-consuming to craft. 

Note that a Controller cannot be included in Wallsharing, which usually makes BBF wallshares like 2xN column.

See the scene on the right for an example of BBF wallsharing.

## Usage

The BBF has many different recipes for smelting iron into steel. The only significant difference between them is their throughput. Each steel ingot takes 360s to smelt with coal or charcoal, but only 240s with coke. Compressed fuels also have slightly higher fuel efficiency because they can process 10 ingots at a time instead of 9 for the same amount of resources. 

Compressing iron doesn't provides any processing benefit.

A full summary of the relevant recipes are provided below. Note that iron ingots can be replaced with iron dust if necessary.

<ContentTabs>
  <Tab title="Comparison between Fuel types">
    | Fuel Type | Amount | Processing Time |
    | --- | --- | --- |
    | <ItemLink id="Railcraft:fuel.coke" showIcon="left" /> | 2 | 240s |
    | <ItemLink id="miscutils:itemCactusCoke" showIcon="left" /> | 8 | 240s |
    | <ItemLink id="miscutils:itemSugarCoke" showIcon="left" /> | 8 | 240s |
    | <ItemLink id="minecraft:coal" showIcon="left" /> | 4 | 360s |
    | <ItemLink id="minecraft:coal:1" showIcon="left" /> | 4 | 360s |
  </Tab>
  <Tab title="Comparison with Compressed Fuel">
    | Fuel Type | Amount | Iron Ingots Processed | Processing Time |
    | --- | --- | --- | --- |
    | <ItemLink id="Railcraft:fuel.coke" showIcon="left" /> | 2 | 1 | 240s |
    | <ItemLink id="Railcraft:cube" showIcon="left" /> | 2(=<ItemImage id="Railcraft:fuel.coke" />18) | 10 | 2400s |
    | <ItemLink id="minecraft:coal:1" showIcon="left" /> | 4 | 1 | 360s |
    | <ItemLink id="gregtech:gt.blockgem3:4" showIcon="left" /> | 4(=<ItemImage id="minecraft:coal:1" />36) | 10 | 3600s |
  </Tab>
</ContentTabs>

The BBF can also boost the output of certain metal oxide dusts (pyrite, magnetite, cassiterite, etc). More specifically, the BBF yields 3 ingots for every 2 dusts--a 50% boost compared to vanilla furnaces or the [<ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" />](./steam_hearth.md). The problem is that the recipes are 120s with coal or charcoal and 80s with coke, which delays steel production.

### Pollution
The BBF releases 200 gibbl/s of pollution into the air while active. If left unchecked, pollution can apply significant debuffs to the player and slowly erodes the surrounding chunks. The debuffs can be avoided by wearing a full hazmat suit, but nothing can stop the effects on the world until LV. There are really three options for mitigating the effects of pollution in the steam age:

- Place BBFs far away from your base to concentrate the pollution elsewhere. <ItemLink id="gregtech:gt.blockmachines:2701" showIcon="left" /> can help transport resources.
- Place BBFs in the nether to concentrate the pollution in an entirely other dimension. It does not travel through the nether portal.
- Disable pollution in .minecraft\config\GregTech\Pollution.cfg.

Later on, use pollution scrubbers and/or [<ItemImage id="gregtech:gt.blockmachines:12020" />Electric Air Filters](./electric_air_filter.md) to actually remove the pollution from chunks. Higher tier armors (ie. Nanosuit) also provide full hazmat protection. 

## References

- [GTNH Wiki : Bricked Blast Furnace](https://wiki.gtnewhorizons.com/wiki/Bricked_Blast_Furnace)
