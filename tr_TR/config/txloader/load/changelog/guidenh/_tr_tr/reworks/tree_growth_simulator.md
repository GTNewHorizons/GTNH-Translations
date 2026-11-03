---
item_ids:
  - gregtech:gt.blockmachines:15541
navigation:
  title: Ağaç Büyütme Simülatörü
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15541
categories:
    - Yapı Revizyonları
author: Skorched
date: 2026-05-27
---

# Ağaç Büyütme Simülatörü

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15541"/>
</GameScene>
<Color id="GREEN">Yeşil Ağaç Büyütme Simülatörü (TGS)</Color>, ağaçları dijital olarak otomatik yetiştirmek ve hasat etmek için IV kademe bir Multobloktur. <Color id="GREEN">Yeşil TGS</Color>, EnderIO Farming Station <ItemImage id="EnderIO:blockFarmStation"/> veya Crop Manager <ItemImage id="gregtech:gt.blockmachines:28001"/> üzerine doğrudan bir yükseltmedir; çünkü çok daha hızlı ve verimlidir. Ayrıca ağaçlar, lag'i önlemek için dünyaya fiziksel olarak yerleştirilmez. <Color id="GREEN">Yeşil TGS</Color> yalnızca kontrolcüde bir fidan, ne hasat edileceğini belirtmek için giriş yolunda belirli bir GregTech aleti ve güç gerektirir. Testereler kütük, dal kesiciler fidan, makaslar yaprak ve bıçaklar meyve üretir. Bazı ağaçlar doğal olarak diğerlerinden daha fazla kaynak üretir. Tarif süresi 5 saniyeye sabittir, ancak daha fazla güç ve daha iyi aletler her iterasyondaki çıktı sayısını önemli ölçüde artırabilir. 
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> - Yeni Yapısal Avantajlar: Odun ve yapraklar otomatik yerleştirilir, yani zahmet etmene gerek yok; toprak çime dönüşür

## Yapım
<Color id="GREEN">Yeşil TGS</Color>'in kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına bir etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir kasayı değiştirebilir. Stoklama giriş yolları ve üretim giriş yolları desteklenmez. Çok amperli ve lazer enerji kapakları da desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı kullanılabilir. Meşe kütükleri ve yapraklar, yapı kurulduğunda ücretsiz olarak oluşturulur ve bu yüzden elle yerleştirilmeleri GEREKMEZ. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15541"/><ItemImage id="gregtech:gt.blockmachines:15541"/>
- 60 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 57 Kademeli Cam (herhangi) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 45-55 <ItemLink id="miscutils:gtplusplus.blockcasings.2:15"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:15"/>
- 25 Toprak <ItemImage id="minecraft:dirt"/> / Çim <ItemImage id="minecraft:grass"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Yeşil TGS</Color>'ler kasa, çerçeve kutusu, cam ve yol/kapak tasarrufu için her bir kenarında duvar paylaşımı yapabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Yeşil TGS</Color>, ağaç yetiştirme ve hasat etmede belirgin şekilde daha hızlı ve verimli olduğu için EnderIO Farming Station veya Crop Manager üzerine doğrudan bir yükseltmedir. Tarif süresi 5 saniyeye sabittir, ancak üretimi ölçeklemek için enerji kapağının kademesine bağlı bir çıktı çarpanı vardır. Temel çıktılar yetiştirilen ağacın tipine göre değişir, ancak genellikle 5 kütük, 5 fidan, 2 yaprak ve 2 meyvedir.

### Çarpan:
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 5 | 9 | 17 | 29 | 45 | 65 | 89 | 117 | 149 | 185 | 225 | 269 | 317 | 369 | 425 |


Giriş yolundaki alet, <Color id="GREEN">Yeşil TGS</Color>'in ürettiği belirli çıktıyı belirler. Aynı giriş yolunda birden fazla alet ve hatta farklı tipler bulunarak aynı anda birden fazla çıktı toplanabilir. Bazı aletler diğerlerinden daha iyidir ve çıktıya ikinci bir çarpan uygular. Desteklenen aletlerin listesi ve çarpanları aşağıda verilmiştir. Enerjisi biten elektrikli aletler, toplanmak üzere çıkış yoluna aktarılır.

- Kütükler - Testere (x1), Daire Testere (x2), Zincirli Testere (x4)
- Fidanlar - Dal Kesici (x1), Aşı Bıçağı (x4)
- Yapraklar - Makas (x1), Tel Keskisi (x2), Otomatik Makas (x4)
- Meyve - Bıçak (x1)

## Otomasyon
<Color id="GREEN">Yeşil TGS</Color>'i verimli kullanmanın zorluğu, elektrikli aletleri diğer ürünlerden ayırmak, yeniden şarj etmek ve makineye geri koymaktır. GregTech'in alet şarj etme yöntemleri (pil tamponları, turbo şarj cihazları vb.) içeriklerini çekilmeye uygun hale getirmez ve bu yüzden otomasyon için kullanılamaz.

Alternatif olarak, çok yüksek dayanıklılığa sahip birden fazla elektriksiz alet kullan. Daha az kaynak üretebilirler ama neredeyse hiç değiştirilmeleri gerekmez. Oriharukon, orikalkum ve Drakonyum iyi seçeneklerdir. Birden fazla elektrikli alet bile çok sık şarj edilmek zorunda değildir. 

Otomasyon yöntemleri burada kolayca gösterilemeyecek kadar biraz karmaşıktır, bu yüzden daha fazla bilgi için [Viki](https://wiki.gtnewhorizons.com/wiki/Tree_Growth_Simulator) sayfasına göz atmaktan çekinme