---
item_ids:
  - Railcraft:machine.alpha:12
quest_ids:
  - AAAAAAAAAAAAAAAAAAAMHw==
navigation:
  title: Gelişmiş Kok Fırını
  parent: ./multiblocks_index.md
  icon: Railcraft:machine.alpha:12
  position: -2001
---

# Gelişmiş Kok Fırını

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="Railcraft:machine.alpha:12" />
</GameScene>

<ItemImage id="Railcraft:machine.alpha:12" /> Gelişmiş Kok Fırını (ACO), kütükleri Odun Kömürüne dönüştürmek için kullanılan MV kademe bir Multibloktur. 

ACO, Basit [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md) için doğrudan bir yükseltmesidir çünkü 90 kat daha hızlıdır, ancak ürettiği Odun Kömürü gibi yanabilir bir Yakıt gerektirir ve Kreozot yağı üretmez. Bu nedenle ACO'nun azami Çıktısı saniyede 1 Odun Kömürüdür, ancak net Çıktısı 16 saniyede 15 Odun Kömürüdür. 

ACO Güç tüketmez ve başlangıçta [<ItemLink id="gregtech:gt.blockmachines:15546" showIcon="left" />](./pyrolyse_oven.md)'ndan daha hızlıdır, ancak daha iyi Isıtma Bobinleri ve Enerji kapakları açıldıkça bu durum hızla değişir. 

ACO'nun yerini EV'de [<ItemLink id="gregtech:gt.blockmachines:15543" showIcon="left" />](./industrial_coke_oven.md) alır.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | MV |
| Yapı Boyutu (GxUxY) | 3x3x4 |
| Güç | Yok |
| Hız Aşırtma | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | 80 gibbl/s Kirlilik üretir |

## Üretim ve İnşa

### Üretim

<RecipesFor id="dreamcraft:AdvancedCokeOvenBrick" handlerId="gt.recipe.blastfurnace" />

<RecipesFor id="Railcraft:machine.alpha:12" />

### Yapı

ACO tek bir Blok tipinden oluşur ve bir Kontrolcü ya da herhangi bir bus/hatch içermez. <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> yapıyı görselleştirmez/inşa etmez, ancak inşa edilmesi çok kolaydır.

ACO hiçbir şekilde döndürülemez.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="Railcraft:machine.alpha:12" showIcon="left" /> | 34, içi boş 1x1x2 merkezli 3x3x4 |

### Duvar Paylaşımı

Bir Railcraft Multibloku olarak **ACO yapısının hiçbir parçasında <Color id="red">duvar paylaşımı yapamaz</Color>** ve oluşması için diğer ACO'lardan en az bir Blok uzakta olmalıdır.

## Kullanım

<GameScene wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/aco_loop.snbt" />
</GameScene>

ACO kütüklerden saniyede bir Odun Kömürü üretir. Bu, Basit [<ItemLink id="gregtech:gt.blockmachines:236" showIcon="left" />](./coke_oven.md)'ndan 90 kat daha hızlıdır, ancak ürettiği Odun Kömürü gibi yanabilir bir Yakıt gerektirir ve Kreozot yağı üretmez. Odun Kömürünün yanma süresi 1600 tick'tir ve bu da ACO'yu 16 saniye besler, böylece toplam Çıktının yalnızca 1/16'sı kadar net kayıp olur. ACO ayrıca Kömürü kömür kokuna, şeker kömürünü şeker kokuna ve kaktüs kömürünü kaktüs kokuna dönüştürebilir (her biri 1 saniye).

Girdiler yapının herhangi bir tarafındaki herhangi bir Bloğa yerleştirilebilir ve Çıktılar yapının herhangi bir tarafındaki herhangi bir Bloktan çekilebilir. ACO bitişik envanterlerden otomatik olarak çekmez, ancak otomatik olarak iter. 

Yandaki sahne, EnderIO kanalları kullanılarak yapılmış kendini besleyen bir döngü örneğini gösterir.

### Odun Kömürü Hızı Karşılaştırması

[<ItemLink id="gregtech:gt.blockmachines:15546" showIcon="left" />](./pyrolyse_oven.md), oyunun başlarında kütükleri Odun Kömürüne dönüştürmek için başka bir seçenektir; hız aşırtılabilir, Azot ile güçlendirilebilir ve Isıtma Bobinlerinin kademesiyle ölçeklenir. 

Oyuncunun ACO ile Piroliz Fırını arasında karar vermesine yardımcı olmak için aşağıdaki tablo, çeşitli Tarifler, Isıtma Bobinleri ve hız aşırtmalar için ortalama saniyede Odun Kömürünü karşılaştırır. Yeşil vurgulanan hücreler Piroliz Fırınının ACO'dan daha hızlı olduğu, kırmızı vurgulanan hücreler ise Piroliz Fırınının daha yavaş olduğu anlamına gelir. ACO'nun hiç EU tüketmediğini, ancak aynı zamanda hiçbir Sıvı yan ürün üretmediğini unutma; bu da mevcut durumuna bağlı olarak belirleyici bir faktör olabilir.

| Hız Aşırtmalar | Piroliz Fırını(Normal) ||| Piroliz Fırını(Azot ile) ||| ACO |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ^^ | Bakır-Nikel | Kantal | Nikrom | Bakır-Nikel | Kantal | Nikrom | ^^ |
| 0(MV) | <Color id="red">0.313/s</Color> | <Color id="red">0.625/s</Color> | <Color id="green">0.939/s</Color> | <Color id="red">0.625/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">1.887/s</Color> | 0.938/s |
| 1(HV) | <Color id="red">0.625/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">1.887/s</Color> | <Color id="green">1.250/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">3.774/s</Color> | ^^ |
| 2(EV) | <Color id="green">1.250/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">3.774/s</Color> | <Color id="green">2.500/s</Color> | <Color id="green">5.000/s</Color> | <Color id="green">7.692/s</Color> | ^^ |

## Kaynaklar

- [GTNH Wiki: Gelişmiş Kok Fırını](https://wiki.gtnewhorizons.com/wiki/Advanced_Coke_Oven)