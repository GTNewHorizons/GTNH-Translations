---
navigation:
  parent: ../tricks_example_index.md
  title: Suya Atma Otomasyonu
  icon: appliedenergistics2:item.ItemMultiMaterial:7
---

# Suya Atma Otomasyonu

Bu düzen bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullanır, bu yüzden bir [otomatik üretim](../ae2_mechanics/autocrafting.md) sistemiyle çalışacak şekilde tasarlanmıştır.

Bazı tarifler bir eşyanın suya atılmasını gerektirir. Aynı tasarım, bir eşyanın belirli bir konuma bırakılmasını gerektiren diğer tarifler için de kullanılabilir. Bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" />, bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> ve iki değiştirilmiş [boru alt ağı](pipe_subnet.md) kullanır.

Bu düzen, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:1" /> üretmek için [şarj cihazı otomasyonu](charger_automation.md) ile birleştirilebilir.

<GameScene offsetX="-85" offsetY="-70">
  <ImportStructure src="../assets/structures/throw_in_water.snbt" />
  <IsometricCamera yaw="180" pitch="0" />
  <BlockAnnotation pos="1 0 0">
  (1) ME Arayüzü: ilgili işleme kalıplarıyla birlikte varsayılan yapılandırma.
  <Row>
    <FloatingImage src="../assets/images/fluix_pattern.png" displayWidth="150" title="Fluix Kalıbı" />
  </Row>
  </BlockAnnotation>
  <BoxAnnotation min="0.7 0 0" max="1 1 1">
  (2) Arayüz: varsayılan yapılandırma.
  </BoxAnnotation>
  <BoxAnnotation min="0 0.7 0" max="1 1 1">
  (3) Oluşum Düzlemi: eşya bırakacak şekilde ayarlanmış.
  </BoxAnnotation>
  <BoxAnnotation min="0.027999878 2 -0.0032958984" max="1 2.3 1">
  (4) Yok Etme Düzlemi: yapılandırılabilir GUI'si yok.
  </BoxAnnotation>
  <BoxAnnotation min="1 1 0" max="2 1.3 1">
  (5) Depolama Veriyolu: kalıp çıktılarına filtrelenmiş.
  </BoxAnnotation>
  <DiamondAnnotation pos="2.5 0.5 0.5">
  Ana ağa veya şarj cihazı otomasyonuna
  </DiamondAnnotation>
</GameScene>

## Yapılandırma ve Kalıplar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) varsayılan yapılandırmasındadır ve ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> kalıbını içerir.
  * <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:7" /> için varsayılan NEI tarifi yeterlidir.
* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> (3) eşya bırakacak şekilde ayarlanmıştır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> (4) GUI'si yoktur ve yapılandırılamaz.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (5) kalıp çıktılarına filtrelenmiştir.

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> malzemeleri yeşil alt ağdaki bitişik <ItemLink id="appliedenergistics2:tile.BlockInterface" /> arayüzüne gönderir.
2. Varsayılan olarak hiçbir şey stoklamayacak şekilde yapılandırılmış olan arayüz, içeriğini [ağ deposuna](../ae2_mechanics/import_export_storage.md) iter.
3. Yeşil alt ağdaki tek depolama, aldığı eşyaları suya bırakan <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> cihazıdır.
4. Turuncu alt ağdaki <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> bırakılan eşyaları almayı dener; ancak <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> yalnızca üretim sonuçlarını kabul edecek şekilde filtrelenmiştir.
5. Eşyalar dünyada dönüşür.
6. Depolama veriyolu dönüşen eşyaları kabul ettiği için yok etme düzlemi artık onları alabilir.
7. Depolama veriyolu sonuçları ME arayüzünde depolar ve ana ağa geri gönderir.