---
navigation:
  parent: /items_blocks_index.md
  title: ME G/Ç Bağlantı Noktası
  icon: appliedenergistics2:tile.BlockIOPort
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockIOPort
---

# ME G/Ç Bağlantı Noktası

<BlockImage id="appliedenergistics2:tile.BlockIOPort"/>

G/Ç Bağlantı Noktası, [depolama hücrelerini](storage_cells.md) [ağ deposundan](../ae2_mechanics/import_export_storage.md) hızla doldurur veya boşaltır. <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> ile döndürülebilir.

## Ayarlar

* Hücre boşaldığında, dolduğunda veya işlem tamamlandığında hücreyi çıkış yuvasına taşı.
* Kızıltaş koşulları için <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> tak.
* Ortadaki ok aktarım yönünü seçer: hücreden ağ deposuna veya ağ deposundan hücreye.

## Yükseltmeler

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> işlem başına taşınan miktarı artırır.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:26" /> yüksek, düşük ve darbe Kızıltaş kontrolü ekler.

Soğuk durumdayken her 5 tick'te bir çalışır, ısındığında ise her tick'te. Her işlem 256 x 2^n eşya aktarır; burada n hızlandırma kartı sayısıdır.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockIOPort" />
