---
item_ids:
  - gregtech:gt.blockmachines:15755
quest_ids:
  - 0U_ex_O9TKWF-ShWD_4UuQ==
navigation:
  title: Bose-Einstein Condensate Containment Field
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15755
  position: -11001
---
# Bose-Einstein Condensate Containment Field
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15755" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left" /> is a UIV tier multiblock for storing entangled condensate in the [BEC Line](./bose_einstein_condensate_line.md)--similar to a fluid tank. 

Entangled condensate is generated in the [<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Entanglement Apparatus</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md) and transferred to the Containment Field via BEC hatches. 

Stored condensate is exposed to all [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) on the current network and only ever leaves the machine when requested by an IO Node for a recipe.

| Property | Details |
| --- | --- |
| Unlock Tier | UIV |
| Structure Size (LxWxH) | 45x45x17 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:15755" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

### Structure

The Containment Field has no tiered components. 

Multi-amp and laser energy hatches are supported for greatly increasing the capacity of the machine. 

The Containment Field can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

Unique to the Containment Field is the <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> which emits a redstone signal if the set condition inside its GUI is true.  
There is a filter for specifying a particular type of entangled condensate, a comparison operator, and a threshold value.  
For example, emit a redstone signal if entangled infinity condensate is greater than or equal to 100,000L. Leave the filter blank to sum all stored condensates together.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left" /> | 1, Front center, 3rd layer |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 1236 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 1045 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 896 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 568 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 508 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 439-442 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 324-343 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1-4, Replaces the <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> on each of the four sides of layer 9 |
| <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |

### Wallsharing

Containment Field may wallshare each of their sides to save lots of blocks, but since the capacity can be increased virtually infinitely with a single Containment Field via the GUI, more than one is generally not built.

## Usage

The Containment Field is the second step in the [BEC Line](./bose_einstein_condensate_line.md) and stores entangled condensate until it is requested by an [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) for a recipe. Condensate both enters and leaves the Containment Field through BEC hatches on the sides of the structure and is exposed to all [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) on the current network. Optionally, use a [<ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left">Maxwell Gate</ItemLink>](./bose_einstein_condensate_maxwell_gate.md) to filter and limit the direction of condensate flow--similar to a diode and fluid filter.

The field strength of the Containment Field is set manually in the GUI of the controller by clicking the "Edit Parameter" button<FloatingImage src="gtnhintergalactic:textures/gui/overlay_button/options.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} />(or with OpenComputers) and determines both the maximum capacity and passive power consumption of the machine; every 1 unit of field strength increases the maximum capacity by 1L at the cost of 1 EU/t. It is not possible to filter or partition the storage based on condensate type.

The maximum capacity is only a soft cap since excess condensate can still enter the Containment Field, but 11% of all condensate is voided each second until it falls back below the maximum capacity. This penalty applies evenly to all stored condensates and never prioritizes any one over the others.  
Avoid this penalty by setting the field strength really high, or by using an unfiltered <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> to disable the [<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Entanglement Apparatus</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md) with a machine controller cover when condensate levels get too high.

> [!CAUTION]
> The Containment Field voids all of its contents if it ever powerfails or is manually disabled. Keep it running at all times while in use unless it is absolutely necessary to shut it down.

If multiple Containment Fields are available on the same network, then the condensate inserted into network is split proportional to their total field strength.  
For example, if one Containment Field has a 150,000 field strength and another has a 50,000 field strength, then the former receives 75% of the condensate and the latter receives only 25% of the condensate.

### OpenComputers Integration

The Containment Field is automatable with OpenComputers and has a few additional functions/methods compared to standard GregTech multiblocks, as seen below. These can be used to dynamically change the field strength of the Containment Field based on the current condensate levels as an extra protection against voiding.

```lua
-- List all available methods for the Containment Field
local component = require('component')
local bec_storage = component.bec_storage

for k,v in pairs(bec_storage) do print(k,v) end

-- Returns all stored condensate as a table mapping fluid names to amounts
bec_storage.getStoredCondensate()

-- Returns the field strength of the Containment Field as a number
bec_storage.getFieldStrength()

-- Sets the field strength of the Containment Field from a number
bec_storage.setFieldStrength(strength)
```
```lua
---@meta

-- Stub for the OpenComputers `bec_storage` component.

---@class BecStorageComponentProxy: ComponentProxy
BecStorageComponentProxy = {}

---Get all condensates stored in **current** Containment Field.
---@return table[string, number] table of condensates stored.
function BecStorageComponentProxy.getStoredCondensate() end

---Get the current field strength of the Containment Field connected.
---@return number current field strength.
function BecStorageComponentProxy.getFieldStrength() end
  
---Config the field strength of the Containment Field. number below 0 will be interpreted as 1.
---@param  strength number
function BecStorageComponentProxy.setFieldStrength(strength) end
```

## References
- [GTNH Wiki : Bose-Einstein Condensate Containment Field](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Containment_Field)
