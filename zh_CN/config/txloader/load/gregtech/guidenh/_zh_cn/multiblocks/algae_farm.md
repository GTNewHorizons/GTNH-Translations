---
item_ids:
  - gregtech:gt.blockmachines:15545
quest_ids:
  - Ds_ok-hRS2ODJNs3LUP9kw==
navigation:
  title: Algae Farm
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15545
  position: -2001
---

# Algae Farm

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15545" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15545" showIcon="left" /> is an MV tier multiblock for cultivating different types of algae. The Algae Farm requires no inputs other than power to run and produces no pollution. The type and amount of algae depends on the tier of the energy hatch, and can be boosted one tier further by supplying GT++ compost. The algae is mainly used as a renewable feedstock for the [<ItemLink id="gregtech:gt.blockmachines:998" showIcon="left" />](./exxonmobil_chemical_plant.md).

| Property | Details |
| --- | --- |
| Unlock Tier | MV |
| Structure Size (LxWxH) | 10x3x6 |
| Power | Regular |
| Overclocks | Unique |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction

### Crafting

<RecipesFor id="gregtech:gt.blockmachines:15545" handlerId="gt.recipe.assembler" />

<RecipesFor id="gregtech:gt.blockcasings12:15" />

<RecipesFor 
  id="gregtech:gt.blockframes:306" 
  handlerBlacklist="neicustomdiagram.diagramgroup.gregtech.materialtools, neicustomdiagram.diagramgroup.gregtech.materialparts" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

### Structure

The Algae Farm has one tiered component. The glass determines the maximum tier of the energy hatch. UMV tier glass removes all restrictions. 

The Algae Farm cannot be rotated.

Buses/hatches may replace any algae casing anywhere on the structure. 

Multi-amp and laser energy hatches are not supported and there can only be ONE regular energy hatch. 

The water is a one-time-cost to prime the machine and inserted into the structure via a reservoir hatch or input hatch. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15545" showIcon="left" /> | 1, Front Center, 3rd layer |
| <ItemImage id="bartworks:BW_TieredGlass" /><Color id="blue">Tiered</Color> Glass | 64 |
| <ItemLink id="gregtech:gt.blockcasings12:15" showIcon="left" /> | 20-25 |
| <ItemLink id="gregtech:gt.blockframes:306" showIcon="left" /> | 6 |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | 5 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only regular Hatch allowed, tier limited by glass</Tooltip> | 1, Any casing |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1, Any casing |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 0+, Any casing |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Any casing |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+, Any casing |

### Wallsharing

Algae Farms may wallshare each of their sides to save on casings, glass, and buses/hatches. No recipe uses more than 1A of power so it is possible to share one energy hatch between two machines.

## Usage

The duration of each iteration and the type/amount of algae produced depends on the tier of the energy hatch, as seen in the following table. Many outputs are not guaranteed and instead have a 90% chance of being produced. For example, an HV Algae Farm always produces 1 brown algae and 90% of the time produces 4 more, for a total of 5 per iteration and an average of 0.066 per second.

Notice the improved scaling for LuV and above. The recipe length is halved with each tier instead of being reduced by 10 seconds which drastically increases the average algae produced. The very last tier is currently unobtainable because there are no craftable energy hatches above UXV.

Optionally, supply GT++ compost through an input bus to boost the tier of the machine by one. For example, an MV Algae Farm could produce brown algae despite not normally being able to and its recipe length would be reduced from 80s to 70s. The amount of compost required per operation doubles with each tier, up to the maximum of 64.

The table below shows the recipe time, the compost needed for boosting, and the average algae produced per second on each tier.

| Voltage | Recipe Time | Compost Required | <ItemImage id="miscutils:item.BasicAgrichemItem" /> Algae | <ItemImage id="miscutils:item.BasicAgrichemItem:1" /> Green | <ItemImage id="miscutils:item.BasicAgrichemItem:2" /> Brown | <ItemImage id="miscutils:item.BasicAgrichemItem:3" /> Golden-Brown | <ItemImage id="miscutils:item.BasicAgrichemItem:4" /> Red |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ULV | 100.0s | 1 | 0.060 /s | 0.018 /s | - | - | - |
| LV | 90.0s | 1 | 0.111 /s | 0.082 /s | - | - | - |
| MV | 80.0s | 2 | 0.125 /s | 0.245 /s | - | - | - |
| HV | 70.0s | 4 | 0.143 /s | 0.337 /s | 0.066 /s | - | - |
| EV | 60.0s | 8 | 0.167 /s | 0.393 /s | 0.160 /s | 0.060 /s | - |
| IV | 50.0s | 16 | 0.200 /s | 0.472 /s | 0.272 /s | 0.112 /s | 0.072 /s |
| LuV | 25.6s | 32 | 0.391 /s | 1.078 /s | 0.648 /s | 0.453 /s | 0.539 /s |
| ZPM | 12.8s | 64 | 0.781 /s | 2.781 /s | 1.766 /s | 1.219 /s | 1.234 /s |
| UV | 6.40s | 64 | 1.563 /s | 7.438 /s | 4.938 /s | 3.375 /s | 2.938 /s |
| UHV | 3.20s | 64 | 3.125 /s | 19.88 /s | 13.63 /s | 9.250 /s | 7.125 /s |
| UEV | 1.60s | 64 | 6.250 /s | 52.25 /s | 36.63 /s | 24.75 /s | 17.38 /s |
| UIV | 0.80s | 64 | 12.50 /s | 134.5 /s | 95.75 /s | 64.50 /s | 42.25 /s |
| UMV | 0.40s | 64 | 25.00 /s | 339.0 /s | 244.0 /s | 164.0 /s | 102.0 /s |
| UXV | 0.20s | 64 | 50.00 /s | 838.0 /s | 608.0 /s | 408.0 /s | 244.0 /s |
| MAX | 0.10s | 64 | 100.0 /s | 2,036 /s | 1,486 /s | 996.0 /s | 578.0 /s |
| MAX+ | 0.05s | 64 | 200.0 /s | 4,872 /s | 3,572 /s | 2,392 /s | 1,356 /s |

The algae itself is primarily used in the [<ItemLink id="gregtech:gt.blockmachines:998" showIcon="left" />](./exxonmobil_chemical_plant.md) as a renewable alternative for methane, sulfuric acid, ethylene, and ammonia. Brown algae is also used to make lithium chloride for smelting MAR-Ce-M200 ingots and red algae is used to make prismarine shards.

## References

- [GTNH Wiki: Algae Farm](https://wiki.gtnewhorizons.com/wiki/Algae_Farm)
