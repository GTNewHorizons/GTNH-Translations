---
navigation:
  parent: ../tricks_example_index.md
  title: Kova Boşaltıcı
  icon: minecraft:bucket
---

# Kova Boşaltıcı

Ayrıca bkz. [Kova Doldurucu](bucket_filler.md).

Bunun bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullandığını, dolayısıyla [otomatik üretim](../ae2_mechanics/autocrafting.md)
düzeneğine entegre edilmek üzere tasarlandığını unutma.

Bazen hayat zahmetlidir ve sıvının kendisine ihtiyaç duyarsın ama sıvıyı yalnızca kovada üretebilirsin. Bazen bir makine bunu senin için yapabilir
(Termal Expansion'daki Sıvı Aktarıcı gibi), ancak bunu senin için kolayca yapan bir mod her zaman elinde olmayabilir. Neyse ki
vanilla Minecraft'ın biraz daha az pratik bir yolu var: <ItemLink id="minecraft:dispenser" />.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/bucket_emptier.snbt" />

  <BoxAnnotation color="#dddddd" min="2 1 3" max="3 2 4">
  (1) ME Arayüzü: Üretimi "Kızıltaş sinyaliyle" seçeneğiyle kilitleyecek şekilde ayarla ve engelleme modunu aç; ilgili işleme kalıplarını ekle.

  <Row>
    <FloatingImage src="../assets/images/water_empty_pattern.png" displayWidth="150" />
    <FloatingImage src="../assets/images/lava_empty_pattern.png" displayWidth="150" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.1 2 3.1" max="2.9 2.2 3.9">
  (2) Arayüz: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.1 2 2.1" max="1.9 2.2 2.9">
  (3) Depolama Veriyolu #1: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.05 1.05 3" max="0.95 1.95 3.2">
  (4) Yok Etme Düzlemi: Yapılandırılacak GUI yok.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.2 1.2 3" max="1.8 1.8 3.2">
  (5) İçe Aktarma Veriyolu: Kovalara göre filtrelenmiş.
  <ItemImage id="minecraft:bucket" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.8 1.1 3.1" max="2 1.9 3.9">
  (6) Depolama Veriyolu #2: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <DiamondAnnotation pos="5 1.5 3.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1), üretimi "Kızıltaş sinyaliyle" seçeneğiyle kilitleyecek ve engelleme modu açık olacak şekilde,
  ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> kalıplarıyla ayarlanmıştır.
  
    ![Şarj Cihazı Kalıbı](../assets/images/water_empty_pattern.png)
    ![Şarj Cihazı Kalıbı](../assets/images/lava_empty_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2) varsayılan yapılandırmasındadır.
* İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> (4) GUI'sizdir ve yapılandırılamaz.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (5) kovalara göre filtrelenmiştir.
  <ItemImage id="minecraft:bucket" scale="2" />
* İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (6) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> bileşenleri arayüze iter.
   (Aslında bir optimizasyon olarak, sağlayıcının yüzlerinin uzantısıymış gibi doğrudan depolama veriyolu üzerinden iter. Eşyalar aslında hiçbir zaman arayüze girmez.)
2. [boru alt ağları](pipe_subnet.md#providing-to-multiple-places) bölümünde açıklanan mekanizmalar sayesinde,
   kova <ItemLink id="minecraft:dispenser" /> içinde son bulur.
3. <ItemLink id="minecraft:comparator" /> dağıtıcıdaki kovayı algılar ve böylece aynı anda dağıtıcıya güç verir ve
   ME arayüzünü kilitler.
4. Dağıtıcı kovadaki sıvıyı boşaltır ve artık içinde boş bir kova vardır.
5. <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> boş kovayı dağıtıcıdan çeker ve
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> aracılığıyla ME Arayüzüne depolayarak ana ağa geri döndürür.
6. Karşılaştırıcı dağıtıcının boş olduğunu görür ve sağlayıcının kilidini açar.