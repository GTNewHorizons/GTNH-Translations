---
navigation:
  parent: /items_blocks_index.md
  title: ME Sıvı Arayüzü
  icon: ae2fc:fluid_interface
item_ids:
  - ae2fc:fluid_interface
categories:
- devices
---

# ME Çift Sıvı Arayüzü

<Row gap="20">
<BlockImage id="ae2fc:fluid_interface" scale="4" />
<ItemImage id="ae2fc:part_fluid_interface" scale="4" />
<ItemImage id="ae2fc:part_fluid_p2p_interface" scale="4" />
</Row>

*"AE2FC'den gelen gizemli güç"*

Bir arayüz küçük bir sandık veya sıvı tankı gibi davranır. Yapılandırılmış yuvaları [ağ depolamasından](../ae2_mechanics/import_export_storage.md)
otomatik olarak doldurulabilir veya oraya boşaltılabilir. Tik başına en fazla dokuz eşya grubu işleyebilir ve bu sayede
yüksek hızlı borularla eşleştirildiğinde hızlı girdi ve çıktı sağlayabilir.

Yalnızca bir sıvı depolayan normal bir tankın aksine, aynı anda dokuz farklı sıvı depolayabilir ve bunun yanında eşya da depolar.
Ağdan ayrıldığında normal bir kap olarak çalışmaya devam eder.

## İç İşleyiş

Arayüz aslında birden fazla yüksek hızlı <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />
ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> veriyolunu, ayrıca birden fazla <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> seviye yayıcısını içeren bileşik bir cihazdır:

<GameScene width="450" height="200" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_internals.snbt" />
  <BoxAnnotation color="#dddddd" min="2.3 0.3 1.3" max="9.7 1 1.7">Depolanan miktarları kontrol eden seviye yayıcıları</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 4 1.3" max="9.7 4.7 1.7">Depolanan miktarları kontrol eden seviye yayıcıları</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 1.3 1.3" max="9.7 2 1.7">Yüksek hızlı içe aktarma veriyolu dizisi, tik başına bir eşya grubu</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2.3 3 1.3" max="9.7 3.7 1.7">Yüksek hızlı dışa aktarma veriyolu dizisi, tik başına bir eşya grubu</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="2 2 1" max="10 3 2">Dokuz bağımsız depolama yuvası</BoxAnnotation>
  <IsometricCamera yaw="15" pitch="15" />
</GameScene>

## Özel Etkileşimler

* Yapılandırılmamış bir arayüze <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> takmak, depolama veriyolunun
gerçekten ağın kendisine takılmış gibi arayüzün ağındaki tüm [depolamaya](../ae2_mechanics/import_export_storage.md)
erişmesini sağlar. Arayüzde herhangi bir eşya yapılandırmak bu davranışı devre dışı bırakır.

<GameScene width="200" height="150" zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/interface_storage.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

* Bir [alt ağ](../ae2_mechanics/subnetworks.md) üzerindeki yapılandırılmamış arayüz, bağlı bir ME arayüzünün doğrudan
alt ağın deposuna itmesini sağlar; arayüz yuvalarını atlar ve bir sonraki yığını göndermeden önce boş alan bekler.

<GameScene width="320" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/fluid_interface_storage.snbt" />
  <BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">Arayüz (düz varyant olmalı)</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">Depolama veriyolu dizisi</BoxAnnotation>
  <BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">Hedef makineleri (birden fazla makine veya girdi yüzü)</BoxAnnotation>
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Varyantlar

Arayüzlerin normal bir blok formu ve düz bir [Kablolar alt parçası](../ae2_mechanics/cables_subparts.md) vardır:

* **Normal arayüz:** her taraftan eşya kabul eder ve çıktı verir, her tarafta ağ bağlantısı sağlar.
* **Düz arayüz:** bir kablo üzerine sık yerleştirilebilir, yalnızca ön yüzünden kabul eder ve çıktı verir, ön yüzünde
  ağ bağlantısı sağlamaz.

İki form bir üretim ızgarasında birbirine dönüştürülebilir.

## Ayarlar

* Üstteki dokuz yuva, korunacak eşya veya sıvı miktarlarını tanımlar.
* Sıvı filtresi ayarlamak için kova gibi bir sıvı kabına sağ tıkla.
* Bir yuvanın hedef miktarını ayarlamak için yanındaki İngiliz Anahtarı'na tıkla.

## Yükseltme Desteği

Arayüz şu [yükseltme kartlarını](upgrade_cards.md) destekler:

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> bulanık eşleştirmeyi etkinleştirir (hasar değerine göre veya NBT'yi yok sayarak).
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> otomatik üretim isteklerini etkinleştirir; önce depolanan eşyaları
  özütler ve depolama yetersiz olduğunda [otomatik üretimi](../ae2_mechanics/autocrafting.md) tetikler.

## Öncelik

Öncelik ayarlamak için GUI'nin sağ üst köşesindeki İngiliz Anahtarı'na tıkla. Daha yüksek öncelikli arayüzler eşyaları önce alır.

## Tarifler

<Recipe id="ae2fc:fluid_interface" />

<RecipeFor id="ae2fc:part_fluid_interface" />
