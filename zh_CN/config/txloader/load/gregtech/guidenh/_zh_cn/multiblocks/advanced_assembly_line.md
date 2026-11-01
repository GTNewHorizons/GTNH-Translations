---
item_ids:
  - gregtech:gt.blockmachines:13532
quest_ids:
  - ZIotzqvnRiKu1_1Hb9i1dg==
navigation:
  title: Advanced Assembly Line
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:13532
  position: -5001
---

# Advanced Assembly Line

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:13532" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" /> (AAL) is an IV tier multiblock for running [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) recipes in parallel by leveraging item pipelining; ingredients are consumed slice-by-slice instead of all at once, much like a real Assembly Line. That means the maximum number of parallels corresponds to the number of solid ingredients in a recipe. 

The AAL supports multi-amp and laser energy hatches for serious overclocking and massive parallel operation, but **CANNOT** tier skip and is harder to automate compared to regular [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md), which makes AAL specialized in late-game mass production like stargate material rather than early-game progression. 

| Property | Details |
| --- | --- |
| Unlock Tier | IV |
| Structure Size (LxWxH) | 3x5-16x4 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | Unique |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction

### Crafting
<RecipesFor id="gregtech:gt.blockmachines:13532" handlerId="gt.recipe.fakeAssemblylineProcess" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gregtech:gt.blockcasings2" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="gregtech:gt.blockcasings2:5" />

<RecipesFor id="gregtech:gt.blockcasings2:9" />

### Structure
The only structural difference between the AAL and the [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) is the controller. 

AAL can be rotated or flipped.

The glass can be any tier and has no effect on the operation of the machine. 

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass and subchannel "length" to specify the number of slices $$(\text{Slices} = \text{Length} + 4)$$

#### Base Structure (Minimum requirements)
| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" /> | First slice, 3rd layer |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 10, Both sides of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 8, Both sides of 3rd layer |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-12, Both sides of 1st layer and center of 4th layer |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 5, Center of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 5, Center of 3rd layer |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Any 4th layer Casing |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1+, Any 1st layer side casings |
| <ItemImage id="gregtech:gt.blockmachines:145" noTooltip />Data Access Hatch | 1, Any both sides of 3rd layer but <Color id="red">**NOT**</Color> on first slice |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 5, Center of 1st layer |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Any 1st layer side casings |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1, Any 1st layer on last slice |

#### Each Additional Slice

<GameScene interactive={true} wrap="square" align="right" width="170" height="130">
  <Block id="gregtech:gt.blockmachines:71" />
  <Block id="gregtech:gt.blockcasings2" x="-1"/>
  <Block id="gregtech:gt.blockcasings2" x="1"/>
  <Block id="gregtech:gt.blockcasings2:5" y="1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="-1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="1" />
  <Block id="gregtech:gt.blockcasings2:9" y="2" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="-1" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="1" />
  <Block id="gregtech:gt.blockcasings2" y="3"/>
</GameScene>

Each additional slice (1 length) requires these blocks:

| Component | Quantity and placement |
| --- | --- |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 2, Both sides of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 2, Both sides of 3rd layer |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-3, Both sides of 1st layer and center of 4th layer |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 1, Center of 2nd layer |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 1, Center of 3rd layer |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1, Center of 1st layer |

In any slice, <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatches">Can use Regular, Multi-Amp, Laser</Tooltip> can replace 4th layer casing and <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> in 1st layer can be replaced with <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatches.

Note that the <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus must be moved to the last slice when you extend AAL slices.

### Wallsharing

AALs may wallshare each of their sides to save on casings, glass, and buses/hatches. That includes any input hatches, maintenance hatches, data access hatches, and output buses. Sharing a data access hatch is particularly valuable for saving TPS and reducing the number of [<ItemLink id="gregtech:gt.blockmachines:15313" showIcon="left" />](./data_bank.md) multiblocks needed to operate.

## Usage

<GameScene wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/aal_operation_ponder.snbt" />
  <ImportPonder src="/assets/ponders/multiblocks/aal/aal_operation_ponder.json" />
</GameScene>

The AAL starts processing once the contents of the buses/hatches align with a stored data stick, much like the regular [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md). Every recipe must pass through N slices on the machine, where N is the number of solid ingredients. Each slice takes $$\text{T} = (\text{base duration} / \text{N})$$ seconds to process the ONE type of item in its input bus before continuing to the next slice for the next item. This repeats until all ingredients are consumed and the final product is sent to the output bus for retrieval. All fluids are consumed at the very start of processing.

The AAL supports parallel processing by allowing the next recipe to begin once the first slice is done with the first recipe. This creates a staggered pattern that allows every slice to work simultaneously, if there are enough resources available.

If the next slice is missing the required item in its input bus, the current slice enters the **STUCK** state which halts the entire machine until the missing item is found/returned. The status light on the face of the controller turns orange to indicate that the machine is STUCK. Use WAILA to locate where exactly the problem occurred.

The scene on the right shows how the AAL processes the same recipe simultaneously slice by slice, why the AAL gets stuck, and how to resolve it.

### Laser Overclocks

The energy consumption of the AAL is the number of active slices times the base EU/t, similar to parallels. The AAL then runs up to N imperfect overclocks where N is the difference between the voltage tier of the lowest tier energy hatch and the voltage tier of the recipe. 

Further overclocks are all laser overclocks, which consume more power and scale even worse than an imperfect overclock. The first one is 2x speed for 4.3x the power and each additional one increases the power multiplier by 0.3, scaling infinitely.

- Imperfect Overclocks - 2x speed for 4.0x power (2/4.0).
- 1st Laser Overclock - 2x speed for 4.3x power (2/4.3).
- 2nd Laser Overclock - 2x speed for 4.6x power (2/4.6).
- 3rd Laser Overclock - 2x speed for 4.9x power (2/4.9).

The increased power cost of laser overclocks means that upgrading the energy hatch(es) is not always going to overclock the machine. It all depends on the recipe's base EU/t and the maximum number of parallels. 

Consider the UIV field generator recipe as an example. There can be up to 14 slices active simultaneously and each one consumes 15/16A of UEV power for a total of 13.1A. That means a 16A UEV energy hatch is enough to cover the base cost of the recipe, but does not grant any laser overclocks. Upgrading to a 64A energy hatch grants one laser overclock because that is greater than 13.1 x 4.3 = 56.4A, but upgrading to a 256A energy hatch does NOT grant a second laser overclock because that is less than 56.4 x 4.6 = 259A. The following table lists the amperage needed for a given number of laser overclocks for on-tier recipes (i.e. UEV recipes with one UEV laser energy hatch) that consume 15/16A of power.


| Slices | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 64 | 256 | 1,024 | 4,096 | 16,384 | 65,536 | 1,048,576 | 4,194,304 | 
| 5 | 64 | 256 | 1,024 | 4,096 | 16,384 | 262,144 | 1,048,576 | 4,194,304 | 
| 6 | 64 | 256 | 1,024 | 4,096 | 16,384 | 262,144 | 1,048,576 | 4,194,304 |
| 7 | 64 | 256 | 1,024 | 4,096 | 65,536 | 262,144 | 1,048,576 | 4,194,304 | 
| 8 | 64 | 256 | 1,024 | 4,096 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 9 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 10 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 11 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 12 | 64 | 256 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 13 | 64 | 256 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 14 | 64 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 15 | 64 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 16 | 256 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |


## References

- [GTNH Wiki: Advanced Assembly Line](https://wiki.gtnewhorizons.com/wiki/Advanced_Assembly_Line)
