---
item_ids:
  - gregtech:gt.blockmachines:31087
navigation:
  title: Steam Hearth
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31087
  position: 1
quest_ids:
  - AAAAAAAAAAAAAAAAAAADZg
---

# Steam Hearth

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" /> is a multiblock furnace available in the Steam age. It uses steam to smelt items in batches, processing up to eight copies of the same recipe at once. Blasting and Smoking modes can further speed up eligible metal and food recipes, respectively.

The Steam Hearth has basic bronze and high pressure steel structures that share the same controller. It does not consume electric power, but the boiler must provide a continuous steam supply.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires a High Pressure Steam Furnace and other materials |
| Dimensions | 3×3×3, with the controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Processing modes | Furnace, Blasting, and Smoking; accepted items depend on the selected recipe map |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing bonuses | In Furnace mode, the basic structure runs at 125% of a singleblock bronze Steam Furnace's speed and 62.5% of its steam consumption rate per parallel |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31087" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, and one Output Bus. The basic structure uses bronze components, while the high pressure structure uses their steel counterparts. **All four types of structure component must be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Six in the basic setup; casing positions on the bottom and middle layers may be replaced with the hatches or buses below, but at least two actual casings must remain |
| Gear Box | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Four, at the center of each edge of the top layer |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Four, at the center of each edge of the bottom layer |
| Firebox | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Three, at the center of the left, right, and rear sides of the middle layer |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |

There are nine positions for casings or hatches. Installing the three required interfaces leaves six casings. Each additional bus replaces another casing. Hatches cannot replace Gear Boxes, Pipe Casings, or Fireboxes.

### Building by Layer

Build the bottom layer first, then the middle layer containing the controller, and finally the four Gear Boxes on top. Empty positions in the preview do not need to be filled with casings. The structure requires neither glass nor Heating Coils.

Place the Steam Hatch and steam Input and Output Buses in suitable casing positions for convenient pipe connections. Ordinary electric machine Input and Output Buses cannot replace the steam versions. Maintenance and Muffler Hatches are not required.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Uses and Processing Modes

The Steam Hearth can process furnace recipes in bulk, producing items such as stone, glass, directly smelted materials, and cooked food. Different inputs may yield different products. Check NEI before smelting, especially before using intermediate products from an ore processing chain.

Right-click the controller with a <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> to cycle through **Furnace → Blasting → Smoking → Furnace**. You can also use the mode button in the GUI. Waila and the controller interface show the current mode.

| Mode | Accepted recipes | Change relative to Furnace mode at the same structure tier |
| --- | --- | --- |
| Furnace | Ordinary furnace recipes | Base speed and steam consumption rate |
| Blasting | Metal recipes accepted by the Et Futurum Blast Furnace | Double speed and steam consumption rate |
| Smoking | Food recipes accepted by the Et Futurum Smoker | Double speed and steam consumption rate |

Blasting and Smoking only process items in their respective recipe maps; they do not automatically fall back to Furnace mode. If an item with a furnace recipe does not process, check the selected mode first. Being a metal or food item alone does not guarantee a recipe in the specialized mode.

> [!NOTE]
> Blasting here corresponds to the Blast Furnace processing introduced in Minecraft 1.14+. It cannot replace an [Electric Blast Furnace](../lv/electric_blast_furnace.md) or Bricked Blast Furnace. It has no heat or Heating Coil mechanic, and selecting Blasting does not enable Electric Blast Furnace recipes.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and steam Output Bus are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Select the appropriate mode for the input and leave space in the Output Bus.
4. Enable the machine and supply a small amount of ingredients. Watch the products and stored steam.
5. Confirm a continuous steam supply before increasing ingredient input and parallel count.

## Steam Supply and Throughput

The Steam Hearth processes up to eight copies of **the same recipe** at once. It does not process eight different items together in one cycle. Actual parallels also depend on ingredient quantities, output space, and the parallel limit set in the GUI.

In Furnace mode, the basic structure runs at 125% of a singleblock bronze Steam Furnace's speed, taking approximately 80% of its time. Its steam consumption rate per parallel is 62.5% of that furnace's rate. Combining these bonuses gives approximately 50% of the total steam consumption for the same item. Running multiple parallels still increases the machine's instantaneous steam demand.

The following comparison uses **the basic structure in Furnace mode, with the same parallel count**, as the baseline:

| Structure and mode | Processing speed | Steam consumption rate |
| --- | --- | --- |
| Basic structure, Furnace | 1× | 1× |
| Basic structure, Blasting or Smoking | 2× | 2× |
| High pressure structure, Furnace | 2× | 2× |
| High pressure structure, Blasting or Smoking | 4× | 4× |

The mode and high pressure bonuses stack. Both increase speed and steam consumption rate together, mainly improving throughput. They do not halve the total steam consumed per item again. Actual time and consumption are also affected by tick and integer rounding.

Size boilers and pipes for **the steam consumption rate during operation**, rather than relying only on the Steam Hatch's 64,000 L capacity.

Use Waila to check the operating steam consumption rate and watch whether stored steam keeps falling during continuous processing. If an interface uses L/t, multiply by 20 to obtain L/s at normal 20 TPS. Use matching units when comparing pipe throughput. If supply is insufficient, lower the parallel limit in the GUI, then expand boiler production or improve the pipes.

> [!WARNING]
> Running out of steam during processing aborts the current operation without returning consumed ingredients. Before upgrading to high pressure or selecting a faster mode, check steam production and pipe throughput.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. However, **all Bronze Plated Bricks, Bronze Gear Boxes, Bronze Pipe Casings, and Bronze Fireboxes must be replaced with their steel counterparts in the table**. Replacing only the casings or Fireboxes, or mixing components from both tiers, fails the tier check.

Stop processing and ingredient input before upgrading. After replacing the components, check the structure again and confirm that the machine reports the high pressure tier before restoring steam and production.

High pressure is a structure tier, not a separate steam fluid. The machine still uses ordinary steam, and the existing Steam Hatch and steam buses can be reused. No electric Energy Hatch is needed. The upgrade doubles speed and steam consumption rate, while the maximum remains eight parallels.

## Automation and Sorting

Steam Input and Output Buses each have four item slots. They do not automatically pull ingredients from adjacent chests or push products into them. Simply placing a chest next to a bus does not automate transport.

- **Input:** Use hoppers, GT Item Pipes, Conveyor Modules, Item Conduits, or similar equipment to insert items through the Input Bus's front face.
- **Output:** Actively extract from the Output Bus's front face with pipes, conduits, or Conveyor Modules, then send the products to storage or the next machine.
- **Steam:** Use fluid pipes to deliver boiler output to the Steam Hatch. Item buses cannot receive steam.
- **Sorting:** Filter the transport equipment for the intended ingredients so items that the current mode cannot process do not fill the input slots.

If you frequently need to process metals, food, and other materials at the same time, use separate machines or switch modes when changing ingredients. More Input Buses increase the item buffer but do not raise the parallel limit. More Output Buses can reduce output blockages.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Controller at the front center of the second layer; correct positions for four Gear Boxes, four Pipe Casings, and three Fireboxes |
| Structure tier mismatch | Casings, Gear Boxes, Pipe Casings, and Fireboxes must all be of the same tier; check for bronze components left after upgrading |
| Missing Steam Hatch or bus | Exactly one Steam Hatch and at least one steam Input and Output Bus; check for incorrect hatch types |
| Structure fails after adding buses | At least two actual casings must remain; buses cannot replace Gear Boxes, Pipe Casings, or Fireboxes |
| Ingredients present but no recipe found | Correct mode, a valid recipe for the item in that mode, and enough output space |
| Stops after starting despite stored steam | Sufficient sustained supply, pipe restrictions or shared supply, and whether the parallel count, high pressure tier, or faster mode exceeds boiler capacity |
| Chest beside a bus does not transfer items | Steam buses do not automatically pull or push items; check active transport equipment, connection faces, directions, and filters |
| Fewer than eight recipes processed | Enough ingredients for the same recipe, the GUI parallel limit, and output space for all products |
| Steam consumption increases after upgrading | High pressure doubles consumption rate, and Blasting or Smoking can double it again; increase the steam supply accordingly |

See [Multiblock Machines](../multiblocks_index.md) for general structure checks and tool controls.

## References

- [GTNH Wiki: Steam Hearth](https://wiki.gtnewhorizons.com/wiki/Steam_Hearth)