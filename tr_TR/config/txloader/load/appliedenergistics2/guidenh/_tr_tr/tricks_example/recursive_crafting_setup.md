---
navigation:
  parent: ../tricks_example_index.md
  title: Özyinelemeli Üretim
  icon: witchery:ingredient:130
---

# Özyinelemeli Üretim Düzeneği

[Otomatik Üretim](../ae2_mechanics/autocrafting.md) bölümünde belirtildiği gibi, otomatik üretim planlayıcısı birincil çıktısı aynı zamanda girdi olan bir tarifi işleyemez. Örneğin <ItemLink id="witchery:ingredient:130" /> eşyasını çoğaltan tarifi işleyemez.

Bir çözüm, <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> cihazını bir [kalıp](../items_blocks/patterns.md) olarak kullanmaktır.

Ardından standart seviye vericisi, sürekli üretim yapan küçük bir düzenek başlatmak için kullanılabilir. Bu bölümde örnek olarak <ItemImage id="witchery:ingredient:130" /><ItemLink id="witchery:ingredient:130" /> eşyasını çoğaltan bir düzenek kullanılmaktadır.

<RecipeFor id="witchery:ingredient:130" />

***

<GameScene zoom="6" width="350" interactive={true}>
  <ImportStructure src="../assets/structures/recursive_recipe_setup.snbt" />
  <IsometricCamera yaw="15" pitch="30" />
  <DiamondAnnotation pos="3.5 0.5 1.5" color="#00ff00">
    Ana ağa
  </DiamondAnnotation>
  <BlockAnnotation pos="2 0 1">
    (1) Arayüz: gerekli ek malzemeleri depolayacak şekilde yapılandır: magma kremi, blaze tozu ve Küçük Nether Yıldızı Tozu Yığını.
    <Row>
      <ItemImage id="minecraft:magma_cream" scale="2" />
      <ItemImage id="minecraft:blaze_powder" scale="2" />
      <ItemImage id="gregtech:gt.metaitem.01:506" scale="2" />
    </Row>
  </BlockAnnotation>
  <BlockAnnotation pos="0 0 0">
    (5) Moleküler Montajcı: <ItemLink id="witchery:ingredient:130" /> eşyasını çoğaltma kalıbını içerir.
    <Row><RecipeFor id="witchery:ingredient:130" /></Row>
    Kurarken içine bir bileşenin elle yerleştirilmesi gerekir.
  </BlockAnnotation>
  <BoxAnnotation min="1.3 1 1.3" max="1.7 1.3 1.7">
    (2) Standart seviye vericisi: “<ItemLink id="witchery:ingredient:130" />” için yapılandır ve “eşyayı üretmek için Kızıltaş sinyali yay” olarak ayarla.
    <Row>
      <ItemImage id="witchery:ingredient:130" scale="2" />
      <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />
    </Row>
  </BoxAnnotation>
  <BoxAnnotation min="1.7 0 1" max="2 1 2">
    (3) İçe aktarma veriyolu #1: arayüzde depolanan eşyalara göre filtrele. Bir Kızıltaş kartı tak. Kızıltaş modunu “Kızıltaş sinyaliyle etkin” olarak ayarla.
    <Row>
      <ItemImage id="minecraft:magma_cream" scale="2" />
      <ItemImage id="minecraft:blaze_powder" scale="2" />
      <ItemImage id="gregtech:gt.metaitem.01:506" scale="2" />
      <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" />
    </Row>
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1">
    (6) İçe aktarma veriyolu #2: varsayılan yapılandırma.
  </BoxAnnotation>
  <BoxAnnotation min="0 1 0" max="1 1.3 1">
    (4) Depolama veriyolu #1: önceliği diğer depolama veriyolundan yüksek. Bu çok önemlidir.
  </BoxAnnotation>
  <BoxAnnotation min="2 0 0.7" max="3 1 1">
    (7) Depolama veriyolu #2: “<ItemLink id="witchery:ingredient:130" />” için filtrele. Önceliği diğer depolama veriyolundan düşük.
    <Row>
      <ItemImage id="witchery:ingredient:130" scale="2" />
    </Row>
  </BoxAnnotation>
</GameScene>

## Yapılandırma

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) Gerekli ek malzemeleri depolayacak şekilde yapılandır: magma kremi, blaze tozu ve Küçük Nether Yıldızı Tozu Yığını.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (2) “<ItemLink id="witchery:ingredient:130" />” için yapılandır ve “eşyayı üretmek için Kızıltaş sinyali yay” olarak ayarla.
* İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (3), arayüzde depolanan eşyaları filtreleyecek şekilde ayarlanmıştır. Bir Kızıltaş kartı tak ve Kızıltaş modunu “Kızıltaş sinyaliyle etkin” olarak ayarla.
* İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (4) önceliği, ikinci depolama veriyolununkinden *yüksek* olmalıdır. Bkz. [Öncelik](../ae2_mechanics/import_export_storage.md#storage-priority).
* <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> (5), <ItemLink id="witchery:ingredient:130" /> eşyasını çoğaltma kalıbını ve elle yerleştirilmiş bir <ItemLink id="witchery:ingredient:130" /> içerir.

  *Kalıp*
  <RecipeFor id="witchery:ingredient:130" />

* İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (6) varsayılan yapılandırmayı kullanır.
* İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (7), “<ItemLink id="witchery:ingredient:130" />” için filtrelenmiştir. [Önceliği](../ae2_mechanics/import_export_storage.md#storage-priority) ilk depolama veriyolununkinden *düşüktür*.

## Nasıl Çalışır

1. Bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> içerdiği ve “eşyayı üretmek için Kızıltaş sinyali yay” olarak ayarlandığı için <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> bir [kalıp](../items_blocks/patterns.md) gibi davranır. “<ItemLink id="witchery:ingredient:130" />” [terminalde](../items_blocks/terminals.md) [otomatik üretilebilen](../ae2_mechanics/autocrafting.md) bir eşya olarak görünür.
2. Bir oyuncudan veya sistemden üretim isteği geldiğinde standart seviye vericisi açılır.
3. İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> standart seviye vericisi tarafından etkinleştirilir ve malzemeleri <ItemLink id="appliedenergistics2:tile.BlockInterface" /> cihazından çeker.
4. Ağda bu malzemeleri depolayabilen tek <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />, montajcının üzerindeki olandır.
5. <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> malzemeleri alır (içinde zaten bir <ItemLink id="witchery:ingredient:130" /> vardır), üretime başlar ve iki <ItemLink id="witchery:ingredient:130" /> üretir.
6. İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> bir <ItemLink id="witchery:ingredient:130" /> çeker.
7. İlk depolama veriyolunun önceliği daha yüksektir, bu yüzden <ItemLink id="witchery:ingredient:130" /> montajcıya geri döner.
8. İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> bir <ItemLink id="witchery:ingredient:130" /> çeker.
9. Montajcı artık <ItemLink id="witchery:ingredient:130" /> kabul edemez, bu yüzden ikinci <ItemLink id="witchery:ingredient:130" /> daha düşük öncelikli depolama veriyoluna girer ve arayüze gönderilir.
10. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (<ItemLink id="witchery:ingredient:130" /> depolayacak şekilde yapılandırılmamıştır) onu ağa geri gönderir.