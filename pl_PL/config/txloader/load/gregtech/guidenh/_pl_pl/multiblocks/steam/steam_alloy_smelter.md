---
item_ids:
  - gregtech:gt.blockmachines:31086
navigation:
  title: Steam Fuser
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31086
  position: 8
quest_ids:
  - WGhhKERfRTiJXKZEPoRf1Q
---

# Steam Fuser

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" /> is a multiblock Alloy Smelter available in the Steam age. It uses steam to make alloys in batches and process eligible molding recipes. As an upgrade to the singleblock Steam Alloy Smelter, it can process up to eight copies of the same recipe at once, producing Bronze, Red Alloy, Brass, and other materials.

The machine has basic bronze and high pressure steel structures that share the same controller. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier. The machine runs on steam and does not need coal or other fuel, heating coils, or a furnace temperature setting.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires a Tumbaga Frame Box, Bronze Fluid Pipes, Blast Furnaces, and other materials |
| Dimensions | Three blocks wide, four blocks deep, and three blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Alloy Smelter recipes at LV or below, requiring no more than 32 EU/t |
| Item interfaces | At least one steam Input Bus and one steam Output Bus; ordinary electric machine item buses cannot replace them |
| Fluid interfaces | Only a Steam Hatch is needed for power; ordinary Input and Output Hatches are not accepted |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing duration | Approximately 1.6 times the duration shown in NEI for the basic structure, or 0.8 times for high pressure |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31086" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, and one Output Bus. The basic structure uses Bronze Plated Bricks and Bronze Pipe Casings, while the high pressure structure uses their steel counterparts. **The casings and Pipe Casings in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 26 in the basic setup; may be replaced with the hatch or buses below, but at least 25 actual casings must remain |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Two, along the center of the second layer, directly behind the controller |
| Glass | <ItemLink id="minecraft:glass" showIcon="left" /> or other supported glass | Existing glass can be reused | Four: one on the left and one on the right of each Pipe Casing |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |

The structure has 29 positions for casings or hatches. Installing the three required interfaces leaves 26 casings. At most one more casing can be replaced with an additional steam Input or Output Bus; adding more interfaces would leave fewer than 25 casings. Hatches and buses cannot replace glass or Pipe Casings.

The bottom and top layers are complete 3×4 planes. From front to back, the second layer consists of "casing, controller, casing", "glass, pipe, glass", "glass, pipe, glass", and a row of three casings. Place the hatch and buses in casing positions.

> [!NOTE]
> Ordinary Glass works in this machine. You do not need to obtain Boron just because the projection shows Borosilicate Glass. Glass does not need to match the bronze or steel structure tier, and can be kept when upgrading to high pressure.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Machine Uses

The Steam Fuser uses the **Alloy Smelter recipe map**, shown as **Alloy Smelter** in English NEI. When checking NEI, confirm that the recipe belongs to the Alloy Smelter, then check the input forms, ratios, recipe tier, and required mold.

| Use | Common recipes and considerations |
| --- | --- |
| Common alloys | Copper and Tin make Bronze; Copper and Zinc make Brass. Use the ingot, dust, or other input forms shown in NEI. |
| Circuit and wire materials | Copper and Redstone make Red Alloy; Silver and Electrotine make Blue Alloy |
| Other low voltage alloys | Gold and Silver make Electrum, Lead and Antimony make Battery Alloy, and Tin and Antimony make Soldering Alloy; check NEI for the exact ratios |
| Rubber processing | Raw Rubber Dust and Sulfur Dust make Rubber Bars for further rubber products |
| Molding | Uses the corresponding mold in eligible recipes to make metal nuggets, ingots, gears, item casings, and other parts; check NEI for the mold and material quantities |

Alloy recipes directly produce alloy ingots, without first mixing alloy dust and smelting it. However, the machine does not accept every Furnace or Electric Blast Furnace recipe. Use the [Steam Hearth](./steam_hearth.md) for ordinary smelting, and the appropriate machine for recipes requiring a blast furnace temperature or higher voltage.

> [!NOTE]
> The machine is available in the Steam age, but only accepts recipes up to LV. The high pressure steel structure raises the machine's structure tier. It does not enable MV or higher recipes. Check the specific recipe's EU/t rather than judging compatibility by the material name alone.

### Input Ratios and Bronze Production

A common Bronze recipe uses **three Copper Ingots and one Tin Ingot to produce four Bronze Ingots**. Recipes using the corresponding dusts or a mixture of ingots and dusts are also available. Choose input forms according to NEI; do not substitute Tiny Piles of Dust, Small Piles of Dust, or metal nuggets using the ingot quantities.

Alloys do not all use the same input ratio. For example, Red Alloy uses Copper and Redstone, while Soldering Alloy uses Tin and Antimony. Check NEI again when changing materials instead of reusing the Bronze ratio.

### Molds and Material Shaping

Some Alloy Smelter recipes require a mold. Place the mold specified in NEI and the material together in the steam Input Bus. Molds marked as not consumed by the recipe remain available for reuse; eight parallels do not require eight molds.

Alloy Smelter molds and Extruder Shapes are different items. Even if their icons or target shapes look similar, use the mold specified by the Alloy Smelter recipe. A mold only shapes materials accepted by that recipe; it does not let the machine process higher voltage recipes.

For continuous production of one part, reserve an input slot for the mold and configure transfer equipment to replenish only the consumed materials. Before changing molds, stop supplying materials, wait for the current operation to finish, and clear leftover inputs to avoid running another molding recipe.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and steam Output Bus are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Check the input forms, ratios, and recipe tier in NEI; insert the corresponding mold if required.
4. Leave space for the output and start the machine with a small amount of material.
5. Watch the input ratios, steam buffer, and output route. Increase parallels after confirming a continuous steam supply.

## Steam Supply and Throughput

The Steam Fuser can process up to eight copies of **the same recipe** at once. This does not mean it can run eight different alloy recipes in one cycle, or that a cycle consumes only eight items. Actual parallels also depend on the quantity of each input, output space, and the parallel limit set in the GUI.

The basic structure takes approximately 1.6 times the recipe duration shown in NEI, while the high pressure structure takes approximately 0.8 times. For example, a Bronze recipe shown as ten seconds takes about 16 seconds in the basic structure or eight seconds at high pressure. With eight parallels, that cycle produces 32 Bronze Ingots; its duration is not divided by eight again.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
| Maximum parallels | 8 | 8 |
| Processing duration relative to NEI | Approximately 1.6× | Approximately 0.8× |
| Steam consumption rate for the same recipe and parallel count | 1× | 2× |
| Total steam consumption per recipe | Baseline | Approximately the same as the basic structure |
| Inputs and outputs per recipe | As shown in NEI | Same as the basic structure |

The basic structure runs at 125% of a singleblock bronze Steam Alloy Smelter's speed and 62.5% of its steam consumption rate per parallel. Its total steam consumption for the same recipe is approximately 50% of the singleblock machine's. However, running more parallels still increases the whole machine's steam consumption rate, so a supply sized for one singleblock machine is not enough for production at maximum parallels.

The high pressure upgrade increases speed and steam consumption rate together. It mainly improves throughput, with approximately the same total steam consumption per recipe as the basic structure. Actual duration and steam consumption are also affected by tick and integer rounding.

The Steam Hatch buffers 64,000 L of steam, but this only covers temporary shortfalls and cannot replace continuous boiler production. Size boilers and pipes for the **steam consumption rate while processing**. When several machines share a pipe, also account for the actual flow reaching each machine.

Use Waila to check the operating steam consumption rate and watch whether the buffer keeps falling during continuous processing. If a value is shown in L/t, multiply by 20 to get L/s at the normal 20 TPS. Use matching units when comparing pipe throughput. If steam supply is insufficient, lower the parallel limit in the GUI, then increase boiler production or improve the piping.

> [!WARNING]
> Running out of steam during processing aborts the current operation, and materials already consumed are not returned. Check steam production and pipe throughput before upgrading to high pressure or increasing the parallel limit.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks and Bronze Pipe Casings with the Solid Steel Machine Casings and Steel Pipe Casings listed in the table. The existing glass, Steam Hatch, and steam buses can be reused.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam, materials, and production.

High pressure is the machine's structure tier. It still uses ordinary steam. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels, and MV or higher recipes are not unlocked.

## Automation and Item Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send materials into the front face of the Input Bus. Reserve slots for each input and replenish them according to the recipe ratio.
- **Molds:** Keep the corresponding mold for recipes that require it. Prevent extraction equipment from removing the mold, and use input filters to avoid inserting the wrong mold.
- **Output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to alloy storage, plate production, or other processing.
- **Steam:** Connect fluid pipes from the boiler to the Steam Hatch. An ordinary Input Hatch cannot replace the Steam Hatch for power.
- **Changing recipes:** Stop supplying materials and wait for the current operation to finish before clearing leftover inputs and molds. Avoid filling the bus with small quantities of materials for different recipes or combining them into an unintended alloy.

The basic setup allows at most one additional steam Input or Output Bus. Choose between more input or output buffering according to where congestion occurs. Additional buses do not raise the parallel limit, at least 25 actual casings must remain, and a second Steam Hatch cannot be installed.

> [!WARNING]
> Set voiding to "Void Nothing" in the GUI when all products must be collected. Clear output congestion when the Output Bus or storage is full to avoid losing alloys and molded parts through enabled voiding.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Is the structure three blocks wide, four blocks deep, and three blocks tall? Is the controller at the front center of the second layer? Are the two Pipe Casings and four glass blocks correctly positioned? |
| Structure tier mismatch | Are the casings and Pipe Casings all of the same tier? Were only some bronze components replaced? |
| Glass positions fail the check | Are supported glass blocks, such as ordinary Glass, used? Were Glass Panes or unsupported decorative blocks used by mistake? |
| Missing Steam Hatch or buses | Is there exactly one Steam Hatch and at least one steam Input Bus and Output Bus? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding interfaces | Are at least 25 actual casings left? Were glass or Pipe Casings replaced with hatches? Were ordinary Input or Output Hatches added by mistake? |
| Inputs present but no recipe found | Is the recipe an Alloy Smelter recipe? Do the input forms and ratios match NEI? Is the mold correct? Is there enough output space? |
| Copper present but Bronze production stops | Is there enough Tin, or is Copper filling every input slot and blocking Tin? Were Copper Nuggets, Tiny Piles of Copper Dust, or other input forms used by mistake? |
| Mold inserted but no shaping occurs | Was an Extruder Shape used by mistake? Does NEI show a molding recipe for that material? Are the material quantity and recipe tier requirements met? |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher recipes. |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |
| Fewer than eight recipes processed at once | Is there enough of every input for eight copies of the same recipe? Is the parallel limit set lower? Can the Output Bus hold all products? |

For general structure checks and tool use, see [Multiblock Machines](../multiblocks_index.md).

## Related Pages

- [GTNH Wiki: Steam Fuser](https://wiki.gtnewhorizons.com/wiki/Steam_Fuser)