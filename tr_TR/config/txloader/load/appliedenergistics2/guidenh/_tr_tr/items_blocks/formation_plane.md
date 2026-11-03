---
navigation:
  parent: /items_blocks_index.md
  title: ME Oluşum Düzlemi
  icon: appliedenergistics2:item.ItemMultiPart:320
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:320
---

# Oluşum Düzlemi

<Row gap="20">
<ItemImage id="appliedenergistics2:item.ItemMultiPart:320" scale="4" />
<ItemImage id="ae2fc:part_fluid_formation_plane" scale="4" />
</Row>

Oluşum düzlemi blok yerleştirir ve eşya düşürür. Yalnızca ekleme yapan bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> gibi çalışır; [cihazlar](../ae2_mechanics/devices.md) eşyaları, örneğin bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> veya <ItemLink id="appliedenergistics2:tile.BlockInterface" /> gibi [ağ depolarına](../ae2_mechanics/import_export_storage.md) eklediğinde bunları yerleştirir veya düşürür.

<GameScene width="350" height="220" zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

Bu cihaz, [boru alt ağı](../tricks_example/pipe_subnet.md) kurulumlarındaki depolama veriyollarıyla aynı mekanikleri kullanır ve eşyaları taşımak yerine blok yerleştirmek veya eşya düşürmek istediğinde onların yerini alabilir.

Bunlar [kablo alt parçalarıdır](../ae2_mechanics/cables_subparts.md).

**Chunk sahiplenmende sahte oyunculara izin ver.**

## Filtreleme

Varsayılan olarak düzlem her şeyi yerleştirir veya düşürür. Filtre yuvalarındaki eşyalar beyaz liste oluşturur. Eşyalar ve sıvılar NEI'den sürüklenebilir; bir sıvı kabıyla sağ tıklamak sıvıyı seçer.

## Öncelik

Öncelik ayarlamak için GUI'nin sağ üst köşesindeki anahtara tıkla. Ağa giren eşyalar en yüksek öncelikli depodan başlar.

## Ayarlar

* Düzlem dünyada blok yerleştirebilir veya eşya düşürebilir.

## Yükseltmeler

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> filtre yuvası sayısını artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> bulanık eşleştirmeyi ve NBT yok sayan filtreleri etkinleştirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> beyaz liste filtrelemesini kara listeye çevirir.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:320" />