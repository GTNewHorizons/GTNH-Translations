---
navigation:
  parent: ../tricks_example_index.md
  title: Throwing-In-Water Automation
  icon: appliedenergistics2:item.ItemMultiMaterial:7
---

# Throwing-In-Water Automation

This setup uses an <ItemLink id="appliedenergistics2:tile.BlockInterface" />, so it is intended to work with an [autocrafting](../ae2_mechanics/autocrafting.md) system.

Some recipes require an item to be thrown into water. The same design can handle other recipes that require dropping an item at a location. It uses a <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" />, a <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" />, and two modified [pipe subnets](pipe_subnet.md).

This setup can be combined with [charger automation](charger_automation.md) to produce <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:1" />.

<GameScene offsetX="-85" offsetY="-70">
  <ImportStructure src="../assets/structures/throw_in_water.snbt" />
  <IsometricCamera yaw="180" pitch="0" />
  <BlockAnnotation pos="1 0 0">
  (1) ME Interface: default configuration, with the relevant processing patterns.
  <Row>
    <FloatingImage src="../assets/images/fluix_pattern.png" displayWidth="150" title="Fluix Pattern" />
  </Row>
  </BlockAnnotation>
  <BoxAnnotation min="0.7 0 0" max="1 1 1">
  (2) Interface: default configuration.
  </BoxAnnotation>
  <BoxAnnotation min="0 0.7 0" max="1 1 1">
  (3) Formation Plane: set to drop items.
  </BoxAnnotation>
  <BoxAnnotation min="0.027999878 2 -0.0032958984" max="1 2.3 1">
  (4) Annihilation Plane: no configurable GUI.
  </BoxAnnotation>
  <BoxAnnotation min="1 1 0" max="2 1.3 1">
  (5) Storage Bus: filtered to the pattern outputs.
  </BoxAnnotation>
  <DiamondAnnotation pos="2.5 0.5 0.5">
  To the main network or charger automation
  </DiamondAnnotation>
</GameScene>

## Configuration And Patterns

* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) is in its default configuration and contains the relevant <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />.
  * For <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:7" />, the default NEI recipe is sufficient.
* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2) is in its default configuration.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> (3) is set to drop items.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> (4) has no GUI and cannot be configured.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (5) is filtered to the pattern outputs.

## How It Works

1. The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> sends ingredients to the adjacent <ItemLink id="appliedenergistics2:tile.BlockInterface" /> on the green subnet.
2. The interface, configured not to stock anything by default, pushes its contents into [network storage](../ae2_mechanics/import_export_storage.md).
3. The only storage on the green subnet is the <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" />, which drops the received items into the water.
4. The <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> on the orange subnet attempts to pick up the dropped items, but the <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> is filtered to accept only craft results.
5. The items transform in the world.
6. The annihilation plane can now pick up the transformed items because the storage bus accepts them.
7. The storage bus stores the results in the ME interface and returns them to the main network.
