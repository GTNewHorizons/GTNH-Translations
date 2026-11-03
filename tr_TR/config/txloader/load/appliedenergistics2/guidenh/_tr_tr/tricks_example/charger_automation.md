---
navigation:
  parent: ../tricks_example_index.md
  title: Şarj Cihazı Otomasyonu
  icon: appliedenergistics2:tile.BlockCharger
---

# Şarj Cihazı Otomasyonu

Bu düzenek bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullanır, bu nedenle bir [otomatik üretim](../ae2_mechanics/autocrafting.md) sistemiyle çalışacak şekilde tasarlanmıştır. Tek başına bir <ItemLink id="appliedenergistics2:tile.BlockCharger" /> için huniler, sandıklar veya başka bir eşya borusu kullan.

<ItemLink id="appliedenergistics2:tile.BlockInterface" />, malzemeleri şarj cihazına gönderir. Bir [boru alt ağı](pipe_subnet.md) veya başka bir eşya borusu, şarj edilmiş sonucu arayüze geri döndürür.

<GameScene>
  <ImportStructure src="../assets/structures/charger_automation.snbt" />
  <BlockAnnotation pos="1 0 0">
  (1) ME Arayüzü: varsayılan yapılandırma, ilgili kalıpla birlikte. Ayrıca güç sağlar.

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="Charger Pattern" />
  </BlockAnnotation>
  <BoxAnnotation min="0.25 1 0.25" max="0.75 1.3 0.75">
  (2) İçe Aktarma Veriyolu: varsayılan yapılandırma.
  </BoxAnnotation>
  <BoxAnnotation min="1.15 1 0.15" max="1.85 1.25 0.85">
  (3) Depolama Veriyolu: varsayılan yapılandırma.
  </BoxAnnotation>
</GameScene>

## Yapılandırma

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) varsayılan yapılandırmasındadır ve ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> öğesini içerir. Ayrıca <ItemLink id="appliedenergistics2:tile.BlockCharger" /> cihazını bir [kablo](../items_blocks/cables.md) gibi besler.

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="Charger Pattern" />

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (2) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />, malzemeleri <ItemLink id="appliedenergistics2:tile.BlockCharger" /> cihazına gönderir.
2. Şarj cihazı eşyayı şarj eder.
3. Yeşil alt ağdaki <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> sonucu çeker ve [ağ depolamasında](../ae2_mechanics/import_export_storage.md) depolamayı dener.
4. Yeşil alt ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> öğesidir; sonucu ME arayüzüne ve ardından ana ağa geri gönderir.