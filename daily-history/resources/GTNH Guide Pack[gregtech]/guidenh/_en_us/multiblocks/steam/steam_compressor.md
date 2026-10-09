---
item_ids:
  - gregtech:gt.blockmachines:31078
navigation:
  title: Steam Squasher
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31078
  position: 4
quest_ids:
  - Plg8vg0gS9Ks2Ddc5sIVOg
---

# Steam Squasher

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> is a multiblock Compressor available in the Steam age. It uses steam to compress materials in batches. As an upgrade to the singleblock Steam Compressor, it can process up to eight copies of the same recipe at once, making material blocks, Compressed Fireclay, and Compressed Air Cells.

The machine has basic bronze and high pressure steel structures that share the same controller. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier or replace machines with special compression tiers.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Pistons, Tumbaga Gears, a Tumbaga Frame Box, and other materials |
| Dimensions | Three blocks wide, seven blocks deep, and three blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Ordinary Compressor recipes at LV or below, requiring no more than 32 EU/t |
| Special limit | Cannot process recipes requiring a special compression tier; the high pressure steel structure does not unlock them |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing bonuses | The basic structure runs at 125% of a singleblock bronze Steam Compressor's speed and 62.5% of its steam consumption rate per parallel |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31078" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, and one Output Bus. The basic structure uses Bronze Plated Bricks, Bronze Pipe Casings, and Iron Blocks, while the high pressure structure uses their steel counterparts. **The casings, Pipe Casings, and metal blocks in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 27 in the basic setup; may be replaced with the hatches or buses below, but at least 14 actual casings must remain |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Ten: eight around the front controller and two more along the center of the second layer inside the structure |
| Metal block | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | Six: three on each of the second and third layers in the fifth row counted from the front |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Fluid Input Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Same hatch | Optional, replacing a casing; supplies recipe fluids |

The new structure has 30 positions for casings or hatches. Installing the three required interfaces leaves 27 casings; adding one Fluid Input Hatch leaves 26. At least 14 actual casings must remain when adding more hatches or buses. Hatches and buses cannot replace Pipe Casings or metal blocks.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Machine Uses

The Steam Squasher uses the Compressor recipe map. When checking NEI, first confirm that the item has a Compressor recipe, then check its tier, input quantity, outputs, and special requirements.

| Use | Common recipes and considerations |
| --- | --- |
| Making material blocks | Eligible metals commonly use nine ingots to make one metal block; some dusts also have block compression recipes. Check NEI for the material and recipe tier. |
| Making building blocks | Compresses Clay Balls, Bricks, Nether Bricks, Glowstone Dust, and other materials into their corresponding blocks; for example, four brick items make one brick block |
| Making Compressed Fireclay | Compresses Fireclay Dust into Compressed Fireclay for later firing; the Compressor does not perform the firing step itself |
| Producing Compressed Air Cells | Compresses Empty Cells into Compressed Air Cells for later air processing |
| Other ordinary compression recipes | Processes Alloy Plates and other materials with eligible recipes; check the Compressor recipe in NEI to confirm compatibility |

### Air Cells and Later Oxygen Production

An ordinary compression recipe turns **one Empty Cell into one Compressed Air Cell**. Empty Cells enter through the steam Input Bus, and Compressed Air Cells leave through the steam Output Bus. This recipe only needs steam for power; it does not need an additional water supply, air supplied through an Input Hatch, or a special air collection device.

Compressed Air Cells can be used in later oxygen and nitrogen production, but this machine only produces Compressed Air Cells. **It does not directly output Oxygen or Nitrogen.** Before further processing, check the uses of Compressed Air Cells and Air fluid in NEI, then supply the fluids, cells, and output interfaces required by the next machine's recipe.

For automation, send Empty Cells to the Compressor and Compressed Air Cells to the next machine. Empty Cells returned by the process can be routed back to the input. Leave enough buffer for cell circulation so all Empty Cells do not become stuck in other machines.

> [!NOTE]
> The machine is available in the Steam age, but only accepts recipes up to LV. The high pressure steel structure raises the machine's structure tier. It does not enable MV or higher-tier recipes, or recipes requiring a special compression tier.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and steam Output Bus are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Check the recipe and input quantity in NEI, and leave space in the Output Bus.
4. Start the machine with a small amount of material and observe the output route and steam buffer.
5. Increase input quantities and parallels after confirming a continuous steam supply.

## Steam Supply and Throughput

The Steam Squasher can process up to eight copies of **the same recipe** at once. This does not mean it can process eight different items in one cycle. Actual parallels also depend on input quantities, output space, and the parallel limit set in the GUI.

For example, if a block compression recipe uses nine ingots to make one metal block, eight parallels require 72 ingots and produce eight metal blocks in one cycle.

The basic structure runs at 125% of a singleblock bronze Steam Compressor's speed, taking roughly 80% as long. Its steam consumption rate per parallel is 62.5% of the singleblock machine's rate. Combining both bonuses gives roughly 50% of the total steam consumption for the same amount of material. However, running more parallels still increases the whole machine's instantaneous steam demand.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | Ordinary Compressor recipes at LV and below | Ordinary Compressor recipes at LV and below |
| Maximum parallels | 8 | 8 |
| Speed relative to the basic structure | 1× | 2× |
| Steam consumption rate for the same recipe and parallel count | 1× | 2× |
| Total steam consumption per recipe | Baseline | Approximately the same as the basic structure |

The high pressure upgrade increases speed and steam consumption rate together. It mainly improves throughput, without halving the total steam cost per item again. Actual duration and steam consumption are also affected by tick and integer rounding.

The Steam Hatch buffers 64,000 L of steam, but this only covers temporary shortfalls and cannot replace continuous boiler production. Size boilers and pipes for the **steam consumption rate while processing**.

Use Waila to check the operating steam consumption rate and watch whether the buffer keeps falling during continuous processing. If a value is shown in L/t, multiply by 20 to get L/s at the normal 20 TPS. Use matching units when comparing pipe throughput. If steam supply is insufficient, lower the parallel limit in the GUI, then increase boiler production or improve the piping.

> [!WARNING]
> Running out of steam during processing aborts the current operation, and materials already consumed are not returned. Check steam production and pipe throughput before upgrading to high pressure or increasing the parallel limit.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Pipe Casings, and Iron Blocks with the Solid Steel Machine Casings, Steel Pipe Casings, and Steel Blocks listed in the table.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam and production.

High pressure is the machine's structure tier. It still uses ordinary steam, and the existing Steam Hatch and steam buses can be reused. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels.

## Automation and Item Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send items into the front face of the Input Bus.
- **Output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to storage or the next machine.
- **Steam:** Connect fluid pipes from the boiler to the Steam Hatch. An ordinary Input Hatch cannot replace the Steam Hatch for power.
- **Recipe fluids:** Only install an additional ordinary Input Hatch and supply the corresponding fluid when the NEI recipe requires a fluid input. Producing Compressed Air Cells does not need this interface.
- **Routing:** Set filters for material blocks, Compressed Fireclay, Compressed Air Cells, and other products so air cells do not enter material storage and intermediates that need firing do not remain at the output.

Block compression recipes often consume several items at once. Size the input buffer for "inputs per recipe × target parallels". Avoid filling the input slots with small quantities of many different materials, leaving too few of each for even one recipe.

Additional Input Buses expand item buffering, while additional Output Buses help prevent output congestion. Neither raises the parallel limit. Keep at least 14 actual casings when expanding, and do not install a second Steam Hatch.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete new structure | Is the structure three blocks wide, seven blocks deep, and three blocks tall? Is the controller at the front center of the second layer? Are the ten Pipe Casings and six metal blocks correctly positioned? |
| Structure tier mismatch | Are the casings, Pipe Casings, and metal blocks all of the same tier? Were only some bronze components replaced, or any Iron Blocks left? |
| Missing Steam Hatch or buses | Is there exactly one Steam Hatch and at least one steam Input Bus and Output Bus? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding hatches | Are at least 14 actual casings left? Were any Pipe Casings or metal blocks replaced with hatches or buses? |
| Inputs present but no recipe found | Does the item have a Compressor recipe? Are there enough inputs for one recipe? Does the recipe require a compression tier? Is there enough output space? |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| Empty Cells do not become Oxygen Cells | The Compressor produces Compressed Air Cells. Oxygen and Nitrogen require further processing in other machines. |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |
| Fewer than eight recipes processed at once | Are there enough inputs for eight copies of the same recipe? Is the parallel limit set lower? Can the output slots hold all products? |

For general structure checks and tool use, see [Multiblock Machines](../multiblocks_index.md).

## Related Pages

- [GTNH Wiki: Steam Squasher](https://wiki.gtnewhorizons.com/wiki/Steam_Squasher)