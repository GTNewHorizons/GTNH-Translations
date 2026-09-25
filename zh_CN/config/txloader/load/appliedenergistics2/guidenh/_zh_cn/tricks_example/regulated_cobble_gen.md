---
navigation:
  parent: ../tricks_example_index.md
  title: Auto-Regulated Cobblestone Generator
  icon: minecraft:cobblestone
---

# Auto-Regulated Cobblestone Generator

Automation of a cobblestone generator is simple, just face an <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> into a standard vanilla
manual cobblestone generator. However, doing this will eventually jam your network full of cobblestone, so some regulation
is desired.

Due to how annihilation planes work (they act like <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />s), we cannot simply put a <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />
facing an <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> with a redstone card (since you cannot go directly import to export
with no storage in between). We have to be a bit more roundabout.

<ItemLink id="appliedenergistics2:item.ItemMultiPart:80" />s allow you to connect and disconnect parts of your network with redstone signals, but they cause
the network to reboot whenever they do this. There is a simple workaround: put the toggle bus on a [subnetwork](../ae2_mechanics/subnetworks.md)
such that it only reboots the subnet.

We can have a self-contained <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> and <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> [subnetwork](../ae2_mechanics/subnetworks.md)
push into an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> on the main network. The toggle bus will connect and disconnect the subnet from a
quartz fiber, cutting power to the planes.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/regulated_cobble_gen.snbt" />

  <BoxAnnotation color="#dddddd" min="3 2 2" max="7 2.3 3">
  (1) Annihilation Planes: No GUI to configure, but can be enchanted with Efficiency and Unbreaking to reduce power draw.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 2" max="2.3 3 3">
  (2) Storage Bus: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 2.3 2" max="2.7 2.7 2.3">
  (3) Toggle Bus: Very important that the toggle bus is on the
  subnetwork, and not the main network.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 2.3" max="2.7 3.3 2.7">
  (4) Level Emitter: Configured with cobblestone and the desired quantity, set to "Emit when levels are below limit".
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 3" max="2 3 2">
  (5) Interface: In its default configuration.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 2.5 1.5" color="#00ff00">
  To Main Network
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" />s (1) Have no GUI to configure, but can be enchanted with Efficiency and Unbreaking to reduce power draw.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2) is in its default configuration.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:80" /> (3) must be on the subnetwork side of the quartz fiber, not the main network, or the main
  network will reboot every time it toggles.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (4) is configured with the desired item and quantity, and set to "Emit when levels are below limit".
* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (5) is in its default configuration.

## How It Works

1. The cobblestone generator makes some cobblestone.
2. The <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" />s break the cobblestone. 
3. The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> stores the cobblestone in the <ItemLink id="appliedenergistics2:tile.BlockInterface" />, sending it into the main network.
4. When the amount of cobblestone in the main network exceeds the set amount, the <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> stops
   sending a signal, turning off the <ItemLink id="appliedenergistics2:item.ItemMultiPart:80" />.
5. This cuts power to the subnetwork, stopping the annihilation planes from working.
