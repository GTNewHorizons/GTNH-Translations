---
navigation:
  parent: /items_blocks_index.md
  title: Kablolar
  icon: appliedenergistics2:item.ItemMultiPart:36
categories:
- network infrastructure
item_id: "appliedenergistics2:item.ItemMultiPart 0-16,20-36,40-56,60-76,520-536"
---

# Kablolar

<GameScene zoom="3" showBackground={false}>
  <ImportStructure src="../assets/structures/cables.snbt" />
  <IsometricCamera yaw="135" pitch="30" />
</GameScene>

Bitişik ME makineleri de bir ME ağı oluşturabilse de, kablolar bir ME ağını geniş alanlara yaymanın hâlâ birincil yoludur.

Farklı renkteki kablolar, bitişik kabloların birbirine bağlanmasını önleyerek [kanalların](../ae2_mechanics/channels.md) dağıtımını daha verimli hale getirebilir. Ayrıca kendilerine bağlı terminallerin rengini de etkilerler, bu yüzden terminaller her zaman mor görünmez. Fluix kablolar her renkteki kabloya bağlanabilir.

**Kanallar ile kablo renklerinin birbiriyle ilgisi olmadığını unutma.**

## Önemli Bir Not

**AE2'de yeniysen ve kanallara henüz alışkın değilsen, mümkün olan her yerde akıllı kabloları ve kalın kabloları kullan. Kanalların ağ üzerindeki yolunu göstererek kanalların nasıl davrandığını anlamayı kolaylaştırırlar.**

## Bir Not Daha

**Kanallar eşya/sıvı/enerji/diğer türdeki borular değildir. Kanalların dahili depolaması yoktur ve ME arayüzleri ile makineler kanallara eşya "girdi" olarak vermez. Kanalların tek yaptığı şey AE2 [cihazlarını](../ae2_mechanics/devices.md) bir ağa bağlamaktır.**

## Cam Kablo

<ItemImage id="appliedenergistics2:item.ItemMultiPart:16" scale="4" />

<ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> en basit kablodur; enerji ve 8 [kanala](../ae2_mechanics/channels.md) kadar iletebilir. Fluix'in varsayılan olduğu 17 renkte gelir ve 16 boyadan herhangi biriyle ilgili renge boyanabilir.

Boyalı bir kablo üretmek için üretim ızgarasında bir boyayı 8 kablo ile çevrele. Üretimde kullanılan kabloların renklerinin aynı olması gerekmez, ancak cam veya akıllı kablo gibi aynı kablo tipinde olmaları gerekir. Dünyadaki kablolar Forge uyumlu herhangi bir boya fırçasıyla da boyanabilir.

Boyalı herhangi bir kablo, boyası gidermek için çalışma masasına konabilir.

Kablolar, <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" /> oluşturmak için Fluix Kristalleri ile sarılabilir ve [kanalların](../ae2_mechanics/channels.md) davranışını daha iyi gözlemlemek için <ItemLink id="appliedenergistics2:item.ItemMultiPart:56" /> olarak da üretilebilir.

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:16" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:11" />

---

## Kaplı Kablo

<ItemImage id="appliedenergistics2:item.ItemMultiPart:36" scale="4" />

<ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> ile karşılaştırıldığında, kaplı kablolar ekstra bir oynanış işlevi sunmaz. Ancak görünümlerini tercih ediyorsan pratik bir dekorasyon olarak kullanılabilirler.

Kaplı kablolar <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> ile aynı şekilde boyanabilir. Dört <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:536" /> olarak üretilebilir.

<Recipe id="appliedenergistics2:item.ItemMultiPart:36" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:31" />

---

## Kalın Kablo

<ItemImage id="appliedenergistics2:item.ItemMultiPart:536" scale="4" />

Yüksek kapasiteli kablolar, normal kabloların 8 kanalı yerine 32 kanal iletebilir. Ancak kalın kablolar bus'ları desteklemez. Üzerlerine bus veya panel yerleştirmeden önce kalın bir kablodan <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> veya <ItemLink id="appliedenergistics2:item.ItemMultiPart:56" /> gibi daha küçük bir kabloya geçmen gerekir.

Kalın kablolar kanalların "en kısa yol" davranışını biraz değiştirir: kanallar önce bir kalın kabloya en kısa yoldan gider, ardından o kalın kablo üzerinden kontrolcüye en kısa yoldan ulaşır.

<Recipe id="appliedenergistics2:item.ItemMultiPart:536" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:531" />

---

## Akıllı Kablo

<Row>

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

</Row>

<ItemLink id="appliedenergistics2:item.ItemMultiPart:36" /> ile benzer görünseler de, akıllı kablolar kanal kullanımını gösterebilir ve teşhis işlevi sunar. Kanallar, kablonun siyah şeritleri üzerinde renkli çizgiler olarak gösterilir; bu da ağdaki kanal kullanımını anlamayı kolaylaştırır. Normal akıllı kablolarda ilk dört kanal kablo rengiyle uyumlu çizgiler olarak gösterilirken son dört kanal beyazdır. Kalın kablolarda ise her çizgi 4 kanalı temsil eder.

<ItemLink id="appliedenergistics2:tile.BlockController" /> bulunan bir ağda, kablo üzerindeki çizgiler kanalların gerçek yollarıyla tam olarak örtüşür.

Ad-hoc ağlardaki akıllı kablolar ise kablonun kendisinden geçen kanal sayısı yerine tüm ağ tarafından kullanılan toplam kanal sayısını gösterir.

Akıllı kablolar <ItemLink id="appliedenergistics2:item.ItemMultiPart:16" /> ile aynı şekilde boyanabilir.

<Recipe id="appliedenergistics2:item.ItemMultiPart:56" />

<Recipe id="appliedenergistics2:item.ItemMultiPart:76" />

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:71" />