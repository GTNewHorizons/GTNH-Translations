---
navigation:
  parent: /items_blocks_index.md
  title: ME Arayüzü
  icon: appliedenergistics2:tile.BlockInterface
item_ids:
  - appliedenergistics2:tile.BlockInterface
  - ae2fc:fluid_interface
categories:
- devices
---

# ME Arayüzü

<Row gap="20">
<BlockImage id="appliedenergistics2:tile.BlockInterface" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:440" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:471" scale="4" />
</Row>

Bir arayüz küçük bir sandık ve sıvı tankı gibi işlev görür. Yuvalarında yapılandırılmış stok seviyelerine göre [ağ depolamasından](../ae2_mechanics/import_export_storage.md) eşya ekler ve çıkarır. Aktarımları tek bir oyun tick'inde, tick başına en fazla dokuz eşya yığınına kadar tamamlamaya çalışır; bu da onu hızlı bir giriş/çıkış yöntemi yapar.

Çoğu sıvı tankının aksine bir arayüz eşyaların yanı sıra en fazla dokuz sıvı türü de depolayabilir. Esasen ek ağ davranışına sahip bir sandık veya çoklu sıvı tankıdır; ağdan bağlantısını kesmek bu davranışı devre dışı bırakır. Bu, çok sayıda farklı şeyden az miktarda depolanması gerektiğinde arayüzleri kullanışlı kılar.

## Bir Arayüzün İç Yapısı

Bir arayüz esasen kendisine <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> eklenmiş bir sandık/tanktır.

<GameScene width="450" height="200" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_internals.snbt" />
  <BoxAnnotation color="#dddddd" min="2.3 0.3 1.3" max="9.7 1 1.7">Seviye yayıcıları stok miktarını kontrol eder</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 4 1.3" max="9.7 4.7 1.7">Seviye yayıcıları stok miktarını kontrol eder</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 1.3 1.3" max="9.7 2 1.7">İçe aktarma veriyolları oyun tick'i başına bir yığın aktarır</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 3 1.3" max="9.7 3.7 1.7">Dışa aktarma veriyolları oyun tick'i başına bir yığın aktarır</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2 2 1" max="10 3 2">Dokuz bağımsız iç yuva</BoxAnnotation>
  <IsometricCamera yaw="15" pitch="15" />
</GameScene>

## Özel Etkileşimler

Yapılandırılmamış bir arayüze bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> bağlamak, arayüzün ağının tüm [ağ depolamasını](../ae2_mechanics/import_export_storage.md) depolama veriyolu ağına açar. Arayüz ağı tek büyük bir sandık gibi davranır. Bir arayüzün istek yuvasına eşya ayarlamak bu davranışı devre dışı bırakır.

Başka bir arayüze bağlı bir arayüz bir [alt ağ](../ae2_mechanics/subnetworks.md) oluşturabilir: kaynak arayüzün isteği yoksa kendi envanterini atlar ve eşyaları doğrudan hedef alt ağdaki depolamaya gönderir; o depolama sonraki partiyi kabul edemiyorsa bekler.

## Varyantlar

Arayüzlerin normal ve düz/[alt parça](../ae2_mechanics/cables_subparts.md) varyantları vardır. Normal arayüzler her taraftan çıktı verir ve alır, ağ bağlantısı sağlar. Düz arayüzler kablo alt parçalarıdır, bu yüzden birkaçı tek bir kabloyu paylaşabilir; kendi depolamalarıyla eşya alışverişi yapabilirler ama ağ bağlantısı sağlamazlar. İki form üretim ızgarasında birbirine dönüştürülebilir.

## Ayarlar

Üst sıra stokta tutulacak eşyaları yapılandırır. Eşyalar doğrudan yerleştirilebilir veya NEI'den sürüklenebilir; miktarını ayarlamak için dolu bir yuvanın üzerindeki İngiliz anahtarına tıkla. Filtre olarak kap eşyası yerine sıvıyı ayarlamak için bir sıvı kabıyla sağ tıkla. Stok için yapılandırılmış bir yuva başka eşya kabul etmez.

## Yükseltmeler

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> bulanık eşleştirmeyi ve NBT yok sayan filtreleri etkinleştirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> arayüzün [otomatik üretim](../ae2_mechanics/autocrafting.md) sisteminden eksik bileşenleri istemesini sağlar.

## Öncelik

Önceliği ayarlamak için GUI'nin sağ üst köşesindeki İngiliz anahtarına tıkla. Yüksek öncelikli arayüzler eşyaları düşük öncelikli arayüzlerden önce alır.

## Tarif

<Row>
<Recipe id="appliedenergistics2:tile.BlockInterface" />
<RecipeFor id="appliedenergistics2:item.ItemMultiPart:440" />
</Row>
