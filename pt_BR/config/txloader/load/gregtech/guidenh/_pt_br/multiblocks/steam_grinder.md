---
item_ids:
  - gregtech:gt.blockmachines:31041
navigation:
  title: Steam Grinder
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31041
  position: 3
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKzA
---

# Steam Grinder

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" /> is a multiblock Macerator available in the Steam age. It uses steam to grind ores and materials in batches. As an upgrade to the singleblock Steam Macerator, it can process up to eight copies of the same recipe at once and is useful in early ore processing lines.

The machine has basic bronze and high pressure steel structures that share the same controller. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier or provide additional ore byproducts.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Diamonds, Pistons, a Tumbaga Frame Box, and other materials |
| Dimensions | 3×3 footprint, four blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Macerator recipes at LV or below, requiring no more than 32 EU/t |
| Output limit | Only the first item in the recipe's output list; the high pressure structure does not add output types |
| Parallels | Up to eight copies of the same recipe; lower recipe power does not raise this limit |
| Processing bonuses | The basic structure runs at 125% of a singleblock bronze Steam Macerator's speed and 62.5% of its steam consumption rate per parallel |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31041" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, and one Output Bus. The basic structure uses bronze components, while the high pressure structure uses their steel counterparts. **The casings, Frame Boxes, and Gear Box Casings in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 17 in the basic setup; may be replaced with the hatches or buses below, but at least 14 actual casings must remain |
| Frame Box | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Eight, at the four corners of the second and third layers |
| Gear Box Casing | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | One, at the center of the fourth layer |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |

The new structure has 20 positions for casings or hatches. Installing the three required interfaces leaves 17 casings; adding buses reduces the casing count accordingly. Hatches and buses cannot replace Frame Boxes or Gear Box Casings.

### Building by Layer

Count layers upward from the base. Choose the controller facing first, then follow the interactive structure or hologram layer by layer.

| Layer | What to place |
| --- | --- |
| First | A full 3×3 base, giving nine casing positions |
| Second | Frame Boxes at all four corners, the controller at the front center, and one casing position at the center of the left, right, and rear sides |
| Third | Frame Boxes at all four corners and one casing position at the center of each of the four sides |
| Fourth | A Gear Box Casing at the center and one casing position at the center of each of the four sides; the four corners do not need blocks |

The empty center positions on the second and third layers do not need to be filled with casings. Place the Steam Hatch and steam Input and Output Buses in suitable casing positions for convenient pipe connections. Ordinary electric machine item buses cannot replace the steam versions.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

> [!NOTE]
> This page describes the new structure in 2.9.0. The current RC-2 also accepts the old hollow 3×3×3 structure, but the hologram and assisted construction use the new structure. The old page's explanation of parallels based on recipe power does not apply to the current version; the machine's maximum is fixed at eight parallels.

## Machine Uses and Outputs

The Steam Grinder uses the Macerator recipe map. When checking NEI, first confirm that the item has a Macerator recipe, then check its tier, input quantity, and **first item output**.

| Use | Common recipes and considerations |
| --- | --- |
| Initial ore crushing | Turns eligible ores into Crushed Ore; this step increases the main output quantity for many common ores, with exact yields shown in NEI |
| Grinding ore intermediates | Turns eligible Crushed Ore into Impure Dust and Centrifuged Ore into dust; the machine does not automatically perform later washing, centrifuging, or smelting steps |
| Grinding materials | Turns ingots, gems, and other materials with matching recipes into dust for alloys and further processing |
| Item recycling | Processes components or items with Macerator recycling recipes; check the outputs before sending in items you still need |

### Why There Are No Byproducts

The machine only produces the **first item output** in the Macerator recipe's output list. Items in the second and later positions in NEI are not produced, even if they have an output chance. This is a machine limitation, rather than a shortage of slots in the Output Bus.

For example, if a recipe lists a main mineral, an ore byproduct, and Stone Dust as three outputs, the Steam Grinder only uses the quantity and chance of the first output. Adding Output Buses, increasing parallels, or upgrading to the high pressure structure does not unlock the remaining outputs.

If you need ore byproducts from the maceration step, consider machines with more outputs, such as the <ItemLink id="gregtech:gt.blockmachines:303" showIcon="left" />. Ore washing and centrifuging also have their own outputs; plan each step according to its machine and NEI recipe.

> [!NOTE]
> The machine is available in the Steam age, but only accepts recipes up to LV. Upgrading to the high pressure steel structure does not enable MV or higher-tier recipes and does not change the first-item-output limit.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and steam Output Bus are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Check the recipe tier and first item output in NEI, and leave space in the Output Bus.
4. Start the machine with a small amount of material and observe the output route and steam buffer.
5. Increase input quantities and parallels after confirming a continuous steam supply.

## Steam Supply and Throughput

The Steam Grinder can process up to eight copies of **the same recipe** at once. This does not mean it can process eight different items in one cycle. Actual parallels also depend on input quantities, output space, and the parallel limit set in the GUI. Lower-power recipes do not raise the maximum above eight.

The basic structure runs at 125% of a singleblock bronze Steam Macerator's speed, taking roughly 80% as long. Its steam consumption rate per parallel is 62.5% of the singleblock machine's rate. Combining both bonuses gives roughly 50% of the total steam consumption for the same amount of material. However, running more parallels still increases the whole machine's instantaneous steam demand.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
| Maximum parallels | 8 | 8 |
| Item output types | Only the recipe's first item output | Only the recipe's first item output |
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
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Frame Boxes, and Bronze Gear Box Casings with the Solid Steel Machine Casings, Steel Frame Boxes, and Steel Gear Box Casings listed in the table. Replacing only the casings, or leaving some bronze frames or gearboxes, fails the new structure's tier check.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam and production.

High pressure is a structure tier, not a separate steam fluid. The machine still uses ordinary steam, and the existing Steam Hatch and steam buses can be reused. No Energy Hatch is needed. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels.

## Automation and Item Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send items into the front face of the Input Bus.
- **Output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to storage or the next machine.
- **Steam:** Connect fluid pipes from the boiler to the Steam Hatch. Item buses cannot receive steam.
- **Routing:** Set filters for ores, Crushed Ore, Impure Dust, and other materials so intermediates do not enter the wrong processing step.

The same grinder may serve several steps in an ore processing line. If both raw ores and newly produced Crushed Ore are sent back to the same Input Bus, check filters and priorities so one step does not continually fill the input slots. For continuous processing through several steps, consider separate machines and check the steam supply shared by the entire line.

Additional Input Buses expand item buffering, while additional Output Buses help prevent output congestion. Neither raises the parallel limit or unlocks byproducts. Keep at least 14 actual casings when expanding, and do not install a second Steam Hatch.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete new structure | Is the footprint 3×3 and the height four blocks? Is the controller at the front center of the second layer? Are the eight Frame Boxes on the second and third layers and the top Gear Box Casing correctly positioned? |
| Structure tier mismatch | Are the casings, Frame Boxes, and Gear Box Casing all of the same tier? Were only some bronze components replaced? |
| Missing Steam Hatch or buses | Is there exactly one Steam Hatch and at least one steam Input Bus and Output Bus? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding buses | Are at least 14 actual casings left? Were any Frame Boxes or the Gear Box Casing replaced with buses? |
| Inputs present but no recipe found | Does the item have a Macerator recipe? Are there enough inputs for one recipe? Is there enough output space? |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| NEI shows byproducts that the machine does not produce | The machine only produces the first item output. Adding Output Buses or upgrading to the high pressure structure does not unlock the remaining outputs. |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |
| Fewer than eight recipes processed at once | Are there enough materials for copies of the same recipe? Is the parallel limit set lower? Can the output slots hold all products? |

For general structure checks and tool use, see [Multiblock Machines](./multiblocks_index.md).

## Related Pages

- [GTNH Chinese Wiki: Steam Grinder](https://gtnh.huijiwiki.com/wiki/大型蒸汽研磨机)