---
item_ids:
  - gregtech:gt.blockmachines:31080
navigation:
  title: Steam Separator
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31080
  position: 5
quest_ids:
  - 0rUmaWIPQPaL93q-_pgKXw
---

# Steam Separator

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" /> is a multiblock Centrifuge available in the Steam age. It uses steam to separate materials in batches and can process up to eight copies of the same recipe at once. It can purify ore dusts, obtain Raw Rubber Dust from Sticky Resin, and collect item and fluid outputs from Centrifuge recipes.

The machine has basic bronze and high pressure steel structures that share the same controller. It makes eligible Centrifuge recipes available in the Steam age. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Cast Iron Plates, Bronze Gears, a Tumbaga Frame Box, and other materials |
| Dimensions | 5×5 footprint, five blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Centrifuge recipes at LV or below, requiring no more than 32 EU/t |
| Inputs and outputs | Steam Input Buses accept items, steam Output Buses output items, and ordinary Output Hatches output fluids; ordinary Input Hatches are not accepted |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing duration | Approximately 1.6× the duration shown in NEI for the basic structure, or 0.8× for the high pressure structure |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31080" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following quantities assume one Steam Hatch, one Input Bus, one Output Bus, and one Output Hatch, allowing both item and fluid outputs to be collected. The basic structure uses bronze components, while the high pressure structure uses their steel counterparts. **The casings, Gear Box Casings, Pipe Casings, and Firebox Casings in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 65 in the setup described above; may be replaced with the hatches or buses below, but at least 60 actual casings must remain |
| Gear Box Casing | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Eight: four around the central Firebox Casing on each of the second and fourth layers |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Four, around the central Firebox Casing on the third layer |
| Firebox Casing | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Three: one at the center of each of the second, third, and fourth layers |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | Install as needed for item outputs, replacing a casing |
| Output Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Same hatch | Install as needed for fluid outputs, replacing a casing |

The structure has 69 positions for casings or hatches. Installing the four interfaces listed above leaves 65 casings. If only processing recipes with item outputs, omitting the Output Hatch requires 66 casings instead. Adding buses or Output Hatches reduces the casing count accordingly, but at least 60 actual casings must remain. Hatches and buses cannot replace Gear Box Casings, Pipe Casings, or Firebox Casings.

Count layers upward from the base. The casing layout differs between layers, so follow the interactive structure or hologram; empty positions do not need to be filled. Install at least one steam Output Bus or ordinary Output Hatch. If a recipe produces both items and fluids, install both types of output interface.

The Firebox Casings are structure blocks. They do not need fuel or a separate water supply. Steam for the machine is produced by an external boiler and supplied through the Steam Hatch.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Machine Uses

The Steam Separator uses the Centrifuge recipe map. When checking NEI, first confirm that the recipe belongs to the **Centrifuge**, then check its tier, input form, Programmed Circuit configuration, and all outputs.

| Use | Common recipes and considerations |
| --- | --- |
| Purifying ore dusts | Turns eligible Impure Dust, Purified Dust, and other intermediates into ordinary dust and corresponding byproducts; check NEI for each mineral's quantities and output forms |
| Processing Sticky Resin | Produces Raw Rubber Dust, a chance of a Plantball, and Glue; both item and fluid outputs must be handled |
| Centrifuging logs | Eligible log recipes produce Methane, while Rubber Wood also has chance-based item outputs; check the Programmed Circuit configuration required by NEI |
| Separating minerals and materials | Processes eligible Netherrack Dust, Endstone Dust, and other Centrifuge recipes, with multiple item or fluid outputs to collect |
| Cell recipes | Only processes Centrifuge recipes with items as inputs; some recipes also require extra Empty Cells, so a filled cell alone may not provide all required inputs |

### Sticky Resin and Rubber

The current Sticky Resin recipe consumes **one Sticky Resin** and produces **three Raw Rubber Dust and 100 L of Glue**, with a **10% chance of one Plantball**.

Send Sticky Resin into the steam Input Bus, collect Raw Rubber Dust and Plantballs through a steam Output Bus, and collect Glue through an ordinary Output Hatch. Glue is a recipe output. **Do not install an Input Hatch to receive it.**

At eight parallels, one cycle consumes eight Sticky Resin and produces 24 Raw Rubber Dust and 800 L of Glue. Plantballs remain chance-based outputs; a cycle is not guaranteed to produce eight. Before continuous operation, leave space for both item types and use fluid pipes to keep extracting Glue.

### Fluid Input Limit

This machine supports fluid **outputs**, but does not accept ordinary Fluid Input Hatches. Recipes that require fluid inputs in NEI cannot be enabled by adding an ordinary Input Hatch, even if they are at LV or below. The Steam Hatch supplies power and cannot serve as an input for recipe fluids such as Air or acids.

For example, a Centrifuge recipe that directly takes Air fluid in NEI requires a Centrifuge that accepts fluid inputs. Filled cells can only be sent into a steam Input Bus when the corresponding recipe explicitly lists them as **item inputs**.

> [!NOTE]
> The machine is available in the Steam age, but only accepts recipes up to LV. Upgrading to the high pressure steel structure does not enable MV or higher-tier recipes and does not remove the fluid input limit.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, and required output interfaces are installed.
2. Connect the steam pipe to the Steam Hatch and confirm that steam actually enters it.
3. Check the recipe tier, all inputs, and Programmed Circuit configuration in NEI, including whether a fluid input is required.
4. Leave space for all item and fluid outputs, then start with a small amount of material and observe the outputs and steam buffer.
5. Increase input quantities and parallels after confirming a continuous steam supply and output collection.

## Steam Supply and Throughput

The Steam Separator can process up to eight copies of **the same recipe** at once. This does not mean it can process eight different items in one cycle. Actual parallels also depend on input quantities, output space, and the parallel limit set in the GUI.

The basic structure takes approximately 1.6× the recipe duration shown in NEI, while the high pressure structure takes approximately 0.8×. For example, the Sticky Resin recipe shown as 15 seconds takes roughly 24 seconds in the basic structure or 12 seconds in the high pressure structure. Parallels increase the number of recipes processed in a cycle without dividing the cycle's duration by the parallel count.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
| Maximum parallels | 8 | 8 |
| Processing duration relative to NEI | Approximately 1.6× | Approximately 0.8× |
| Steam consumption rate for the same recipe and parallel count | 1× | 2× |
| Total steam consumption per recipe | Baseline | Approximately the same as the basic structure |

The high pressure upgrade increases speed and steam consumption rate together. It mainly improves throughput, with approximately the same total steam cost per item as the basic structure. Actual duration and steam consumption are also affected by tick and integer rounding.

The Steam Hatch buffers 64,000 L of steam, but this only covers temporary shortfalls and cannot replace continuous boiler production. Size boilers and pipes for the **steam consumption rate while processing**. Item input, item output, and fluid output must also keep up when increasing parallels.

Use Waila to check the operating steam consumption rate and watch whether the buffer keeps falling during continuous processing. If a value is shown in L/t, multiply by 20 to get L/s at the normal 20 TPS. Use matching units when comparing pipe throughput. If steam supply is insufficient, lower the parallel limit in the GUI, then increase boiler production or improve the piping.

> [!WARNING]
> Running out of steam during processing aborts the current operation, and materials already consumed are not returned. Check steam production and pipe throughput before upgrading to high pressure or increasing the parallel limit.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Gear Box Casings, Bronze Pipe Casings, and Bronze Firebox Casings with the Solid Steel Machine Casings, Steel Gear Box Casings, Steel Pipe Casings, and Steel Firebox Casings listed in the table.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam and production.

High pressure is the machine's structure tier. It still uses ordinary steam, and the existing Steam Hatch, steam buses, and Output Hatches can be reused. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels.

## Automation and Output Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send items into the front face of the Input Bus. Also supply the Empty Cells and Programmed Circuit configuration required by the recipe.
- **Item output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to main output storage, byproduct storage, or the next machine.
- **Fluid output:** Extract Glue, Methane, and other products from ordinary Output Hatches. Configure storage and filters for each fluid type, and provide enough Output Hatches for recipes with multiple fluid outputs.
- **Steam:** Connect a separate steam supply line to the Steam Hatch, keeping fluid product lines away from it.
- **Ore routing:** Set filters for ordinary dust, Impure Dust, Purified Dust, and small byproducts so items that have already been centrifuged do not fill the input buffer again.

Centrifuge recipes often produce several different items at once. A single Output Bus with four slots may not hold all outputs. Additional Output Buses expand item output space, but do not raise the parallel limit. Keep at least 60 actual casings when adding hatches or buses, and do not install a second Steam Hatch.

> [!WARNING]
> To collect all byproducts, set the GUI's voiding mode to "Do Not Void" and provide space for every item and fluid output. If fluid voiding is enabled, Glue and other products may be discarded when an Output Hatch is missing or blocked.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Is the footprint 5×5 and the height five blocks? Is the controller at the front center of the second layer? Are the Gear Box Casings, Pipe Casings, and Firebox Casings positioned as shown in the hologram? |
| Structure tier mismatch | Are the casings, Gear Box Casings, Pipe Casings, and Firebox Casings all of the same tier? Were only some bronze components replaced? |
| Missing Steam Hatch or Input Bus | Is there exactly one Steam Hatch and at least one steam Input Bus? Were ordinary electric machine item buses used by mistake? |
| Missing output interface | Is at least one steam Output Bus or ordinary Output Hatch installed? Are both required interface types installed for the recipe's outputs? |
| Structure fails after adding hatches | Are at least 60 actual casings left? Were any Gear Box Casings, Pipe Casings, or Firebox Casings replaced with hatches? |
| Inputs present but no recipe found | Does the item have a Centrifuge recipe? Was a Thermal Centrifuge recipe checked by mistake? Are the input quantities, Empty Cells, and circuit configuration correct? |
| LV recipe with fluid inputs does not process | This machine does not accept ordinary Input Hatches. Use a Centrifuge that accepts the required input form. |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| Item outputs appear but Glue or other fluids are missing | Is an ordinary Output Hatch installed? Is it locked to the wrong fluid? Is fluid voiding enabled? Have pipes already extracted the product? |
| No Plantballs or other chance-based byproducts | Is the output chance-based? Getting none from a small number of recipes can be normal; also check output space and voiding settings. |
| Insufficient output space | Is there room for all item and fluid outputs? Is one four-slot Output Bus insufficient? Are Output Hatches blocked or locked to the wrong fluid? |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |

For general structure checks and tool use, see [Multiblock Machines](./multiblocks_index.md).

## Related Pages

- [GTNH Chinese Wiki: Steam Separator](https://gtnh.huijiwiki.com/wiki/大型蒸汽离心机)