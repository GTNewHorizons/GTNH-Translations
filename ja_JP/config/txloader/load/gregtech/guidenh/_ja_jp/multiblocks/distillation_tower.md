---
item_ids:
  - gregtech:gt.blockmachines:1126
navigation:
  title: Distillation Tower
  parent: ./multiblocks-index.md
  icon: gregtech:gt.blockmachines:1126
  position: 11
---

# Distillation Tower

<GameScene interactive={true} wrap="square" align="right" width="320" height="300">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1126" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> (Distillation Tower, abbreviated DT and often called the "large distillery") is an HV-tier processing multiblock. It separates one fluid into all of the fractions listed by its NEI recipe at the same time. As a direct upgrade from the singleblock Distillery, it is commonly used to process oil, Wood Tar, biomass, and many chemical fluids.

The required height of a Distillation Tower depends on the number of fluid outputs in the recipe. Each fluid output occupies its own output layer, so check the target recipe before building instead of copying the height of another tower.

| Property | Details |
| --- | --- |
| Unlock tier | HV; the controller recipe requires EV-tier circuits, so a Cleanroom is generally needed first |
| Structure size | 3×3×3–12, hollow above the bottom layer and capped at the center of the top layer |
| Power | Standard Energy Hatches; multiple hatches are allowed, but Multi-Amp Energy Hatches and Laser Energy Hatches are not supported |
| Overclocking | Standard imperfect overclocking: each overclock uses 4× the power and halves the duration |
| Processing bonuses | Maximum parallel of 1, with no additional speed or power bonuses |
| Maintenance and pollution | Requires maintenance, produces no pollution, and does not need a Muffler Hatch |

## Crafting and Construction

The current recipes for the controller and Clean Stainless Steel Machine Casing are shown below.

<RecipesFor id="gregtech:gt.blockmachines:1126" />

<RecipesFor id="gregtech:gt.blockcasings4:1" />

The Distillation Tower has a fixed 3×3 footprint and a variable height. Place the controller in the center of the front face on the bottom layer, and put the input interfaces on that layer. Starting with the second layer, every layer must contain at least one Output Hatch. Keep the center of each intermediate layer as air and cap the center of the top layer with a Clean Stainless Steel Machine Casing.

For a total height of $$h$$, the structure must retain at least $$7h-5$$ actual Clean Stainless Steel Machine Casings. Hatches and buses do not count toward this minimum.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> | 1, in the center of the front face on the bottom layer |
| <ItemLink id="gregtech:gt.blockcasings4:1" showIcon="left" /> | At least 16–79 |
| Input Hatch | At least 1, in any bottom-layer casing position |
| Input Bus | Optional, in any bottom-layer casing position; install one when a recipe requires item inputs |
| Output Bus | Optional, in any bottom-layer casing position; install one when a recipe produces item outputs |
| Output Hatch | At least 1 on every layer above the bottom, for a total minimum of 2–11 |
| Standard Energy Hatch | At least 1, in any suitable casing position |
| Maintenance Hatch | 1, in any suitable casing position |

The minimum 3-layer structure needs 2 output layers and at least 16 casings. A common recipe with four fluid outputs needs a 5-layer structure, 4 output layers, and at least 30 casings. The maximum 12-layer structure can handle 11 fluid outputs and needs at least 79 casings.

A layer can contain more than one Output Hatch, but adding hatches cannot reduce the casing count below the minimum. Using one Output Hatch per layer is usually the easiest arrangement to route. Additional hatches on a layer only add buffering or another output interface for the same fluid assigned to that layer; they do not allow the machine to process another output.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview the structure and assist with construction. Right-click in the air to open the channel settings, set the `height` subchannel from 3 to 12 to choose the total projected height, then use the projector on the controller.

## Capabilities

A singleblock Distillery normally uses a Programmed Circuit to select one target fraction, while the other fractions are not produced at the same time. The Distillation Tower runs its own Distillation Tower recipes and obtains every fluid output from the same batch of input. This is the main reason it improves material efficiency and simplifies complex chemical processing lines.

Common uses include:

- **Oil fractionation**: Produces fractions such as Heavy Fuel, Light Fuel, Naphtha, and Refinery Gas at the same time, supplying Diesel, Cetane-Boosted Diesel, and oil-cracking production lines.
- **Wood chemistry**: Processes Wood Tar, Wood Vinegar, and Wood Gas into fuels and chemical feedstocks such as Benzene, Toluene, Phenol, and Methanol.
- **Biomass processing**: Recovers multiple byproducts from fluids such as Fermented Biomass.
- **Chemical separation**: Processes diluted acids, cracked fuels, and other fluids whose recipes contain multiple useful outputs.

Follow NEI's Distillation Tower recipe for the exact inputs, outputs, Programmed Circuit, power usage, and duration. Some recipes include item inputs or item byproducts, so fluid hatches alone are not always sufficient.

## Tower Height and Layered Outputs

First count the number of **fluid outputs** $$n$$ in the NEI recipe; item outputs do not affect tower height. The required total height is:

$$
h=\max(3,n+1)
$$

The minimum height is always 3, so even a recipe with only one fluid output still requires two output layers. A structure may be taller than the recipe requires, in which case the extra Output Hatches at the top remain unused, but it cannot be shorter than required.

Read fluid outputs in NEI **from left to right, then from bottom to top**. The first fluid output goes to the Output Hatch on the second layer, the second goes to the third layer, and so on. For example, a recipe with four fluid outputs uses layers two through five and therefore requires a tower at least 5 layers tall.

> [!WARNING]
> Output Hatches are not assigned automatically according to their existing fluid or connected pipe filters. Connecting the wrong layer sends a product into the wrong tank or pipe, which can mix fluids or block the production line. Recheck every layer against NEI whenever the recipe changes.

## Power and Throughput

HV is the tier at which the controller becomes available, but the Distillation Tower is not limited to HV power. Its available voltage is determined by the installed standard Energy Hatches. Replacing them with higher-tier hatches allows the machine to process higher-voltage recipes and [overclock](../tierskipping-overcloking-parallels/overclocking.md). Two standard Energy Hatches of the same tier can also provide [dual-hatch tier skipping](../tierskipping-overcloking-parallels/tierskipping.md) under the normal multiblock rules.

The Distillation Tower does not support Multi-Amp Energy Hatches or Laser Energy Hatches and has no parallel capability. Each standard imperfect overclock uses 4× the power and halves the duration. The machine can continue overclocking after reaching 1 tick, but this does not make it process multiple copies of a recipe at once.

Producing every fraction at the same time is a property of the Distillation Tower's recipes, not a parallel bonus. When evaluating throughput, use the input amount, duration, and power shown in the Distillation Tower recipe in NEI rather than extrapolating from one output recipe of a singleblock Distillery.

> [!WARNING]
> Losing power during processing aborts the current recipe and destroys the inserted inputs. After upgrading Energy Hatches or using dual-hatch tier skipping, make sure the cables, transformers, and generators can continuously provide the required power.

## Automation and Output Routing

Connect every output layer to a separate fluid pipe and tank. The Distillation Tower only starts its next operation when all relevant products have output space, so filling the buffer for one low-demand byproduct can stop the entire tower.

| Method | Considerations |
| --- | --- |
| Standard Output Hatch | Connect each layer to a separate tank; the tank should buffer temporary downstream shutdowns |
| ME Output Hatch | Each output layer still needs its own hatch; right-click the hatch with Wire Cutters to allow ME cables to connect from any side |
| Void Overflow | Enable it only when the affected product can safely be discarded; fluid that cannot enter a full downstream destination is permanently destroyed |
| Shared casings or hatches | Wallsharing saves materials, but shared Output Hatches can make two towers block each other unless their outputs on that layer are compatible |

If a recipe needs a Programmed Circuit or another item input, install an Input Bus on the bottom layer. If it produces dust or another item output, install an Output Bus as well. After connecting the automation, process one batch first and verify the actual product and destination tank on every layer before enabling continuous input.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Structure is incomplete | The total height is 3–12; each intermediate center is air; the top center is capped; every layer above the bottom has an Output Hatch; at least $$7h-5$$ actual casings remain |
| Insufficient output space | The tower is tall enough for every fluid output; the relevant Output Hatch, pipe, or tank is not full; an Output Bus is installed when the recipe has an item output |
| Inputs and power are present but no recipe is available | The input fluid, Programmed Circuit, and other items match NEI; items are in an Input Bus; the Energy Hatch provides sufficient voltage |
| Products enter the wrong pipe | Re-read NEI from left to right and bottom to top, then compare it with the Output Hatches from the second layer upward |
| The tower still forms at its old height after being extended | The old top-center cap was removed; every new layer has an Output Hatch; a manual structure check was run after construction |
| Machine stops immediately after starting | Check available power, cable loss, energy buffers, and maintenance status before inserting more test materials |

See [Multiblock Machines](./multiblocks-index.md) for general multiblock operation. In IV, the Dangote Distillus becomes available; in LuV, the Mega Distillation Tower can provide greater throughput.

## References

- [GTNH Wiki: Distillation Tower](https://wiki.gtnewhorizons.com/wiki/Distillation_Tower)