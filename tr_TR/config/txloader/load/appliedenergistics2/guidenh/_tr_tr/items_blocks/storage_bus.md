---
navigation:
  parent: /items_blocks_index.md
  title: ME Depolama Veriyolu
  icon: appliedenergistics2:item.ItemMultiPart:220
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:220
- ae2fc:part_fluid_storage_bus
- thaumicenergistics:part.base:2
---

# Depolama Veriyolu

<Row gap="20">
<ItemImage id="appliedenergistics2:item.ItemMultiPart:220" scale="4" />
<ItemImage id="ae2fc:part_fluid_storage_bus" scale="4" />
<ItemImage id="thaumicenergistics:part.base:2" scale="4" />
</Row>

Depolama veriyolu, bitişikteki envanteri [ağ depolamasına](../ae2_mechanics/import_export_storage.md) dönüştürür. Ağ, içeriğini görebilir ve [cihazları](../ae2_mechanics/devices.md) karşılamak için eşya ekleyebilir veya çekebilir.

Bir veya daha fazla depolama veriyolunu tek depolaması olarak bir [alt ağa](../ae2_mechanics/subnetworks.md) yerleştirerek, veriyolları eşya transferi için kaynak veya hedef olarak da işlev görebilir (bkz. [Boru Alt Ağı](../tricks_example/pipe_subnet.md)). Çekmeceler gibi büyük, optimize edilmiş envanterler sorun değildir, ancak çok sayıda yuvası olan optimize edilmemiş envanterler performansı düşürebilir.

Depolama veriyolları [Kabloların alt parçalarıdır](../ae2_mechanics/cables_subparts.md).

## Filtreleme

Varsayılan olarak veriyolu her şeyi depolar. Filtre yuvalarına yerleştirilen eşyalar bir beyaz liste oluşturur. Eşyalar ve sıvılar NEI'den filtrelerin içine sürüklenebilir ve bir sıvı kabıyla sağ tıklamak kap eşyası yerine sıvıyı ayarlar.

## Öncelik

Önceliği ayarlamak için GUI'nin sağ üst köşesindeki İngiliz Anahtarı'na tıkla. Eşyalar önce en yüksek öncelikli depolamaya girer. Eşit önceliklerde, eşyayı zaten içeren depolama tercih edilir; filtrelenmiş depolamalar filtrelenmiş eşyalarını zaten içeriyor sayılır. Çıkarma en düşük öncelikten başlar.

## Ayarlar

* Veriyolu, bitişikteki envanterin mevcut içeriğine göre bölümlenebilir.
* Veriyolunun çekemediği eşyaların ağa görünür kalıp kalmayacağını seçebilirsin (örneğin bir <ItemLink id="appliedenergistics2:tile.BlockInscriber" /> cihazının orta girdi yuvası).
* Filtreleme, ekleme ve çıkarmaya ya da yalnızca eklemeye uygulanabilir.
* Veriyolu çift yönlü, yalnızca ekleme veya yalnızca çıkarma olabilir.

## Yükseltmeler

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> filtre yuvası sayısını artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> bulanık eşleştirmeyi ve NBT yok sayan filtreleri etkinleştirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> beyaz listeyi kara listeye çevirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" /> cevher sözlüğü adına göre filtreler.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:220" />

