---
item_ids:
  - gregtech:gt.blockmachines:3018
quest_ids:
  - RLJR8nFySzSaZLeCRsabDg==
navigation:
  title: Beam Stabilizer
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3018
  position: -8001
---
# Beam Stabilizer
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3018" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" /> is a UV tier multiblock that temporarily buffers particle beams and re-releases them at a custom rate. The Beam Stabilizer does not require any power or maintenance to run, and particle beams passing through also do not suffer any penalties or lose any energy/focus. Only the rate is reduced to the value set in the GUI of the controller, but nothing is ever lost. 

The Beam Stabilizer is completely optional, but may assist with the [Beam Line](./beam_line.md) and/or the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md). Also try the [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md) and [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) before processing recipes in the [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md).

| Property | Details |
| --- | --- |
| Unlock Tier | UV |
| Structure Size (LxWxH) | 11x7x7 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:3018" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Structure

The Beam Stabilizer has no tiered components. The glass can be any tier and has no effect on the operation of the machine. 

The Beam Stabilizer can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" /> | 1, Front center, 3rd layer |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 95 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 15 |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 9 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Above controller |
| <ItemLink id="gregtech:gt.blockmachines:10504" showIcon="left" /> | 1, Center of opposite side of the controller |

### Wallsharing
Beam Stabilizers may wallshare each of their sides to save on casings. However, it is not possible to share the beam input hatch or beam output hatch due to the restrictions on their locations.

## Usage
The Beam Stabilizer temporarily buffers particle beams and re-releases them at a custom rate. It does not require any power or maintenance to run and never shuts down unless manually disabled. Particle beams also do not suffer any penalties or lose any energy/focus when passing through the machine. Only the rate is reduced to the value set in the GUI of the controller, but nothing is ever lost.  
For example, if an electron beam with a rate of 100 enters a Beam Stabilizer with a target beam rate of 40, then the machine first outputs two beams with a rate of 40 and then a beam with a rate of 20.

The buffer has a maximum capacity of 100k particles and ignores any particle beams that do not have the same particle type, energy, or focus. The only stat that could be different is the input beam rate which means the Beam Stabilizer could use the [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) to filter particle beams prior to them entering the machine. Particles are not added to the buffer or removed from the buffer while the machine is disabled.

## References
- [GTNH Wiki : Beam Stabilizer](https://wiki.gtnewhorizons.com/wiki/Beam_Stabilizer)
