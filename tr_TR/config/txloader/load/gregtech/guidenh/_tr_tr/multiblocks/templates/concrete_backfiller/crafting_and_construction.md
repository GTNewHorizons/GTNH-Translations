### Crafting

<RecipesFor id={<Param name="controllerId" />} />
<RecipesFor id={<Param name="casingId" />} handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler,bq_quest" />
<RecipesFor id={<Param name="frameId" />} />

### Structure

The Concrete Backfiller is available in two tiers, but the only structural difference between them is the type of casings and the controller itself. 

There can be multiple regular energy hatches for overclocking. 

An input/output bus is optional and exclusively for holding mining pipes (note that the controller is fixed to "Void all" voiding mode - the machine will void mining pipes if there is no space in the controller inventory).

The Concrete Backfiller cannot be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id={<Param name="controllerId" />} showIcon="left" /> | 1, Front bottom center |
| <ItemLink id={<Param name="casingId" />} showIcon="left" /> | 3-8 |
| <ItemLink id={<Param name="frameId" />} showIcon="left" /> | 15 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Only Regular Hatches allowed, need to be at least <Param name="tier" />+ </Tooltip> | 1+, Any 1st layer casing |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Maintenance Hatch | 1, Any 1st layer casing |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 0+, Any 1st layer casing |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 1+, Any 1st layer casing |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 0+, Any 1st layer casing |