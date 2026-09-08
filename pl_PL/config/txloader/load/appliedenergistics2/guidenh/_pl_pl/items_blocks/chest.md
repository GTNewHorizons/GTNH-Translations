---
navigation:
  parent: /items_blocks_index.md
  title: ME Chest
  icon: appliedenergistics2:tile.BlockChest
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockChest
---

# ME Chest

<BlockImage id="appliedenergistics2:tile.BlockChest" meta="0" nbt='{inv:{item0:{},item1:{id:"appliedenergistics2:item.ItemBasicStorageCell.1k",Count:1b,tag:{ic:1L,it:1s,__guidenh_encoded_keys_v1:[0:{v:1L,k:"@0"},1:{v:{Craft:0b,Cnt:1L,id:"minecraft:stone",Count:0b,Damage:0s,Req:0L},k:"#0"}]},Damage:0s}},proxy:{p:0,g:341L,k:-1L},orientation_up:"UP",SORT_BY:"NAME",terminalSettings:[0:{uuid_l:-8061629327903583552L,uuid_m:-937944366173238364L,savedString:"""",map:[]}],VIEW_MODE:"ALL",paintedColor:16b,id:"BlockChest",priority:0,SORT_DIRECTION:"ASCENDING",orientation_forward:"NORTH",internalCurrentPower:40.0d}' scale="4" />

The ME Chest is like a miniature network containing an <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" />, an <ItemLink id="appliedenergistics2:tile.BlockDrive" />, and an <ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" />. It can be used as a small network storage, but its functionality is limited by the fact that it can only hold a single [storage cell](storage_cells.md).

It is particularly useful for interacting with the cells inside it individually. The terminal integrated into it can only access the cells inside the chest, while [devices](../ae2_mechanics/devices.md) in a normal network can access any [network storage](../ae2_mechanics/import_export_storage.md), including the ME Chest.

It has two GUIs, with different GUIs opened depending on the side. Interacting with the terminal on the top opens the terminal interface. A storage bus can access the storage of the cells inside the ME Chest from any side without a cell slot. Logistics systems can only insert items into it and cannot extract items from it. Interacting with other sides opens the GUI for placing a storage cell and setting its priority. Item logistics systems can only output the cell through the side with the cell slot.

It can be rotated using the <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" />.

It has only a small AE energy buffer, so without an [energy cell](energy_cells.md), attempting to input and output too many items simultaneously may cause it to run out of energy.

The terminal can be dyed using the <ItemLink id="appliedenergistics2:item.ToolColorApplicator" />.

<GameScene width="250" height="100" zoom="4" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/chest_color.snbt" />
  <IsometricCamera yaw="105" pitch="30" />
</GameScene>

## Settings

The ME Chest has the same settings as <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" /> and <ItemLink id="appliedenergistics2:item.ItemMultiPart:360" />, but does not support <ItemLink id="appliedenergistics2:item.ItemViewCell" />.

## Cell Status LEDs

The cells inside the chest can indicate their status through their LEDs:

| Color | Status |
| :--- | :--- |
| Green | Empty |
| Blue | Contains items |
| Orange | [Types](../ae2_mechanics/bytes_and_types.md) are full, cannot add new types |
| Red | [Bytes](../ae2_mechanics/bytes_and_types.md) are full, cannot add new items |
| Black | No energy or the chest is missing a [channel](../ae2_mechanics/channels.md) |

## Priority

The priority can be set by clicking the wrench in the top-right corner of the GUI. Items entering the network will preferentially enter the storage location with the highest priority. If two storage locations have the same priority, the one that already contains the item will be preferred. A cell with a [partition](cell_workbench.md) is considered to already contain the item when priorities are equal. Items extracted from storage will preferentially be extracted from the location with the lowest priority. This priority system causes high-priority storage locations to be filled while low-priority locations are emptied during item input and output.

## Recipe

<RecipeFor id="appliedenergistics2:tile.BlockChest" />