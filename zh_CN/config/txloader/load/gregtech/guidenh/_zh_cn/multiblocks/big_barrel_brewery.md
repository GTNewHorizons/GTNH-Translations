---
item_ids:
  - gregtech:gt.blockmachines:3011
quest_ids:
  - 3SzKMSj0StOAOzVmInDjZQ==
navigation:
  title: Big Barrel Brewery
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:3011
  position: -3001
---
# Big Barrel Brewery
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3011" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:3011" showIcon="left">Big Barrel Brewery (BBB)</ItemLink> is an HV tier multiblock for mass brewing. The BBB is a direct upgrade from the singleblock brewery because it runs at 150% speed and offers 4 parallels per voltage tier. The BBB is primarily used for making biomass and bacteria for the [<ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" />](./bacterial_vat.md).

| Property | Details |
| --- | --- |
| Unlock Tier | HV |
| Structure Size (LxWxH) | 3x3x5 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:3011" />

<RecipesFor id="gregtech:gt.blockcasings10:15" />

<RecipesFor id="gregtech:gt.blockframes:305" />

### Structure
The BBB has no tiered components. The glass can be any tier and has no effect on the operation of the machine.

Multi-amp and laser energy hatches are not supported, but there can be multiple regular energy hatches for overclocking/parallel.

The BBB can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3011" showIcon="left" /> | 1, Front center, 3rd layer |
| <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> | 14-22 |
| <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | 4, Each corner of 1st layer |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 6 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> |

### Wallsharing
BBBs may wallshare each of their sides to save on casings, frame boxes, glass, and buses/hatches.

No recipe uses more than 1A of power so it is possible to share one energy hatch between two machines.

## Usage
The BBB can process [Brewery](/singleblock/brewery.md) recipes at 150% speed.

Parallels increase by 4 per voltage tier, as seen in the following table:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Parallels | 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |
{: widths="60"}

Even if a single Energy Hatch can supply 2A to the machine, the machine processes the recipe using 1A per hatch. Therefore, a single Energy Hatch providing 2A cannot process recipes of the same tier in parallel.

## References
- [GTNH Wiki : Big Barrel Brewery](https://wiki.gtnewhorizons.com/wiki/Big_Barrel_Brewery)
