---
item_ids:
  - gregtech:gt.blockmachines:15535
navigation:
  title: Evrensel Kimyasal Yakıt Motoru
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15535
categories:
    - Yapı Yenilemeleri
author: Skorched
date: 2026-05-27
---

# Evrensel Kimyasal Yakıt Motoru
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15535"/>
</GameScene>
<Color id="GREEN">Evrensel Kimyasal Yakıt Motoru (UCFE)</Color>, neredeyse her tür yanıcı sıvıdan güç üretmek için kullanılan IV kademe bir multibloktur. <Color id="GREEN">UCFE</Color>, Büyük Gaz Türbini <ItemImage id="gregtech:gt.blockmachines:15527"/>, Rocketdyne F-1A Motoru <ItemImage id="gregtech:gt.blockmachines:996"/> ve Büyük Yanma Motoru <ItemImage id="gregtech:gt.blockmachines:15533"/> tariflerini, EU/t değerinde üst sınır OLMAYAN çok verimli tek bir makinede etkili biçimde birleştirir. Tek istisna, hâlâ Büyük Yarı Sıvı Yakıcı <ItemImage id="gregtech:gt.blockmachines:31026"/> gerektiren yarı sıvılardır. Diğer tek girdi gereksinimi, yakıtın verimini %150'lik maksimuma kadar artıran yanma destekleyicisidir. Roket yakıtları, gaz/dizel yakıtlara göre önemli ölçüde daha az yanma destekleyicisi kullanır.

[GTNH Güç Planlayıcısı ](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Yalnızca yapının kendisi değişti; multibloğun temel işlevselliği öncekiyle aynı.

## Yapım
<Color id="GREEN">UCFE</Color>'nin kademeli bileşenleri yoktur. Dinamo Kapağı, yapının arkasındaki orta kasayla sınırlıdır. Kalan buslar/kapaklar, yapının herhangi bir yerindeki herhangi bir dengeli titanyum makine gövdesinin yerini alabilir. <Color id="BLUE">Çok Amperli ve Lazer Enerji Kapakları</Color> ciddi güç üretimi için desteklenir. Tercih edilirse yakıt ve yanma destekleyicisi aynı girdi kapağından sağlanabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15535"/><ItemImage id="gregtech:gt.blockmachines:15535"/>
- 100-115 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 72 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 39 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings4:13"/><ItemImage id="gregtech:gt.blockcasings4:13"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:14"/><ItemImage id="gregtech:gt.blockcasings2:14"/>
- 10 <ItemLink id="gregtech:gt.blockcasings4:3"/><ItemImage id="gregtech:gt.blockcasings4:3"/>
- 1 Dinamo Kapağı (arka ortadaki makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Girdi Kapağı (herhangi bir makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />

### Duvar Paylaşımı
<Color id="GREEN">UCFE</Color>'ler kasa, çerçeve kutusu ve bus/kapak tasarrufu için her bir yüzünü duvar paylaşımına açabilir. Konumuyla ilgili kısıtlama nedeniyle bu, girdi kapağını içermez. Maksimum kaynak tasarrufu için dikey olarak duvar paylaşımı yapılması önerilir; ancak bunun için kontrolcünün ters çevrilmesi gerekir.

## Kullanım
<Color id="GREEN">UCFE</Color> her saniye girdi kapağındaki/kapaklarındaki tüm yakıtı ve yanma destekleyicisini tüketir. Üretilen enerji bir sonraki saniye boyunca dinamo kapağına aktarılır. Dinamo kapağının tamponu dolarsa makine anında durur. Üretilen toplam EU/t, dinamo kapağının işleme kapasitesinden büyükse fazla güç yok edilir.

İpucu metninin söylediğinin aksine, <Color id="GREEN">UCFE</Color>'nin herhangi bir ısınma süresi yoktur ve üretebileceği maksimum gücü hemen verir. Bu, yakıt tasarrufu için bir Lapotronik Süperkapasitöre bağlı RS mandalı gerektirmediği anlamına gelir. Bunun yerine, güç %95'in altındayken <Color id="GREEN">UCFE</Color>'yi aktifleştirmek için bir enerji dedektörü kaplaması ve bir makine kontrolcü kaplaması kullan.

## Yakıt
<Color id="GREEN">UCFE</Color> gaz, dizel ve roket yakıtlarından güç üretir. En popüler seçenekler nitrobenzen, setan takviyeli dizel, yüksek oktanlı benzin, yoğun hidrazin yakıt karışımı ve yeşil roket yakıtıdır. Ağır yakıt, ham petrol ve Nefarious Oil gibi yarı sıvıların dahil OLMADIĞINI unutma; çünkü bunlar yalnızca Büyük Yarı Sıvı Yakıcı <ItemImage id="gregtech:gt.blockmachines:31026"/> içinde yakılabilir.

## Yanma Destekleyicisi
Yakıt dışında <Color id="GREEN">UCFE</Color>'ye giren tek diğer girdi, yanma tepkimeleri için gerekli koşulları sağlayan sıvı bir madde olan yanma destekleyicisidir. Yanma destekleyicisi ayrıca aşağıdaki denkleme göre yakıtın verimini artırır; burada $$C$$ yakılan yakıt tipiyle ilişkili bir sabit, $$R$$ ise yanma destekleyicisinin yakıta oranıdır. Maksimum verim %150'dir ve toplam EU/t üzerinde hiçbir yumuşak sınır veya üst sınır YOKTUR.

<Latex formula="EU/t = L/s \times EU/L \times 1.5e^{-C/R} \div 20">
  Burada:
  - $$C$$: Yakıt tipiyle ilişkili sabit
  - $$R$$: Yanma Destekleyicisinin yakıta oranı
</Latex>

Aşağıdaki grafik, $$C$$'nin iki farklı değeri için verim ile yanma destekleyicisinin yakıta oranı ($$R$$) arasındaki ilişkiyi gösterir. Roket yakıtlarının yaklaşık 0,5 oranında zirveye ulaştığına dikkat et; bu, yanma destekleyicisi girdi hızının yakıt girdi hızının %50'sini aşmaması gerektiği anlamına gelir. Ancak gaz/dizel yakıtları yaklaşık 2,0 oranında zirveye ulaşır; bu da yanma destekleyicisi girdi hızının yakıt girdi hızının %200'ünü aşmaması gerektiği anlamına gelir. Oran yalnızca L/s'ye dayandığından bu ilişki yakıtın enerji değerinden bağımsız olarak geçerlidir.

<FunctionGraph title="Efficiency of Fuels Based on Promoter Ratio" xRange="0..2" domain="0..2" xLabel="Combustion Promotor to Fuel Ratio ($$R$$)" yLabel="Efficiency (%)"> <Plot expr="1.5*e^((-0.04)/x)*100" color="#ff55ff" label="Gas/Diesel Fuels (C=0.04)"/>
<Plot expr="1.5*e^((-0.005)/x)*100" color="#ffff55" label="Rocket Fuels (C=0.005)"/>
</FunctionGraph>
