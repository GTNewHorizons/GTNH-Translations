---
item_ids:
  - gregtech:gt.blockmachines:31083
navigation:
  title: Steam Presser
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31083
  position: 2
quest_ids:
  - s6AEHSKiQe2XveT_oDZbZg
---

# Steam Presser

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" /> is a multiblock Forge Hammer available in the Steam age. It uses steam to process ores and materials in batches, replacing a singleblock Steam Forge Hammer for tasks such as making plates and Long Rods. It can process up to eight copies of the same recipe at once.

The machine has basic bronze and high pressure steel structures that share the same controller. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Cast Iron Plates, an Anvil, a Tumbaga Frame Box, and other materials |
| Dimensions | 5×5 footprint, seven blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Forge Hammer recipes at LV or below, requiring no more than 32 EU/t |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing bonuses | The basic structure runs at 125% of a singleblock bronze Steam Forge Hammer's speed and 62.5% of its steam consumption rate per parallel |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31083" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, and one Output Bus. The basic structure uses Bronze Plated Bricks, Bronze Pipe Casings, and Iron Blocks, while the high pressure structure uses their steel counterparts. **All three types of structure component must be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 39 in the basic setup; may be replaced with hatches or buses, but at least 35 actual casings must remain |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Two, at the center of the sixth and seventh layers |
| Metal block | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | Two, at the center of the fourth and fifth layers |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Fluid Input Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Same hatch | Optional, replacing a casing; supplies recipe fluids, such as acids used to process mineral crop products |

There are 42 positions for casings or hatches. Installing the three required interfaces leaves 39 casings; adding one Fluid Input Hatch leaves 38. At least 35 actual casings must remain when adding hatches or buses. Hatches and buses cannot replace Pipe Casings or metal blocks.

### Building by Layer

Count layers upward from the base. Choose the controller facing first, then follow the interactive structure or hologram layer by layer. **The front of the base extends one block ahead of the controller**, so do not place the controller on the frontmost edge of the base.

| Layer | What to place |
| --- | --- |
| First | A 5×5 base with the four corners omitted, giving 21 casing positions |
| Second | The controller and the nine surrounding casing positions shown in the hologram |
| Third | One casing position on each side to start the left and right pillars |
| Fourth and fifth | Continue both pillars and place one Iron Block at the center of each layer; use Steel Blocks for the high pressure structure |
| Sixth | Six casing positions as shown in the hologram, with the first Pipe Casing at the center |
| Seventh | The second Pipe Casing directly above the first |

Empty positions in the preview do not need to be filled with casings. Place the Steam Hatch and steam Input and Output Buses in lower casing positions for convenient pipe connections. Ordinary electric machine item buses cannot replace the steam versions.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Machine Uses

The Steam Presser uses the Forge Hammer recipe map. When checking NEI, first confirm that the item has a Forge Hammer recipe, then check its tier, input quantity, and outputs.

| Use | Common recipes and considerations |
| --- | --- |
| Making metal plates | Many early metals use three ingots to make two plates; parallels increase the number of recipes processed at once without changing the material ratio |
| Making Long Rods | Eligible materials use two Rods to make one Long Rod; check NEI for the material and recipe tier |
| Crushing ores | Processes ores with matching recipes into Crushed Ore or gems; outputs vary by ore rather than always producing the same kind of intermediate item |
| Finishing ore processing | Processes eligible Centrifuged Ore into dust; the macerator route may provide additional byproducts, so compare the complete output lists in NEI first |
| Processing mineral crops | Uses a Fluid Input Hatch to process CropsNH harvest products with Forge Hammer recipes at LV or below, producing Purified Crushed Ore or Impure Dust |

The machine only performs the Forge Hammer step. It does not automatically wash, centrifuge, or smelt the outputs. Route items according to their actual products when building an ore processing line, so intermediates that need further processing are not sent straight to a furnace.

> [!NOTE]
> The machine's unlock tier and its maximum recipe tier are separate limits. It always runs on steam. Upgrading to the high pressure steel structure does not enable MV or higher-tier Forge Hammer recipes.

### Mineral Crop Products

Installing a Fluid Input Hatch allows the machine to process CropsNH mineral crop harvests. For example, Coppon Fiber, Tine Twig, and Ferrofern Leaf have LV Forge Hammer recipes that require Sulfuric Acid, providing a continuous source of their corresponding minerals. Other crops may require different fluids or recipe tiers; check each recipe in NEI.

These common recipes use a Programmed Circuit to select the output: configuration 1 produces Purified Crushed Ore, while configuration 2 produces Impure Dust. Send the harvest products to a steam Input Bus, set the circuit as shown in NEI, and supply enough recipe fluid through an ordinary Fluid Input Hatch.

Steam still enters through the Steam Hatch to power the machine. Acids and other recipe fluids enter through a separate Fluid Input Hatch. Both hatches are needed; an Input Hatch cannot replace the Steam Hatch. Crop and recipe fluid requirements increase with the number of parallels.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and steam Output Bus are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Leave space in the Output Bus and insert a small amount of material, enough for at least one recipe. Also supply any required fluids and circuit configuration.
4. Start the machine and observe the output route and steam buffer.
5. Increase input quantities and parallels after confirming a continuous steam supply.

## Steam Supply and Throughput

The Steam Presser can process up to eight copies of **the same recipe** at once. This does not mean it can process eight different items in one cycle. Actual parallels also depend on input quantities, output space, and the parallel limit set in the GUI.

For example, if one plate recipe uses three ingots to make two plates, eight parallels require 24 ingots and produce 16 plates in one cycle. Inserting only eight ingots is not enough for eight parallels.

The basic structure runs at 125% of a singleblock bronze Steam Forge Hammer's speed, taking roughly 80% as long. Its steam consumption rate per parallel is 62.5% of the singleblock machine's rate. Combining both bonuses gives roughly 50% of the total steam consumption for the same amount of material. However, running more parallels still increases the whole machine's instantaneous steam demand.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
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
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Pipe Casings, and Iron Blocks with the Solid Steel Machine Casings, Steel Pipe Casings, and Steel Blocks listed in the table. Replacing only the casings, or leaving even one Iron Block, fails the tier check.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam and production.

High pressure is a structure tier, not a separate steam fluid. The machine still uses ordinary steam, and the existing Steam Hatch and steam buses can be reused. No Energy Hatch is needed. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels and the recipe tier limit remains LV.

## Automation and Item Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send items into the front face of the Input Bus.
- **Output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to storage or the next machine.
- **Steam:** Connect fluid pipes from the boiler to the Steam Hatch. Item buses cannot receive steam.
- **Recipe fluids:** When processing mineral crops or other recipes with fluid inputs, connect a separate fluid pipe to an ordinary Input Hatch to supply the acids or other fluids required by NEI.
- **Routing:** Set input filters for plate production, Long Rod production, and ore processing as needed, so different materials do not fill all four input slots. Route mineral products to later machines according to their actual item types.

Additional Input Buses expand item buffering, while additional Output Buses help prevent output congestion. Neither raises the eight-parallel limit. Keep at least 35 actual casings when adding Fluid Input Hatches or buses, and do not install a second Steam Hatch.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Is the footprint 5×5 and the height seven blocks? Is the controller on the second layer, one block behind the frontmost edge of the base? Are the two upper Pipe Casings and two central metal blocks correctly positioned? |
| Structure tier mismatch | Are the casings, Pipe Casings, and metal blocks all of the same tier? Are any Iron Blocks or bronze components left after upgrading? |
| Missing Steam Hatch or buses | Is there exactly one Steam Hatch and at least one steam Input Bus and Output Bus? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding buses | Are at least 35 actual casings left? Were any Pipe Casings or metal blocks replaced with buses? |
| Inputs present but no recipe found | Does the item have a Forge Hammer recipe? Are there enough inputs for one recipe? Are the required fluids and circuit configuration supplied? Is there enough output space? |
| Mineral crop products do not process | Is an ordinary Fluid Input Hatch installed and supplied with the required acid or other fluid? Is the circuit configuration correct? Is the recipe at LV or below? |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |
| Fewer than eight recipes processed at once | Are there enough materials for copies of the same recipe? Is the parallel limit set lower? Can the output slots hold all products? |

For general structure checks and tool use, see [Multiblock Machines](../multiblocks_index.md).

## References

- [GTNH Wiki: Steam Presser](https://wiki.gtnewhorizons.com/wiki/Steam_Presser)