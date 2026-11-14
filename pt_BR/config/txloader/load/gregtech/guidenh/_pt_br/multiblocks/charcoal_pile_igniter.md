---
item_ids:
  - gregtech:gt.blockmachines:1155
quest_ids:
  - AAAAAAAAAAAAAAAAAAAB8Q==
navigation:
  title: Charcoal Pile Igniter
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1155
  position: -501
---
# Charcoal Pile Igniter
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/cpi_structure.snbt" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:1155" showIcon="left" /> (CPI) is a Steam tier multiblock for mass producing charcoal from logs. 

The CPI is significantly faster than the [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md) but cannot be automated, does not produce creosote oil, and generates pollution.

The time required to convert logs into brittle charcoal blocks scales with the square root of the number of logs meaning larger batches are more efficient. A maximum size CPI takes 603 seconds to produce approximately 896 charcoal from 605 logs. That is nearly two orders of magnitude faster than the Coke Oven which takes 60 seconds to produce 1 charcoal from 1 log.

| Property | Details |
| --- | --- |
| Unlock Tier | Steam |
| Structure Size (LxWxH) | 3-13x3-13x3-7 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces 100 gibbl/s pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:1155" />

### Structure
The dimensions of the CPI are incredibly flexible.

Brick floors from 1x1 to 11x11 are acceptable; they do not have to be square.

The logs can be stacked between 1 and 5 layers, without any air gaps. The machine will not form if there are missing logs inside the structure.  
The type of logs can be mixed and they can have any rotation.

After the logs are placed, surround the logs in dirt or grass.

Finally, place the CPI controller on the top layer, so that a log is at the bottom of the machine.

The controller always faces upward - you cannot rotate it to face in any other direction.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1155" showIcon="left" /> | 1, Top layer, touching a log below |
| <ItemImage id="minecraft:log" />Any Log | 1-605, Fills the cube formed by dirts and bricks |
| <ItemImage id="minecraft:dirt" />Dirt or Grass | 4-340, Covering the logs |
| <ItemLink id="minecraft:brick_block" showIcon="left" /> | 1-121, Underneath the logs |

### Wallshare

CPI cannot wallshare, and will not work when there are 2 or more controllers on the same pile.

## Usage
<FunctionGraph
  title="Duration of CPI by Log Count"
  width="260" wrap="square" align="right" xLabel="Logs" xRange="0..605"
>
  <Plot expr="10*sqrt(6*x)" label="duration" />

</FunctionGraph>

As soon as the structure is built correctly, the CPI controller lights up, starts spinning, and emits smoke to indicate that it has begun converting the logs into brittle charcoal blocks. 

Use the following equation to determine the duration of the "recipe" (in seconds) from the total number of logs. Note that larger batches are more efficient because they produce more charcoal per second, on average.

<Latex formula="\text{Duration (s)}=10\sqrt{6 \times \text{Logs}}" />

The pollution of the CPI similarly scales with the duration of the recipe and therefore the number of logs, as seen in the following equation. This always averages out to 100 gibbl/s, but the pollution is **released all at once at the very beginning** of a recipe instead of during processing. That means no additional pollution is generated while the machine is running despite the particle effects making it appear otherwise.

<Latex formula="\text{Pollution (gibbl)} = 100 \times \text{Duration}" />

Once finished, the <ItemLink id="gregtech:gt.blockreinforced:4" showIcon="left" /> blocks inside the structure must be broken manually with an axe. Each block drops 1-2 charcoal, which is slightly more efficient than the [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md) to compensate for the extra effort. Applying luck/fortune to an axe does **NOT** increase the charcoal drop rate, but you can use the Lumber Axe from Tinkers' Construct to clear them out much faster.


## References
- [GTNH Wiki : Charcoal Pile Igniter](https://wiki.gtnewhorizons.com/wiki/Charcoal_Pile_Igniter)