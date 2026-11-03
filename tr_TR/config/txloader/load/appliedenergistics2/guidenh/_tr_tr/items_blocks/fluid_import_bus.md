---
navigation:
  parent: /items_blocks_index.md
  title: ME Sıvı İçe Aktarma Veriyolu
  icon: ae2fc:part_fluid_import
categories:
- devices
item_ids:
- ae2fc:part_fluid_import
---

# ME Sıvı İçe Aktarma Veriyolu

<ItemImage id="ae2fc:part_fluid_import" scale="4" />

*"AE2FC'den gelen gizemli güç"*

İçe aktarma veriyolu, bitişik bir kaptan eşyaları ve sıvıları (ve bir eklenti tarafından desteklendiğinde ek malzeme
türlerini) çeker ve [ağ depolamasında](../ae2_mechanics/import_export_storage.md) saklar.

Gecikmeyi azaltmak için veriyolu, yakın zamanda hiçbir şey içe aktarmadığında düşük frekanslı bir uyku moduna girer.
Bir eşyanın içe aktarılması onu uyandırır ve saniyede dört işlem yaparak tam hıza döndürür.

Bir [kablo alt parçasıdır](../ae2_mechanics/cables_subparts.md).

## Filtre Ayarları

Varsayılan olarak erişilebilen tüm eşyalar içe aktarılır. Bir filtre yuvasına eşya eklemek beyaz liste modunu etkinleştirir
ve yalnızca o eşyaya izin verir. Eşyalar, sahibi olmasan bile NEI'den bir filtre yuvasına sürüklenebilir. Kap eşyasını
filtrelemek yerine sıvı filtresi ayarlamak için kova veya tank gibi bir sıvı kabına sağ tıkla.

## Yükseltme Desteği

Veriyolu şu [yükseltme kartlarını](upgrade_cards.md) destekler:

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:27" /> filtre yuvası sayısını artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> işlem başına aktarılan miktarı artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> filtreyi kara listeye çevirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> kızıltaş kontrolü ekler (yüksek, düşük veya darbe etkinleştirme).

## Aktarım Hızı

| Hız kartları | İşlem başına miktar |
| :--- | :--- |
| 0 | 1 |
| 1 | 8 |
| 2 | 32 |
| 3 | 64 |
| 4 | 96 |

## Tarif

<RecipeFor id="ae2fc:part_fluid_import" />

