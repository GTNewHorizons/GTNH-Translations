---
item_ids:
  - gregtech:gt.blockmachines:31084
navigation:
  title: Steam Blender
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31084
  position: 7
quest_ids:
  - WEwrzX4ZRkSxJ3M6cBesfA
---

# Steam Blender

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" /> is a multiblock Mixer available in the Steam age. It uses steam to mix materials in batches and can process up to eight copies of the same recipe at once. It can make Bronze Dust, Brass Dust, Fireclay Dust, and other materials, and can directly accept and output fluids to make eligible products such as Salt Water.

The machine has basic bronze and high pressure steel structures that share the same controller. It makes eligible Mixer recipes available in the Steam age. Upgrading to the high pressure structure increases throughput, but does not raise the maximum recipe tier.

| Property | Details |
| --- | --- |
| Unlock tier | Steam; the controller recipe requires Tumbaga Rings, Tumbaga Rotors, a Tumbaga Frame Box, and other materials |
| Dimensions | 5×5 footprint, four blocks tall; controller at the front center of the second layer |
| Power | Exactly one Steam Hatch; no Energy Hatch |
| Recipe range | Mixer recipes without fluid cells at LV or below, requiring no more than 32 EU/t |
| Item interfaces | Steam Input and Output Buses; ordinary electric machine item buses cannot replace them |
| Fluid interfaces | Ordinary Input Hatches supply recipe fluids, and ordinary Output Hatches collect fluid products; separate from the Steam Hatch used for power |
| Parallels | Up to eight copies of the same recipe; the high pressure structure does not raise this limit |
| Processing duration | Approximately 1.6× the duration shown in NEI for the basic structure, or 0.8× for the high pressure structure |
| Upgrades and overclocking | The high pressure structure doubles speed and steam consumption rate; no voltage overclocking |
| Maintenance and pollution | No maintenance, no pollution, and no Muffler Hatch required |

## Crafting and Construction

The current recipes for the controller, basic casing, and Steam Hatch are shown below. Click the items in the table to view recipes for the other components.

<RecipesFor id="gregtech:gt.blockmachines:31084" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Structure Materials

The following setup uses one Steam Hatch, one Input Bus, one Output Bus, one Input Hatch, and one Output Hatch to handle item and fluid recipes. The basic structure uses bronze components, while the high pressure structure uses their steel counterparts. **The casings, Frame Boxes, Gear Box Casings, and Pipe Casings in one machine must all be of the same tier.**

| Component | Basic structure | High pressure structure | Quantity and position |
| --- | --- | --- | --- |
| Casing | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | 35 in the setup described above; may be replaced with the hatches or buses below, but at least 25 actual casings must remain |
| Frame Box | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Four: one in front of, behind, to the left of, and to the right of the central Gear Box Casing on the second layer |
| Gear Box Casing | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Two: one at the center of each of the second and fourth layers |
| Pipe Casing | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | One, at the center of the third layer |
| Controller | <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" /> | Same controller | One, at the front center of the second layer |
| Steam Hatch | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Same hatch | Exactly one, replacing a casing |
| Input Bus | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Same bus | Install as needed for item inputs, replacing a casing; can also provide the Programmed Circuit setting |
| Output Bus | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Same bus | Install as needed for item outputs, replacing a casing |
| Input Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Same hatch | Install as needed for fluid inputs, replacing a casing |
| Output Hatch | For example, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Same hatch | Install as needed for fluid outputs, replacing a casing |

The new structure has 40 positions for casings or hatches. Installing the five interfaces listed above leaves 35 casings. For mixing only dusts, a Steam Hatch, steam Input Bus, and steam Output Bus are sufficient, leaving 37 casings. Adding buses or hatches reduces the casing count accordingly, but at least 25 actual casings must remain. Hatches and buses cannot replace Frame Boxes, Gear Box Casings, or Pipe Casings.

The structure check requires at least one type of recipe input interface and at least one type of output interface; it does not require every item and fluid interface to be installed. For actual processing, provide interfaces for all recipe inputs and outputs. When several input fluids are required, a single ordinary Input Hatch cannot hold them all at once, so provide the corresponding number of Input Hatches.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. Master channel tier 1 selects the basic structure, and tier 2 selects the high pressure structure. After assisted construction, install the hatches and check the structure.

## Machine Uses

### Recipe Map and Fluid Cells

The Steam Blender uses the **Multiblock Mixer recipe map**, shown as **Multiblock Mixer** in English NEI. Singleblock Mixer recipes involving fluid cells usually become recipes that directly accept and output the corresponding fluids in this map. Item requirements, including Programmed Circuits, must still be met.

When checking NEI, confirm that the recipe belongs to this map, then check item quantities, fluid types and quantities, Programmed Circuit configuration, recipe tier, and all outputs.

| Use | Common recipes and considerations |
| --- | --- |
| Mixing alloy dusts | Copper Dust and Tin Dust become Bronze Dust; Copper Dust and Zinc Dust become Brass Dust. Check input ratios and circuit configuration; the product is dust, not ingots. |
| Fireclay Dust | Mixes Brick Dust and Clay Dust for subsequent refractory material recipes |

> [!NOTE]
> The machine is available in the Steam age, but only accepts recipes up to LV. Check the recipe's EU/t to determine whether an alloy dust, chemical mixture, or other material can be processed. The high pressure steel structure does not enable MV or higher-tier recipes.

### Programmed Circuits and Bronze Dust

Many Mixer recipes require a <ItemLink id="gregtech:gt.integrated_circuit:1" showIcon="left" />. Set the configuration required by NEI in the circuit slot of the steam Input Bus GUI.

The current common Bronze Dust recipe requires **three Copper Dust, one Tin Dust, and a Programmed Circuit configured to 1** per recipe, producing **four Bronze Dust**. Send Copper Dust and Tin Dust into the steam Input Bus, set the circuit configuration to 1, and collect Bronze Dust through the steam Output Bus.

At eight parallels, one cycle consumes 24 Copper Dust and eight Tin Dust and produces 32 Bronze Dust. Keep a 3:1 input ratio during continuous operation so Copper Dust does not fill every slot and prevent Tin Dust from entering.

Arrange subsequent smelting for Bronze Dust using NEI. Other alloy dusts may require an Electric Blast Furnace or other machines.

### First Startup

1. Check the structure and confirm that the Steam Hatch and required item and fluid interfaces are installed.
2. Connect the steam pipe to the Steam Hatch, and supply each recipe fluid to its ordinary Input Hatch.
3. Check the recipe without fluid cells, all input quantities, Programmed Circuit configuration, and recipe tier in NEI.
4. Set the circuit, leave space for all item and fluid outputs, then start with a small amount of material.
5. Observe the steam buffer, input ratios, and outputs. Increase parallels after confirming continuous input supply and output collection.

## Steam Supply and Throughput

The Steam Blender can process up to eight copies of **the same recipe** at once. This does not mean it can run eight different recipes in one cycle, or that a cycle only consumes eight items. Actual parallels also depend on input ratios, item and fluid quantities, output space, and the parallel limit set in the GUI.

The basic structure takes approximately 1.6× the recipe duration shown in NEI, while the high pressure structure takes approximately 0.8×. For example, the Bronze Dust recipe shown as two seconds takes roughly 3.2 seconds in the basic structure or 1.6 seconds in the high pressure structure. Parallels increase the number of recipes processed in a cycle without dividing the cycle's duration by the parallel count.

| Property | Basic structure | High pressure structure |
| --- | --- | --- |
| Accepted recipe tiers | LV and below | LV and below |
| Maximum parallels | 8 | 8 |
| Processing duration relative to NEI | Approximately 1.6× | Approximately 0.8× |
| Steam consumption rate for the same recipe and parallel count | 1× | 2× |
| Total steam consumption per recipe | Baseline | Approximately the same as the basic structure |
| Inputs and outputs per recipe | As specified by the NEI recipe | Same as the basic structure |

The high pressure upgrade increases speed and steam consumption rate together. It mainly improves throughput, with approximately the same total steam cost per recipe as the basic structure. Actual duration and steam consumption are also affected by tick and integer rounding. During continuous production, item and recipe fluid transfer rates must increase along with processing speed.

The Steam Hatch buffers 64,000 L of steam, but this only covers temporary shortfalls and cannot replace continuous boiler production. Size boilers and pipes for the **steam consumption rate while processing**, and use separate lines for recipe fluids.

Use Waila to check the operating steam consumption rate and watch whether the buffer keeps falling during continuous processing. If a value is shown in L/t, multiply by 20 to get L/s at the normal 20 TPS. Use matching units when comparing pipe throughput. If steam supply is insufficient, lower the parallel limit in the GUI, then increase boiler production or improve the piping.

> [!WARNING]
> Running out of steam during processing aborts the current operation, and items and recipe fluids already consumed are not returned. Check steam production and pipe throughput before upgrading to high pressure or increasing the parallel limit.

## Upgrading to High Pressure

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={2} />
</GameScene>

The high pressure structure keeps the same dimensions, hatch positions, and controller. Replace **all** Bronze Plated Bricks, Bronze Frame Boxes, Bronze Gear Box Casings, and Bronze Pipe Casings with the Solid Steel Machine Casings, Steel Frame Boxes, Steel Gear Box Casings, and Steel Pipe Casings listed in the table.

Stop processing and material input before upgrading. After replacing the components, check the structure again and confirm the machine displays the high pressure tier before restoring steam, inputs, and production.

High pressure is the machine's structure tier. It still uses ordinary steam, and the existing Steam Hatch, steam buses, and ordinary Input and Output Hatches can be reused. The upgrade doubles speed and steam consumption rate, but the maximum remains eight parallels, and MV or higher-tier recipes remain unavailable.

## Automation and Output Routing

Steam Input and Output Buses each have four item slots, and the Input Bus has an additional circuit slot. They do not automatically pull from adjacent chests or push products into them; placing a chest next to a bus is not enough for automation.

- **Item input:** Use hoppers, GT item pipes, conveyors, or item conduits to send materials into the front face of the Input Bus. Supply the correct recipe ratios and reserve slots for each dust type.
- **Item output:** Actively extract from the front face of the Output Bus with pipes, conduits, or conveyors, then route products to material storage or the next processing machine.
- **Fluid input:** Use separate lines and Input Hatches for each fluid type, checking filters, fluid locks, and quantities. Connect the steam supply line to the Steam Hatch.
- **Fluid output:** Extract products from the Output Hatch, or place a tank against its front face for automatic output.
- **Programmed Circuit:** Keep the required configuration when producing one material. Before changing recipes, stop input and wait for the current operation to finish, then handle remaining items and fluids and adjust the circuit.
- **Hatch colors:** Leave hatches unpainted during initial construction if desired. After painting them, make sure the items, fluids, and circuit required by one recipe can still be read as part of the same input group.

If a recipe requires more item types than one bus can hold, add steam Input Buses. Multiple fluids or large quantities per cycle may also require additional hatches. Keep at least 25 actual casings when adding interfaces, and do not install a second Steam Hatch.

> [!WARNING]
> To collect all products, set the GUI's voiding mode to "Do Not Void" and provide space for every item and fluid output. If fluid voiding is enabled, Salt Water, Aqua Regia, and other products may be discarded when an Output Hatch is missing or blocked.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Incomplete structure | Is the footprint 5×5 and the height four blocks? Is the controller at the front center of the second layer? Are Frame Boxes, Gear Box Casings, and Pipe Casings positioned as shown in the hologram? |
| Structure tier mismatch | Are the casings, Frame Boxes, Gear Box Casings, and Pipe Casings all of the same tier? Were only some bronze components replaced? |
| Missing input or output interface | Is at least one type of recipe input and one type of output installed? Are both the item buses and fluid hatches required by the recipe present? |
| Missing Steam Hatch or unable to install steam buses | Is there exactly one Steam Hatch? Were ordinary electric machine item buses used by mistake? |
| Structure fails after adding hatches | Are at least 25 actual casings left? Were any Frame Boxes, Gear Box Casings, or Pipe Casings replaced with hatches? |
| Dusts present but no recipe found | Do input forms, types, and ratios match NEI? Are quantities sufficient and the circuit configuration correct? Was a mixing recipe for another machine checked by mistake? |
| Filled fluid cells do not process | Was a singleblock recipe checked? Confirm direct fluid inputs in the recipe map without cells, then supply ordinary Input Hatches. |
| Both acids present but Aqua Regia does not process | Is the required circuit configuration set? Are the two fluids in separate ordinary Input Hatches? Is output space available? Have hatch colors separated the inputs? |
| Alloy dust appears instead of ingots | This is the normal output of a dust mixing recipe. Arrange subsequent smelting using NEI. |
| Recipe tier too high | Does the recipe shown in NEI exceed LV? The high pressure structure also cannot process MV or higher-tier recipes. |
| Only low parallels | Is there enough of every item and fluid input? Do hatch capacity or output space limit the amount per cycle? Is the GUI parallel limit set too low? |
| Item outputs appear but fluids are missing | Is an ordinary Output Hatch installed? Is it locked to the wrong fluid? Is fluid voiding enabled? Have pipes already extracted the product? |
| Insufficient output space | Is there room for all item and fluid outputs? Are Output Buses or Output Hatches blocked? Are extraction and filter settings correct? |
| Machine stops despite steam in the hatch | Can the continuous supply keep up? Are pipes restricted or sharing steam with other machines? Do the current parallel count and high pressure tier exceed boiler capacity? |
| Chest next to a bus does not transfer items | Steam buses do not automatically pull or push items. Check the active transfer equipment, connection face, direction, and filters. |

For general structure checks and tool use, see [Multiblock Machines](./multiblocks_index.md).

## Related Pages

- [GTNH Chinese Wiki: Steam Blender](https://gtnh.huijiwiki.com/wiki/大型蒸汽搅拌机)