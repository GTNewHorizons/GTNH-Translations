---
item_ids:
  - gregtech:gt.blockmachines:28055
navigation:
  title: Endüstriyel Çiftlik
  parent: crops.md
  icon: gregtech:gt.blockmachines:28055
categories:
    - Ekinler
    - Yeni Multibloklar
author: Skorched
date: 2026-05-24
---

# Endüstriyel Çiftlik
Oyunun belirli bir noktasında, onları gerçekten sınırlarına kadar zorlamaya çalışıyorsan, ufak eski ekin yöneticilerin zorlanmaya başlar. CropsNH kendi çözümüyle gelir: <Color id="GREEN">Endüstriyel Çiftlik</Color>

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:28055" />
</GameScene>
<Color id="GREEN">Endüstriyel Çiftlik</Color>, ekinlerin büyük ölçekli yetiştirilmesi ve hasadı için MV kademe bir multibloktur. <Color id="GREEN">Endüstriyel Çiftlik</Color> aynı anda yalnızca tek bir ekin tipi yetiştirebilir, ancak kapasite tohum yataklarının kademesi ve makinenin uzunluğuyla önemli ölçüde artar. <Color id="GREEN">Endüstriyel Çiftlik</Color>, makinenin içindeki ekinlerin büyümesini, sanki dünyaya fiziksel olarak yerleştirilmişler gibi simüle eder. Tek girdiler su, güç ve gübreleme birimi mevcutsa gübredir. Çıktılar, ekinin ortalama istatistiklerine, çevresel bonuslara ve yükseltme birimi bonuslarına göre ölçeklenir. Aralarından seçim yapabileceğin 5 farklı yükseltme birimi ve makinenin uzunluğuna bağlı olarak 1-12 yükseltme yuvası vardır, ancak bunlar tohum yataklarının kademesiyle tam olarak eşleşmelidir. 
<br clear="all"/>
## İnşaat:
<Color id="GREEN">Endüstriyel Çiftlik</Color>'in uzunluğu, tohum yataklarının kademesine bağlı olarak 3-14 blok arasında değişir. Yükseltme birimleri yapının üst katmanındaki herhangi bir odun çerçeveyle sınırlıdır ve tohum yataklarının kademesiyle tam olarak eşleşmelidir. Yollar/kapaklar, yapının her iki ucunun merkezindeki tuğlalı tarım kasalarıyla sınırlıdır. Cam, enerji kapağının maksimum kademesini belirler. Lazer enerji kapakları desteklenmez, ancak hız aşırtmalı büyüme hızlandırma birimi mevcutsa birden fazla çok amperli enerji kapağı olabilir. Aksi takdirde, gerektiği kadar birden fazla normal enerji kapağı olabilir. Yapıyı, sırasıyla makinenin kademesini ve camın kademesini belirten "if_tier" ve "glass" alt kanallarıyla görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> kullan. "if_upgrade" alt kanalı 1 olarak ayarlanmadıkça yükseltme birimleri otomatik olarak yerleştirilmez.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:28055" /> <ItemImage id="gregtech:gt.blockmachines:28055" />
- 26-48 <ItemLink id="cropsnh:cropsnh.casings1" /> <ItemImage id="cropsnh:cropsnh.casings1" />
- 4-48 Kademeli Cam <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 3-36 Tohum Yatağı (Kademeli) <ItemImage id="cropsnh:cropsnh.seedBed:2" />
- 1-12 <ItemLink id="gregtech:gt.blockframes:809" /> <ItemImage id="gregtech:gt.blockframes:809" />
- 0-12 Yükseltme Birimi (herhangi bir odun çerçeve) <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" />
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı:
<Color id="GREEN">Endüstriyel Çiftlik</Color>, kasalar, cam ve yol/kapaklardan tasarruf etmek için her bir yanında duvar paylaşımı yapabilir. Üst katmanı, doğrudan üstünde ve baş aşağı duran başka bir çiftlikle üst üste bindirmek en etkilidir ve tam bir yükseltme birimi setini paylaştığı için şiddetle önerilir. 

## Kullanım:
> [!WARNING]
> Bu bölüm matematik açısından oldukça ağırdır, ancak doğrudan hesaplama yapmana gerek yoksa her şeyin nasıl ölçüldüğüne dair genel bir fikir edinmek için metni kullanabilirsin

<Color id="GREEN">Endüstriyel Çiftlik</Color>, kademe veya uzunluktan bağımsız olarak sabit 5 saniyelik bir döngüyle çalışır. Her döngünün başında <Color id="GREEN">Endüstriyel Çiftlik</Color>, girdi kapağından su ve gübreleme birimi mevcutsa giriş yolundan gübre tüketir. Tüketilen miktar, aşağıdaki denklemlerde görüldüğü gibi makinenin toplam tohum kapasitesine bağlıdır. Makinenin içinde gerçekte kaç tohum bulunduğu önemli değildir. 
<Latex formula="\text{Water/Cycle (L) = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil" />
<Latex formula="\text{Fertilizer/Cycle (L)} = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil "/>

<Color id="GREEN">Endüstriyel Çiftlik</Color>, içindeki ekinlerin büyümesini simüle eder ve ortalama sonucu ölçekler. Fiziksel dünyadaki ekinlerle aynı denklemlerin tümünü kullanır; ancak nem bonusu ve gökyüzü bonusu otomatik olarak maksimuma çıkarılır. Doğrudan gökyüzü erişimi gerektirmez ve hava durumunu önemsemez. Ekinin besin değerini bulmak için önce tüm çeşitli çevresel bonusları topla. 
<Latex scale="0.8" formula="\text{Humidity Bonus} = \text{Max} \Bigg( 0,\text{ Min} \Bigg( 1,\frac{\text{Biome Humidity\%} - 0.5}{0.3 }\Bigg)\Bigg) \times 14"/>

<Latex scale="0.8" formula="\text{Biome Bonus} = \text{Min}(2\text{, Biome Preferences Met}) \times 14"/>
<Latex scale="0.8" formula="\text{Nutrients} = 17.9 + \text{Fertilization Bonus} + \text{Max}(\text{Humidity Bonus, Biome Bonus})" />

> [!NOTE]
> <Color id="GREEN">Gübreleme Bonusu </Color> gübrelenmemişse 1, gübrelenmişse 1.5'tir

Ardından, ekinlerin genel büyüme yüzdesini büyüme hızından ve büyüme çarpanından hesapla. Bunlar, aşağıdaki denklemlerde görüldüğü gibi öncelikle besin değerine ve ekinin ortalama istatistiklerine bağlıdır. Gübreleme biriminin, yukarıdaki gübreleme bonusuna ek olarak büyüme çarpanını %50 artırdığını unutma. Ekinler teorik olarak 5 saniyeden kısa sürede daha fazla büyüyebilse bile döngü başına maksimum büyüme %100'dür. 
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients} \geq \text{Crop Tier} \times 2) = \frac{(6 + \text{Crop Growth}) \times (100 + \text{Nutrients} - 10 \times \text{Crop Tier})}{100}" />
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients}< \text{Crop Tier} \times 2) = \text{Max}\Biggl(0,\frac{(6 + \text{Crop Growth}) \times (100 + 4 \times (\text{Nutrients} - 10 \times \text{Crop Tier}))}{100}\Biggr)" />
<Latex scale="0.65" formula="\text{Growth Mult} = (1 + \text{Growth Acceleration Units}) \times {\text{Fertilization Bonus}} \times 2^{\text{OC}}" />

> [!NOTE]
> Buradaki $$\text{OC}$$, hız aşırtma sayısını ifade eder

<Latex scale="0.65" formula="\text{Growth\%} = \text{Min} \Bigg( 1, \frac{1}{\lceil \text{Crop Growth Points} \div (\text{Growth Speed} \times \text{Growth Mult} \times (100 \div 256)) \rceil} \Bigg)" />

Son olarak, genel çıktıyı toplamsal bonus ve çarpım bonusu üzerinden hesapla. Bunlar öncelikle ekinin ortalama istatistiklerine bağlıdır ve gübreleme birimi tarafından bir kez daha artırılır. Tohum yatağı bonusu ile gelişmiş hasat birimi bonusları da burada uygulanır.

<Latex scale="0.60" formula="\text{Additive Bonus} = 0.01 \times (\text{Crop Gain} + 1)" />
<Latex scale="0.60" formula="\text{Mult Bonus} = (\text{Crop Drop Rate})^{\text{Crop Tier}} \times 1.03^{\text{Crop Gain}} \times (1 + \text{Seed Bed Bonus} + 0.5_{\text{fertilizer}}) \times (1 + 0.2 \times \text{Harvesting Units})"/>
<Latex scale="0.60" formula="\text{Output} = (\text{Output Stack Size} + \text{Additive Bonus})\times \text{Output Base Chance} \times \text{Mult Bonus} \times \text{Growth}\%" />

## Yükseltme Birimleri:
<Color id="GREEN">Endüstriyel Çiftlik</Color>, ekinlerin büyüme hızını ve makinenin genel performansını iyileştirmek için çeşitli yükseltme birimleriyle donatılabilir. Aralarından seçim yapabileceğin 5 farklı yükseltme birimi vardır ve bunlar yapının üst katmanındaki odun çerçevelerle sınırlı olduğundan makinenin uzunluğuna bağlı olarak 1-12 yükseltme yuvası bulunur. Yükseltme birimlerinin kademesi, tohum yataklarının kademesiyle tam olarak eşleşmelidir. 
- <ItemImage id="cropsnh:cropsnh.advancedHarvestingUnit:2" /> __Gelişmiş Hasat Birimi (MV+)__: Bu birim, birim başına damla miktarlarını +%20 ve güç tüketimini +%50 artırır. Daha yüksek kademe birimler tamamen aynı faydaları sunar. Yapı başına en fazla 2 gelişmiş hasat birimi olabilir
- <ItemImage id="cropsnh:cropsnh.fertilizerUnit:2" /> __Gübreleme Birimi (MV+)__: Bu birim, çıktı üretimini artırmak için <Color id="GREEN">Endüstriyel Çiftlik</Color>'in her döngünün başında her zaman <Color id="GREEN">Zenginleştirilmiş Gübre</Color> tüketmesini gerektirir. Ayrıca eşya gübresinin makinede kullanılmasını engeller. Bu, büyüme hızını x1.5, damla sayısını +%50 ve güç tüketimini +%50 artırır, ancak gübre tükenirse işlemeyi durdurur. Daha yüksek kademe birimler tamamen aynı faydaları sunar ancak döngü başına daha fazla zenginleştirilmiş gübre gerektirir. Yapı başına yalnızca 1 gübreleme birimi olabilir
- <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" /> __Çevresel İyileştirme Birimi (MV+)__: Bu birim, kontrolcünün arayüzünde bir çevresel modül yuvası açar ve birim başına güç tüketimini +%50 artırır. Çevresel modüller, ekinlere ideal büyüme koşulları sağlamak için makinenin içindeki simüle edilmiş sıcaklığı ve/veya biyomu değiştirir. Daha yüksek kademe birimler tamamen aynı faydaları sunar. Yapı başına en fazla 2 çevresel iyileştirme birimi olabilir
- <ItemImage id="cropsnh:cropsnh.growthAccelerationUnit:2" /> __Büyüme Hızlandırma Birimi (MV+)__: Bu birim, ekinlerin büyüme hızını +%100 ve birim başına güç tüketimini +%125 artırır. Bu birim hız aşırtmalı büyüme hızlandırma birimiyle uyumsuzdur ve daha yüksek kademe birimler tamamen aynı faydaları sunar. Yapı başına büyüme hızlandırma birimi sayısında sınır yoktur
- <ItemImage id="cropsnh:cropsnh.overclockedGrowthAccelerationUnit:7" /> __Hız Aşırtmalı Büyüme Hızlandırma Birimi (ZPM+)__: Bu birim, <Color id="RED">Çok Amperli Enerji Kapakları</Color> kullanma yeteneğini açar ve <Color id="GREEN">Endüstriyel Çiftlik</Color>'in diğer multibloklar gibi yeterli güçle hız aşırtılmasına olanak tanır. Temel gerilim, tohum yataklarının kademesine bağlıdır. Her hız aşırtma, temel döngü süresini etkilemeden çıktı üretimini, su tüketimini ve gübre tüketimini ikiye katlar. Bu birim büyüme hızlandırma birimiyle uyumsuzdur ve daha yüksek kademe birimler tamamen aynı faydaları sunar. Yapı başına yalnızca 1 hız aşırtmalı büyüme hızlandırma birimi olabilir