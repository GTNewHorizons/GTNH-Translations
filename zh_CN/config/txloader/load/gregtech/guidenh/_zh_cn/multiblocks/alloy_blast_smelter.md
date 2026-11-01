---
item_ids:
  - gregtech:gt.blockmachines:810
quest_ids:
  - AAAAAAAAAAAAAAAAAAAFiA==
navigation:
  title: Alloy Blast Smelter
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:810
  position: -5001
---

# Alloy Blast Smelter

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:810" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" /> (ABS) is an IV tier multiblock for smelting dusts into molten alloys. Compared to [<ItemLink id="gregtech:gt.blockmachines:15566" showIcon="left" />](./industrial_mixing_machine.md) and [<ItemLink id="gregtech:gt.blockmachines:31023" showIcon="left" />](./zyngen.md), processing the dusts to molten alloy directly makes ABS handle basic alloy recipes faster and more efficiently. However, unlike those machines, ABS cannot tier skip - makes the ABS suited to mass production rather than tier progression.

The ABS can even be used to smelt some of the tougher alloys such as Indalloy 140, which have no recipe in any other machine. 

There are no tiered components or any sort of bonuses and there is no tier skipping, even when overclocking with multiple energy hatches. 

The minimum casing requirement is very low to allow for many buses/hatches since there are 12 unique programmed circuits to handle all ABS Recipes. The ABS is superseded by the [<ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" />](./mega_alloy_blast_smelter.md) in UV.

| Property | Details |
| --- | --- |
| Unlock Tier | IV |
| Structure Size (LxWxH) | 3x3x4 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces 200 gibbl/s pollution, and require Muffler Hatch |

## Crafting and Construction

### Crafting

<RecipesFor id="gregtech:gt.blockmachines:810" />

<RecipesFor id="miscutils:miscutils.blockcasings:14" />

<RecipesFor id="miscutils:miscutils.blockcasings:15" />

### Structure

The ABS has no tiered components. 

ABS can be rotated or flipped.

Multi-amp and laser energy hatches are not supported, but there can be multiple regular energy hatches for overclocking. The only caveat is that there is NO tier skipping (ie. 2 IV energy hatches can run the ABS at LuV voltage but cannot process LuV recipes).

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" /> | 1, Front Bottom Center |
| <ItemLink id="miscutils:miscutils.blockcasings:14" showIcon="left" /> | 16, 2nd-3rd layer with a hole in the center  |
| <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> | 3-12, Fills 1st and 4th layer  |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Muffler Hatch | 1+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1+, Can replace any <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> |

You can install more than one <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Muffler Hatch, but the pollution reduction is **average** of all installed mufflers, not the sum. For example, using <ItemLink id="gregtech:gt.blockmachines:96" /> and <ItemLink id="gregtech:gt.blockmachines:95" /> makes pollution decreased to 43%, which creates more pollution than using only one <ItemLink id="gregtech:gt.blockmachines:96" />.

You can also add some <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus to save some casings - just take care about minimum requirements.

### Wallsharing

ABS may wallshare each of their sides to save on casings, coils, and buses/hatches. However, reducing the number of unique input buses may not be very helpful considering the sheer amount of programmed circuits in the recipes.

## Usage

The following tables list all 71 recipes by their voltage tier and programmed circuit (PC). In total, there are 12 unique programmed circuits to be spread out across 8 input buses if the last few are combined. Some are also not very useful until after the [<ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" />](./mega_alloy_blast_smelter.md) is unlocked.

Input separation<FloatingImage src="gregtech:textures/gui/overlay_button/input_separation_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> should be enabled on the ABS to prevent SOLID ingredients in different input buses from being used in the same recipe, including any programmed circuits. That means a single ABS with many input buses can support many different programmed circuits simultaneously. Just don't forget to stay above the minimum number of casing blocks. 
FLUID ingredients are **always shared regardless of input separation**, unless the input hatch is colored.

<ContentTabs
  title="Organized ABS Recipes"
>

<Tab title="Recipes organized by Voltage Tier">

| Tier | PC | Molten Alloy | ABS Only |
| ---- | -- | ------------ | -------- |
| LV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1054" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1033" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1056" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1034" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1079" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(From Base) | <Color id="red">✗</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1096" /> | <Color id="red">✗</Color> |
| MV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1057" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:346" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1341" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1095" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1035" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1040" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1041" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1042" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Direct) | <Color id="red">✗</Color> |
| ^^ | 7 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1043" /> | <Color id="green">✓</Color> |
| ^^ | 11 | <ItemLink id="NotEnoughItems:neiFluidDisplay:620" /> | <Color id="red">✗</Color> |
| HV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:624" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1030" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1031" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1055" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1032" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1050" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1051" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1036" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1037" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1045" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1046" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1047" /> | <Color id="green">✓</Color> |
| EV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1065" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1064" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1053" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1028" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1052" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1044" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:701" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1048" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1059" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1049" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1358" /> | <Color id="red">✗</Color> |
| ^^ | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:351" /> | <Color id="red">✗</Color> |
| IV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1038" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1058" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1080" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1063" /> | <Color id="green">✓</Color> |
| ^^ | 14 | <ItemLink id="NotEnoughItems:neiFluidDisplay:981" /> | <Color id="red">✗</Color> |
| ^^ | 15 | <ItemLink id="NotEnoughItems:neiFluidDisplay:979" /> | <Color id="red">✗</Color> |
| ^^ | 20 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1003" /> | <Color id="red">✗</Color> |
| ^^ | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1005" /> | <Color id="red">✗</Color> |
| LuV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:748" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1066" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1372" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1062" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1069" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1373" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1039" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1070" /> | <Color id="green">✓</Color> |
| ZPM | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1067" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1074" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1071" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1072" /> | <Color id="green">✓</Color> |
| UV | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1075" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1076" /> | <Color id="red">✗</Color> |
| ^^ | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:1078" /> | <Color id="green">✓</Color> |
| UHV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1077" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1073" /> | <Color id="green">✓</Color> |
| UEV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:826" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1081" /> | <Color id="green">✓</Color> |
| UIV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:172" /> | <Color id="green">✓</Color> |
| UXV | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:184" /> | <Color id="green">✓</Color> |
{: widths="60, 60, 400, 80"}

</Tab>

<Tab title="Recipes organized by Programmed Circuit">

| Tier | PC | Molten Alloy | ABS Only |
| ---- | -- | ------------ | -------- |
| LV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1054" /> | <Color id="red">✗</Color>  |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1033" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1056" /> | <Color id="red">✗</Color> | 
| MV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1057" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:346" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1341" /> | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:624" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1030" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1031" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1055" /> | <Color id="red">✗</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1065" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1064" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1053" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1038" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:748" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1066" /> | <Color id="red">✗</Color> | 
| LV | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1034" /> | <Color id="red">✗</Color> | 
| MV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1095" /> | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1032" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1372" /> | <Color id="red">✗</Color> | 
| LV | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1079" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(From Base) | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1050" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1051" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1036" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1037" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1045" /> | <Color id="red">✗</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1028" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1052" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1044" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1058" /> | <Color id="red">✗</Color> | 
| UV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1075" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1076" /> | <Color id="red">✗</Color> | 
| MV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1035" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1040" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1041" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1042" /> | <Color id="green">✓</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1046" /> | <Color id="green">✓</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:701" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1048" /> | <Color id="green">✓</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1080" /> | <Color id="green">✓</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1062" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1069" /> | <Color id="green">✓</Color> | 
| ZPM | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1067" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1074" /> | <Color id="green">✓</Color> | 
| UHV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1077" /> | <Color id="green">✓</Color> | 
| UEV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:826" /> | <Color id="green">✓</Color> | 
| UIV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:172" /> | <Color id="green">✓</Color> | 
| MV | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Direct) | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1047" /> | <Color id="green">✓</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1059" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1049" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1358" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1373" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1039" /> | <Color id="green">✓</Color> | 
| MV | 7 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1043" /> | <Color id="green">✓</Color> | 
| LV | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1096" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1063" /> | <Color id="green">✓</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1070" /> | <Color id="green">✓</Color> | 
| ZPM | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1071" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1072" /> | <Color id="green">✓</Color> | 
| UHV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1073" /> | <Color id="green">✓</Color> | 
| UEV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1081" /> | <Color id="green">✓</Color> | 
| MV | 11 | <ItemLink id="NotEnoughItems:neiFluidDisplay:620" /> | <Color id="red">✗</Color> | 
| IV | 14 | <ItemLink id="NotEnoughItems:neiFluidDisplay:981" /> | <Color id="red">✗</Color> | 
| IV | 15 | <ItemLink id="NotEnoughItems:neiFluidDisplay:979" /> | <Color id="red">✗</Color> | 
| IV | 20 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1003" /> | <Color id="red">✗</Color> | 
| EV | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:351" /> | <Color id="red">✗</Color> | 
| IV | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1005" /> | <Color id="red">✗</Color> | 
| UV | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:1078" /> | <Color id="green">✓</Color> | 
| UXV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:184" /> | <Color id="green">✓</Color> | 
{: widths="60, 60, 400, 80"}

</Tab>

</ContentTabs>

## References

- [GTNH Wiki: Alloy Blast Smelter](https://wiki.gtnewhorizons.com/wiki/Alloy_Blast_Smelter)
