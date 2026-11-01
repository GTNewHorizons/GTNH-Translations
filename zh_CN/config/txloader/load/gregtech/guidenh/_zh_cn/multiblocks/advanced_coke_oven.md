---
item_ids:
  - Railcraft:machine.alpha:12
quest_ids:
  - AAAAAAAAAAAAAAAAAAAMHw==
navigation:
  title: Advanced Coke Oven
  parent: ./multiblocks_index.md
  icon: Railcraft:machine.alpha:12
  position: -2001
---

# Advanced Coke Oven

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="Railcraft:machine.alpha:12" />
</GameScene>

The <ItemImage id="Railcraft:machine.alpha:12" /> Advanced Coke Oven (ACO) is an MV tier multiblock for burning logs into charcoal. 

The ACO is a direct upgrade to the basic [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md) because it is 90x faster, but it requires a burnable fuel such as the very charcoal that it produces and it does not produce creosote oil. Therefore, the ACO's maximum output is 1 charcoal per second, but its net output is 15 charcoal per 16 seconds. 

The ACO does not consume power and is initially faster than the [<ItemLink id="gregtech:gt.blockmachines:15546" showIcon="left" />](./pyrolyse_oven.md), but that quickly changes as better heating coils and energy hatches are unlocked. 

The ACO is superseded by the [<ItemLink id="gregtech:gt.blockmachines:15543" showIcon="left" />](./industrial_coke_oven.md) in EV.

| Property | Details |
| --- | --- |
| Unlock Tier | MV |
| Structure Size (LxWxH) | 3x3x4 |
| Power | None |
| Overclocks | None |
| Maintenance | No maintenance needed |
| Pollution | Produces 80 gibbl/s pollution |

## Crafting and Construction

### Crafting

<RecipesFor id="dreamcraft:AdvancedCokeOvenBrick" handlerId="gt.recipe.blastfurnace" />

<RecipesFor id="Railcraft:machine.alpha:12" />

### Structure

The ACO consists of a single type of block and does not have a controller or any buses/hatches. The <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> does not visualize/build the structure, but it is very easy to build.

ACO cannot be rotated at all.

| Component | Quantity and placement |
| --- | --- |
| <ItemLink id="Railcraft:machine.alpha:12" showIcon="left" /> | 34, 3x3x4 with hollow 1x1x2 center |

### Wallsharing

As a Railcraft multiblock, **the ACO <Color id="red">cannot wallshare</Color> any part of its structure** and must be at least one block apart from other ACOs to form.

## Usage

<GameScene wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/aco_loop.snbt" />
</GameScene>

The ACO produces one charcoal per second from logs. That is 90x faster than the basic [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md), but it requires a burnable fuel such as the very charcoal that it produces and it does not produce creosote oil. Charcoal has a burntime of 1600 ticks which fuels the ACO for 16 seconds, resulting in a net loss of only 1/16 of the total output. The ACO can also turn coal into coal coke, sugar charcoal into sugar coke, and cactus charcoal into cactus coke (1 second each).

Inputs can be inserted into any block on any side of the structure and outputs can be extracted from any block on any side of the structure. The ACO does not auto-pull from adjacent inventories but it does auto-push. 

The scene on the side shows an example of a self-feeding loop using EnderIO conduits.

### Charcoal Rate Comparison

The [<ItemLink id="gregtech:gt.blockmachines:15546" showIcon="left" />](./pyrolyse_oven.md) is another option for turning logs into charcoal in the early game that can be overclocked, boosted with nitrogen, and scales with the tier of its heating coils. 

To help the player decide between the ACO and the Pyrolyse Oven, the following table compares their average charcoal per second for various recipes, heating coils, and overclocks. The cells highlighted green mean the Pyrolyse Oven is faster than the ACO and the cells highlighted in red mean the Pyrolyse Oven is slower. Note that the ACO does not consume any EU, but it also produces no fluid byproducts, which may also be a deciding factor depending on your current situation.

| Overclocks | Pyrolyse Oven(Normal) ||| Pyrolyse Oven(With Nitrogen) ||| ACO |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^^ | Cupronickel | Kanthal | Nichrome | Cupronickel | Kanthal | Nichrome | ^^ |
| 0(MV) | <Color id="red">0.313/s</Color> | <Color id="red">0.625/s</Color> | <Color id="green">0.939/s</Color> | <Color id="red">0.625/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">1.887/s</Color> | 0.938/s |
| 1(HV) | <Color id="red">0.625/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">1.887/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">3.774/s</Color> | ^^ |
| 2(EV) | <Color id="green">1.250/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">3.774/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">5.000/s</Color> | <Color id="green">7.692/s</Color> | ^^ |

## References

- [GTNH Wiki: Advanced Coke Oven](https://wiki.gtnewhorizons.com/wiki/Advanced_Coke_Oven)
