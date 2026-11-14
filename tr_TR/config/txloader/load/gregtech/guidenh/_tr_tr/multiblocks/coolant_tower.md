---
item_ids:
  - gregtech:gt.blockmachines:32025
navigation:
  title: Coolant Tower
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:32025
  position: -4001
---
# Coolant Tower
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:32025" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:32025" showIcon="left" /> is an EV tier multiblock for condensing regular steam back into distilled water.  

The Coolant Tower is effectively a [<ItemLink id="gregtech:gt.blockmachines:15524" showIcon="left" />](./large_steam_turbine.md) without the turbine or the ability to generate power.

| Property | Details |
| --- | --- |
| Unlock Tier | EV |
| Structure Size (LxWxH) | 11x11x13 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:32025" />
<RecipesFor id="gregtech:gt.blockconcretes:8" handlerId="gt.recipe.fluidsolidifier" />
<RecipesFor id="gregtech:gt.blockframes:370" />

### Structure
The Coolant Tower has no tiered components, but the light concrete can be replaced by any Light/Dark concrete variations. Search `stoneConcrete` on NEI for all available variations. 

There is no energy hatch, muffler hatch, or maintenance hatch, and the Coolant Tower can be rotated or flipped (surprisingly).

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:32025" showIcon="left" /> | 1, Front center, 2nd layer |
| <ItemImage id="gregtech:gt.blockconcretes:8" />Any Light/Dark concrete variants | 252-277 |
| <ItemLink id="gregtech:gt.blockframes:370" showIcon="left" /> | 28 |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Any 2nd layer edge concretes |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1+, Any 2nd layer edge concretes |

### Wallsharing
The Coolant Tower can wallshare to save some frames and concretes, although it is not very useful since Coolant Tower processes all steam in its hatches at fixed 1s time - the throughput is determined by hatch capacity rather than the number of machines.

## Usage
The Coolant Tower converts ALL steam in its input hatches into distilled water on a fixed 1 second cycle. There is no upper limit on the amount of steam that can be condensed at once, but it only works with regular GregTech steam and not the superheated, supercritical, or dense versions. The conversion ratio is always 160L of steam for 1L of distilled water.

> [!WARNING]
> Coolant Tower will void all distilled water when there are no output space. Make sure input hatches' capacity aren't higher than output hatches', and all output pulled out before next steam converted to distilled water.

The Coolant Tower is useful when you need steam converted into Distilled Water instantly, rather than generating power.  
One example or application is the [<ItemLink id="gregtech:gt.blockmachines:12791" showIcon="left" />](./high_temperature_gas_cooled_reactor.md) which is commonly used to breed rare materials rather than generate power.  
Another example is skipping the last step in a large turbine chain. The [<ItemLink id="gregtech:gt.blockmachines:15524" showIcon="left" />](./large_steam_turbine.md) generates less power compared to [<ItemLink id="gregtech:gt.blockmachines:15526" showIcon="left" />](./large_steam_turbine.md) and [<ItemLink id="gregtech:gt.blockmachines:15525" showIcon="left" />](./large_steam_turbine.md) which makes some player to completly skips steam turbine to save resources by running fewer turbines.