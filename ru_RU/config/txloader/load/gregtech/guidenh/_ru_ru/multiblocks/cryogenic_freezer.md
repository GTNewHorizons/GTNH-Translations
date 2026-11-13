---
item_ids:
  - gregtech:gt.blockmachines:15565
  - gregtech:gt.blockmachines:967
quest_ids:
  - AAAAAAAAAAAAAAAAAAAH8w==
navigation:
  title: Cryogenic Freezer
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15565
  position: -5001
---
# Cryogenic Freezer
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15565" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15565" showIcon="left" /> is an IV tier multiblock for mass cooling hot ingots and fluids.

The Cryogenic Freezer is a direct upgrade from the [<ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" />](./vacuum_freezer.md) because it runs at 300% speed, only uses 90% of the EU/t normally required, and offers a fixed 16 parallels.  
The other upgrade option for the Vacuum Freezer is the [<ItemLink id="gregtech:gt.blockmachines:15518" showIcon="left" />](./endothermic_fridge.md) but it only outperforms the Cryogenic Freezer if it can take full advantage of its 256 parallels (4+ overclocks) or use subspace cooling.

<Template 
  name="properties" 
  tier="IV" 
  size="7x5x4"
  reqMaintenance
  pollution="500" 
  reqMuffler 
/>

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:15565" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="miscutils:gtplusplus.blockcasings.3:10" />

<RecipesFor id="miscutils:blockFrameGtGrisium" />

<RecipesFor id="gregtech:gt.blockmachines:967" />

### Structure
The Cryogenic Freezer has no tiered components, and can be rotated or flipped.

Multiblock requires at least 1 Input Bus/Hatch and 1 Output Bus/Hatch to form.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15565" showIcon="left" /> | 1, Front center, 2nd layer |
| <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> | 46-56 |
| <ItemLink id="miscutils:blockFrameGtGrisium" showIcon="left" /> | 24 |
| <ItemLink id="gregtech:gt.blockmachines:967" showIcon="left" /> | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Muffler Hatch | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 0+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 0+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> |

### Wallsharing

Cryogenic Freezers may wallshare each of their sides to save on casings, frame boxes, and buses/hatches. The most efficient way to save <ItemLink id="miscutils:gtplusplus.blockcasings.3:10" showIcon="left" /> is to share the whole bottom layer by rotating one machine 180 degrees. No recipe uses more than 1A of power so it is possible to share one energy hatch between two machines.

> [!WARNING]
> Sharing two or more energy hatches between two machines can cause a powerfail, because a single machine will draw 4A to achieve tier skipping. Ensure the total amperage provided by the shared hatches is <Latex formula="2\times4^n" scale="0.6" />A (2, 8, 32...) so that every machine can always pull 1A.

## Usage

The Cryogenic Freezer consumes 10 L/s of <ItemLink id="NotEnoughItems:neiFluidDisplay:1214" showIcon="left" /> during operation through a specialized <ItemLink id="gregtech:gt.blockmachines:967" showIcon="left" />. If it ever runs out, the machine crashes immediately and causes a random maintenance issue to occur. Cryotheum is primarily sourced from evolved cold blazes on Europa or the cryotheum bee. Blizz dust can also be made from blaze powder if necessary.

## References
- [GTNH Wiki : Cryogenic Freezer](https://wiki.gtnewhorizons.com/wiki/Cryogenic_Freezer)