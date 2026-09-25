---
navigation:
  parent: /tricks_example_index.md
  title: Item/Fluid "Pipe" Subnet
  icon: appliedenergistics2:item.ItemMultiPart:220
---

# Item/Fluid "Pipe" Subnet

A simple method of emulating an item and/or fluid pipe with AE2 [devices](../ae2_mechanics/devices.md), useful for, well, anything you'd use an item or fluid pipe for.
This includes returning the result of a craft to a <ItemLink id="appliedenergistics2:tile.BlockInterface" />.

There are generally two different methods of achieving this:

## Import Bus -> Storage Bus

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) Import Bus: Can be filtered.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) Storage Bus: Can be filtered. This (and other storage busses you want to be a destination)
    must be the only storage on the network.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    Source
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    Destination
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

The <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (1) on the source inventory imports the items or fluid, and attempts to store them in [network storage](../ae2_mechanics/import_export_storage.md).
Since the only storage on the network is the <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2) (which is why this is a subnet and not on your main network), the items or fluid
are placed in the destination inventory, thus being transferred. Energy is provided through a <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" />.
Both the import bus and storage bus can be filtered, but the setup will transfer everything it can access if no filters are applied.
This setup also works with multiple import busses and multiple storage busses.

## Storage Bus -> Export Bus

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/storage_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) Storage Bus: Can be filtered. This (and other storage busses you want to be a source)
    must be the only storage on the network.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) Export Bus: Must be filtered.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    Source
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    Destination
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

The <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> on the destination inventory attempts to pull items in its filter from [network storage](../ae2_mechanics/import_export_storage.md).
Since the only storage on the network is the <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (which is why this is a subnet and not on your main network), the items or fluid
are pulled from the source inventory, thus being transferred. Energy is provided through a <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" />.
Because export busses must be filtered to function, this setup only operates if you filter the export bus.
This setup also works with multiple storage busses and multiple export busses.

## A Setup That Does Not Work (Import Bus -> Export Bus)

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dd3333" thickness="1">
    Import Bus: Since the network has no storage, there is nowhere for it to import to.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dd3333" thickness="1">
    (2) Export Bus: Since the network has no storage, there is nothing for it to export.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
    Source
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
    Destination
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

A setup with just an import and export bus will not work. The import bus will attempt to pull from the source inventory
and store the items or fluid in network storage. The export bus will attempt to pull from network storage and put the
items or fluid in the destination inventory. However since this network **has no storage**, the import bus can't import
and the export bus can't export, so nothing happens.

## Inputting And Outputting Through 1 Face

Say you have some machine that can receive input and have its output pulled through 1 face. (Like a <ItemLink id="appliedenergistics2:tile.BlockCharger" />)
You can both push in the ingredients and pull out the result, by combining the 2 pipe subnet methods:

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_export_pipe.snbt" />
  <BoxAnnotation min="4 1 1" max="5 1.3 2" color="#dddddd" thickness="1">
    (1) Import Bus: Can be filtered.
  </BoxAnnotation>
  <BoxAnnotation min="2 1 1" max="3 1.3 2" color="#dddddd" thickness="1">
    (2) Storage Bus: Can be filtered. This (and other storage busses you want to push and pull items)
    must be the only storage on the network.
  </BoxAnnotation>
  <BoxAnnotation min="2 0 1" max="3 1 2" color="#dddddd" thickness="1">
    (3) Thing You Want To Push To And Pull From: In this case a Charger.
  </BoxAnnotation>
  <BoxAnnotation min="0 1 1" max="1 1.3 2" color="#dddddd" thickness="1">
    (4) Export Bus: Must be filtered.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
    Source
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
    Destination
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Interfaces

It turns out there are [devices](../ae2_mechanics/devices.md) besides import busses and export busses that push items into
and pull items out of [network storage](../ae2_mechanics/import_export_storage.md)!
Of relevance here is the <ItemLink id="appliedenergistics2:tile.BlockInterface" />. If an item is inserted that the interface is not set to stock, the interface will
push it to network storage, which we can exploit similarly to the import bus -> storage bus pipe. Setting an interface to
stock some item will pull it from network storage, similar to the storage bus -> export bus pipe. Interfaces can be set to
stock some things and not stock others, allowing you to remotely push and pull through storage busses, if you for some reason want to do that.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/interface_pipes.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    Interface
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    Storage Bus
  </BoxAnnotation>
  <BoxAnnotation min="3.7 0 2" max="4 1 3" color="#dddddd" thickness="1">
    Storage Bus
  </BoxAnnotation>
  <BoxAnnotation min="0 1 2" max="1 1.3 3" color="#dddddd" thickness="1">
    Interface
  </BoxAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## One-To-Many and Many-To One (and many-to-many)

Of course, you don't have to use just one <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> or <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> or <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />

<GameScene zoom="3" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/many_to_many_pipe.snbt" />
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Providing To Multiple Places

From all this, we can derive a method to send ingredients from one <ItemLink id="appliedenergistics2:tile.BlockInterface" /> to many different
locations, like an array of machines, or several different faces of one machine.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/fluid_interface_storage.snbt" />
  <BoxAnnotation min="2.7 0 1" max="3 1 2" color="#dddddd" thickness="1">
    Interface (must be flat, not fullblock)
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 4" color="#dddddd" thickness="1">
    Storage Busses
  </BoxAnnotation>
  <BoxAnnotation min="0 0 0" max="1 1 4" color="#dddddd" thickness="1">
    Places you want to pattern-provide to (multiple machines, or multiple faces of 1 machine)
  </BoxAnnotation>
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>
