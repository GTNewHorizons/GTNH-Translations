---
item_ids:
  - gregtech:gt.blockmachines:31082
navigation:
  title: Steam Purifier
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31082
  position: 6
quest_ids:
  - zorY0c3BQuqLJp7ThOLG-g
---

# Steam Purifier

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" /> is a multiblock ore washing machine available in the Steam age. It uses steam and water to process minerals in batches and can process up to eight copies of the same recipe at once. Its **Ore Washer** and **Simple Washer** modes let you choose between collecting byproducts and washing quickly.

The machine has basic bronze and high pressure steel structures that share the same controller. It makes washing Crushed Ores available in the Steam age, while Simple Washer mode can also quickly wash eligible Impure Dusts and Purified Dusts. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Cast Iron Plates, Tin Rotors, a Tumbaga Frame Box, and other materials |
| Dimensions | Nine blocks wide, five blocks deep, and six blocks tall; controller at the front center of the small cube's second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Ore Washer or Simple Dust Washer recipes at LV or below, requiring no more than 32 EU/t |
| Inputs and outputs | Steam Input Buses accept items, Input Hatches accept recipe water, and steam Output Buses output items |
| Operating modes | Defaults to Ore Washer mode; switch to Simple Washer mode with a screwdriver or the GUI |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing duration | Approximately 1.6× the duration shown in NEI for the basic structure, or 0.8× for the high pressure structure |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31082" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following setup uses one Steam Hatch, one Input Bus, one Output Bus, and one Input Hatch. The basic structure uses bronze components, while the high pressure structure uses their steel counterparts. **The casings, Gear Box Casings, and Pipe Casings in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 59 in the setup described above; may be replaced with the hatches or buses below, but at least 55 actual casings must remain |
| Gear Box Casing | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Eight, in the tank's base around the central casing |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | 12, forming the pipes inside the tank and the connecting pipes above |
| Glass | For example, <ItemLink id="minecraft:glass" showIcon="left" /> | Existing glass can be reused | 24, forming two layers of tank walls; use glass blocks accepted by the hologram |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" /> | Same controller | One, at the front center of the small cube's second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | At least one, replacing a casing |
| Input Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Same hatch | At least one, replacing a casing, to supply water |

The structure has 63 positions for casings or hatches. Installing the four interfaces listed above leaves 59 casings. Adding Input Hatches or buses reduces the casing count accordingly, but at least 55 actual casings must remain. Hatches and buses cannot replace Gear Box Casings, Pipe Casings, or glass.

Count layers upward from the base. The structure consists of a small cube, a glass tank beside it, and pipes above. The controller is not at the center of the entire structure, which is nine blocks wide. Follow the interactive structure or hologram. The controller can only face horizontally, and the structure cannot be rotated around its front face; empty positions in the hologram do not need to be filled.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

### Tank Water and Recipe Water

Steam, water in the structure's tank, and recipe water serve different purposes:

| Location | Purpose |
| --- | --- |
| Steam Hatch | Receives steam produced by an external boiler to power the machine |
| Input Hatch | Receives ordinary Water or the Distilled Water required by the recipe; each recipe consumes its water from here |
| Structure's tank | Eight water positions around the central Pipe Casing on the second layer; place water sources manually or let the machine fill them |

Keep the Pipe Casing in the center of the tank. The eight surrounding water positions can initially be left empty. When checking the tank, the machine takes **1,000 L of ordinary Water** at a time from Input Hatches to place one water source block. If all eight positions are empty, the initial fill consumes up to **8,000 L of additional ordinary Water**. This is separate from the current cycle's recipe water, so provide enough buffer before starting.

You can also use water buckets to fill all eight positions manually. **Water placed in the tank does not replace recipe water in Input Hatches.** Keep supplying the Input Hatches after the tank is filled. Tank water is not consumed by each recipe, but if a source is removed, the machine will attempt to refill it during a later check. The structure check accepts water sources or air; flowing water cannot replace source blocks.

Ore Washer mode includes Distilled Water recipes, but automatic filling of an empty tank only uses **ordinary Water**. Before washing with Distilled Water, fill the tank with buckets or install an extra Input Hatch containing ordinary Water for automatic filling.

## Machine Uses

### Two Washing Modes

<kbd>Right-click</kbd> the controller with a <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" />, or click the mode button in the GUI, to switch between Ore Washer and Simple Washer modes.

| Property | Ore Washer mode | Simple Washer mode |
| --- | --- | --- |
| Recipe map | Ore Washer recipes in NEI | Simple Dust Washer recipes in NEI |
| Common inputs | Crushed Ores and other eligible mineral intermediates | Eligible Crushed Ores, Impure Dusts, and Purified Dusts |
| Common main outputs | Crushed Ores become Purified Crushed Ores | Crushed Ores become Purified Crushed Ores; Impure Dusts and Purified Dusts become ordinary dusts |
| Byproducts | Collects Stone Dust and mineral byproducts listed in the recipe; some outputs are chance-based | Only produces the cleaned main product, without ore washing or centrifuging byproducts |
| Typical water per recipe | 1,000 L of ordinary Water or 200 L of Distilled Water; check the corresponding NEI recipe | 100 L of ordinary Water |
| Typical duration shown in NEI | 25 seconds with ordinary Water or 15 seconds with Distilled Water; individual recipes may differ | Five ticks, or 0.25 seconds at the normal 20 TPS |

Choose Ore Washer mode when you need mineral byproducts, and leave output space for every product. Choose Simple Washer mode when you only need the main product quickly. Simple washing is fast and uses little water, making it suitable for bulk processing materials whose byproducts you have decided to skip.

For Impure Dusts and Purified Dusts, also check [Steam Separator](./steam_centrifuge.md) recipes. Centrifuging can often recover corresponding byproducts while producing ordinary dust, whereas simple washing skips those byproducts. Choose the processing route using the specific mineral's NEI recipes.

> [!WARNING]
> Simple Washer mode does not produce the byproducts from normal ore washing or centrifuging. Switching back to Ore Washer mode cannot recover those byproducts from items already processed in Simple Washer mode. Check the current mode before processing minerals whose byproducts you need.

### Mineral Processing Routes

Washing Crushed Ore usually produces **Purified Crushed Ore**, rather than ordinary dust ready for every crafting recipe. Choose subsequent grinding, centrifuging, or other processing steps in NEI, and route items by their name and form.

- **Keep byproducts:** Send Crushed Ore into Ore Washer mode, collect Purified Crushed Ore, Stone Dust, and mineral byproducts separately, then arrange subsequent processing.
- **Wash quickly:** Send eligible Crushed Ore into Simple Washer mode and collect only Purified Crushed Ore.
- **Quickly purify ore dusts:** Send eligible Impure Dust or Purified Dust into Simple Washer mode to obtain ordinary dust. Use centrifuging instead if you need its corresponding byproducts.

Not every material or mineral form has a Simple Dust Washer recipe. Purified Crushed Ore and Purified Dust are different items. An item having "Purified" in its name does not mean it can be processed again in Simple Washer mode.

### First Startup

1. Check the structure and confirm that the Steam Hatch, steam Input Bus, steam Output Bus, and Input Hatch are installed.
2. Use separate lines to supply steam to the Steam Hatch and water to the Input Hatch. If the tank is empty, first buffer enough ordinary Water for automatic filling.
3. Select the desired mode and check the corresponding recipe map, input form, water type, and all outputs in NEI.
4. Leave space for every output, then start with a small amount of material and observe the tank, outputs, steam buffer, and Input Hatch contents.
5. Increase input quantities and parallels after confirming continuous steam and water supplies and output collection.

> [!NOTE]
> In the current version, the machine may briefly show "No Water" during its first startup or a periodic tank check. After the check, it will try again at the next recipe check. Confirm water in the Input Hatch and source blocks in the tank, then wait and observe. If it still cannot run, use the troubleshooting section below.

## Steam Supply, Water Supply, and Throughput

The Steam Purifier can process up to eight copies of **the same recipe** at once. This does not mean it can process eight different minerals in one cycle. Actual parallels also depend on input quantities, recipe water, output space, and the parallel limit set in the GUI.

The basic structure takes approximately 1.6× the recipe duration shown in NEI, while the high pressure structure takes approximately 0.8×. A typical ordinary Water washing recipe shown as 25 seconds takes roughly 40 seconds in the basic structure or 20 seconds in the high pressure structure. A Simple Dust Washer recipe shown as five ticks takes roughly eight ticks in the basic structure or four ticks in the high pressure structure. Actual continuous throughput also depends on recipe checks, input supply, and output handling.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
| Maximum parallels | 8 | 8 |
| Processing duration relative to NEI | Approximately 1.6× | Approximately 0.8× |
| Steam consumption rate for the same recipe and parallel count | 1× | 2× |
| Total steam consumption per recipe | Baseline | Approximately the same as the basic structure |
| Water per recipe | As specified by the NEI recipe | Same as the basic structure |

Parallels increase the number of recipes processed in a cycle without dividing the cycle's duration by the parallel count. At eight parallels, a typical ordinary Water washing cycle requires **8,000 L of Water**, a Distilled Water cycle requires **1,600 L of Distilled Water**, and a simple washing cycle requires **800 L of Water**. If the tank still needs automatic filling at startup, provide additional ordinary Water for that separately.

Simple Washer mode uses little water per recipe, but processes quickly, so the Input Hatch buffer and water pipes can still become bottlenecks. The high pressure upgrade does not reduce water per recipe. With processing speed doubled, continuous production also requires a higher water supply rate.

The Steam Hatch buffers 64,000 L of steam, but this only covers temporary shortfalls and cannot replace continuous boiler production. Size boilers and pipes for the **steam consumption rate while processing**, and also watch whether the Input Hatch's water supply keeps up.

Use Waila to check the operating steam consumption rate and watch whether the buffer keeps falling during continuous processing. If a value is shown in L/t, multiply by 20 to get L/s at the normal 20 TPS. Use matching units when comparing pipe throughput. If steam or water supply is insufficient, lower the parallel limit in the GUI, then increase boiler production or improve the piping.

> [!WARNING]
> Running out of steam during processing aborts the current operation, and materials already consumed are not returned. Check steam production and pipe throughput before upgrading to high pressure or increasing the parallel limit.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Gear Box Casings, and Bronze Pipe Casings with the Solid Steel Machine Casings, Steel Gear Box Casings, and Steel Pipe Casings listed in the table. Glass does not participate in the bronze versus steel tier check, so the existing ordinary glass can be reused.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam, water, and production.

High pressure is the machine's structure tier. It still uses ordinary steam, and the existing Steam Hatch, steam buses, and Input Hatches can be reused. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels, and MV or higher-tier recipes remain unavailable.

## Automation and Output Routing

Steam Input and Output Buses each have four item slots. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Input:** Use hoppers, GT item pipes, conveyors, or item conduits to send minerals into the front face of the Input Bus. Filter by forms such as Crushed Ore, Impure Dust, and Purified Dust.
- **Output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to main output storage, byproduct storage, or the next machine.
- **Steam and water:** Use separate lines, connecting steam to the Steam Hatch and water to Input Hatches. Arrange separate buffers and interfaces for washing with Distilled Water and filling the tank with ordinary Water.
- **Byproducts:** In Ore Washer mode, handle Stone Dust and mineral byproducts as well as the main output. Filtering only the main output will leave other items accumulating in the bus.
- **Mode changes:** Stop material input and wait for the current operation to finish. Check the mode and remaining inputs before resuming transfer, so subsequent materials are not processed through the other route unintentionally.

Ore washing recipes can produce several different items at once. A single Output Bus with four slots may not hold all products during continuous processing. Additional Output Buses expand output space, but do not raise the parallel limit. Keep at least 55 actual casings when adding hatches or buses, and do not install a second Steam Hatch.

> [!WARNING]
> To collect all byproducts, set the GUI's voiding mode to "Do Not Void" and provide space for every output. If item voiding is enabled, main products or byproducts may be discarded when the output is blocked.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Is the structure nine blocks wide, five deep, and six tall? Is the controller at the front center of the small cube's second layer? Are pipes, Gear Box Casings, glass, and water positions arranged as shown in the hologram? |
| Structure tier mismatch | Are the casings, Gear Box Casings, and Pipe Casings all of the same tier? Were only some bronze components replaced? |
| Missing hatch or bus | Is there exactly one Steam Hatch and at least one steam Input Bus, steam Output Bus, and Input Hatch? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding hatches | Are at least 55 actual casings left? Were glass, Gear Box Casings, or Pipe Casings replaced with hatches? |
| Tank does not fill automatically | Is there ordinary Water in the Input Hatch? Each empty water position requires 1,000 L. Distilled Water alone cannot fill the tank automatically; you can also place source blocks with buckets. |
| Tank has water but processing does not start | Does the Input Hatch still contain the water required by the recipe? Tank water cannot replace recipe water. Are there only flowing water blocks instead of sources? |
| Brief "No Water" message | The machine may be performing its first or periodic tank check. Confirm water quantities and wait for the next recipe check. If it still cannot run, check the mode, recipe, and structure. |
| Minerals present but no recipe found | Is the correct Ore Washer or Simple Washer mode selected? Does a corresponding recipe exist? Were Purified Crushed Ore and Purified Dust confused? Is the input water type correct? |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| No Stone Dust or mineral byproducts | Is Simple Washer mode selected? Are the byproducts chance-based? Is item voiding enabled? Have pipes already extracted them? |
| Insufficient output space | Is there room for every output? Is one four-slot Output Bus insufficient? Are Stone Dust or byproducts left in the bus? |
| Only low parallels or frequent waiting | Are input quantities, Input Hatch water, and output space sufficient? Can water supply keep up with Simple Washer mode? Is the GUI parallel limit set too low? |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |

For general structure checks and tool use, see [Multiblock Machines](../multiblocks_index.md).

## Related Pages

- [GTNH Wiki: Steam Purifier](https://wiki.gtnewhorizons.com/wiki/Steam_Purifier)