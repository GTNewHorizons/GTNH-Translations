---
item_ids:
  - gregtech:gt.blockmachines:32026
quest_ids:
  - n7yjRSr0R7O2agebw73FGA==
  - 3yz1WCEzQ_KQxW8p7_29-Q==
  - smCKxKkMSeyIAUeFInS4hQ==
  - hWXZi-whQfmgWO0EII7g2g==
navigation:
  title: Component Assembly Line
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:32026
  position: -8001
---
# Component Assembly Line
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib name="main" controller="gregtech:gt.blockmachines:32026">
    <Tier value="1" locked />
    <Channel name="glass" value="6" />
  </ImportStructureLib>
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:32026" showIcon="left" /> (CoAL) is a UV tier multiblock for bulk crafting component parts such as motors, pumps, and even field generators. 

Despite its name, the CoAL does not require ingredients to be inserted in any particular order--everything can go in a single input bus/hatch. No datasticks or optical hatches are required either. 

The reason for using the CoAL for component parts over the regular [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) or [<ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />](./advanced_assembly_line.md) is that all recipe costs are reduced by 25%, including the length of the recipe itself.  
The only limitation is that components are made 64 at a time which makes CoAL use far more resources than planned, especially for field generators, when entering a new tier.

| Property | Details |
| --- | --- |
| Unlock Tier | UV |
| Structure Size (LxWxH) | 33x9x10 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting

<RecipesFor id="gregtech:gt.blockmachines:32026" handlerId="gt.recipe.fakeAssemblylineProcess" />

<RecipesFor id="gregtech:gt.blockcasings8:7" />

<RecipesFor id="gregtech:gt.blockcasings9" />

<RecipesFor id="gregtech:gt.blockcasings9:1" />

<RecipesFor id="gregtech:gt.blockcasings2:5" />

<RecipesFor id="gregtech:gt.blockcasings2:9" />

<RecipesFor id="gregtech:gt.blockframes:316" handlerBlacklist="gt.recipe.unpackager" />

### Structure

The Component Assembly Line has a fixed-length and does NOT consist of any "slices" like the regular [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) or other Assembly-line variants. 

The component assembly line casings are a tiered component that determine the maximum tier of recipes and the speed bonus for lower tier recipes, and glass must be UV+ but has no effect on the operation of the machine. 

The Component Assembly Line can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannels "glass" and "component_casing" to specify the tier of those components.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:32026" showIcon="left" /> | 1, Front center, 8th layer |
| <ItemLink id="gregtech:gt.blockcasings8:7" showIcon="left" /> | 516-646 |
| <ItemLink id="gregtech:gt.blockcasings9" showIcon="left" /> | 126 |
| <ItemLink id="gregtech:gt.blockcasings9:1" showIcon="left" /> | 124 |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 55 |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 30 |
| <ItemLink id="gregtech:gt.blockframes:316" showIcon="left" /> | 2-4 |
| <ItemImage id="bartworks:BW_TieredGlass:5" />Any &cUV+&r Tiered Glass | 280 |
| <ItemImage id="GoodGenerator:componentAssemblylineCasing" />&9Tiered&r Component Assembly Line Casing | 43 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Any outer <ItemLink id="gregtech:gt.blockcasings8:7" showIcon="left" /> of 9th layer |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1, Casings around controller |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+ |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Any side bottom edge casing |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+ |

### Wallsharing

CoALs may wallshare each of their sides to save on casings, glass, and buses/hatches. Overlapping the top layer with another one directly overhead and upside down is very effective because it shares an entire set of component assembly line casings.

## Usage

The tier of component assembly line casings on a CoAL determine which recipes it can run; the casing tier must be greater than or equal to the component parts being crafted (ie. UV parts require at least UV component assembly line casings).

For every casing tier above the minimum requirement of a recipe, the recipe time is halved. This does not require any additional power; it simply cuts the recipe's required time in half.
In addition, CoAL performs 2/4 Imperfect Overclock (draw 4x power to make recipe 2x faster) - since Multi-Amp and Laser hatches are supported, this lets the CoAL assemble components significantly faster than the other options.

> [!NOTE]
> Due to the high cost of these casings, players usually skip some tiers to save on both time and resources. Note that the 25% discount from the CoAL does not always "pay back" the cost to make a specific tier of casing.

{/* Skipping wiki's Casing material listing to make user use NEI at themselves rather than just reading */}

## References
- [GTNH Wiki : Component Assembly Line](https://wiki.gtnewhorizons.com/wiki/Component_Assembly_Line)