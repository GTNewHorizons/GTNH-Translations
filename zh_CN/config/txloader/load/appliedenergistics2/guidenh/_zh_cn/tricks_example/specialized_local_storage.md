---
navigation:
  parent: ../tricks_example_index.md
  title: Specialized Local Storage
  icon: appliedenergistics2:tile.BlockDrive
---

# Specialized Local Storage

Utilizing one of the [special behaviors of the Interface](../items_blocks/interface.md#special-interactions), a
[subnetwork](../ae2_mechanics/subnetworks.md) can present the contents of its storage to the main network, without being able
to see the main network's storage, and taking up only 1 [channel](../ae2_mechanics/channels.md).

This is useful for local storage at some farm, so that the items will not overflow into your main storage.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/local_storage.snbt" />

  <BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
  (1) Some method of importing items (in this case an interface)
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
  (2) Drive: Has some cells in it. The cells should be filtered to whatever the farm outputs.
  The cells can have Equal Distribution Cards and Overflow Destruction Cards.
  <Row><ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:69" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:68" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
  (3) Crafting Terminal: This can see the contents of the Drive on the subnet, but not the contents of your main network's storage.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
  (4) Interface #2: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
  (5) Storage Bus: Has priority set higher than the main storage, can be filtered to whatever the farm outputs.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
  Crafting Terminal: This can see both the contents of the main network's storage *and* the subnetwork.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
  To Main Network
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

* The first <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) simply accepts items from whatever farm you have and pushes them into the subnet.
* The <ItemLink id="appliedenergistics2:tile.BlockDrive" /> (2) has some [cells](../items_blocks/storage_cells.md) in it. The cells should be
  [partitioned](../items_blocks/cell_workbench.md) to whatever the farm outputs.
The cells can have <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:69" />s and <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" />s.
* The second <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (4) is in its default configuration.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> has its [priority](../ae2_mechanics/import_export_storage.md#storage-priority) set
  higher than the main storage. It can be filtered to whatever the farm outputs.

## How It Works

* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> on the subnet shows the <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> on the main network the contents of
the <ItemLink id="appliedenergistics2:tile.BlockDrive" />. This means the storage bus can directly pull items from and push items to the cells in the drive.
* The storage bus is set to high [priority](../ae2_mechanics/import_export_storage.md#storage-priority) so that items are preferentially
  put back in the subnet instead of in your main storage.
* Importantly, if the cells in the subnet fill up, the items will not overflow into the main network. If the farm is of a type
that breaks if it backs up, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" />s can be used to delete the excess items instead. 
* If the farm outputs multiple items, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:69" />s can stop one item from filling all the cells
and not letting the other items be stored.
