---
item_ids:
  - gregtech:gt.blockmachines:15760
quest_ids:
  - HvtY6xu3RAKjwhAZCTwK8A==
navigation:
  title: Bose-Einstein Condensate Maxwell Gate
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15760
  position: -11001
---
# Bose-Einstein Condensate Maxwell Gate
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15760" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left" /> is a UIV tier multiblock for limiting condensate flow in only one direction in the [BEC Line](./bose_einstein_condensate_line.md)--similar to an ME storage bus. 

The Maxwell Gate may be emplaced anywhere on a BEC network and effectively splits it into two separate subnetworks that connect to the <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> on either side of the structure. Everything on the left network is exposed to the right network, but not the other way around. 

The Maxwell Gate can also filter for specific condensates and only consumes 1A UIV while active, regardless of either network's status. 

Set the filter manually in the GUI of the controller or by filling input hatches with the original fluid of the desired condensate.

> [!WARNING]
> In this guide, "Left Network" means exposed network, and "Right Network" is watching network. terms are unified for ease of explanation.
>
> You should check your machine's side and flipped status - the term `left` and `right` are based on default machine formation - flipping controller will change direction.

| Property | Details |
| --- | --- |
| Unlock Tier | UIV |
| Structure Size (LxWxH) | 11x17x11 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

> [!TIP]
> You can check Maxwell Gate's side by checking controller animation - It shows some "flows" that moves from input network to output network.

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:15760" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Structure

The Maxwell Gate has no tiered components, and can be rotated or flipped.

The energy hatch may replace any electromagnetically-isolated casing anywhere on the structure. 

Multi-amp and laser energy hatches are supported, but it only ever consumes 1A UIV(33,554,432 EU/t) anyway.  
Power tier doesn't matters, so you can provide 4A UEV, 16A UHV, or else.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left" /> | 1, Front center, 6th layer |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 148 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 92 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 75-90 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 84 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 70 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 68 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 40 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 24 |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 2, Center of each left and right casing |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Can replace any <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> |

### Wallsharing

The Maxwell Gate may wallshare each of its sides to save few blocks, and can share 1 Energy Hatch between two machines.

## Usage

The Maxwell Gate or BEC Diode is an optional step in the [BEC Line](./bose_einstein_condensate_line.md) for controlling condensate exposure/visibility. The Maxwell Gate does not push, pull, or buffer any condensate itself.

The Maxwell Gate may be emplaced anywhere on a BEC network and effectively splits it into two separate subnetworks that connect to the <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> on either side of the structure. Everything on the left network is exposed to everything on the right network, but not the other way around.

For the [<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Entanglement Apparatus</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md) to push condensate to a [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Containment Fields</ItemLink>](./bose_einstein_condensate_containment_field.md) through a Maxwell Gate, the Entanglement Apparatus __**must**__ be on the right network and the Containment Field __**must**__ be on the left network, as seen in the following image.  
Equal distribution rules still apply; if multiple Containment Fields are available, then the condensate is split proportional to their total field strength.

For the [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Observation Array</ItemLink>](./bose_einstein_condensate_observation_array.md) to pull condensate from a Containment Field through a Maxwell Gate, the Observation Array __**must**__ be on the right network and the Containment Field __**must**__ be on the left network, as seen in the following image.  
Contaminant penalties still apply; each unrequested condensate significantly slows down processing speed and if there are ever more than three contaminants in the network at once then the recipe immediately fails and voids.  

![Valid and invalid Maxwell Gate setups - Image from Fox](/assets/images/multiblocks/bec_diode_setup.png)

The Maxwell Gate allows all condensate through by default but it can also filter for specific condensates.  
Set the filter manually in the GUI of the controller <FloatingImage src="gtnhintergalactic:textures/gui/overlay_button/options.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} />or by filling input hatches with the original fluid of the desired condensate. 

Filtering is particularly useful for passive condensate production and prevents contaminants from being exposed to the Observation Array. Without it, condensate would have to be requested on-demand which could take a very long time since the Entanglement Apparatus cannot be overclocked.

### OpenComputers Integration
The Maxwell Gate is automatable with OpenComputers and has a few additional functions/methods compared to standard GregTech multiblocks, as seen below. These can be used to dynamically change the condensate filter with a script, instead of using actual fluids and input hatches.

```lua
-- List all available methods for the Maxwell Gate
local component = require('component')
local bec_diode = component.bec_diode

for k,v in pairs(bec_diode) do print(k,v) end

-- Returns the fluid name of the current condensate filter
bec_diode.getCondensateFilter()

-- Sets the condensate filter to the given fluid name
bec_diode.setCondensateFilter('name')
```

Below table shows fluid name OpenComputers uses, and which condensate matches. 
| Condensate | Names in OC |
| --- | --- |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:941" showIcon="left" /> | entangled_neutronium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:942" showIcon="left" /> | entangled_cosmicneutronium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:943" showIcon="left" /> | entangled_bedrockium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:944" showIcon="left" /> | entangled_chromaticglass |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:945" showIcon="left" /> | entangled_celestialtungsten |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:946" showIcon="left" /> | entangled_infinity |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:947" showIcon="left" /> | entangled_hypogen |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:948" showIcon="left" /> | entangled_transcendentmetal |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:949" showIcon="left" /> | entangled_dimshiftedsuperfluid |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:950" showIcon="left" /> | entangled_phononmedium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:951" showIcon="left" /> | entangled_quarkgluonplasma |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:952" showIcon="left" /> | entangled_spacetime |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:953" showIcon="left" /> | entangled_time |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:954" showIcon="left" /> | entangled_space |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:955" showIcon="left" /> | entangled_cosmicsolder |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:956" showIcon="left" /> | entangled_mhdcsm |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:957" showIcon="left" /> | entangled_magmatter |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:958" showIcon="left" /> | entangled_universium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:959" showIcon="left" /> | entangled_eternity |


## References
- [GTNH Wiki : Bose-Einstein Condensate Maxwell Gate](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Maxwell_Gate)
