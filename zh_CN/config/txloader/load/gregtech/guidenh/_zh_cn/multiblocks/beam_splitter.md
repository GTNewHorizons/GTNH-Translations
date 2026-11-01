---
item_ids:
  - gregtech:gt.blockmachines:3017
quest_ids:
  - RLJR8nFySzSaZLeCRsabDg==
navigation:
  title: Beam Splitter
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3017
  position: -8001
---
# Beam Splitter
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3017" />
</GameScene>
The <ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" /> is a UV tier multiblock for filtering and/or splitting particle beams. 

The Beam Splitter only supports one beam input hatch and four filtered beam output hatches, but it does not require any power or maintenance to run. 

The Beam Splitter is completely optional, but may assist with the [Beam Line](./beam_line.md) and/or the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md). Also try the [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md) and [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) before processing recipes in the [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md).

| Property | Details |
| --- | --- |
| Unlock Tier | UV |
| Structure Size (LxWxH) | 9x9x3 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:3017" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Structure
The Beam Splitter has no tiered components. The glass can be any tier and has no effect on the operation of the machine. 

The Beam Splitter can be rotated or flipped.

The Beam Splitter only supports <ItemLink id="gregtech:gt.blockmachines:3014" showIcon="left" />.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" /> | 1, Front bottom center |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 42 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 27, Edge and corner of both ends of the machine |
| <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 9 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Above controller |
| <ItemLink id="gregtech:gt.blockmachines:3014" showIcon="left" /> | 4, On the opposite side of the controller, each gap is 1 block |

### Wallsharing

Beam Splitters may wallshare each of their sides to save on casings and glass. However, it is not possible to share the beam input hatch or filtered beam output hatches due to the restrictions on their locations.

## Usage

<GameScene interactive={true} wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/beam_splitter_example_ponder.snbt" />
  <ImportPonder src="/assets/ponders/multiblocks/beam_splitter/beam_splitter_example_ponder.json" />
</GameScene>

The Beam Splitter filters and/or splits an input particle beam into 1-4 parts and never shuts down unless manually disabled. Particle beams also do not suffer any penalties or lose any energy/focus when passing through the machine. Only the rate is split evenly between all valid outputs. Fractional rates are always rounded down.

The scene on the right shows the Beam Splitter's operation with an example.

The Beam Splitter perfectly complements the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) because the latter generates many different types of particles from the same beam output hatches and it would be wasteful for those to all go to the same [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md).

There is no possible way to join particle beams together so recipes are going to be split across machines and therefore the particles should be too.

## References
- [GTNH Wiki : Beam Splitter](https://wiki.gtnewhorizons.com/wiki/Beam_Splitter)
