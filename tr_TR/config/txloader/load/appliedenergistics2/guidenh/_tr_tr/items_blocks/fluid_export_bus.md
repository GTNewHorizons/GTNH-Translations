---
navigation:
  parent: /items_blocks_index.md
  title: ME Sıvı Dışa Aktarma Veriyolu
  icon: ae2fc:part_fluid_export
categories:
- devices
item_ids:
- ae2fc:part_fluid_export
---

# ME Sıvı Dışa Aktarma Veriyolu

<ItemImage id="ae2fc:part_fluid_export" scale="4" />

*"AE2FC'den gizemli güç"*

Bu cihaz eşyaları ve sıvıları (ve bir eklenti desteklediğinde ek materyal türlerini) [ağ
depolamasından](../ae2_mechanics/import_export_storage.md) çeker ve bağlı olduğu kaba iter.

Ek yükü azaltmak için veriyolu son zamanlarda etkin değilse düşük frekanslı bir uyku moduna girer.
Başarılı bir dışa aktarımdan sonra saniyede dört işlem yaparak tam hıza döner.

Bir [kablo alt parçasıdır](../ae2_mechanics/cables_subparts.md).

## Filtre Ayarları

Varsayılan olarak hiçbir şey dışa aktarılmaz. Bir filtre yuvasına eşya eklemek beyaz liste oluşturur ve yalnızca seçilen eşyaya izin verir.
Eşyalar ve sıvılar, şu anda elinde olmasalar bile doğrudan NEI'den bir filtre yuvasına sürüklenebilir.
Kabın kendisini filtrelemek yerine sıvı filtresi ayarlamak için kova veya tank gibi bir sıvı kabına sağ tıkla.

## Yükseltme Desteği

Veriyolu şu [yükseltme kartlarını](upgrade_cards.md) destekler:

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> filtre yuvası sayısını artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> işlem başına aktarılan miktarı artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> filtreyi kara listeye çevirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> [otomatik üretim](../ae2_mechanics/autocrafting.md) talep eder; önce depolanan eşyaları kullanma veya her zaman yeni üretme seçenekleriyle.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> Kızıltaş kontrolü ekler (yüksek, düşük veya darbe etkinleştirme).

## Aktarım Hızı

| Hız kartları | İşlem başına miktar |
| :--- | :--- |
| 0 | 1 |
| 1 | 8 |
| 2 | 32 |
| 3 | 64 |
| 4 | 96 |

## Tarif

<RecipeFor id="ae2fc:part_fluid_export" />

