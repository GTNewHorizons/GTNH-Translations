---
item_ids:
  - gregtech:gt.blockmachines:143
  - gregtech:gt.blockmachines:144
quest_ids:
  - uYT4jmFtQhOo5PoJLDyh-w==
  - b-YCbvcNT4uEjg2pN-H6jw==
navigation:
  title: Concrete Backfiller
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:143
  position: -2001
---
# Concrete Backfiller
<Row wrap="square" align="right" width="220">
  <ContentTabs background="transparent">
    <Tab title="T1">
      <GameScene interactive={true} width="0" zoom="1">
        <ImportStructureLib name="main" controller="gregtech:gt.blockmachines:143" />
      </GameScene>
    </Tab>
    <Tab title="T2">
      <GameScene interactive={true} width="0" zoom="1">
        <ImportStructureLib name="main" controller="gregtech:gt.blockmachines:144" />
      </GameScene>
    </Tab>
  </ContentTabs>
</Row>

The <ItemLink id="gregtech:gt.blockmachines:143" showIcon="left" /> is an MV tier multiblock for filling in the area below it with light concrete to seal any air gaps where mobs could spawn. 

The Concrete Backfiller is available in two tiers to further increase its range. Filled concrete will prevent mobs from spawning underground. If you want to prevent mobs from spawning around your base, use this machine or move bases to the [<ItemLink id="personalspace:personalPortal" showIcon="left">Personal Dimension</ItemLink>](/dimensions/personal_dimension.md).

| Property | Details |
| --- | --- |
| Unlock Tier | MV(T1) |
| ^^ | EV(T2) |
| Structure Size (LxWxH) | 3x3x7 |
| Power | Regular |
| Overclocks | Imperfect |
| Maintenance | Need Maintenance |
| Pollution | Produces no pollution |

## Crafting and Construction
<ContentTabs background="transparent">
  <Tab title="T1">
    <Template 
      name="concrete_backfiller/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:143"
      casingId="gregtech:gt.blockcasings2"
      frameId="gregtech:gt.blockframes:305"
      tier="MV"
    />
  </Tab>
  <Tab title="T2">
    <Template 
      name="concrete_backfiller/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:144"
      casingId="gregtech:gt.blockcasings4:2"
      frameId="gregtech:gt.blockframes:28"
      tier="EV"
    />
  </Tab>
</ContentTabs>

### Wallshare
The Concrete Backfiller can wallshare, although it is not meaningful since wallsharing makes most of the machines' working areas overlap.

## Usage
The Concrete Backfiller slowly fills in the area below it with <ItemLink id="gregtech:gt.blockconcretes:8" showIcon="left"/> to seal any air gaps where mobs could spawn. The Concrete Backfiller does NOT break or replace blocks and does NOT stop when it reaches a wall. Liquids (i.e. water and lava) can either be skipped or filled based on the liquid filling setting<FloatingImage src="gregtech:textures/gui/overlay_button/LiquidMode.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> in the GUI of the controller. Each block of light concrete consumes 144L of wet concrete from the input hatch.

The vertical range of the Concrete Backfiller is from bedrock to the layer just below the machine. The horizontal range is square despite being listed as a radius and depends on the tier of the machine. The T1 machine's radius is 16 blocks (33x33), and the T2 machine's radius is 64 blocks (129x129). The fill area is centered on the controller rather than being perfectly chunk-aligned like the [<ItemLink id="gregtech:gt.blockmachines:1157" showIcon="left" />](./fluid_drilling_rig.md).

The filling speed depends on the supplied voltage, as seen in the table below. Exceeding the minimum voltage tier applies imperfect overclocks which consume 4x the power for 2x the speed. There is no benefit to exceeding UV power since the machine cannot go faster than 1 block per tick. The power consumption is always 0.75A of the supplied voltage.

| Voltage | MV | HV | EV | IV | LuV | ZPM | UV+ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Seconds per Block | 3.00 | 1.50 | 0.75 | 0.40 | 0.20 | 0.10 | 0.05 |
{: widths="100,"}

When first enabled, the Concrete Backfiller deploys its mining pipes from the center of the machine straight down to bedrock. This can take a few seconds depending on the current y-level of the machine and voids any blocks in the way. If necessary, press the "abort and retract mining pipes" button<FloatingImage src="gregtech:textures/gui/overlay_button/retract_pipes.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> inside the GUI of the controller to immediately stop the process. Supply mining pipes through an input bus and retrieve them from an output bus, or just use the slot inside the controller.

## References
- [GTNH Wiki : Concrete Backfiller](https://wiki.gtnewhorizons.com/wiki/Concrete_Backfiller)