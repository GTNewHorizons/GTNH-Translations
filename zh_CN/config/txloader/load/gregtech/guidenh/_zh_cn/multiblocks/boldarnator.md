---
item_ids:
  - gregtech:gt.blockmachines:15556
quest_ids:
  - AAAAAAAAAAAAAAAAAAABhQ==
navigation:
  title: Boldarnator
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15556
  position: -5001
---
# Boldarnator
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15556" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15556" showIcon="left" /> is an IV tier multiblock for creating and harvesting basic rocks.

The Boldarnator is a direct upgrade from the [singleblock rock breaker](/singleblock/rock_breaker.md) because it runs at 300% speed, only uses 75% of the EU/t normally required, and offers 8 parallels per voltage tier.

| Property | Details |
| --- | --- |
| Unlock Tier | IV |
| Structure Size (LxWxH) | 5x7x5 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces 100 gibbl/s pollution, and require Muffler Hatch |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:15556" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="miscutils:gtplusplus.blockcasings.2" />

<RecipesFor id="gregtech:gt.blockframes:81" />

### Structure

The Boldarnator has no tiered components. The glass can be any tier and has no effect on the operation of the machine.

Multi-amp and laser energy hatches are not supported, but there can be multiple regular energy hatches for overclocking.

The lava and water are spawned for free once the structure is formed, and therefore do NOT need to be placed manually.

The Boldarnator can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15556" showIcon="left" /> | 1, Front center, 3rd layer |
| <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> | 50-55 |
| <ItemLink id="gregtech:gt.blockframes:81" showIcon="left" /> | 36 |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 12 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Muffler Hatch | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+, Can replace any <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> |

### Wallsharing

Boldarnators may wallshare each of their sides to save on casings, glass, frameboxes, and buses/hatches. That includes the tanks on either side, but the fluids cannot be switched without horizontally flipping one of the controllers first (sneak right-click with a wrench).

No recipe uses more than 0.5A of power so it is possible to share one energy hatch between four machines.

## Usage

The Boldarnator can create <ItemLink id="minecraft:cobblestone" showIcon="left" />, <ItemLink id="minecraft:stone" showIcon="left" />, <ItemLink id="minecraft:netherrack" showIcon="left" />, <ItemLink id="Botania:stone:1" showIcon="left" />, <ItemLink id="etfuturum:cobbled_deepslate" showIcon="left" />, <ItemLink id="minecraft:obsidian" showIcon="left" />, and can simulate <ItemLink id="thaumicbases:genLeaves:2" showIcon="left" /> and <ItemLink id="thaumicbases:genLeaves:3" showIcon="left" />'s behaviors (which convert the block underneath into its corresponding block, like <ItemLink id="minecraft:soul_sand" showIcon="left" />, <ItemLink id="minecraft:quartz_ore" showIcon="left" />, and <ItemLink id="minecraft:end_stone" showIcon="left" />), at the cost of a 10% chance to consume the leaves.

The Boldarnator offers 8 parallels per voltage tier. The following table shows the parallels and the processing rate of each block per tier.

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Parallels | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |
| <ItemLink id="minecraft:cobblestone" showIcon="left" />/s | 4 | 20 | 88 | 128 | 400 | 960 | 2,240 | 3,840 | 8,640 | 19,200 | 42,240 | 46,080 | 99,840 | 215,040 | 460,800 |
| <ItemLink id="minecraft:stone" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="minecraft:netherrack" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="Botania:stone:1" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="etfuturum:cobbled_deepslate" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="minecraft:obsidian" showIcon="left" />/s | 0.5 | 2.4 | 10 | 15 | 38 | 96 | 225 | 640 | 1,440 | 3,200 | 5,280 | 5,760 | 12,480 | 26,880 | 57,600 |
{: widths="90"}

You can check the recipes that the Boldarnator can process in NEI. It shows which items are required for processing, including items that are consumed during processing and items that are not. Currently, there are 4 recipes that consume items:
1. <ItemLink id="minecraft:obsidian" showIcon="left" /> - Consumes 1 redstone per operation.
1. <ItemLink id="minecraft:netherrack" showIcon="left" /> - Consumes 1 glowstone per operation.
1. <ItemLink id="thaumicbases:genLeaves:2" showIcon="left" /> - 10% chance to consume leaves per operation.
1. <ItemLink id="thaumicbases:genLeaves:3" showIcon="left" /> - 10% chance to consume leaves per operation.

## References

- [GTNH Wiki : Boldarnator](https://wiki.gtnewhorizons.com/wiki/Boldarnator)
