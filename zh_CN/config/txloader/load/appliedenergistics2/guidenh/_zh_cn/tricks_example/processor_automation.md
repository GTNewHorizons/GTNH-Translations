---
navigation:
  parent: ../tricks_example_index.md
  title: Processor Automation
  icon: appliedenergistics2:item.ItemMultiMaterial:23
---

# Automation of Processor Production

There are many ways of automating [processors](../items_blocks/processors.md), and this is one of them.

This general layout can be done with any type of item logistics pipe or conduit or duct or whatever the mod calls it, as
long as you can filter it.

![The Process FLow Diagram](../assets/images/processor_flow_diagram.png)

Here is detailed how to do it with just AE2, using ["pipe" subnets](pipe_subnet.md).

Note that since this uses a <ItemLink id="appliedenergistics2:tile.BlockInterface" />, it is meant to integrate into your [autocrafting](../ae2_mechanics/autocrafting.md)
setup. If you just want to automate a processor standalone, replace the ME Interface with another barrel, and directly put the ingredients in the upper barrel.

This happens to be backwards-compatible
with previous AE2 versions, because even if the <ItemLink id="appliedenergistics2:tile.BlockInscriber" />s are sided, the pipe subnets still insert to and
extract from the correct faces.

## A Lesson In Pattern Encoding

Often, the [pattern](../items_blocks/patterns.md) you need to encode **WILL NOT MATCH WHAT YOU SEE IN NEI**, or what NEI outputs when you click the + button.
In this case, NEI will output 2 separate patterns, one for the printed components and one for the final assembly, and the printed
components pattern will include a [press](../items_blocks/presses.md). This is not what we want, because this is not what the setup will do. We want 1 pattern that
inputs the raw resources and outputs the completed processor, and since the press is already in the inscriber, we should not put it in the pattern.

---

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/processor_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="5 1 0" max="6 2 1">
  (1) ME Interface: In its default configuration, with the relevant processing patterns.

  <Row>
    <FloatingImage src="../assets/images/logic_pattern.png" displayWidth="150" title="Logic Pattern" />
    <FloatingImage src="../assets/images/calculation_pattern.png" displayWidth="150" title="Calculation Pattern" />
    <FloatingImage src="../assets/images/engineering_pattern.png" displayWidth="150" title="Engineering Pattern" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.7 2 0" max="5 3 1">
  (2) Storage Bus #1: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="4.3 2 1">
  (3) Export Bus #1: Filtered to Silicon, has 2 Acceleration Cards
  <Row><ItemImage id="gregtech:gt.metaitem.01:17020" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="4.3 3 1">
  (4) Export Bus #2: Filtered to Gold Ingot, has 2 Acceleration Cards
  <Row><ItemImage id="minecraft:gold_ingot" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="4.3 4 1">
  (5) Export Bus #3: Filtered to Certus Quartz Crystal, has 2 Acceleration Cards
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:10" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 6 0" max="4.3 5 1">
  (6) Export Bus #4: Filtered to Diamond, has 2 Acceleration Cards
  <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 0" max="2 2 1">
  (7) Export Bus #5: Filtered to Redstone Dust, has 2 Acceleration Cards
  <Row><ItemImage id="minecraft:redstone" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="3 2 1">
  (8) Inscriber #1: In its default configuration. Has a Silicon Press and 4 Acceleration Cards
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 3 0" max="3 4 1">
  (9) Inscriber #2: In its default configuration. Has a Logic Press and 4 Acceleration Cards
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="3 5 1">
  (10) Inscriber #3: In its default configuration. Has a Calculation Press and 4 Acceleration Cards
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="3 6 1">
  (11) Inscriber #4: In its default configuration. Has an Engineering Press and 4 Acceleration Cards
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 0" max="1 3 1">
  (12) Inscriber #5: In its default configuration. Has 4 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 2 0" max="3 1 1">
  (13) Import Bus #1: In its default configuration, has 2 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 4 0" max="3 3 1">
  (14) Import Bus #2: In its default configuration, has 2 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 5 0" max="3 4 1">
  (15) Import Bus #3: In its default configuration, has 2 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 6 0" max="3 5 1">
  (16) Import Bus #4: In its default configuration, has 2 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 3 0" max="1 3.3 1">
  (17) Storage Bus #2: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1.7 0" max="1 2 1">
  (18) Storage Bus #3: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 0" max="0.7 3 1">
  (19) Import Bus #5: In its default configuration, has 2 Acceleration Cards
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="5 0.7 0" max="6 1 1">
  (20) Storage Bus #4: In its default configuration.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.3 2.7 0.3" max="3.7 3 0.7">
  Quartz Fiber powers all 3 inscribers because inscribers act like cables and thus transmit energy
  </BoxAnnotation>

  <DiamondAnnotation pos="7 1.5 0.5" color="#00ff00">
  To Main Network
  </DiamondAnnotation>

  <IsometricCamera yaw="185" pitch="5" />
</GameScene>

## Configurations

* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) is in its default configuration, with the relevant <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />s.
  Note that the patterns go direct from raw resources to the completed processor, and do **NOT** include the [press](../items_blocks/presses.md).

  ![Logic Pattern](../assets/images/logic_pattern.png)
  ![Calculation Pattern](../assets/images/calculation_pattern.png)
  ![Engineering Pattern](../assets/images/engineering_pattern.png)

* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />ses (2, 17, 18, 20) are in their default configurations.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />ses (3-7) are filtered to the relevant ingredient. They have 2 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" />s.
<Row>
  <ItemImage id="gregtech:gt.metaitem.01:17020" scale="2" />
  <ItemImage id="minecraft:gold_ingot" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:10" scale="2" />
  <ItemImage id="minecraft:diamond" scale="2" />
  <ItemImage id="minecraft:redstone" scale="2" />
</Row>
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />ses (13-16, 19) are in their default configurations. They have 2 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" />s.
* The <ItemLink id="appliedenergistics2:tile.BlockInscriber" />s are in their default configurations. They have the relevant [press](../items_blocks/presses.md),
and 4 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" />s.
<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="2" />
</Row>

## How It Works

1. The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> pushes the ingredients into the barrel.
2. The first [pipe subnet](pipe_subnet.md) (orange) pulls the silicon, redstone dust, and the relevant processor's ingredient
(Gold Ingot, Certus Quartz Crystal, or Diamond) out of the barrel and puts them in the relevant <ItemLink id="appliedenergistics2:tile.BlockInscriber" />.
3. The first four <ItemLink id="appliedenergistics2:tile.BlockInscriber" />s make the <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:20" />, and the <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:22" />,
<ItemLink id="appliedenergistics2:item.ItemMultiMaterial:23" />, or <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:24" />.
4. The second and third [pipe subnet](pipe_subnet.md)s (green) take the printed circuits out of the first four <ItemLink id="appliedenergistics2:tile.BlockInscriber" />s
    and put them in the fifth, final assembly <ItemLink id="appliedenergistics2:tile.BlockInscriber" />.
5. The fifth <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> assembles the [processor](../items_blocks/processors.md).
6. The fourth [pipe subnet](pipe_subnet.md) (purple) puts the processor in the ME Interface, returning it to the main network.
