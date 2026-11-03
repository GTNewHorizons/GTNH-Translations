---
navigation:
  parent: /items_blocks_index.md
  title: ME Seviye Vericisi
  icon: appliedenergistics2:item.ItemMultiPart:280
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:280
---

# Seviye Vericisi

<ItemImage id="appliedenergistics2:item.ItemMultiPart:280" scale="4" />

Seviye vericisi, [ağ deposundaki](../ae2_mechanics/import_export_storage.md) bir eşyanın miktarına göre kızıltaş sinyali yayar. Bir varyantı ise ağın [enerji](../ae2_mechanics/energy.md) seviyesine göre yayar. Eşyalar ve sıvılar NEI'den filtre yuvasına sürüklenebilir veya bir sıvı kabıyla sağ tıklayarak bir sıvı seçilebilir.

Seviye vericileri [Kablolar](../ae2_mechanics/cables_subparts.md) alt parçalarıdır ve çoğu [cihaz](../ae2_mechanics/devices.md) Bloklarının aksine bir [kanal](../ae2_mechanics/channels.md) gerektirmez.

## Ayarlar

* Verici “büyük veya eşit” ve “küçük” modlarını destekler.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> ile, bir eşya üretilirken yayabilir veya eşyayı üretmek için sinyal yayabilir.

## Yükseltmeler

* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> bulanık eşleştirmeyi ve NBT'yi yok sayan filtreleri etkinleştirir.
* <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> üretim işlevini etkinleştirir.

## Üretim İşlevi

Üretim kartı takıldığında verici üretim moduna geçer. “Üretim sırasında yay” özelliği, [otomatik üretim](../ae2_mechanics/autocrafting.md) bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> aracılığıyla süzülmüş eşyayı yaparken kızıltaşı açar. “Eşya üretmek için yay” özelliği, içeriksiz sanal bir [desen](patterns.md) oluşturur; o eşyayı talep etmek bu vericiden kızıltaş yayar. Aynı eşya için bir arayüze gerçek bir desen de koyma.

Bu, sonsuz çiftlikler veya olasılıklı çıktısı olan makineler ile “1 kırıktaş = 2 kırıktaş” gibi [özyinelemeli tarifler](../tricks_example/recursive_crafting_setup.md) için kullanışlıdır.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:280" />

