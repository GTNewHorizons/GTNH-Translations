---
item_ids:
  - gregtech:gt.blockmachines:1000
navigation:
  title: Electric Blast Furnace
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:1000
  position: 5
quest_ids:
  - AAAAAAAAAAAAAAAAAAAATQ
---

# Electric Blast Furnace

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1000" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> (Electric Blast Furnace, abbreviated EBF) is a processing multiblock available in LV. Electricity and Heating Coils let it reach temperatures that a Bricked Blast Furnace cannot. Its first major use is usually producing aluminium; later, it handles many metals and other materials that require high-temperature processing.

The EBF is usually a new player's first **GT electric multiblock**, and an important step toward MV materials. Building it brings together structure requirements, item and fluid interfaces, maintenance, and continuous power. The experience of getting your first EBF running reliably carries over to many later multiblocks.

The tier at which you obtain the controller is separate from the power required by its recipes. Although your first Energy Hatches are LV, common aluminium recipes need MV power. Two LV Energy Hatches and a sufficient power supply allow an early EBF to run these recipes.

| Property | Details |
| --- | --- |
| Unlock tier | LV; two LV Energy Hatches commonly provide the power for early MV recipes |
| Structure size | 3×3×4; the center of each of the two middle layers is air |
| Power | Supports multiple normal Energy Hatches; does not support Multi-Amp Energy Hatches or Laser Target Hatches |
| Overclocking and parallels | Normally uses regular overclocks; sufficient excess heat converts some into perfect overclocks; no additional parallel bonus |
| Processing bonuses | Every 900 K above the recipe requirement multiplies power use by 95%; every 1800 K allows one perfect overclock |
| Maintenance and pollution | Requires maintenance and a Muffler Hatch; base pollution is 400 gibbl/s, with actual emissions reduced by the Muffler Hatch tier |

For a first build, start with **Cupronickel Coils, two LV Energy Hatches, short cables, and a small batch of aluminium ingredients**. Forming the structure is only the first step: the recipe, temperature, output space, and continuous power supply must all be suitable before processing can finish successfully.

## Crafting and Construction

### Understanding the Controller and Interfaces

The controller displays machine status, checks the structure, and provides controls. Items, fluids, and power enter through the components below. Buses and hatches only become part of the EBF when installed in valid structure positions.

| Component | Purpose |
| --- | --- |
| Input Bus | Holds item ingredients such as dusts and Programmed Circuits |
| Output Bus | Receives item products such as ingots and hot ingots |
| Input Hatch | Supplies fluids required by the recipe, such as nitrogen |
| Output Hatch | Receives fluid products listed in the recipe |
| Energy Hatch | Receives EU from the external power network and powers the multiblock |
| Maintenance Hatch | Allows tools to repair maintenance issues |
| Muffler Hatch | Vents pollution; its vent face must remain clear |

An Input Bus and an Input Hatch serve different purposes. Putting dust in the controller's slot, or connecting a fluid pipe to an Input Bus, does not replace the required interfaces.

### Preparing the Components

Current recipes for the controller and Heat Proof Machine Casings are shown below. Heating Coils come in several tiers; check NEI for their materials and recipes before crafting them.

<RecipesFor id="gregtech:gt.blockmachines:1000" />

<RecipesFor id="gregtech:gt.blockcasings:11" />

<RecipesFor id="gregtech:gt.blockcasings5:0" />

The bottom layer holds the controller and most interfaces. Each of the two middle layers is a ring of eight Heating Coils of the same tier, with air in the center. The top center must contain the Muffler Hatch. Fill the remaining bottom and top-ring positions with Heat Proof Machine Casings, or with interfaces allowed in those positions.

| Component | Quantity and position |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> | One, at the front center of the bottom layer |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> or other Heating Coils | Sixteen, in the two middle layers; all must be the same tier |
| <ItemLink id="gregtech:gt.blockcasings:11" showIcon="left" /> | 0–12, filling unused positions in the bottom layer and top ring |
| Normal Energy Hatch | At least one, in the bottom layer; two <ItemLink id="gregtech:gt.blockmachines:41" showIcon="left" />s are commonly used for early MV recipes |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | One, in the bottom layer |
| <ItemLink id="gregtech:gt.blockmachines:91" showIcon="left" /> | One, at the top center; keep its vent face unobstructed |
| Input Bus or Input Hatch | At least one input interface, in the bottom layer; provide item and fluid inputs as required by the recipe |
| Output Bus or Output Hatch | At least one output interface; Output Buses go in the bottom layer, while Output Hatches can also occupy the top ring |

At least one input and one output interface are required. With only two LV Energy Hatches, one Maintenance Hatch, one Input Bus, and one Output Bus, you need **11 Heat Proof Machine Casings** for the remaining positions. Additional fluid hatches or buses can replace casings in allowed positions; they cannot replace coils or the Muffler Hatch.

The animation below also includes an <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> for recipes that use gas, so it uses **10 Heat Proof Machine Casings**. If your first recipe has no fluid input, you can initially leave a casing there and replace it with an Input Hatch later.

### Building Layer by Layer

Press play to see the construction sequence, or drag the timeline to revisit a step. The animation starts with the controller, then adds the bottom-layer interfaces, both coil rings, the top layer, and a roof for rain protection.

<GameScene interactive={true} width="480" height="340">
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_build.json" />
</GameScene>

1. **Choose the front and place the controller.** Reserve a 3×3 base and place the controller at its front center, facing outward. Leave access to maintenance, item and fluid interfaces, and cable connections.
2. **Complete the base.** The other eight bottom-layer positions accept Energy Hatches, a Maintenance Hatch, and input/output interfaces. Fill unused positions with Heat Proof Machine Casings. The bottom center is also part of the structure and must not be left empty.
3. **Place the first coil ring.** Build a 3×3 ring of eight Cupronickel Coils above the base, leaving air in the center.
4. **Place the second coil ring.** Add another ring of the same coils, for sixteen in total. All coils must be the same tier; do not mix Cupronickel and Kanthal layers.
5. **Finish the top and install the Muffler Hatch.** Put the Muffler Hatch in the center of the fourth layer, normally venting upward. Fill the outer eight positions with casings, or substitute fluid Output Hatches where needed.
6. **Check the structure.** Keep both middle-layer center blocks clear of torches, cables, pipes, and other blocks. If the EBF does not form, recheck the structure in the controller GUI and look for missing or incorrectly placed components.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview and help build the structure. The `coil` subchannel selects the coil tier. After construction, check the structure at the controller and repair maintenance issues at the Maintenance Hatch.

> [!WARNING]
> Protect Energy Hatches, generators, and Battery Buffers from rain. Leave at least one air block in front of the Muffler Hatch's vent and build the roof higher up. Do not place a roof directly on an upward-facing Muffler Hatch or block its vent with cables or pipes.

Older guides may require gas Output Hatches in the top ring to recover exhaust gases. That special exhaust recovery system has been removed in the current version. If a recipe produces fluids, provide Output Hatches for the outputs shown in NEI; bottom-layer Output Hatches can receive gases too. The top ring remains a valid location for Output Hatches.

### Completing Maintenance

A newly placed EBF usually has maintenance issues. Open the Maintenance Hatch, hold the relevant GT tool on your cursor, and click its maintenance button to repair the issue. The Soldering Iron also needs charge and solder. Return to the controller afterward and confirm that every issue has been repaired.

| Controller message | Tool |
| --- | --- |
| Pipe is loose | Wrench |
| Screws are loose | Screwdriver |
| Something is stuck | Soft Mallet |
| Platings are dented | Hard Hammer |
| Circuitry is burned out | Soldering Iron |
| Something does not belong here | Crowbar |

In LV, you can also put the tools in a Toolbox and right-click the Maintenance Hatch with it to repair several issues at once. Maintenance issues can occasionally recur while the machine runs, so keep the hatch accessible after automation.

Maintenance affects actual power use. One issue reduces EBF efficiency to 90%, raising a 120 EU/t recipe to about **133 EU/t**. This exceeds the nominal 128 EU/t output of four LV generators. Completing all maintenance is especially important for an early EBF powered through two LV Energy Hatches.

## Capabilities

The EBF runs recipes listed under Electric Blast Furnace in NEI. Common uses include aluminium, steel, high-temperature alloys, and dusts that require a specified temperature. Some recipes also require a Programmed Circuit or a gas input. A material may have several gas-assisted recipes with different times and costs.

When designing a production line, check the recipe's items, fluids, EU/t, temperature, and output type. Some recipes produce **hot ingots**, which need a [Vacuum Freezer](../hv/vacuum_freezer.md) before further processing. Regular ingots do not need freezing.

Input Buses hold dusts and Programmed Circuits; Input Hatches supply the gases or other fluids required by the recipe. Output Buses collect items, and Output Hatches collect fluids. You can install multiple input interfaces, but do not assume that every blast furnace recipe needs gas.

### Producing Your First Aluminium

Check the Electric Blast Furnace recipes for <ItemLink id="gregtech:gt.metaitem.01:11019" showIcon="left" /> in NEI. Choose one for which you can obtain all ingredients, fluids, and circuits. Different aluminium sources and gas options can have different processing times; do not apply one recipe's requirements to every aluminium recipe.

For your first trial, work through this checklist:

1. **Read the recipe requirements.** Check the ingredients, circuit setting, fluid quantity, EU/t, and temperature. An early build normally uses a 120 EU/t recipe that two LV Energy Hatches can support.
2. **Check structure and maintenance.** The controller should report no structure or maintenance issues, the Muffler Hatch should be able to vent, and the machine should be enabled.
3. **Prepare the outputs.** Leave enough space in the appropriate Output Bus and Output Hatch. Keep output protection enabled during your first trials so useful products are not voided as overflow.
4. **Prepare power first.** Let the boiler and generators stabilize, or charge the batteries beforehand. Make sure both Energy Hatches receive power continuously.
5. **Insert only a small batch.** Put dusts and the required circuit in an Input Bus and supply fluids to an Input Hatch. Watch one complete recipe finish.
6. **Add automation afterward.** Confirm that products reach the correct output interfaces and stored energy does not continually decrease before increasing the input quantity.

If the machine loses power during the trial, investigate the supply first. Repeatedly inserting more ingredients will not fix it. Steel is another important early use for the EBF; compare different ingredients and gas options before moving some steel production away from the Bricked Blast Furnace.

## Power and Overclocking

### Why Use Two LV Energy Hatches?

The EBF uses normal Energy Hatches. With only one normal Energy Hatch, recipe calculations use 1 A of available power. With two hatches of the same tier, their combined amperage can support recipes one tier higher. Each LV Energy Hatch accepts at most 2 A LV, giving a combined maximum of **4 A × 32 EU = 128 EU/t**. This supports common 120 EU/t MV recipes.

This form of tier skipping describes the higher-tier recipes the machine can run. **The external cables still carry 32 V LV power.** Supply more LV amperage; do not feed MV voltage directly into LV Energy Hatches. Cable capacity, generator count, and hatch count must all meet the power requirement.

| Configuration | Available power and use |
| --- | --- |
| One LV Energy Hatch | Recipe calculations use 1 A LV, or 32 EU/t; cannot start common 120 EU/t recipes |
| Two LV Energy Hatches | Accept up to 4 A LV combined, nominally 128 EU/t; suitable for early MV recipes |
| One MV Energy Hatch | Recipe calculations use 1 A MV, or 128 EU/t; requires a suitable MV supply and cables |

There is only **8 EU/t of headroom** between 128 EU/t and a 120 EU/t recipe. The following calculation assumes all four LV packets travel paths with the same loss and no other loads:

| Loss per packet before reaching a hatch | Maximum power received by the EBF | Headroom for a 120 EU/t recipe |
| --- | --- | --- |
| 0 EU | 4 × 32 = 128 EU/t | 8 EU/t |
| 1 EU | 4 × 31 = 124 EU/t | 4 EU/t |
| 2 EU | 4 × 30 = 120 EU/t | 0 EU/t |
| 3 EU | 4 × 29 = 116 EU/t | Insufficient power |

Real paths can have different cable lengths and losses, so calculate each separately. Energy Hatch buffers can temporarily sustain the machine, but a continually falling buffer means average input is insufficient. Starting successfully does not guarantee that the complete recipe will finish. See [Local Energy Networks](../../power/enet.md) and [Cable Loss](../../power/cable_loss.md) for details.

> [!WARNING]
> Losing power during processing aborts the current recipe and can destroy ingredients already consumed. Confirm sufficient continuous power before your first batch. Include cable losses instead of relying only on the generators' nominal output.

### Option 1: Direct Power Through Short Cables

Four <ItemLink id="gregtech:gt.blockmachines:1120" showIcon="left" />s can supply an early EBF, each outputting at most 1 A LV. The example below assigns two turbines to each Energy Hatch and keeps both branches short.

<GameScene interactive={true} width="480" height="340" zoom="1.2">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
  <ImportPonder src="/assets/ponders/ebf_power_direct.json" />
</GameScene>

- Each hatch receives power from two turbines; its branch needs at least 2 A LV capacity. If all four turbines share one supply trunk, that trunk needs at least 4 A capacity.
- Use a Wrench to face turbine energy outputs toward the cables. Steam must enter through valid fluid input faces; simply placing a turbine against an Energy Hatch does not guarantee a connection.
- Continuous turbine output requires continuous steam. An unwarmed boiler, exhausted fuel, or insufficient pipe distribution can stop a turbine from generating.
- This setup has very little headroom and is suited to a dedicated early EBF supply. Recalculate the load if you connect other machines.

When adding roofs over the turbines and Energy Hatches, keep the Muffler Hatch vent clear. The animation's arrows show connection directions; actual power still depends on cables, generators, and a steady supply of fuel and steam.

### Option 2: A Battery Buffer Near the EBF

You can place a <ItemLink id="gregtech:gt.blockmachines:171" showIcon="left" /> near the EBF, install four usable LV batteries, and connect both Energy Hatches through short cables. The buffer's maximum output amperage depends on the number of usable batteries: **a four-slot buffer with only one battery cannot output 4 A**.

<GameScene interactive={true} width="480" height="340" zoom="1.1">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <ImportPonder src="/assets/ponders/ebf_power_buffer.json" />
</GameScene>

This example uses eight LV Steam Turbines and also supplies other LV machines. Adjust the generator count to your actual load. Along with the EBF's 120 EU/t, account for cable losses, losses associated with the Battery Buffer, and other machines.

Point the buffer's output face toward the EBF branch and connect generators to its other valid input faces. The output trunk needs at least 4 A LV capacity, and each Energy Hatch branch needs at least 2 A. Size the generator-side cables for the combined current that can pass through them too.

The buffer smooths fluctuations from the generators and allows shorter cables near the EBF. It still needs enough average generation. Charge the batteries, then run several consecutive batches. If charge falls after each batch, increase generation, reduce cable loss, or reduce other loads. Adding battery capacity only delays the time at which the batteries run out.

> [!WARNING]
> Energy Hatch voltage limits still apply. Do not connect MV power directly to LV Energy Hatches. When upgrading to MV power, replace the hatches and check the cables too. Cables must meet both voltage and amperage limits or they may burn out.

### Upgrading Power and Overclocking

Higher-tier or additional normal Energy Hatches can support higher-power recipes and shorten processing through [tier skipping](../../tierskipping_overcloking_parallels/tierskipping.md) and [overclocking](../../tierskipping_overcloking_parallels/overclocking.md). Each regular overclock multiplies EU/t by four and halves duration. Available power and temperature still limit the number of overclocks.

For example, ignoring excess-heat discounts, one regular overclock raises a 120 EU/t recipe to about 480 EU/t and halves its duration. After upgrading the Energy Hatch, check generator count and steam supply again; the original 120 EU/t power budget is no longer sufficient.

## Temperature and Heating Coils

### Meeting the Recipe Requirement

Coils of the same tier determine the base temperature. Cupronickel Coils with two LV Energy Hatches provide **1801 K**, enough for aluminium recipes requiring 1300 K. Still check the specific recipe you choose.

| Coil | Temperature with two LV Energy Hatches or one MV Energy Hatch |
| --- | --- |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> | 1801 K |
| <ItemLink id="gregtech:gt.blockcasings5:1" showIcon="left" /> | 2701 K |
| <ItemLink id="gregtech:gt.blockcasings5:2" showIcon="left" /> | 3601 K |

The machine also adjusts temperature according to **the voltage tier of the sum of its normal Energy Hatches' nominal voltages**. MV is the baseline; each tier above it adds 100 K. One HV Energy Hatch with Cupronickel Coils therefore gives 1901 K. Changing the number of same-tier hatches can also change temperature. With only one LV Energy Hatch, Cupronickel Coils give 1701 K.

This temperature calculation is separate from incoming cable voltage, actual amperage, and cable loss. After upgrading coils or Energy Hatches, use a <ItemLink id="gregtech:gt.metaitem.01:32762" showIcon="left" /> to check the actual temperature. Do not infer it from the EU/t the machine is currently consuming.

If machine temperature is below the recipe requirement, more power will not make the recipe start. Replace all sixteen coils with the same tier and check coils shared with adjacent machines too.

### Benefits of Excess Heat

Every 900 K above the recipe requirement gives another multiplicative 5% power discount. Every 1800 K lets one regular overclock become a perfect overclock. A perfect overclock still multiplies EU/t by four, but divides duration by four, so that overclock does not increase total energy per recipe.

| Temperature above the recipe requirement | Power multiplier | Overclocks that can become perfect |
| --- | --- | --- |
| Less than 900 K | 100% | 0 |
| 900–1799 K | 95% | 0 |
| 1800–2699 K | 0.95 × 0.95 = 90.25% | 1 |
| 2700–3599 K | 0.95³ ≈ 85.74% | 1 |
| 3600–4499 K | 0.95⁴ ≈ 81.45% | 2 |

For example, one HV Energy Hatch and Nichrome Coils give 3701 K. An aluminium recipe requiring 1300 K has 2401 K of excess heat, giving two 5% power discounts and allowing one perfect overclock. Check NEI and the machine display for the resulting recipe power and duration.

Perfect overclocks improve overclocks that your power supply already supports. Extra heat does not create extra power. First get the early machine running reliably, then compare the costs of better coils, more power, and additional EBFs.

## Wall Sharing and Automation

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right">
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

Multiple EBFs can share side-wall casings and coils. Four in a 2×2 arrangement reduce the coil count from 64 for independent structures to 42. Shared coils must meet every connected machine's tier requirements, so check all affected EBFs when upgrading.

Maintenance Hatches and some input/output interfaces can also be shared. Power must cover all machines running simultaneously. Shared Energy Hatches make machines compete for amperage, which is especially likely to cause power failures when using two-hatch tier skipping.

For automation, arrange dust, circuit, and fluid inputs and leave enough output space for hot ingots, regular items, and fluids. If an EBF feeds a Vacuum Freezer, test with a small batch and confirm that only hot ingots requiring cooling reach it. See the [Vacuum Freezer guide](../hv/vacuum_freezer.md#hot-ingot-routing) for input filtering, item transport, and storage settings.

With multiple Input Buses, check the controller's **input separation** setting. When enabled, each bus's items are considered as a separate recipe group. Keep the dusts and circuit needed for a recipe in a bus that can match them together. Separate buses and circuits for different recipes can reduce unintended recipe matches.

Before obtaining a Vacuum Freezer, prioritize recipes that produce regular ingots and whose downstream processing is available to you. Later, you can dedicate EBFs to aluminium, steel, and high-temperature materials. Four EBFs sharing coils save structure materials, but simultaneous operation still requires enough power for all four.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Structure is incomplete | All sixteen coils are the same tier; both middle centers are air; the Muffler Hatch is in the top center; the base has Energy Hatches, a Maintenance Hatch, and input/output interfaces |
| A new machine has maintenance issues | Repair with all six tools at the Maintenance Hatch, then confirm at the controller; forming the structure and completing maintenance are separate steps |
| Insufficient temperature | Scan the actual temperature and check coil tier, power configuration, and the recipe's temperature requirement in NEI |
| Ingredients are present but no recipe is found | Check ingredient types and quantities, circuit setting, fluids, and EU/t; with input separation, make sure required items are not split across buses |
| Insufficient voltage or power | Check for two LV Energy Hatches in an early build, or suitable hatches for upgraded recipes; Input Bus tier does not determine machine voltage |
| Machine stops immediately after starting | Check generation, cable capacity and loss, and continuous power to the hatches; do not repeatedly insert expensive ingredients to test |
| Machine runs briefly, then loses power | Watch battery and hatch buffers for a continuous decline; check boiler steam output, pipe distribution, other loads, and maintenance |
| A four-slot Battery Buffer provides insufficient power | Check for four usable, charged LV batteries, the correct output face, and enough average generation |
| Insufficient output space | Check that the appropriate Output Buses and Output Hatches exist, are not full, and can hold the complete recipe output |
| Pollution cannot be vented | Check that the Muffler Hatch vents into air and that an advanced Muffler Hatch has any required Air Filter |
| Cables burn out or Energy Hatches explode | Check cable voltage and amperage limits, overvoltage at Energy Hatches, and exposure to rain |

See [Multiblock Machines](../../gtnh_basics/multiblocks.md) for general rules. As material demand grows, additional EBFs can divide the workload instead of relying only on repeated overclocks of one machine.

## References

- [GTNH Wiki: Electric Blast Furnace](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)