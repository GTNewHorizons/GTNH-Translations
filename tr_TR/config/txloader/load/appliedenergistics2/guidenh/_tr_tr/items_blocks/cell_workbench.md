---
navigation:
  parent: /items_blocks_index.md
  title: Hücre Tezgahı
  icon: appliedenergistics2:tile.BlockCellWorkbench
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockCellWorkbench
---

# Hücre Tezgahı

<ItemImage id="appliedenergistics2:tile.BlockCellWorkbench" scale="4" />

Hücre Tezgahı [depolama hücrelerini](storage_cells.md) ve <ItemLink id="appliedenergistics2:item.ItemViewCell" /> yapılandırmak için kullanılabilir.

Hücrelere [yükseltme kartları](upgrade_cards.md) takabilir veya hücrenin depolayabileceği eşya türlerini kısıtlamak için "bölümlemeler" yapılandırabilirsin.

Gerekli eşyaya veya sıvıya sahip değilsen filtre yuvasına yerleştirmek için NEI'den sürükleyebilirsin.

Demir kova veya sıvı tankı gibi bir sıvı kabını <Color id="YELLOW"><KeyBind id="key.container_interaction.desc" /></Color> tuşuna basılı tutarak kullanmak, filtre olarak demir kova veya tank eşyası yerine sıvıyı ayarlar.

## Ayarlar

Hücre Tezgahının sol üstünde ve sağ üstünde birkaç düğme vardır. Bazı düğmeler yalnızca ilgili özelliği destekleyen hücreler için gösterilir:

* **Temizle**: Tezgahdaki tüm bölümleme ayarlarını temizler.
* **Depolamayı Bölümle**: Bölümleme yuvalarını hücrede şu anda depolanan eşyalara göre otomatik doldurur.
* **Kopyalama Modu**: Hücre çıkarıldığında tezgahın bölümleme ayarlarının korunup korunmayacağını belirler. Varsayılan olarak temizlenirler. Koruma etkinleştirildiğinde aynı bölümleme ayarları diğer hücrelere kopyalanabilir. Yeni hücrenin zaten bölümleme ayarları varsa hücrenin kendi ayarları önceliklidir.
* **Bulanık Karşılaştırma**: Bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" showIcon="left" linksTo="../items_blocks/upgrade_cards.md#Fuzzy Card"/> takılıyken kullanılabilir. Bölümlemelerin bulanık eşleştirmeyi nasıl yapacağını ayarlar.
* **Cevher Sözlüğü Filtresi**: Bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" showIcon="left" linksTo="../items_blocks/upgrade_cards.md#Ore Dictionary Filter Card"/> takılıyken kullanılabilir. Filtreleme için cevher sözlüğü adlarının girilmesini sağlar. Etkinleştirildiğinde normal bölümleme yuvaları gizlenir ve bulanık moda göre öncelik kazanır.
* **Hücre Kısıtlaması**: Kısıtlama ayarları GUI'sini açmak için tıkla:
  * **Maksimum Eşya Sayısı**: Her eşya türünü ayrı ayrı sınırlamak yerine hücrede depolanan toplam eşya sayısını sınırlar.
  * **Maksimum Eşya Türü**: Hücrenin depolayabileceği farklı eşya türü sayısını sınırlar.

  `0` girilmesi ilgili kısıtlamayı devre dışı bırakır. Kısıtlama değerleri hücrenin kendi kapasitesini veya maksimum eşya türü sayısını aşamaz. Her iki kısıtlamayı da temizlemek için sıfırlama düğmesine tıkla.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockCellWorkbench" />