---
navigation:
  parent: ../tricks_example_index.md
  title: İşlemci Otomasyonu
  icon: appliedenergistics2:item.ItemMultiMaterial:23
---

# İşlemci Üretiminin Otomasyonu

[İşlemcileri](../items_blocks/processors.md) otomatikleştirmenin birçok yolu var; bu da onlardan biri.

Bu genel düzen, filtreleyebildiğin sürece modun adı ne olursa olsun her tür eşya lojistiği borusu, kanalı veya oluğuyla uygulanabilir.

![Süreç Akış Diyagramı](../assets/images/processor_flow_diagram.png)

Burada bunun yalnızca AE2 ile, ["boru" alt ağlarını](pipe_subnet.md) kullanarak nasıl yapılacağı ayrıntılı olarak anlatılıyor.

Bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullandığı için bunun [otomatik üretim](../ae2_mechanics/autocrafting.md)
düzenine entegre edilmek üzere tasarlandığını unutma. Bir işlemciyi tek başına otomatikleştirmek istiyorsan ME Arayüzü yerine başka bir varil koy ve malzemeleri doğrudan üstteki varile koy.

Bu arada bu, önceki AE2 sürümleriyle geriye dönük uyumludur; çünkü <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> blokları yönlü olsa bile boru alt ağları yine de doğru yüzlerden ekler ve
çeker.

## Kalıp Kodlama Dersi

Çoğu zaman kodlaman gereken [kalıp](../items_blocks/patterns.md) **NEI'DE GÖRDÜĞÜNLE EŞLEŞMEZ** ya da NEI'nin + düğmesine tıkladığında verdiğiyle eşleşmez.
Bu durumda NEI iki ayrı kalıp verir: biri baskılı bileşenler, diğeri son montaj için; baskılı
bileşenler kalıbı ise bir [baskı kalıbı](../items_blocks/presses.md) içerir. Bunu istemiyoruz çünkü düzenin yapacağı şey bu değil. Ham kaynakları alıp tamamlanmış işlemciyi veren 1 kalıp
istiyoruz ve baskı kalıbı zaten yontucunun içinde olduğundan onu kalıba koymamalıyız.

---

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/processor_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="5 1 0" max="6 2 1">
  (1) ME Arayüzü: Varsayılan yapılandırmasında, ilgili işleme kalıplarıyla.

  <Row>
    <FloatingImage src="../assets/images/logic_pattern.png" displayWidth="150" title="Mantık Kalıbı" />
    <FloatingImage src="../assets/images/calculation_pattern.png" displayWidth="150" title="Hesaplama Kalıbı" />
    <FloatingImage src="../assets/images/engineering_pattern.png" displayWidth="150" title="Mühendislik Kalıbı" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.7 2 0" max="5 3 1">
  (2) Depolama Veriyolu #1: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="4.3 2 1">
  (3) Dışa Aktarma Veriyolu #1: Silisyum'a filtrelenmiş, 2 Hızlandırma Kartı var
  <Row><ItemImage id="gregtech:gt.metaitem.01:17020" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="4.3 3 1">
  (4) Dışa Aktarma Veriyolu #2: Altın Külçesi'ne filtrelenmiş, 2 Hızlandırma Kartı var
  <Row><ItemImage id="minecraft:gold_ingot" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="4.3 4 1">
  (5) Dışa Aktarma Veriyolu #3: Certus Kuvars Kristali'ne filtrelenmiş, 2 Hızlandırma Kartı var
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:10" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 6 0" max="4.3 5 1">
  (6) Dışa Aktarma Veriyolu #4: Elmas'a filtrelenmiş, 2 Hızlandırma Kartı var
  <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 0" max="2 2 1">
  (7) Dışa Aktarma Veriyolu #5: Kızıltaş Tozu'na filtrelenmiş, 2 Hızlandırma Kartı var
  <Row><ItemImage id="minecraft:redstone" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="3 2 1">
  (8) Yontucu #1: Varsayılan yapılandırmasında. Silisyum Baskı Kalıbı ve 4 Hızlandırma Kartı var
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 3 0" max="3 4 1">
  (9) Yontucu #2: Varsayılan yapılandırmasında. Mantık Baskı Kalıbı ve 4 Hızlandırma Kartı var
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="3 5 1">
  (10) Yontucu #3: Varsayılan yapılandırmasında. Hesaplama Baskı Kalıbı ve 4 Hızlandırma Kartı var
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="3 6 1">
  (11) Yontucu #4: Varsayılan yapılandırmasında. Mühendislik Baskı Kalıbı ve 4 Hızlandırma Kartı var
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 0" max="1 3 1">
  (12) Yontucu #5: Varsayılan yapılandırmasında. 4 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 2 0" max="3 1 1">
  (13) İçe Aktarma Veriyolu #1: Varsayılan yapılandırmasında, 2 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 4 0" max="3 3 1">
  (14) İçe Aktarma Veriyolu #2: Varsayılan yapılandırmasında, 2 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 5 0" max="3 4 1">
  (15) İçe Aktarma Veriyolu #3: Varsayılan yapılandırmasında, 2 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 6 0" max="3 5 1">
  (16) İçe Aktarma Veriyolu #4: Varsayılan yapılandırmasında, 2 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 3 0" max="1 3.3 1">
  (17) Depolama Veriyolu #2: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1.7 0" max="1 2 1">
  (18) Depolama Veriyolu #3: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 0" max="0.7 3 1">
  (19) İçe Aktarma Veriyolu #5: Varsayılan yapılandırmasında, 2 Hızlandırma Kartı var
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="5 0.7 0" max="6 1 1">
  (20) Depolama Veriyolu #4: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.3 2.7 0.3" max="3.7 3 0.7">
  Kuvars Fiber üç yontucunun hepsine güç verir çünkü yontucular kablo gibi davranıp enerji iletir
  </BoxAnnotation>

  <DiamondAnnotation pos="7 1.5 0.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="185" pitch="5" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1), ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> kalıplarıyla birlikte varsayılan yapılandırmasındadır.
  Kalıpların doğrudan ham kaynaklardan tamamlanmış işlemciye gittiğini ve [baskı kalıbını](../items_blocks/presses.md) **İÇERMEDİĞİNİ** unutma.

  ![Mantık Kalıbı](../assets/images/logic_pattern.png)
  ![Hesaplama Kalıbı](../assets/images/calculation_pattern.png)
  ![Mühendislik Kalıbı](../assets/images/engineering_pattern.png)

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2, 17, 18, 20) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> (3-7) ilgili malzemeye filtrelenmiştir. 2 adet <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> içerirler.
<Row>
  <ItemImage id="gregtech:gt.metaitem.01:17020" scale="2" />
  <ItemImage id="minecraft:gold_ingot" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:10" scale="2" />
  <ItemImage id="minecraft:diamond" scale="2" />
  <ItemImage id="minecraft:redstone" scale="2" />
</Row>
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (13-16, 19) varsayılan yapılandırmasındadır. 2 adet <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> içerirler.
* <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> blokları varsayılan yapılandırmasındadır. İlgili [baskı kalıbını](../items_blocks/presses.md)
ve 4 adet <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> içerirler.
<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="2" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="2" />
</Row>

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> malzemeleri varile iter.
2. İlk [boru alt ağı](pipe_subnet.md) (turuncu), silisyumu, kızıltaş tozunu ve ilgili işlemcinin malzemesini
(Altın Külçesi, Certus Kuvars Kristali veya Elmas) varilden çekip ilgili <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> içine koyar.
3. İlk dört <ItemLink id="appliedenergistics2:tile.BlockInscriber" />, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:20" /> ile <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:22" />,
<ItemLink id="appliedenergistics2:item.ItemMultiMaterial:23" /> veya <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:24" /> üretir.
4. İkinci ve üçüncü [boru alt ağı](pipe_subnet.md) (yeşil), baskılı devreleri ilk dört <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> içinden alıp
    beşinci, son montaj <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> içine koyar.
5. Beşinci <ItemLink id="appliedenergistics2:tile.BlockInscriber" />, [işlemciyi](../items_blocks/processors.md) birleştirir.
6. Dördüncü [boru alt ağı](pipe_subnet.md) (mor), işlemciyi ME Arayüzüne koyar ve ana ağa geri döndürür.