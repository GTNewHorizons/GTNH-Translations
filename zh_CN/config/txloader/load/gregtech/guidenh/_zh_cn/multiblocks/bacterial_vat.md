---
item_ids:
  - gregtech:gt.blockmachines:12712
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKAQ==
navigation:
  title: Bacterial Vat
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:12712
  position: -3001
---
# Bacterial Vat

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12712" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" /> (BV) is an HV tier multiblock for mass fermenting fluids.

Bacteria contained within the vat break down organic compounds into something new, such as Saccharomyces Escherichia turning grape juice into wine. The species of bacteria, and therefore the recipe, is determined by placing a petri dish with a culture inside the controller block of the machine.

The fermenting process itself is closely tied to the carrying capacity of the environment, meaning the output hatch should stay as close as possible to 50% capacity for maximum growth and productivity.

Although the BV is mandatory for progression in UV, the player can later craft all the necessary fluids in the [<ItemLink id="gregtech:gt.blockmachines:31151" showIcon="left" />](./quantum_force_transformer.md).

| Property | Details |
| --- | --- |
| Unlock Tier | HV |
| Structure Size (LxWxH) | 5x5x4 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction

### Crafting
<RecipesFor id="gregtech:gt.blockmachines:12712" />

<RecipesFor id="gregtech:gt.blockcasings4:1" />

<ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> is skippable and only needed for recipes that require radiation.

<RecipesFor id="gregtech:gt.blockmachines:12713" />

### Structure

The BV has one tiered component. The glass determines the **maximum recipe tier, but not the maximum energy hatch tier**.

BV can be rotated or flipped.

Multi-amp and laser energy hatches are not supported, but there can be multiple regular energy hatches for overclocking.

Only one output hatch and one radio hatch are allowed.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" /> | 1, Front bottom center |
| <ItemLink id="gregtech:gt.blockcasings4:1" showIcon="left" /> | 19-45, Whole 1st and 4th layer |
| <ItemImage id="bartworks:BW_TieredGlass" /><Color id="blue">Tiered</Color> Glass | 32, 2nd and 3rd layer with a hollow center |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed</Tooltip> | 1+, Can replace any casing |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Can replace any casing |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 0+, Can replace any casing |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Can replace any casing |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Can replace any casing |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1, Can replace any casing |
| <ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> | 0-1, Can replace any casing |

### Wallsharing

BVs may wallshare each of their sides to save on glass, casings, and buses/hatches. That includes both the output hatch and the radio hatch which helps simplify automation setups and save on radioactive materials. If sharing between four machines, one hatch can go on top and the other can go on bottom.

No recipe uses more than 1A of power so it is possible to share one energy hatch between two machines.

## Usage
BV recipes have 4 Requirements to operate: Glass Tier, Voltage, Culture and Radioactive.

You can check these requirements on NEI. For example, the recipe below requires:
- EV+ Glass Tier
- HV+ Voltage
- Need at least 83 sievert
- Requires <ItemImage id="bartworks:BioLabParts" nbt='tag:{Name:"Binni Bacteria"}' label="right" />

<RecipeFor id="NotEnoughItems:neiFluidDisplay:94" />

Note that this is an HV recipe, although it requires at least EV tiered glass to operate.

### Culture
All BV recipes require a specific petri dish with a culture inside the controller block. Petri dishes are acquired from the [<ItemImage id="gregtech:gt.blockmachines:12699" noTooltip />Bio Lab](/singleblock/bio_lab.md), an HV+ singleblock machine for all biotechnology related recipes.

You can check [<ItemImage id="gregtech:gt.blockmachines:12699" noTooltip />Bio Lab](/singleblock/bio_lab.md) guide for more information about how to produce a petri dish with a culture.

### Radio Hatch
A few exotic and alien species of bacteria require radiation to survive which is supplied through a radio hatch containing rods or long rods of radioactive materials.

A <ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> is similar to an input bus except it continuously consumes items regardless if a recipe is running or not. Fortunately, the radio hatch can be disabled at any time with a machine controller cover.

The radioactive material inside the radio hatch determines the strength of the radiation in sieverts (sv), but the built in radiation shutter can reduce that by a custom amount. There is no benefit to reducing the sieverts other than needing to have an exact amount for a specific recipe, since material with high sieverts usually has shorter lifespans.

You can control radiation shutter by clicking the screwdriver button<FloatingImage src="gregtech:textures/gui/overlay_button/screwdriver.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} /> on top left of the radio hatch GUI.

Different materials also have different lifespans, but most are quite short. The following table lists a few of the many radioactive materials by their strength, lifespan, and mass.

<Column width="380">
  | Material | Strength | Lifespan | Mass |
  |----------|----------|-----------|------|
  | <ItemLink id="gregtech:gt.metaitem.01:23090" showIcon="left" /> | 83 sv | 198.80 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22090" showIcon="left" /> | ^^ | 397.60 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23096" showIcon="left" /> | 90 sv | 98.75 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22096" showIcon="left" /> | ^^ | 197.50 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23097" showIcon="left" /> | 92 sv | 80.850 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23098" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.02:22097" showIcon="left" /> | ^^ | 161.70 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22098" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.01:23100" showIcon="left" /> | 94 sv | 66.20 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23101" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.02:22100" showIcon="left" /> | ^^ | 132.40 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22101" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.01:23103" showIcon="left" /> | 95 sv | 59.90 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22103" showIcon="left" /> | ^^ | 119.80 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23324" showIcon="left" /> | 130 sv | 14.40 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22324" showIcon="left" /> | ^^ | 28.80 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23326" showIcon="left" /> | 140 sv | 10.65 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22326" showIcon="left" /> | ^^ | 21.70 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23327" showIcon="left" /> | 150 sv | 7.85 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22327" showIcon="left" /> | ^^ | 15.70 s | 2 kg |
  {: widths="200, 60, 60, 60"}
</Column>

You can enable sound muffling by clicking the sound button in hatch GUI or right-clicking the radio hatch with a hammer.

### Output rate

The BV is a closed system with a limited carrying capacity (K) for bacteria to grow. All closed systems follow a sigmoidal population curve meaning the growth rate is initially slow due to a small starting population, increases in rate as the population grows, and then slows down again as the finite resources in the environment become a limiting factor. **Maximum growth in a closed system occurs at K/2**.

The size of the output hatch on the BV is equivalent to the carrying capacity (K) of the bacterial culture. Very little growth occurs when the output hatch is empty or when the output hatch is close to full. Ideally, the output hatch stays as close as possible to 50% capacity for maximum growth and productivity. More specifically, both the input AND output fluids are multiplied by up to x1,001 based on how close the output hatch is to K/2 or half-full. The solid ingredients and culture are not affected. The multiplier (m) is calculated with the following equation where Fill% is the current fluid level out of the maximum capacity.

<Latex formula="m=\lceil -4,000\times(\text{Fill}\% - 0.5)^2\rceil + 1,001" />

This equation is quadratic to reflect the derivative of the sigmoidal population curve. The ceiling operator, however, adds a small buffer around K/2 that rounds up values close to the maximum multiplier, which means the output hatch does not have to be perfectly 50% capacity to achieve the x1,001 gain. Larger output hatches have a larger buffer, but initially require more fluid to reach K/2. It is recommended to start with a very small output hatch and work up to larger sizes as more output fluid is obtained. The following table lists all the different output hatches and their thresholds for earning the maximum x1,001 multiplier (m). The graph visually depicts the general relationship based on the percentage fill level.

<Row>
  <Column width="310">
| Hatch | Minimum | K/2 | Maximum | Range |
| --- | --- | --- | --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" scale="0.8"> ULV</ItemLink> | 3,874 L | 4,000 L | 4,126 L | 252 L |
| <ItemLink id="gregtech:gt.blockmachines:61" showIcon="left" scale="0.8"> LV</ItemLink> | 7,748 L | 8,000 L | 8,252 L | 504 L |
| <ItemLink id="gregtech:gt.blockmachines:62" showIcon="left" scale="0.8"> MV</ItemLink> | 15,495 L | 16,000 L | 16,505 L | 1,010 L |
| <ItemLink id="gregtech:gt.blockmachines:63" showIcon="left" scale="0.8"> HV</ItemLink> | 30,989 L | 32,000 L | 33,011 L | 2,022 L |
| <ItemLink id="gregtech:gt.blockmachines:64" showIcon="left" scale="0.8"> EV</ItemLink> | 61,977 L | 64,000 L | 66,023 L | 4,046 L |
| <ItemLink id="gregtech:gt.blockmachines:65" showIcon="left" scale="0.8"> IV</ItemLink> | 123,953 L | 128,000 L | 132,047 L | 8,094 L |
| <ItemLink id="gregtech:gt.blockmachines:66" showIcon="left" scale="0.8"> LuV</ItemLink> | 247,905 L | 256,000 L | 264,095 L | 16,190 L |
| <ItemLink id="gregtech:gt.blockmachines:67" showIcon="left" scale="0.8"> ZPM</ItemLink> | 495,810 L | 512,000 L | 528,190 L | 32,380 L |
| <ItemLink id="gregtech:gt.blockmachines:68" showIcon="left" scale="0.8"> UV</ItemLink> | 991,619 L | 1,024,000 L | 1,056,381 L | 64,762 L |
| <ItemLink id="gregtech:gt.blockmachines:69" showIcon="left" scale="0.8"> UHV</ItemLink> | 1,983,237 L | 2,048,000 L | 2,112,763 L | 129,526 L |
| <ItemLink id="gregtech:gt.blockmachines:12103" showIcon="left" scale="0.8"> UEV</ItemLink> | 3,966,474 L | 4,096,000 L | 4,225,526 L | 259,052 L |
| <ItemLink id="gregtech:gt.blockmachines:12104" showIcon="left" scale="0.8"> UIV</ItemLink> | 7,932,947 L | 8,192,000 L | 8,451,053 L | 518,106 L |
| <ItemLink id="gregtech:gt.blockmachines:12105" showIcon="left" scale="0.8"> UMV</ItemLink> | 15,865,893 L | 16,384,000 L | 16,902,107 L | 1,036,214 L |
| <ItemLink id="gregtech:gt.blockmachines:12106" showIcon="left" scale="0.8"> UXV</ItemLink> | 31,731,785 L | 32,768,000 L | 33,804,215 L | 2,072,430 L |
| <ItemLink id="gregtech:gt.blockmachines:12737" showIcon="left" scale="0.8"> Giant</ItemLink> | 48,418,862 L | 50,000,000 L | 51,581,138 L | 3,162,276 L |
{: widths="55, 85, 85, 85, 75"}
</Column>
<FunctionGraph xRange="0..100" xLabel="Fill %" yLabel="Multiplier" width="220">
  <Plot expr="(-4000 * (x/100 - 0.5)^2) + 1001" />
</FunctionGraph>
</Row>

Note that the multiplier (m) is calculated at the very start of a recipe. This is important when the BV is running continuously because the output from the previous recipe factors into the calculation of the multiplier (m) for the next one. Ideally, the range of optimal production should be greater than the amount of output fluid to guarantee the maximum multiplier.

## References
- [GTNH Wiki - Bacterial Vat](https://wiki.gtnewhorizons.com/wiki/Bacterial_Vat)
