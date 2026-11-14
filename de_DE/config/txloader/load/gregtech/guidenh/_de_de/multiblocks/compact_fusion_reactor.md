---
item_ids:
  - gregtech:gt.blockmachines:32019
  - gregtech:gt.blockmachines:32020
  - gregtech:gt.blockmachines:32021
  - gregtech:gt.blockmachines:32022
  - gregtech:gt.blockmachines:32023
navigation:
  title: Compact Fusion Reactor
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:32019
  position: -6001
---
# Compact Fusion Reactor
<Column wrap="square" align="right" width="220">
  <ContentTabs>
    <Tab title="T1">
      <GameScene interactive={true} >
        <ImportStructureLib controller="gregtech:gt.blockmachines:32019" />
      </GameScene>
    </Tab>
    <Tab title="T2">
      <GameScene interactive={true} >
        <ImportStructureLib controller="gregtech:gt.blockmachines:32020" />
      </GameScene>
    </Tab>
    <Tab title="T3">
      <GameScene interactive={true} >
        <ImportStructureLib controller="gregtech:gt.blockmachines:32021" />
      </GameScene>
    </Tab>
    <Tab title="T4">
      <GameScene interactive={true} >
        <ImportStructureLib controller="gregtech:gt.blockmachines:32022" />
      </GameScene>
    </Tab>
    <Tab title="T5">
      <GameScene interactive={true} >
        <ImportStructureLib controller="gregtech:gt.blockmachines:32023" />
      </GameScene>
    </Tab>
  </ContentTabs>
</Column>

The <ItemLink id="gregtech:gt.blockmachines:32019" showIcon="left">Compact Fusion Reactor</ItemLink>(I\~V) is an LuV\~UEV tier multiblock for mass producing plasmas and molten rare metals from nuclear fusion. 

Unlike the regular [<ItemLink id="gregtech:gt.blockmachines:1193" showIcon="left">Fusion Reactor</ItemLink>](./fusion_reactor.md), the Compact Fusion Reactor has a built-in 64 parallels plus an additional 64 for every machine tier above the minimum recipe tier. Multi-amp and laser energy hatches are also supported to compensate for energy hatches being able to pull more than 2A of power.  Overclocks only occur when the tier of the machine exceeds the minimum recipe tier.

The Compact Fusion Reactor is not technically required for progression, but it is extremely useful for producing catalyst for the [<ItemLink id="gregtech:gt.blockmachines:1004" showIcon="left" />](./dimensionally_transcendent_plasma_forge.md) and generating power in the [<ItemLink id="gregtech:gt.blockmachines:15523" showIcon="left" />](./xl_turbo_plasma_turbine.md) or the [<ItemLink id="gregtech:gt.blockmachines:32017" showIcon="left" />](./extreme_heat_exchanger.md) with a series of [<ItemLink id="gregtech:gt.blockmachines:15519" showIcon="left" />](./xl_turbo_steam_turbines.md) behind it.

| Property | Details |
| --- | --- |
| Unlock Tier | LuV(T1) |
| ^^ | ZPM(T2) |
| ^^ | UV(T3) |
| ^^ | UHV(T4) |
| ^^ | UEV(T5) |
| Structure Size (LxWxH) | 47x47x7 |
| Power | Any Hatches allowed, includes Multi-Amp and Laser Hatches |
| Overclocks | Perfect |
| Maintenance | No maintenance needed |
| Pollution | Produces no pollution |

## Crafting and Construction
While the structure of the Compact Fusion Reactor remains the same, the types of blocks required and the minimum tier of Energy Hatches vary by tier.
<ContentTabs>
  <Tab title="T1">
    <Template 
      name="compact_fusion_reactor/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:32019"
      casingId="gregtech:gt.blockcasings:6"
      fusionCoilId="GoodGenerator:compactFusionCoil"
      frameId="gregtech:gt.blockframes:325"
      glassId="bartworks:BW_TieredGlass:3"
    />
  </Tab>
  <Tab title="T2">
    <Template 
      name="compact_fusion_reactor/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:32020"
      casingId="gregtech:gt.blockcasings4:6"
      fusionCoilId="GoodGenerator:compactFusionCoil:1"
      frameId="gregtech:gt.blockframes:328"
      glassId="bartworks:BW_TieredGlass:4"
    />
  </Tab>
  <Tab title="T3">
    <Template 
      name="compact_fusion_reactor/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:32021"
      casingId="gregtech:gt.blockcasings4:8"
      fusionCoilId="GoodGenerator:compactFusionCoil:2"
      frameId="gregtech:gt.blockframes:129"
      glassId="bartworks:BW_TieredGlass:5"
    />
  </Tab>
  <Tab title="T4">
    <Template 
      name="compact_fusion_reactor/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:32022"
      casingId="miscutils:gtplusplus.blockcasings.3:12"
      fusionCoilId="GoodGenerator:compactFusionCoil:3"
      frameId="gregtech:gt.blockframes:394"
      glassId="bartworks:BW_TieredGlass:6"
    />
  </Tab>
  <Tab title="T5">
    <Template 
      name="compact_fusion_reactor/crafting_and_construction"
      controllerId="gregtech:gt.blockmachines:32023"
      casingId="miscutils:gtplusplus.blockcasings.6"
      fusionCoilId="GoodGenerator:compactFusionCoil:4"
      frameId="gregtech:gt.blockframes:397"
      glassId="bartworks:BW_TieredGlass:7"
    />
  </Tab>
</ContentTabs>

### Wallsharing

Compact Fusion Reactors may wallshare each of their sides to save on casings, glass, frame boxes, and buses/hatches. However, that does not include any of the compact fusion coils.

> [!TIP]
> You can place <ItemLink id="appliedenergistics2:tile.BlockWirelessConnector" showIcon="left" /> and ME Cables inside the structure to connect Stocking Input Hatches or <ItemLink id="gregtech:gt.blockmachines:2713" showIcon="left" /> wallshared by two reactors.
> Right click the ME Hatches with a wire cutter to make them connectable from all directions.

## Usage

> [!NOTE]
> Read [<ItemLink id="gregtech:gt.blockmachines:1193" showIcon="left">Regular Fusion Reactor Guide</ItemLink>](./fusion_reactor.md) if you aren't familiar with how the Fusion Reactor works.
> This guide explains the Compact Fusion Reactor's unique functionality like parallel processing, high-amp energy hatches, and more.

The Compact Fusion Reactor functions the same as a regular [<ItemLink id="gregtech:gt.blockmachines:1193" showIcon="left">Fusion Reactor</ItemLink>](./fusion_reactor.md). There can be up to 32 energy hatches per machine to increase its total energy capacity and split the total power consumed. Consecutive recipes do not pay the start cost which means a lot of power can be saved by continuously running the Compact Fusion Reactor or at least increasing the size of crafting requests.

Overclocks only occur when the tier of the Compact Fusion Reactor exceeds the minimum recipe tier, similar to the regular Fusion Reactor. They have nothing to do with the tier of the energy hatches or the available power. The T2\~T3 machines run 2/2 perfect overclocks while the last two tiers run 4/4 perfect overclocks.

The Compact Fusion Reactor offers a significant number of parallels. There is a built-in 64 parallels plus an additional 64 for every machine tier above the minimum recipe tier. Furthermore, recipes that are overclocked beyond 0.05s (1 tick) multiply the total number of parallels as compensation for the capped speed. A Mk-I recipe in a Mk-V Compact Fusion Reactor can have up to 5120 parallels, for example.

The voltage of the energy hatches is irrelevant as long as it is above the minimum tier and supplies enough EU/t. However, there are potential scenarios where the energy hatches can draw more than 2A of power depending on the recipe, tier of the machine, and number of parallels/overclocks.  
The solution is switching to 4A or even 16A energy hatches in those scenarios. Laser energy hatches can also technically work but they are extreme overkill and not worth it at all, especially because the power the controller takes from each hatch is always the same; there cannot be one really high amp energy hatch to compensate for many low amp energy hatches.  

Check the table below to see each tier's Overclocks, maximum power usage, capacity required, and Minimal Requirements to run recipes universally.
| Tier | Overclocks |: Energy Hatches :|||
| --- | --- | --- | --- | --- |
| ^^ | ^^ | Min Tier | Max Power Use/Hatch | Energy Capacity/Hatch | 
| T1 | None | LuV | 65,536 EU/t (2A LuV) | 5M EU |
| T2 | 2/2 | ZPM | 524,288 EU/t (4A ZPM) | 10M EU |
| T3 | 2/2 | UV | 3,145,728 EU/t (6A UV) | 20M EU |
| T4 | 4/4 | UHV | 16,777,216 EU/t (8A UHV) | 160M EU |
| T5 | 4/4 | UEV | 83,886,080 EU/t (10A UEV) | 640M EU |
{: widths="40,50,30,,70"}

<br />

> [!WARNING]
> Reducing the number of Energy Hatches doesn't make each hatch draw more power. Each hatch always pulls <Latex formula="\text{Recipe EU/t}\div32" scale="0.6" />.
> 
> Also, unlike other multiblocks, reducing the Reactor's power throughput won't reduce the parallels or overclocks it tries to run. The Reactor will always try to operate at full capacity, even if it cannot draw the power the recipe requires.

Like other TecTech multiblocks, the Compact Fusion Reactor’s operation can be controlled via parameters; however, the only setting that can be adjusted is the batch size.  
Unlike parallels, increasing the batch size does NOT improve the throughput of the machine. It processes multiple recipes at once with longer duration, which helps to save TPS and reduce lagging.

## References
- [GTNH Wiki : Compact Fusion Reactor](https://wiki.gtnewhorizons.com/wiki/Compact_Fusion_Reactor)