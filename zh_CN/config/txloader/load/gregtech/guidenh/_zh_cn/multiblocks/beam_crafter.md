---
item_ids:
  - gregtech:gt.blockmachines:3015
quest_ids:
  - xTkeDXIZSlmRkde8LZgzLw==
navigation:
  title: Beam Crafter
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3015
  position: -8001
---
# Beam Crafter

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3015" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" /> is a UV tier multiblock that captures particle beams for crafting recipes.

If necessary, use the [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md), [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md), and/or the [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) to control the flow of particle beams following the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md).

| Property | Details |
| --- | --- |
| Unlock Tier | UV |
| Structure Size (LxWxH) | 11x17x5 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction

### Crafting

<RecipesFor id="gregtech:gt.blockmachines:3015" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

<RecipesFor id="gregtech:gt.blockcasings3:10" handlerBlacklist="bq_quest" />

<RecipesFor id="gregtech:gt.blockmachines:10503" handlerBlacklist="gt.recipe.scanner" />

### Structure

The Beam Crafter has no tiered components. The glass can be any tier and has no effect on the operation of the machine.

The Beam Crafter can be rotated or flipped.

<ItemLink id="gregtech:gt.blockmachines:2715" showIcon="left" /> and <ItemLink id="gregtech:gt.blockmachines:2714" showIcon="left" /> are incompatible with the Beam Crafter, so use regular or stocking input buses/hatches.

Multi-Amp and Laser Energy Hatches are supported, but they **do not overclock** the machine.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" /> | 1, Front center, 1st layer |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 0-225 |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 26 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 16 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 2, Center of both ends of the structure |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Can use Regular, Multi-Amp, Laser</Tooltip> | 1+, Can replace any <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Input Bus | 1+, Can replace any <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Input Hatch | 0+, Can replace any <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Output Bus | 1+, Can replace any <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Output Hatch | 0+, Can replace any <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> |

### Wallsharing

Beam Crafters may wallshare each of their sides to save on casings and glass. However, it is not possible to share the beam input hatches due to the restrictions on their locations.

## Usage
The Beam Crafter is the final step in the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) and captures one or more of the output particle beams for recipes. More specifically, it permanently buffers up to 2B of each particle type and only ever consumes them when a recipe requires them.

There is no passive decay and it does not matter which beam input hatch the particles enter through. **However, particles are only added to the buffer while the Beam Crafter is actively processing a recipe.**

Beam Crafter recipes start immediately upon receiving any valid inputs and only finish when the machine receives enough of the required particles, similar to how the [<ItemLink id="gregtech:gt.blockmachines:15331" showIcon="left" />](./research_station.md) consumes computation. Therefore, the duration of recipes is strictly determined by the rate at which particles are consumed. It could be instantaneous if there are enough particles stored in the buffer, or last forever if the collision energy of the LHC is not high enough to produce the required particles.

All available recipes are listed in the following table along with their requirements and the module(s) that can produce both particles on their own. The "None" column refers to using only a [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) to produce the required particles - no LHC necessary.

| Recipe | Tier | Particle 1 || Particle 2 || Modules |||||
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | Type | Amount | Type | Amount | None | CMS | ATLAS | ALICE | LHCb |
| <ItemLink id="miscutils:dustNeptunium238" showIcon="left" /> | EV | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="miscutils:particleBase:24" showIcon="left" />(1) | LuV | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 120 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 720 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="miscutils:particleBase:24" showIcon="left" />(64) | ^^ | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 5 | <ItemLink id="gtnhlanth:particle:6" showIcon="left" /> | 3 | &c✗ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32300" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 20 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="ExtraUtilities:unstableingot:2" showIcon="left" /> | ZPM | <ItemLink id="gtnhlanth:particle:1" showIcon="left" /> | 5 | <ItemLink id="gtnhlanth:particle:2" showIcon="left" /> | 5 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:1306" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 2 | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 2 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32301" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 20 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="miscutils:itemDustRadioactiveMineralMix" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="miscutils:MU-metaitem.01:32105" showIcon="left" /> | UV | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:11" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 3000 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 3000 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32302" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 20 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:12" showIcon="left">ATLAS Casing</ItemLink> | UHV | <ItemLink id="gtnhlanth:particle:7" showIcon="left" /> | 900 | <ItemLink id="gtnhlanth:particle:7" showIcon="left" /> | 900 | &c✗ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemImage id="bartworks:BioLabParts" nbt='tag:{Name:"Xenoxene Xenoxsis"}' label="right" format='&7Xenoxene Petri Dish' /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:13" showIcon="left">ALICE Casing</ItemLink> | UEV | <ItemLink id="gtnhlanth:particle:9" showIcon="left" /> | 450 | <ItemLink id="gtnhlanth:particle:9" showIcon="left" /> | 450 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:14" showIcon="left">LHCb Casing</ItemLink> | UIV | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 750 | <ItemLink id="gtnhlanth:particle:14" showIcon="left" /> | 750 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.01:32417" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:8" showIcon="left" /> | 50 | <ItemLink id="gtnhlanth:particle:10" showIcon="left" /> | 30 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32270" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | &c✗ | &c✗ | &c✗ | &c✗ | &a✓ |
| <ItemLink id="gregtech:gt.metaitem.03:32235" showIcon="left" /> | UMV | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:13" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32236" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:13" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32238" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32237" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32239" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 200 | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 200 | &c✗ | &c✗ | &a✓ | &c✗ | &a✓ |
| <ItemLink id="gregtech:gt.metaitem.03:32240" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 25 | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 25 | &c✗ | &c✗ | &a✓ | &c✗ | &a✓ |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:183" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 50 | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 5 | &c✗ | &c✗ | &c✗ | &c✗ | &a✓ |
{: widths="200, 30, 90, 40, 90, 40, 32, 32, 32, 32, 32"}

The CMS module only supports a few basic recipes such as the two for unknown particles. The ATLAS module supports nearly every recipe because it has such a large pool of particles, but that also makes it difficult to obtain any one in particular. The ALICE module is also quite flexible, but its pool is much smaller for more concentrated crafts. The LHCb module supports the most advanced recipes like the ZPIC wafer and stable boson containment unit, and has a higher yield of the two rarest particles.

## References

- [GTNH Wiki : Beam Crafter](https://wiki.gtnewhorizons.com/wiki/Beam_Crafter)
