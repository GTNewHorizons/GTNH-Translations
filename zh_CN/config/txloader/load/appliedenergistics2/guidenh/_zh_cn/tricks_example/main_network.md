---
navigation:
  parent: ../tricks_example_index.md
  title: An Example "Main Network"
  icon: appliedenergistics2:tile.BlockController
---

# An Example "Main Network"

Many other setups reference a "Main Network". You might also ask how all these [devices](../ae2_mechanics/devices.md) come
together into a functional system. Here is an example:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/structures/small_base_network.snbt" />

  <BoxAnnotation color="#33dd33" min="3 1 5" max="7 7 9">
  A big cluster of ME Interfaces and assemblers provides a lot of space for crafting patterns.
  The checkerboard pattern allows interfaces to utilize multiple assemblers in parallel while keeping it compact.
  Groups of 8 make it impossible for channels to route incorrectly.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 10 13" max="5 11 14">
  You don't actually need that big of a controller, all those huge rings and cubes designs you see in people's bases
  are mainly just to look cool.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 12 13" max="4 13 14">
  Every good network has an energy cell, to allow higher energy input per gametick and
  smooth out power fluctuations.
  </BoxAnnotation>
    
  <BoxAnnotation color="#33dd33" min="4 1 2" max="7 4 4">
  You probably want to use some other mod's power source, a reactor or solar panel or generator or
  whatever. Vibration Chambers are ok-ish but AE2 is designed to be used in a modpack and use your
  base's main power generator.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 1 15" max="8 3 16">
  Facades can be used to hide stuff behind walls.
  </BoxAnnotation>
  <BoxAnnotation color="#33dd33" min="3 3 15" max="5 10 16">
  Facades can be used to hide stuff behind walls.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8 9 13" max="10 10 14">
  You don't need that many drive bays and cells for your general storage, 2-4 Drives worth of 4k or 16k
  cells is almost always enough.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 13" max="7 11 14">
  For bulk storage, you want big cells filtered to specific items, in separate drives set to a higher
  priority.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 9 10" max="4 13 11.7">
  Interface-based auto-stocking.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 10 6" max="5 12 9">
  The logical expansion of the charger automation setup to multiple chargers.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 9 2" max="5 10 5">
  Processor automation using pipe subnets to connect the inscribers.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 3" max="7 11 4">
  Processor automation using pipe subnets to connect the inscribers.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8.2 9.2 7.2" max="8.8 10 7.8">
  The wireless access point is in the middle because its range is spherical.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 1 14" max="15 5 16">
  Typically you'll have 1-2 big crafting CPUs for big jobs and a few smaller ones to handle secondary
  jobs while the big CPUs are busy.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 3 5" max="11 4 6">
  Sometimes subnets might need their own controller if there are more than 8 devices (like distributing to more
  than 8 places).
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="11 1 7" max="14 4 9">
  Cobblestone farm.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="12 1 10.3" max="14.7 3.7 12.7">
  Throwing-In-Water automation.
  </BoxAnnotation>

  <IsometricCamera yaw="220" pitch="15" />
</GameScene>
