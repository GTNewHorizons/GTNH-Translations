---
navigation:
  parent: /ae2_mechanics_index.md
  title: İçe Aktarma, Dışa Aktarma ve Depolama
  icon: appliedenergistics2:item.ItemMultiPart:240
item_ids:
- appliedenergistics2:item.ItemMultiPart:260
- ae2fc:part_fluid_export
- thaumicenergistics:part.base:3
- appliedenergistics2:item.ItemMultiPart:240
- ae2fc:part_fluid_import
- thaumicenergistics:part.base
- appliedenergistics2:item.ItemMultiPart:220
- ae2fc:part_fluid_storage_bus
- thaumicenergistics:part.base:2
---

{/* most of the content on this page should be moved to individual item pages (items_blocks directory); should be rewritten in the future*/}

# İçe Aktarma, Dışa Aktarma ve Depolama

> [!NOTE]
> Bazı bağlantılar, sayfaları henüz yazılmadığı için kırık. [GitHub](https://github.com/GTNewHorizons/GTNH-Guide-Pack) üzerinden katkıda bulunarak GTNH'nin geliştirilmesine destek ol!

## "İçe Aktarma" ve "Dışa Aktarma", "Okuma" ve "Yazma"

AE'de **içe aktarma** ve **dışa aktarma**nın tüm kullanımları ME ağının kendisine göre tanımlanır. **İçe aktarma**, bir şeyi ME ağına getirmek; **dışa aktarma** ise bir şeyi ME ağından dış dünyaya çıkarmak anlamına gelir. Örneğin bir ME Dışa Aktarma Veriyolu, ME ağındaki içeriği harici bir envantere aktarır.

"Okuma" ve "Yazma" kavramları da ME ağı etrafında döner. Okuma, ME Ağının diğer envanterlerden okuması; yazma ise ME Ağının bir bilgisayar gibi diğerlerine yazması anlamına gelir. Aynı durum "Salt Okunur" ve "Salt Yazılır" için de geçerlidir. Örneğin bir ağdaki Depolama Veriyolu "Salt Okunur" olarak ayarlandığında ME Ağı yalnızca o Depolama Veriyolunun hedefini okuyabilir ve içine içerik koyamaz; "Salt Yazılır" ise tam tersidir.

# Veriyolları
AE2, ME ağı ile dış dünya arasındaki lojistiği yönetmek için [kablo](../items_blocks/cables.md) alt parçaları sağlar.

## İçe Aktarma Veriyolları ve Dışa Aktarma Veriyolları
<ItemLink id="appliedenergistics2:item.ItemMultiPart:240" showIcon="left" />, <ItemLink id="ae2fc:part_fluid_import" showIcon="left" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" showIcon="left" /> ve <ItemLink id="ae2fc:part_fluid_export" showIcon="left" />, AE deposu ile harici kaplar arasında eşyalar veya sıvılarla etkileşime girebilir.

Bunları bir kabın bitişiğindeki kabloya takmak, ME Ağı ile harici kap arasında eşya ve sıvı alışverişine olanak tanır.

<GameScene zoom="4" width="300" rotateX="-10" rotateY="0">
    <ImportStructure src="../assets/structures/io_system_import_export.snbt" />
</GameScene>

GTNH'de ME Veriyolları, aşağıdaki kurallar çerçevesinde GregTech Girdi/Çıktı Veriyolları ve Kapakları ile etkileşime girebilir:
* ME Eşya Veriyolları, bir GT Veriyolunun ön yüzüne takıldığında eşyalarla <Color id="Red">yalnızca</Color> etkileşime girebilir.
* ME Eşya Veriyolları, bir GT Sıvı Kapağının ön yüzüne takıldığında eşyalarla <Color id="Red">yalnızca</Color> etkileşime girebilir.
* ME Sıvı Veriyolları, bir GT Sıvı Kapağının herhangi bir yüzüne takıldığında sıvılarla etkileşime girebilir.

## Depolama Veriyolları
<ItemLink id="appliedenergistics2:item.ItemMultiPart:220" showIcon="left" /> ve <ItemLink id="ae2fc:part_fluid_storage_bus" showIcon="left" />, bağlı kaplardaki eşyaları veya sıvıları ME ağına okuyabilir ve AE depolaman için bir "harici sabit disk" gibi davranır.

<GameScene zoom="4" width="300" rotateX="-10" rotateY="0">
    <ImportStructure src="../assets/structures/io_system_storage_bus.snbt" />
</GameScene>

Depolama Veriyollarının kullanımı, harici depolamayı basitçe açığa çıkarmanın çok ötesine geçer. Özellikle GTNH'de otomasyonun çekirdek bir parçasıdır.

## Diğer Veriyollar
GTNH, Thaumcraft 4'ü desteklemek için AE2'ye Esans Veriyolları ekler. Esansı depolamak ve otomatikleştirmek için AE sistemini kullanabilirsin.
Ayrıntılar için <ItemLink id="thaumicenergistics:part.base" showIcon="left" />, <ItemLink id="thaumicenergistics:part.base:3" showIcon="left" /> ve <ItemLink id="thaumicenergistics:part.base:2" showIcon="left" /> sayfalarına bak.

# Depolama Önceliği
Tüm Depolama Veriyollarının önceliği, arayüzlerinin sağ üst köşesinden ayarlanabilir. Bir ME ağında öncelik bir tam sayıdır. Yüksek değerler lojistik sisteminin eşyaları veya sıvıları orada depolamayı tercih etmesini sağlarken, düşük değerler eşyaları veya sıvıları önce oradan almayı tercih etmesini sağlar.

Aşağıdaki örnek kavramı netleştirmeye yardımcı olabilir. Ağda her birine farklı öncelikte bir Depolama Veriyolu takılı iki sandık olduğunu ve her birinde birer <ItemLink id="minecraft:stone" showIcon="left" /> bulunduğunu varsayalım:
* ME Ağına bir Taş aktardığında AE onu önceliği daha yüksek olan sandıkta depolar.
* ME Ağından bir Taş aldığında AE onu önce önceliği daha düşük olan sandıktan çeker.
* Taşı malzeme olarak gerektiren bir istek için [otomatik üretim](./autocrafting.md) kullandığında AE, Taşı önce önceliği daha düşük olan sandıktan kullanır.

Depolama Veriyollarına ek olarak <ItemLink id="appliedenergistics2:tile.BlockDrive" showIcon="left" /> önceliği de ayarlanabilir.

# Yükseltme Kartları
Tüm ME Veriyolları, ek işlevsel ayarlar kazanmak için [yükseltme kartları](./upgrade_card.md) kabul edebilir. Faren bir veriyolunun arayüzünün sağ üst köşesindeki kart yuvalarının üzerine geldiğinde o veriyolunun hangi yükseltme kartlarını desteklediği gösterilir; farklı yükseltme kartlarının açıklamaları da hangi veriyolu türlerine uygulandıklarını listeler.