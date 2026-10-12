---
item_ids:
  - gregtech:gt.blockmachines:1172
navigation:
  title: Cleanroom
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1172
  position: 12
quest_ids:
  - AAAAAAAAAAAAAAAAAAADrA
---

# Cleanroom

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1172" tier={2} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" /> is a multiblock facility available in HV. It provides a clean environment for machines placed inside it, enabling recipes for more advanced or less expensive circuits, circuit boards, and other products.

The Cleanroom itself does not take processing ingredients or output products. Place the actual processing machines inside, supply them with their own power, and arrange their item and fluid I/O. The Cleanroom's Energy Hatch only powers the environment.

| Property | Details |
| --- | --- |
| Unlock tier | HV; the Cleanroom can be maintained with LV power |
| Dimensions | External width and length of 3–15 blocks each, height of 4–15 blocks; a rectangular footprint is allowed |
| First build | 5×5×5, providing a usable interior of 3×3×3 |
| Power | Exactly one ordinary Energy Hatch; an LV Energy Hatch can accept 2A |
| Cleanness | Gradually rises from 0% to 100%; below 100%, item outputs from recipes requiring a Cleanroom may be lost |
| Overclocking and bonuses | Upgrading the Energy Hatch speeds up cleaning; it grants no extra speed, parallels, or power discount to machines inside |
| Maintenance and pollution | Requires one Maintenance Hatch; each maintenance issue lowers maximum cleanness by 10 percentage points; no pollution may be generated inside |

> [!WARNING]
> **Wait for 100% cleanness before supplying ingredients for recipes that require a Cleanroom.** Below 100%, a machine may consume the ingredients and run the recipe normally, yet lose an item output.

## Crafting and Construction

The current recipes for the controller, Plascrete Blocks, and Filter Machine Casings are shown below.

<RecipesFor id="gregtech:gt.blockmachines:1172" />

<RecipesFor id="gregtech:gt.blockreinforced:2" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

### Your First 5×5×5 Cleanroom

These dimensions include the walls, floor, and ceiling, leaving a 3×3×3 interior. Complete the shell and power supply first, then add access and transport ports as needed.

| Component | Basic quantity and position |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" /> | One, at the center of the ceiling; the controller must face horizontally, never up or down |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | Eight, filling the rest of the ceiling's inner area |
| <ItemLink id="gregtech:gt.blockreinforced:2" showIcon="left" /> | 87, forming the floor, walls, and ceiling perimeter; this count already accounts for the two required hatches |
| Energy Hatch | Exactly one, replacing a Plascrete Block |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | Exactly one, replacing a Plascrete Block |

The preview above shows the shell. When building, replace two Plascrete Blocks with the Energy Hatch and Maintenance Hatch. Each additional valid transport port or glass block replaces one more Plascrete Block.

Build in the following order:

1. Lay a solid 5×5 floor and build the four walls, reserving positions for power, maintenance, and access.
2. Build the ceiling perimeter with Plascrete Blocks. Place the controller in the center and the eight Filter Machine Casings in the remaining inner positions.
3. Install the Energy Hatch and Maintenance Hatch, then close all remaining gaps.
4. Place processing machines, cables, and pipes within the walls, above the floor, and below the filters. Processing machines cannot replace wall blocks.
5. Check the structure, fix all maintenance issues, connect a stable power supply, and wait for 100% cleanness.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Before expanding, stop production and ingredient input. Check and clean the rebuilt room before resuming processing.

### Expansion and Casing Replacements

The footprint may be rectangular. Keep the controller at the center of the ceiling and fill every other position inside the ceiling perimeter with Filter Machine Casings. If the width or length is even, either middle position along that axis is valid. If both are even, there are four possible central positions.

The default configuration requires **at least 20 actual Plascrete Blocks** and limits replacements with other valid blocks. The replacement share is calculated as “replacement blocks ÷ (Plascrete Blocks + replacement blocks)”; its percentage is rounded down to an integer and must not exceed **30%**. Filters and the controller are excluded from this calculation. Energy and Maintenance Hatches, doors, glass, and transport ports all count as replacements.

| Replacement | Placement rules |
| --- | --- |
| Ordinary Energy Hatch and Maintenance Hatch | Plascrete positions; exactly one of each |
| GT Machine Hulls and Cable Diodes | Plascrete positions; used for transport through the shell |
| Valid glass | Plascrete positions; ordinary vanilla glass is invalid |
| IC2 Reinforced Door | Side walls, away from vertical edges and corners; not in the floor or ceiling |
| OpenBlocks Elevators and Ender IO Travel Anchors | Plascrete positions, including the floor |

EV and higher tier glass is accepted. The pack's default configuration also allows specific blocks such as BartWorks tiered glass, including HV glass. Therefore, not every valid glass needs to be EV, and not every decorative glass is a valid replacement.

The Cleanroom does not need Input Buses, Output Buses, fluid hatches, or a Muffler Hatch, and these cannot replace its wall blocks. Deliver items and fluids to the processing machines' own interfaces inside.

Extra Utilities' <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> is recommended as a doorway, allowing players to pass through without reducing cleanness.

## Uses and First Startup

**Some recipes** in Circuit Assemblers, Laser Engravers, Assembling Machines, Cutting Machines, and Autoclaves require a clean environment. Check the individual recipe's “Requires Cleanroom” note in NEI.

Before the first startup, switch off the processing machines or hold back their ingredients, then prepare the room:

1. Confirm that the controller reports a complete structure with the correct hatch counts.
2. Fix all six maintenance issues. See [Multiblock Machines: Maintenance](./multiblocks_index.md#maintenance).
3. Close the doors and make sure no equipment inside generates pollution.
4. Supply the Cleanroom continuously and watch its cleanness rise.
5. At 100%, connect each processing machine to its own power supply and insert the ingredients to start processing.

Ordinary GT singleblock machines can start recipes requiring a Cleanroom once cleanness is above 0%, but their outputs are not guaranteed safe. Item loss due to insufficient cleanness is decided **when the recipe starts and consumes its ingredients**. Reaching 100% halfway through processing cannot recover an output already selected for loss.

100% cleanness only removes losses caused by the environment. A recipe with inherently probabilistic outputs still uses the chances shown in NEI.

Some later multiblocks, such as the Large Chemical Reactor and Hyper-Intensity Laser Engraver, do not need to be placed in a Cleanroom. **All multiblock machines have a built-in cleanroom environment.**

## Cleanness and Power

HV is the controller's unlock tier, not the minimum power tier. With an LV Energy Hatch, the Cleanroom initially consumes **40 EU/t**. Consumption gradually decreases as cleanness rises, reaching **4 EU/t** at 100%.

40 EU/t exceeds the rated output of one LV generator, but the Cleanroom's LV Energy Hatch can accept 2A. For a first build, use two LV generators or another LV supply that can continuously provide enough power, with cabling rated for the current. A single 32 EU/t LV generator cannot clean the room from 0% on its own. Account for cable losses as well.

The following example assumes an **external height of five blocks, no maintenance issues, closed doors, and cleaning from 0% to 100%**. Times assume normal operation at 20 TPS.

| Energy Hatch tier | Startup consumption | Consumption at 100% | Approximate cleaning time |
| --- | --- | --- | --- |
| LV | 40 EU/t | 4 EU/t | 15 minutes |
| MV | 40 EU/t | 4 EU/t | 15 minutes |
| HV | 160 EU/t | 16 EU/t | 7 minutes 30 seconds |
| EV | 640 EU/t | 64 EU/t | 3 minutes 45 seconds |

MV does not clean faster than LV. Starting at HV, standard lossy overclocking multiplies power by four and halves cleaning time per overclock. Taller rooms take longer to clean; increasing only width or length does not lengthen a cleaning cycle.

**Power the Cleanroom and its processing machines separately.** The Cleanroom's Energy Hatch tier does not limit the voltage of machines inside or grant them overclocking bonuses. Add the Cleanroom's consumption to that of all processing machines when sizing the power supply.

Keep the room running after reaching 100%. Do not switch it off to save its idle power. After a shutdown, power failure, or broken structure, restore the environment and confirm 100% cleanness before resuming processing.

## Access, Power, and Transport Through the Walls

### Access

An IC2 Reinforced Door provides access. When an open door is detected, the Cleanroom continuously loses cleanness, normally two percentage points every five seconds. Close doors after use. For frequent access, use Extra Utilities' <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> to avoid repeatedly opening a door.

Wooden doors, vanilla iron doors, holes, and ordinary pipes are not valid Cleanroom wall blocks. Do not leave a gap for power cables or ME cables.

### Power Through the Walls

Embed a **GT Machine Hull** or **Cable Diode** of the appropriate tier in the wall, connecting the external power supply to the internal machine cables. For example, an <ItemLink id="gregtech:gt.blockmachines:13" showIcon="left" /> can carry HV power through the wall.

A Machine Hull outputs power through its front face and accepts power from its other faces. Face its output inward and connect the cables on both sides. For higher current, use a suitably rated Cable Diode and check the current capacity of both cable runs.

> [!WARNING]
> When upgrading the voltage supplied to internal machines, also check the Machine Hulls, Cable Diodes, and cables in the wall. Connecting higher-tier power to an old lower-tier port causes an overvoltage explosion. An unpowered hull used only for item transport does not need upgrading with the machine's voltage.

### Items and Fluids

GT Machine Hulls have an item slot and a fluid buffer, allowing them to serve as transfer containers through the wall. Use pipes or Conveyor Modules on either side to insert into and extract from this buffer, then deliver to the internal machines. The hull does not process recipes or automatically distribute everything to the intended machines.

Use separate ports for ingredients, products, and different fluids where practical, so unwanted materials cannot fill a shared small buffer. Configure the processing machines' input faces, output faces, and automatic output separately; a hull in the wall does not replace those settings.

With AE2, establish a link using <ItemLink id="appliedenergistics2:tile.BlockWirelessConnector" showIcon="left" />s inside and outside the room, then connect the internal ME Interfaces, buses, and other devices. Wireless Connectors do not occupy wall positions, leaving more room in the casing replacement allowance.

Powering the ME network does not supply GT EU to its processing machines. Provide machine power through Machine Hulls, Cable Diodes, or a separately configured GT EU P2P setup.

## Maintenance, Pollution, and Monitoring

Each unresolved maintenance issue lowers maximum cleanness by **10 percentage points**. One issue caps it at 90%, and two at 80%. The Cleanroom may still run, but it cannot reach a safe 100%. After repairs, wait for cleanness to recover before resuming recipes that require the environment.

> [!WARNING]
> Do not put polluting generators or other polluting equipment inside the Cleanroom. Pollution from a machine inside resets cleanness to zero and triggers all six maintenance issues, stopping the Cleanroom. A Muffler Hatch cannot fix this. Move the pollution source outside, then repair, restart, and clean the room again.

Use the controller GUI and Waila to check cleanness, maintenance, and operation. An Industrial Information Panel or a Needs Maintenance Cover connected to a light or alarm can help monitor maintenance issues. Having no maintenance issues does not mean cleanness is already 100%; check the environment after opening doors, power failures, or restarting.

The controller also emits a redstone signal on every side reflecting cleanness. **100% corresponds to signal strength 15.** To control ingredient input automatically, check for strength 15. Any nonzero signal is insufficient, since low cleanness can also produce a signal. Structure checks and redstone updates have a delay, so keep doors closed, power stable, and maintenance resolved alongside any interlock.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | External dimensions, a central ceiling controller facing horizontally, filters throughout the inner ceiling, and fully enclosed walls and floor |
| Wrong hatch count | Exactly one ordinary Energy Hatch and one Maintenance Hatch; no Input Buses, fluid hatches, or Muffler Hatch in the shell |
| Room fails to form after adding glass or ports | Whether the replacements are valid, at least 20 Plascrete Blocks remain, and all replacements together satisfy the percentage limit |
| Immediate shutdown with LV power | Whether only one 32 EU/t generator is connected; sufficient sustained startup power, cable current capacity, cable losses, and energy buffer |
| MV power does not speed up cleaning | MV has no cleaning overclock; faster cleaning starts at HV. Upgrade the Energy Hatch and supply cabling before raising voltage |
| Cleanness stays at 90% or 80% | Unresolved maintenance issues; if cleanness keeps falling, also check for open Reinforced Doors |
| Ingredients consumed but an item output is missing | Whether cleanness was 100% when the recipe started; then check inherent output chances and the machine's output configuration |
| Internal machine still requires a Cleanroom | Whether it is fully inside, the Cleanroom is formed with cleanness above 0%, and a structure check has occurred since placement or expansion |
| Cleanroom runs but an internal machine does not | Separate machine power, voltage, ingredients, fluids, Integrated Circuit configuration, and output space |
| Cleanness suddenly resets with all maintenance issues | Find and remove an internal pollution source, repair maintenance, and restart; hold back processing ingredients |

See [Multiblock Machines](./multiblocks_index.md) for general tool controls, maintenance, and power failure guidance.

## References

- [GTNH Wiki: Cleanroom](https://wiki.gtnewhorizons.com/wiki/Cleanroom)