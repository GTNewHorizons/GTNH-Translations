### Crafting

<RecipesFor id={<Param name="controllerId" />} handlerBlacklist="gt.recipe.scanner,gt.recipe.researchStation" />
<RecipesFor id={<Param name="casingId" />} handlerBlacklist="gt.recipe.researchStation" />
<RecipesFor id={<Param name="fusionCoilId" />} />
<RecipesFor id={<Param name="frameId" />} handlerBlacklist="gt.recipe.unpackager" />
<RecipesFor id={<Param name="glassId" />} handlerBlacklist="enhancedlootbags,gt.recipe.chemicalbath" />

### Structure

The Compact Fusion Reactor is effectively a larger Fusion Reactor with similar restrictions on the location of the buses/hatches. Input hatches are limited to specific glass blocks on each side, output hatches are limited to the same glass blocks on each side, and energy hatches are limited to specific casings on each curve. 

The glass is NOT tiered--there is a very specific type of glass needed for each structure tier, but it can be either normal or transparent.

Every tier has a minimum voltage for the energy hatches.

The Compact Fusion Reactor can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id={<Param name="controllerId" />} showIcon="left" /> | 1, Middle center, 4th layer |
| <ItemLink id={<Param name="casingId" />} showIcon="left" /> | 1662-1695 |
| <ItemLink id={<Param name="fusionCoilId" />} showIcon="left" /> | 560 |
| <ItemLink id={<Param name="frameId" />} showIcon="left" /> | 128 |
| <ItemLink id={<Param name="glassId" />} showIcon="left" /> | 63-93 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1-32 |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+ |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 1+ |