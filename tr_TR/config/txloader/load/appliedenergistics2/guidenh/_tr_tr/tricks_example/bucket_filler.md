---
navigation:
  parent: ../tricks_example_index.md
  title: Kova Doldurucu
  icon: minecraft:water_bucket
---

# Kova Doldurucu

Ayrıca bkz. [Kova Boşaltıcı](bucket_emptier.md).

Not: Bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullandığı için bunun [otomatik üretim](../ae2_mechanics/autocrafting.md) kurulumuna entegre olmak üzere tasarlandığını unutma.

Bazen hayat elverişsizdir ve sıvının kendisi yerine kovalarca sıvıya ihtiyaç duyarsın. Bazen bunu senin için bir makine yapabilir
(Thermal Expansion'daki Sıvı Aktarıcı gibi), ama bunu her zaman senin için kolayca yapan bir modun olmayabilir. Neyse ki
vanilla Minecraft'ın biraz daha az elverişli bir yolu var: <ItemLink id="minecraft:dispenser" />.

**Not: Çoğu zaman bunu yapmak zorunda değilsin, çünkü bir
[Kalıp Kodlama Terminali](../items_blocks/terminals.md#pattern-encoding-terminal) içindeki Sıvı Muadilleri, üretim tarifinde
kova yerine sıvının kendisini kullanmana izin verir.**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/bucket_filler.snbt" />

  <BoxAnnotation color="#dddddd" min="2 1 3" max="3 2 4">
  (1) ME Arayüzü: İlgili işleme kalıplarıyla birlikte, üretimi "Kızıltaş sinyaliyle" kilitleyecek şekilde ayarla.

  <Row>
    <FloatingImage src="../assets/images/water_fill_pattern.png" displayWidth="150" />
    <FloatingImage src="../assets/images/lava_fill_pattern.png" displayWidth="150" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.8 1.1 3.1" max="2 1.9 3.9">
  (2) Arayüz: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.1 1.1 3" max="1.9 1.9 3.2">
  (3) Depolama Veriyolu #1: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.05 1.05 3" max="0.95 1.95 3.2">
  (4) Oluşum Düzlemi: Bir evirici kart kullanılarak kovaları kara listeye alacak şekilde süzüldü.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.2 2 2.2" max="1.8 2.2 2.8">
  (5) İçe Aktarma Veriyolu: Bir evirici kart kullanılarak kovaları kara listeye alacak şekilde süzüldü.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.1 2 3.1" max="2.9 2.2 3.9">
  (6) Depolama Veriyolu #2: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <DiamondAnnotation pos="5 1.5 3.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1), ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> kalıplarıyla birlikte üretimi "Kızıltaş sinyaliyle" kilitleyecek şekilde ayarlanmıştır.
  
    ![Şarj Cihazı Kalıbı](../assets/images/water_fill_pattern.png)
    ![Şarj Cihazı Kalıbı](../assets/images/lava_fill_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2) varsayılan yapılandırmasındadır.
* İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> (4), bir evirici kart kullanılarak kovaları kara listeye alacak şekilde süzülmüştür.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (5), bir evirici kart kullanılarak kovaları kara listeye alacak şekilde süzülmüştür.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
* İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (6) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> malzemeleri arayüze iter.
   (Aslında, bir optimizasyon olarak, bunları doğrudan depolama veriyolu ve oluşum düzleminden, sanki sağlayıcının yüzlerinin uzantılarıymış gibi iter. Eşyalar aslında hiçbir zaman arayüz bloklarına girmez.)
2. [boru alt ağlarında](pipe_subnet.md#providing-to-multiple-places) ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> içinde açıklanan mekanizmalar sayesinde,
   kova <ItemLink id="minecraft:dispenser" /> içine girer ve sıvı oluşum düzlemi tarafından yerleştirilir.
3. <ItemLink id="minecraft:comparator" /> dağıtıcıdaki kovayı algılar ve böylece aynı anda hem dağıtıcıya güç verir hem de
   ME arayüzünü kilitler.
4. Dağıtıcı sıvıyı kovayla içine çeker, artık içinde dolu bir kova vardır.
5. <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> dolu kovayı dağıtıcıdan çeker ve
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> aracılığıyla ME Arayüzüne depolayarak ana ağa geri döndürür.
6. Karşılaştırıcı dağıtıcının boş olduğunu görür ve sağlayıcının kilidini açar.