---
item_ids:
  - gregtech:gt.blockmachines:15513
quest_ids:
  - AAAAAAAAAAAAAAAAAAAH9w==
navigation:
  title: Amazon Warehousing Depot
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15513
  position: -5001
---

# Amazon Warehousing Depot
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15513" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15513" showIcon="left" />(AWD) is an IV tier multiblock for packaging and unpackaging various items.

The AWD is a direct upgrade from the singleblock packager and unpackager because it can process both types of recipes, runs up to 900% speed, only uses 75% of the EU/t normally required, and offers 16 parallels per voltage tier.

Input separation should be enabled on the AWD for using different schematics within the same machine.

| Property | Details |
| --- | --- |
| Unlock Tier | IV |
| Structure Size (LxWxH) | 3x5x3 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces 40 gibbl/s pollution, and require Muffler Hatch |

## Crafting and Construction

### Crafting

<RecipesFor id="gregtech:gt.blockmachines:15513" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="miscutils:gtplusplus.blockcasings.3:9" />

<RecipesFor id="gregtech:gt.blockframes:32" 
handlerBlacklist="neicustomdiagram.diagramgroup.gregtech.materialtools, neicustomdiagram.diagramgroup.gregtech.materialparts" />

### Structure

The AWD has one tiered component - The item pipe casings, which determine the speed bonus of the machine.

The glass can be any tier and has no effect on the operation of the machine.

AWD can be rotated or mirrored.

Multi-amp and laser energy hatches are not supported, but there can be multiple regular energy hatches for overclocking. Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannels "item_pipe" and "glass" to specify the tier of those components.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15513" showIcon="left" /> | 1, Front right, 2nd layer |
| <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> | 4-15 |
| <ItemImage id="gregtech:gt.blockcasings11" /><Color id="blue">Tiered</Color> Item Pipe Casing | 3 |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 3 |
| <ItemLink id="gregtech:gt.blockframes:32" showIcon="left" /> | 2 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Can replace <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Muffler Hatch | 1+, Can replace <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+, Can replace <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> |

### Wallsharing

AWDs may wallshare each of their sides except for the right side (controller is in the way) to save on casings, frame boxes, and buses/hatches. No recipe uses more than 1A of power so it is possible to share one energy hatch between two machines.

## Usage

The AWD has two operating modes, listed below. Switch between modes in the GUI of the controller or by right-clicking the controller with a screwdriver. The packager mode is useful for the tiny and small piles of dust from the [<ItemLink id="gregtech:gt.blockmachines:15563" showIcon="left" />](./electric_implosion_compressor.md) and for creating scrap boxes. The unpackager mode is a nice-to-have for recycling certain items such as old [<ItemLink id="gregtech:gt.blockmachines:13106" showIcon="left" />](./lapotronic_supercapacitor.md) capacitors.

- Packager - Runs ONLY packager recipes.
- Unpackager - Runs ONLY unpackager recipes.

Input separation<FloatingImage src="gregtech:textures/gui/overlay_button/input_separation_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> should be enabled on the AWD to prevent SOLID ingredients in different input buses from being used in the same recipe, including any schematics. That means a single AWD with many input buses can support many different schematics simultaneously. Just don't forget to stay above the minimum number of supply depot casings.

### Speed Upgrades from Item Pipe Casing

AWD can be upgraded by using higher-tier Item Pipe Casing. The speed bonus for each Item Pipe Casing is listed below. 

| Item Pipe Casing | Speed |
| --- | --- |
| <ItemLink id="gregtech:gt.blockcasings11" showIcon="left" /> | 200% |
| <ItemLink id="gregtech:gt.blockcasings11:1" showIcon="left" /> | 300% |
| <ItemLink id="gregtech:gt.blockcasings11:2" showIcon="left" /> | 400% |
| <ItemLink id="gregtech:gt.blockcasings11:3" showIcon="left" /> | 500% |
| <ItemLink id="gregtech:gt.blockcasings11:4" showIcon="left" /> | 600% |
| <ItemLink id="gregtech:gt.blockcasings11:5" showIcon="left" /> | 700% |
| <ItemLink id="gregtech:gt.blockcasings11:6" showIcon="left" /> | 800% |
| <ItemLink id="gregtech:gt.blockcasings11:7" showIcon="left" /> | 900% |

## References

- [GTNH Wiki: Amazon Warehousing Depot](https://wiki.gtnewhorizons.com/wiki/Amazon_Warehousing_Depot)
