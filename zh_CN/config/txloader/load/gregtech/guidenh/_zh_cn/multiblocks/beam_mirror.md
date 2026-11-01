---
item_ids:
  - gregtech:gt.blockmachines:3016
quest_ids:
  - _xupoCqbT52qN_3zQonWNg==
navigation:
  title: Beam Mirror
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3016
  position: -8001
---
# Beam Mirror
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3016" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" /> is a UV tier multiblock for bending particle beams at 90° or 180° angles. 

The Beam Mirror only supports one beam input hatch and one beam output hatch, but it does not require any power or maintenance to run. Particle beams also do not suffer any penalties or lose any of their stats when passing through the machine. 

The Beam Mirror is completely optional, but may assist with the [Beam Line](./beam_line.md) and/or the [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md). Check the [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) and [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) to modify beams before processing recipes in the [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md).

| Property | Details |
| --- | --- |
| Unlock Tier | UV |
| Structure Size (LxWxH) | 5x3x5 (90°) |
| ^^ | 5x3x6 (180°) |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
### Crafting
<RecipesFor id="gregtech:gt.blockmachines:3016" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Structure
The Beam Mirror has no tiered components. 

The glass can be any tier and has no effect on the operation of the machine. 

The Beam Mirror can be rotated or flipped.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to visualize/build the structure with subchannel "glass" to specify the tier of the glass and the projector stack size to specify the angle (1 for 90°, and 2 for 180°).

<ContentTabs>
  <Tab title="90° Structure">
  | Component | Quantity and placement |
  | --- | --- |
  | <ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" /> | 1, Front bottom center |
  | <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 31 |
  | <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 9, Cover both ends of the machine |
  | <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 5 |
  | <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Above controller |
  | <ItemImage id="gregtech:gt.blockmachines:10504" noTooltip /><Tooltip label="Beam Output Hatch">Normal/Filtered both supported</Tooltip> | 1, Top of the side opposite the controller, must be rotated so its back faces the glass |
  </Tab>

  <Tab title="180° Structure">
  | Component | Quantity and placement |
  | --- | --- |
  | <ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" /> | 1, Front bottom center |
  | <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 52 |
  | <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 9, Cover both ends of the machine |
  | <ItemImage id="bartworks:BW_TieredGlass" />Any Tiered Glass | 8 |
  | <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Above controller |
  | <ItemImage id="gregtech:gt.blockmachines:10504" noTooltip /><Tooltip label="Beam Output Hatch">Normal/Filtered both supported</Tooltip> | 1, Top of the side opposite the controller, must be rotated so its back faces the glass |
  </Tab>
</ContentTabs>


### Wallshare

Beam Mirrors may wallshare each of their sides to save on casings. Sharing is useful for bending the outputs of the [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) because the beam output hatches are so close together.

## References

- [GTNH Wiki : Beam Mirror](https://wiki.gtnewhorizons.com/wiki/Beam_Mirror)
