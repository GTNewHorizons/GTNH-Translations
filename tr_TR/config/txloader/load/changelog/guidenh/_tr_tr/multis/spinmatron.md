---
item_ids:
  - gregtech:gt.blockmachines:1033
navigation:
  title: Spinmatron-2737
  parent: multis.md
  icon: gregtech:gt.blockmachines:1033
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-25
---

# Spinmatron-2737
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1033" />
</GameScene>
<Color id="GREEN">Spinmatron-2737</Color>, tozları, sıvıları ve diğer eşyaları alt bileşenlerine veya yapı taşlarına ayırmak için seri santrifüjleme yapan ZPM kademesi bir multobloktur. Standart modda <Color id="GREEN">Spinmatron</Color>, Endüstriyel Santrifüj <ItemImage id="gregtech:gt.blockmachines:15512"/> makinesinin doğrudan yükseltmesidir; çünkü <Color id="RED">%300</Color> hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%70</Color>'ini kullanır ve türbin kademesi toplamı başına <Color id="GREEN">4</Color> paralel sunar. Devasa olmayan türbinler daha az paralel katkısı sağlar ve kaçınılmalıdır. Ayrıca sınırsız kademe atlaması vardır; bu da gerilimden bağımsız olarak her tarifi çalıştırabileceği anlamına gelir. <Color id="GREEN">Spinmatron</Color>'un çalışması için $$\text{Recipe Tier} \times 10 L/s$$ gazyağı VEYA paralel sayısını 1,25 ile daha da çarpmak için aynı miktarda biyokatalizli itki sıvısı gerekir.

<Color id="GREEN">Spinmatron</Color>'un ayrıca performansını ve yeteneklerini etkileyen üç modu vardır (Hafif, Standart veya Ağır). Hafif mod +%100 hız bonusu verir, ancak azami tarif kademesi $$\text{Voltage Tier} - 3$$ ile sınırlıdır. Standart Mod yukarıda açıklanmıştır. Ağır Mod paralel sayısını 32'ye böler, T3 yapı gerektirir ve biyokatalizli itki sıvısı gerektirir. Ağır mod yalnızca özellikle gerektiren durumlarda kullanılmalıdır. 
<br clear="all"/>

## İnşaat:
<Color id="GREEN">Spinmatron</Color>'un çerçeve kutularının ve merkezi rotor bloklarının materyaliyle ilişkili dört yapı kademesi vardır. Her yapı kademesi, azami paralel sayısını artırmak için kontrolcünün içinde 2 ek türbin yuvası verir. Veriyolları/kapaklar yapının herhangi bir yerindeki titreşime dayanıklı bir kasanın<ItemImage id="gregtech:gt.blockcasings12:9"/> yerini alabilir. Cam her kademede olabilir ve makinenin çalışmasına etkisi yoktur. <Color id="GREEN">Çok amperli ve Lazer Enerji Kapakları</Color> desteklenir, ancak overclock'lar kapak kademesi + 1 ile sınırlıdır. Animasyonları devre dışı bırakmak için kontrolcüye tornavida uygula. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan; camın kademesini belirtmek için "glass" alt kanalını, genel yapı kademesini belirlemek içinse tek bir yığında tutulan projektör sayısını kullan.

Türbinlerin kendisi rotor düzeneklerine GİRMEZ. Bunun yerine onları kontrolcüde bölme kontrolcü ayarları altına yerleştir. Gerçekte oraya konmadan da rotor düzeneklerinde görsel olarak görünürler. Statik ve animasyonlu türbin dokuları arasında geçiş yapmak için kontrolcüye tornavidayla sağ tıkla. Bölme kontrolcü ayarlarında T2 biyokatalizli itki sıvısını etkinleştirme seçeneği de vardır; <Color id="GREEN">Spinmatron</Color> makinenin içinde gazyağı yerine onun bulunduğunu otomatik olarak algılamaz. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:1033"/><ItemImage id="gregtech:gt.blockmachines:1033"/>
- 550-711 <ItemLink id="gregtech:gt.blockcasings12:9"/><ItemImage id="gregtech:gt.blockcasings12:9"/>
- 264 <ItemLink id="GoodGenerator:supercriticalFluidTurbineCasing"/><ItemImage id="GoodGenerator:supercriticalFluidTurbineCasing"/>
- 160 <ItemLink id="gregtech:gt.blockcasings9"/><ItemImage id="gregtech:gt.blockcasings9"/>
- 144 <ItemLink id="gregtech:gt.blockglass1:6"/><ItemImage id="gregtech:gt.blockglass1:6"/>
- 81 Kademeli Cam (herhangi) <ItemImage id="bartworks:BW_GlasBlocks"/>
- 56 Merkezi Rotor Bloğu (multiblok kademesine göre kademeli) <ItemImage id="gregtech:gt.blockmetal4:13"/>
- 54 <ItemLink id="miscutils:gtplusplus.blockcasings.5:2"/><ItemImage id="miscutils:gtplusplus.blockcasings.5:2"/>
- 24 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 9 Çerçeve Kutusu (multiblok kademesine göre kademeli) <ItemImage id="miscutils:blockFrameGtPikyonium64B"/>
- 8 <ItemLink id="gregtech:gt.blockmachines:30010"/> <ItemImage id="gregtech:gt.blockmachines:30010"/>
- 1+ Enerji Kapağı (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 Bakım Kapağı (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ Giriş Yolu (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ Çıkış Yolu (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ Çıkış Kapağı (herhangi bir titreşime dayanıklı kasa) <ItemImage id="gregtech:gt.blockmachines:60"/>
### Duvar Paylaşımı:
<Color id="GREEN">Spinmatron</Color>'lar kasa, rotor düzeneği ve veriyolu/kapak tasarrufu için her kenarını duvar paylaşımına açabilir. Ancak bu, kontrolcünün içinde saklandıkları için türbinlerin kendisini kapsamaz. 

## Kullanım:
Standart modda <Color id="GREEN">Spinmatron</Color>, %300 hızda çalıştığı, normalde gereken EU/t'nin yalnızca %70'ini kullandığı ve türbin kademesi toplamı başına 4 paralel sunduğu için Endüstriyel Santrifüj'ün doğrudan yükseltmesidir. Devasa türbinler en etkilisidir çünkü büyük/normal/küçük türbinler kademe değerlerinin toplama yalnızca %75/%50/%25'ini katkı olarak verir. Örneğin iki devasa adamantiyum türbinli (Kademe 10) bir Spinmatron toplamda 4 x (10+10) = 80 paralele sahiptir.

Spinmatron'un aşağıda listelenen üç çalışma modu vardır. Modları kontrolcünün arayüzündeki "display machine information" altından değiştir. Hafif mod petekler ve saf olmayan tozlar gibi düşük kademe tarifler için mükemmeldir. Standart mod $$\text{Voltage Tier} - 3$$ kısıtının üzerindeki daha yüksek kademe tarifler için idealdir. Ağır mod ise yalnızca özellikle gerektiren durumlarda kullanılmalıdır.

- Hafif Mod - +%100 hız bonusu verir, ancak azami tarif kademesi $$\text{Voltage Tier} - 3$$ ile sınırlıdır.
- Standart Mod - Orijinal açıklamada değişiklik yok.
- Ağır Mod - Paralelleri 32'ye böler, en az T3 yapı gerektirir ve gazyağı yerine biyokatalizli itki sıvısı gerektirir.