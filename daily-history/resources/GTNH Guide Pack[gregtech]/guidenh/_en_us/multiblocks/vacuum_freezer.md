---
item_ids:
  - gregtech:gt.blockmachines:1002
navigation:
  title: Vacuum Freezer
  parent: ./multiblocks-index.md
  icon: gregtech:gt.blockmachines:1002
  position: 10
---

# Vacuum Freezer

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1002" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> (Vacuum Freezer, abbreviated VF and often called the "freezer") is an HV-tier processing multiblock. It is commonly paired with the [Electric Blast Furnace](../tiers/lv/electric-blast-furnace.md) to cool its hot ingots into regular ingots that can undergo further processing.

Not every Electric Blast Furnace product needs cooling. Before setting up a production line, check the product's uses in NEI. If the furnace already produces a regular ingot, it does not need to pass through the Vacuum Freezer.

| Property | Details |
| --- | --- |
| Unlock tier | HV |
| Structure size | 3×3×3, with an air block at the center |
| Power | Standard Energy Hatches; Multi-Amp Energy Hatches and Laser Energy Hatches are not supported |
| Overclocking | Standard imperfect overclocking: each overclock uses 4× the power and halves the duration |
| Processing bonuses | No additional speed, power, or parallel bonuses |
| Maintenance and pollution | Requires maintenance, produces no pollution, and does not need a Muffler Hatch |

## Crafting and Construction

The current recipes for the controller and casing are shown below.

<RecipesFor id="gregtech:gt.blockmachines:1002" />

<RecipesFor id="gregtech:gt.blockcasings2:1" />

Build a hollow 3×3×3 shell with the controller in the center of the second layer on the front face. The single block at the center must remain air; no coils, ice, or coolant are required inside the structure.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> | 1, in the center of the second layer on the front face |
| <ItemLink id="gregtech:gt.blockcasings2:1" showIcon="left" /> | At least 16; the remaining casing positions may be replaced by the hatches and buses listed below |
| Energy Hatch | At least 1, in any casing position |
| Maintenance Hatch | 1, in any casing position |
| Input Bus or Input Hatch | At least one of either type, in any casing position |
| Output Bus or Output Hatch | At least one of either type, in any casing position |

Use an Input Bus and Output Bus to cool hot ingots. For fluid recipes, install the Input and Output Hatches required by the recipe. Both kinds of interface may be installed at the same time, but the structure must retain at least 16 actual Frost Proof Machine Casings; hatches and buses do not count toward this minimum.

A machine used only for hot ingots, with one Energy Hatch, one Maintenance Hatch, one Input Bus, and one Output Bus, requires **21 Frost Proof Machine Casings**. Adding more hatches or buses reduces the required number of casing blocks accordingly, down to the minimum of 16.

Use the <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> to preview the structure and assist with construction. Once it is complete, run a structure check and use maintenance tools to resolve any maintenance problems shown by the controller.

## Capabilities

The Vacuum Freezer does more than cool hot ingots. Its recipes also include liquefying certain gases, restoring coolant cells, and cooling plasmas. Recipes have different voltage and input/output requirements, so an item's name alone does not determine whether the machine can process it.

- **Hot ingot cooling**: Converts hot ingots from the Electric Blast Furnace into their regular counterparts, such as Hot Nichrome Ingots.
- **Fluid cooling**: Accepts the gases or plasmas required by a recipe through Input Hatches and sends the products to Output Hatches.
- **Coolant cell restoration**: Only cells and components with a matching Vacuum Freezer recipe can be processed; not every reactor component can be repaired here.

The structure itself does not consume coolant, although individual recipes may require fluid inputs. Follow the inputs, outputs, and power usage shown in NEI.

## Power and Throughput

HV is the tier at which the machine becomes available, but the Vacuum Freezer is not limited to HV power. Upgrading its Energy Hatch raises the available voltage and overclocks eligible recipes. It also follows the usual multiblock [tier-skipping rules](../tierskipping-overcloking-parallels/tierskipping.md).

The Vacuum Freezer has no heating coils, so it does not receive the Electric Blast Furnace's heat discounts or heat-based perfect overclocks. Each standard imperfect [overclock](../tierskipping-overcloking-parallels/overclocking.md) quadruples power usage and halves processing time, increasing the total energy consumed by each operation.

After expanding an Electric Blast Furnace production line, check whether hot ingots are accumulating at the Vacuum Freezer's input. The furnace's parallels, coil bonuses, and recipe duration all affect its actual output rate. Matching the Energy Hatch tier of the two machines does not guarantee matching throughput.

> [!WARNING]
> Losing power during processing aborts the current recipe and destroys the inserted inputs. The power network must meet the recipe voltage and continuously provide the power required while the machine runs.

## Hot Ingot Routing

An Electric Blast Furnace may produce both hot ingots and items that do not require cooling. Filtering the Vacuum Freezer's input prevents regular products from filling its Input Bus.

A regular Input Bus supports recipe filtering. Right-click it with a Screwdriver to toggle the filter, without holding Shift; Shift-right-click changes other input settings. When enabled, the bus only accepts items recognized by the machine's recipe map. Recipe filtering is not the same as accepting only hot ingots, because the Vacuum Freezer can process other items as well.

Use the following guidelines when choosing a transport system:

| Transport system | Routing considerations |
| --- | --- |
| GregTech Item Pipes | Enable valid recipe filtering on the Vacuum Freezer and leave another reachable destination for the remaining products; account for pipe distance and the routing behavior of Restrictive Item Pipes |
| Ender IO Item Conduits | Configure insertion filters and destination priorities so that the Vacuum Freezer receives items that need cooling while other products go to storage |
| AE2 | Filter for specific hot ingots; devices with ore dictionary filtering can use `ingotHot*` to match hot ingots |

After connecting the automation, insert one hot ingot and one regular product separately and verify their destinations. Make sure cooled ingots also have a reliable output route so that a full Output Bus cannot stop production.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Structure is incomplete | The center is air; at least 16 Frost Proof Machine Casings remain; an Energy Hatch, Maintenance Hatch, input interface, and output interface are present |
| Inputs will not enter | The bus belongs to a formed machine; recipe filtering is configured correctly; transport direction, filters, and priorities are correct |
| Inputs are present but no recipe is available | The input actually requires cooling; the item or fluid matches a recipe; the Energy Hatch provides sufficient voltage |
| Insufficient output space | The correct Output Bus or Output Hatch exists, is not full, and can hold the complete recipe output |
| Machine stops immediately after starting | Check available power, cable loss, energy buffers, and maintenance status before inserting more test materials |

See [Multiblock Machines](./multiblocks-index.md) for general multiblock operation. For greater cooling capacity later in progression, look into the Cryogenic Freezer.

## References

- [GTNH Wiki: Vacuum Freezer](https://wiki.gtnewhorizons.com/wiki/Vacuum_Freezer)
- [GTNH Chinese Wiki: Vacuum Freezer](https://gtnh.huijiwiki.com/wiki/真空冷冻机)