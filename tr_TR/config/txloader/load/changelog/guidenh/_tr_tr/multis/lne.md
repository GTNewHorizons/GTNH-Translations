---
item_ids:
  - gregtech:gt.blockmachines:31088
navigation:
  title: Büyük Nötralizasyon Motoru
  parent: multis.md
  icon: gregtech:gt.blockmachines:31088
categories:
    - Yeni Multibloklar
author: Skorched
date: 2026-05-25
---

# Büyük Nötralizasyon Motoru
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31088" />
</GameScene>
<Color id="GREEN">Büyük Nötralizasyon Motoru (LNE)</Color>, daha yüksek gerilim kademesi gereksinimleri için EV kademe bir multiblok asit jeneratörüdür. <Color id="GREEN">LNE</Color>, tek blok asit jeneratörlerinden doğrudan bir yükseltmedir çünkü <Color id="BLUE">%500</Color> verimliliğe kadar sunar, 1A'dan fazla güç çıktısı verebilir ve yapılandırılabilir yakıt tüketim oranlarına sahiptir. <Color color="#55ffff">Bazlar</Color>, makinenin verimliliğini artırmak için kullanılabilir. Güç, arkadaki bir dinamo kapağı aracılığıyla alınır ve <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir. <Color id="GREEN">LNE</Color>'nin <Color id="RED">Zehirli Kalıntı</Color> adında kendi tehlike sistemi vardır. Bu, kontrolcünün kapasitesini aşarsa multiblok <Color id="RED">patlar!</Color>. <Color id="GREEN">LNE</Color>'yi, bir <ItemLink id="gregtech:gt.blockmachines:13106"/> <ItemImage id="gregtech:gt.blockmachines:13106"/> öğesine bağlı bir RS mandalıyla otomatik olarak açıp kapatarak yakıttan tasarruf et.
<br clear="all"/>

## Yapım:
<Color id="GREEN">LNE</Color>'nin kademeli bir bileşeni vardır. Kullanılan "ana kasa" makinenin kademesini belirler; bu da makinenin baz bozunumunu ve kapasitesini belirler. Girdi kapakları, giriş yolları, dinamo ve zehirli kalıntı sensör kapağı (açıklanacaktır) "ana" kasalardan herhangi birinin yerini alabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/> <ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.
| Kademe | Kasa |
| -------------- | --------------- |
| 1 | Güçlendirilmiş Cansız Makine Gövdesi <ItemImage id="gregtech:gt.blockcasings12:5"/> |
| 2 | Hassas Sabit Makine Gövdesi <ItemImage id="gregtech:gt.blockcasings12:6"/> |
| 3 | Nihai Statik Makine Gövdesi <ItemImage id="gregtech:gt.blockcasings12:7"/> |

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:31088"/> <ItemImage id="gregtech:gt.blockmachines:31088"/>
- 34 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 30-46 Kademeli "Ana" Kasalar <ItemImage id="gregtech:gt.blockcasings12:5"/>
- 15 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 1+ Dinamo Kapağı (herhangi bir kademeli kasa) <ItemImage id="gregtech:gt.blockmachines:15230"/>
- 1+ Girdi Kapağı (herhangi bir kademeli kasa) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:3019"/> (herhangi bir kademeli kasa)<ItemImage id="gregtech:gt.blockmachines:3019"/>
- 0+ Giriş Yolu (herhangi bir kademeli kasa) <ItemImage id="gregtech:gt.blockmachines:70"/>

### Duvar Paylaşımı:
<Color id="GREEN">LNE</Color>'ler, kasalar, çerçeve kutuları ve yollar/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşabilir.

## Kullanım:
<Color id="GREEN">LNE</Color> asitlerden güç üretir. Çok çeşitli asitler mevcuttur ve mevcut asitlerin birçoğunun EU değerleri değiştirilmiştir, bu yüzden eski favorilerinden bazılarını çift kontrolden geçirmeye değer. Bununla birlikte, tamamen yeni <ItemLink id="gregtech:gt.metaitem.01:2177"/> <ItemImage id="gregtech:gt.metaitem.01:2177"/> dahil olmak üzere bazı yeni asit hatları eklenmiştir.

### Baz Güçlendirme
<Color id="GREEN">LNE</Color>, aşağıdaki tabloya göre asit yakıtlarının verimliliğini artırmak için giriş yolunda bir baz alabilir. Bu bazlar, giriş yolundaki giriş sırasına göre tek tek tüketilir.
| Baz | Verimlilik | Kullanım Oranı |
| --------------- | --------------- | --------------- |
| Sodyum Hidroksit | %150 | 60 / dakika |
| Potasyum Hidroksit | %190 | 24 / dakika |
| Sezyum Hidroksit | %250 | 6 / dakika |
| Fransiyum Hidroksit | %500 | 5 / dakika |

### Bozunum Güçlendirme
<Color id="GREEN">LNE</Color>, bozunum güçlendirmesini artırmak için giriş yolunda <Color id="RED">Robot Kolları</Color> kabul edebilir. Bozunum güçlendirmesi, <Color id="GREEN">IV</Color> veya altındaysa $$1.2^{\text{Arm Tier}}$$, <Color color="#ff55ff">LuV</Color> veya üzerindeyse $$1.4^{\text{Arm Tier}}$$ olarak hesaplanır. Bu bozunum güçlendirmesini $$\sqrt{\text{Arm Count}}$$ ile çarpmak için en fazla 16 adete kadar birden çok robot kolu yerleştir. Her dakika, <Color id="GREEN">LNE</Color>'nin bir robot kolunu yok etme şansı vardır; şu şekilde hesaplanır:
<Latex formula="\text{Void Chance} = \frac{\text{Arm Count}}{45 \times (1+\text{Arm Tier})}"/>

### Zehirli Kalıntı
<Color id="GREEN">LNE</Color>, asitlerin yakılmasından <Color id="RED">Zehirli Kalıntı</Color> üretir. Kalıntı miktarı makinenin kapasitesini aşarsa makine patlar. Her tikte zehirli kalıntı aşağıdaki denklemlerle artar __ve__ azalır:
<Latex formula="\text{+Residue}=\text{Residue Rate} \times \text{Fuel Consumption(L)} \times \text{Random}(0.5:15)">
  - <Latex formula="\text{Residue Rate} = 0.05 \times \text{Base Fuel Value (EU/L)}^{0.8}"/>
</Latex>
<Latex formula="\text{-Residue}=\text{Base Decay} \times \text{Decay Boost} \times (\text{Toxic Residue})^{0.08}"/>
Kalıntı, <Color id="GREEN">LNE</Color> devre dışıyken 10 kat daha yavaş bozunur, bu nedenle denklemlere her zaman doğrudan güvenilmemelidir.

## Zehirli Kalıntı Sensör Kapağı <ItemImage id="gregtech:gt.blockmachines:3019"/>
<Color id="GREEN">Zehirli Kalıntı Sensör Kapağı</Color>, herhangi bir kademeli kasanın yerini alabilir ve jeneratörün özellikle tehlike sistemiyle ilgili otomasyonunu kolaylaştırır. Jeneratörün <Color id="RED">Zehirli Kalıntı</Color> değerini okur ve belirli eşiklere göre kızıltaş girişlerine izin veren ayarların yapılandırılmasına olanak tanıyan bir GUI'ye sahiptir.