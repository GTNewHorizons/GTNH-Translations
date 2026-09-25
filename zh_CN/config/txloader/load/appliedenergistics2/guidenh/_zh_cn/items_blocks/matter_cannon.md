---
navigation:
  parent: /items_blocks_index.md
  title: Matter Cannon
  icon: appliedenergistics2:item.ToolMassCannon
categories:
- tools
item_ids:
- appliedenergistics2:item.ToolMassCannon
---

# Matter Cannon

<ItemImage id="appliedenergistics2:item.ToolMassCannon" scale="4" />

The matter cannon is a portable railgun that fires small items as projectiles, including <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:6" /> and metal nuggets. Damage depends on the ammunition: heavier items such as gold nuggets deal more damage than matter balls. Each shot consumes 1600 AE.

When `matterCannonBlockDamage` is enabled, the cannon can break blocks according to their hardness and the ammunition's damage. Recharge it in an <ItemLink id="appliedenergistics2:tile.BlockCharger" />.

Like a [storage cell](storage_cells.md), the cannon's ammunition magazine can be filled by placing it in the component slot of an <ItemLink id="appliedenergistics2:tile.BlockChest" />.

## Upgrades

The cannon supports these [upgrades](upgrade_cards.md), installed with an <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />:

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> enables fuzzy matching and NBT-ignoring filters.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> switches the whitelist to a blacklist.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> increases energy use per shot and projectile power.
* ~~<ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" /> voids excess ammunition when full.~~
* ~~<ItemLink id="ae2fc:energy_card" /> increases battery capacity.~~

## Recipe

<RecipeFor id="appliedenergistics2:item.ToolMassCannon" />


