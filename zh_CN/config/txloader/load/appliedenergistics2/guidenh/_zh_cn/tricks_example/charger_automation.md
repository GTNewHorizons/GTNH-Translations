---
navigation:
  parent: ../tricks_example_index.md
  title: Charger Automation
  icon: appliedenergistics2:tile.BlockCharger
---

# Charger Automation

This setup uses an <ItemLink id="appliedenergistics2:tile.BlockInterface" />, so it is intended to work with an [autocrafting](../ae2_mechanics/autocrafting.md) system. For a standalone <ItemLink id="appliedenergistics2:tile.BlockCharger" />, use hoppers, chests, or another item pipe.

The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> sends ingredients into the charger. A [pipe subnet](pipe_subnet.md) or another item pipe returns the charged result to the interface.

<GameScene>
  <ImportStructure src="../assets/structures/charger_automation.snbt" />
  <BlockAnnotation pos="1 0 0">
  (1) ME Interface: default configuration, with the relevant pattern. It also supplies power.

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="Charger Pattern" />
  </BlockAnnotation>
  <BoxAnnotation min="0.25 1 0.25" max="0.75 1.3 0.75">
  (2) Import Bus: default configuration.
  </BoxAnnotation>
  <BoxAnnotation min="1.15 1 0.15" max="1.85 1.25 0.85">
  (3) Storage Bus: default configuration.
  </BoxAnnotation>
</GameScene>

## Configuration

* The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) is in its default configuration and contains the relevant <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />. It also powers the <ItemLink id="appliedenergistics2:tile.BlockCharger" />, like a [cable](../items_blocks/cables.md).

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="Charger Pattern" />

* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (2) is in its default configuration.
* The <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3) is in its default configuration.

## How It Works

1. The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> sends ingredients into the <ItemLink id="appliedenergistics2:tile.BlockCharger" />.
2. The charger charges the item.
3. The <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> on the green subnet pulls out the result and attempts to store it in [network storage](../ae2_mechanics/import_export_storage.md).
4. The only storage on the green subnet is the <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />, which sends the result back into the ME interface and then to the main network.
