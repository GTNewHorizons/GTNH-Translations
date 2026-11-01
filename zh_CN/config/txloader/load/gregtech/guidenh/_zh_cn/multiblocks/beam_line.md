---
navigation:
  title: Beam Line
  parent: ./multiblocks_index.md
  icon: gtnhlanth:particle:5
  position: -7001
---
# Beam Line
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/beamline.snbt" />
</GameScene>

The **Beam Line** is a series of four ZPM tier multiblocks chained together that engraves wafers with a photon beam and ultra precise masks.

The line begins with the [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) which generates a particle beam from one of seven different source materials.  
The [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">Linear Accelerator (LINAC)</ItemLink>](./linear_accelerator.md) then accelerates the particle beam to increase its total energy at the cost of focus.  
The [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md) accelerates the particle beam even more until it produces a photon beam from the radiation of the high speed particles.  
The [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md) captures the photon beam and carefully focuses it onto wafers to engrave them. 

Each multiblock requires its own power but most of it should be concentrated into the Synchrotron to increase the processing speed of the final recipe. The only other input is coolant for the LINAC and Synchrotron which both perfectly recycle it into hot coolant.

Beam Line can be an alternative method for wafer engraving. Compared with [<ItemLink id="gregtech:gt.blockmachines:3004" showIcon="left">Hyper Intensity Laser Engraver (HILE)</ItemLink>](./hyper_intensity_laser_engraver.md), Beam Line offers advantages such as the ability to perform serious overclocking using Multi-Amp/Laser Hatches from the point of construction (while HILE can do this on UEV+) and eliminating the need for intermediate processes like [<ItemLink id="gregtech:gt.blockmachines:1169" showIcon="left">Large Chemical Reactor (LCR)</ItemLink>](./large_chemical_reactor.md), but it requires a large amount of material to build, and to produce all wafers, a total of **5** distinct Beam Line multiblocks must be constructed. In addition, while it can save indium and sunnarium by bypassing the LCR, it uses borax and lanthanum as materials instead.

| Property | Details |
| --- | --- |
| Unlock Tier | ZPM |
| Structure Size (LxWxH) | Varies |
| Power | Varies |
| Overclocks | Varies |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction

You can check each multiblock's documents to see how to craft and construct the Beam Line multiblocks.
- [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md)
- [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left" />](./linear_accelerator.md)
- [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md)
- [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)

### Crafting

Beam Line requires <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:10504" showIcon="left" /> and <ItemLink id="gregtech:gt.blockmachines:10502" showIcon="left" /> to connect between different Beam Line multiblocks.

<RecipesFor id="gregtech:gt.blockmachines:10503" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gregtech:gt.blockmachines:10504" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gregtech:gt.blockmachines:10502" handlerBlacklist="bq_quest" />

### Structure
Connect the 4 multiblocks in order by using <ItemLink id="gregtech:gt.blockmachines:10502" showIcon="left" /> to make the Beam Line work. Pipes do not need to be colored but they cannot cross or bend.

1. [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left" />](./linear_accelerator.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)

> [!WARNING]
> ALL Beam Line multiblocks require <ItemLink id="bartworks:BW_TieredGlass:3" showIcon="left">LuV+ Tier Glass Block</ItemLink> to operate.

Optionally, you can use the [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md), [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md), and/or [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) on UV+ to redirect or optimize the particle beam as necessary. They really only assist with the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) but they are fully compatible with the Beam Line as well.

## Usage

### Recipes

<RecipeUsage id="gregtech:gt.blockmachines:10508" handlerId="gtnhlanth.recipe.tc" wrap="square" align="right" />

Beam Line (more precisely, the [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)) recipes in NEI have only a photon, a mask, and doped wafers as input and engraved wafers as output. However, the photon is symbolic and not an actual item or input for the recipe. It is only there to establish that the final particle beam must specifically be a photon beam, not an electron beam or anything else. 

There are also a few extra requirements listed at the bottom of the recipe concerning the characteristics of the particle beam. The energy must be within a particular range, the focus must be greater than or equal to a certain value, and the base amount or rate determines the processing speed of the recipe.

To process the recipe, you must manage Beam Line multiblocks to meet the requirements that recipe demands.

#### Workflow
The general workflow for processing Beam Line recipes is listed below and explained in much more intricate detail in the following subsections about each of the individual multiblocks. 

1. The [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) sets the initial stats of the particle beam based on the input or source material and the voltage of the machine. Check the machine's guide for more details about the particles that each material can create.  
  &b✓ Energy  &b✓ Focus  &b✓ Rate
1. The [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">Linear Accelerator (LINAC)</ItemLink>](./linear_accelerator.md) accelerates the particle beam to boost its overall energy at the cost of focus.  
  Increase the length of the LINAC or give it more power to strengthen the effect and reach higher energy levels.  
  Supply cooling fluids to preserve the focus as much as possible in the process. The cooling fluid is returned in a heated state and can be recycled after proper treatment.  
  &a↑ Energy  &c↓ Focus  &7→ Rate
1. The [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md) accelerates the particle beam again until it produces a photon beam from the radiation of the high speed particles.  
  Upgrade the antenna casings to keep the beam energy high and increase the beam rate more efficiently.  
  Supply cooling fluids to again preserve the focus as much as possible in the process. The cooling fluid is returned in a heated state and can be recycled after proper treatment.  
  Increasing the power supply increases the rate of the beam without decreasing its energy and focus, which makes the Beam Line easily upgradeable by only increasing the tier and throughput of the Synchrotron's Energy Hatches.  
  Upgrading the Synchrotron's energy hatches is the only way to increase the beam's rate, which determines recipe processing times.  
  &c↓ Energy  &c↓ Focus  &a↑ Rate
1. The [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md) captures the final photon beam and does the actual laser engraving.  
  The Target Chamber does not change any of the characteristics of the beam after it leaves the Synchrotron. It only checks that the beam energy and beam focus meet any recipe requirements and uses the beam rate to determine the duration of the recipe. 

### Craftable Wafers
The wide range of beam energy, focus, and rate requirements means that a single Beam Line is not enough for all possible recipes. 

At a minimum, there must be five Beam Lines with varying [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">LINAC</ItemLink>](./linear_accelerator.md) lengths, energy hatches, and coolant. The following table lists the recipes that the Beam Line can process, by group.

| Output By Group || Min Power | Beam Energy || Min Focus |
| --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | Min | Max | ^^ |
| 1 | <ItemLink id="gregtech:gt.metaitem.03:32036" showIcon="left" /> | 1,920 EU/t (EV) | 0.5 eV | 4 eV | 35 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32038" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 40 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32060" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 25 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32062" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 30 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32064" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 30 |
| 2 | <ItemLink id="gregtech:gt.metaitem.03:32046" showIcon="left" /> | 1,920 EU/t (EV) | 3 eV | 10 eV | 45 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32056" showIcon="left" /> | 1,920 EU/t (EV) | 3 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32054" showIcon="left" /> | 1,920 EU/t (EV) | 5 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32050" showIcon="left" /> | 1,920 EU/t (EV) | 5 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32044" showIcon="left" /> | 1,920 EU/t (EV) | 6 eV | 12 eV | 45 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32040" showIcon="left" /> | 1,920 EU/t (EV) | 7 eV | 12 eV | 40 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32042" showIcon="left" /> | 1,920 EU/t (EV) | 8 eV | 10 eV | 40 |
| 3 | <ItemLink id="gregtech:gt.metaitem.03:32048" showIcon="left" /> | 1,920 EU/t (EV) | 100 eV | 200 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32052" showIcon="left" /> | 1,920 EU/t (EV) | 100 eV | 200 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32058" showIcon="left" /> | 1,920 EU/t (EV) | 190 eV | 200 eV | 50 |
| 4 | <ItemLink id="gregtech:gt.metaitem.01:32714" showIcon="left" /> | 30,720 EU/t (LuV) | 1,000 eV | 3,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32160" showIcon="left" /> | 1,920 EU/t (EV) | 1,000 eV | 4,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32070" showIcon="left" /> | 30,720 EU/t (LuV) | 1,000 eV | 3,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32071" showIcon="left" /> | 30,720 EU/t (LuV) | 2,000 eV | 7,000 eV | 50 |
| 5 | <ItemLink id="gregtech:gt.metaitem.03:32162" showIcon="left" /> | 1,920 EU/t (EV) | 1,500 eV | 10,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32164" showIcon="left" /> | 1,920 EU/t (EV) | 3,200 eV | 9,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32266" showIcon="left" /> | 1,920 EU/t (EV) | 6,000 eV | 14,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32068" showIcon="left" /> | 30,720 EU/t (LuV) | 3,000 eV | 9,000 eV | 55 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.01:32668" showIcon="left" /> | 30,720 EU/t (LuV) | 5,000 eV | 12,000 eV | 60 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32071" showIcon="left">Crystal SoC (Ce:LuAG)</ItemLink> | 30,720 EU/t (LuV) | 5,000 eV | 12,000 eV | 60 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32068" showIcon="left">Raw Advanced Crystal Chip (Ce:LuAG)</ItemLink> | 30,720 EU/t (LuV) | 6,000 eV | 14,000 eV | 70 |
{: widths="10, 300, 110, 65, 65, 50"}

As you can see - there are 5 groups for processing, organized by their energy range:
- Group 1 (2-4 eV)
- Group 2 (8-10 eV)
- Group 3 (190-200 eV)
- Group 4 (2,000-3,000 eV)
- Group 5 (6,000-9,000 eV)

Upgrade only the energy hatches on the Synchrotron to scale the throughput of the Beam Lines. Most of the other variables are designed specifically to stay within a particular energy range or above a minimum focus.  
The voltage of the Target Chamber is simply a minimum requirement that has no effect on the operation of the machine, since it does not increase the beam's rate, only its energy.

> [!TIP]
> You may have noticed, but <ItemLink id="gregtech:gt.metaitem.03:32046" showIcon="left" /> and <ItemLink id="gregtech:gt.metaitem.03:32056" showIcon="left" /> from Group 2 can also be included in Group 1, if Group 1's energy is larger than 3 eV! Just keep an eye on minimal focus requirements.

## References
- [GTNH Wiki : Beam Line](https://wiki.gtnewhorizons.com/wiki/Beam_Line)
