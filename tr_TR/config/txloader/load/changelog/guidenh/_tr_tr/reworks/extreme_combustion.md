---
item_ids:
  - gregtech:gt.blockmachines:15534
navigation:
  title: Ekstrem Yanma Motoru
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15534
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Ekstrem Yanma Motoru

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15534"/>
</GameScene>
<Color id="GREEN">Ekstrem Yanma Motoru (ECE)</Color>, yanıcı yakıtlardan güç üretmek için kullanılan bir IV kademesi multibloğudur. <Color id="GREEN">ECE</Color>, <Color id="GREEN">Büyük Yanma Motoruna</Color> göre doğrudan bir yükseltmedir çünkü 5 katından fazla güç çıktısı verebilir. Ancak <Color id="GREEN">ECE</Color>'ye çalışması için 8.000 L/saat yağlayıcı verilmesi gerekir ve isteğe bağlı olarak 40 L/s sıvı oksijenle makine takviye edilebilir. Takviye şiddetle önerilir çünkü maksimum güç çıktısını üçe katlar ve yakıt verimliliğini %100'den %150'ye çıkarır. Güç, makinenin arkasındaki 4A dinamo kapağından alınır. Makine çalışırken dinamo kapağını kırma, yoksa patlar. Lapotronik Süperkapasitöre bağlı bir RS mandalıyla <Color id="GREEN">ECE</Color>'yi otomatik açıp kapatarak yakıttan tasarruf et. <ItemImage id="gregtech:gt.blockmachines:13106"/> <Color id="GREEN">ECE</Color>'nin yerini, üretebileceği güç miktarında üst sınır olmayan Evrensel Kimyasal Yakıt Motoru alır. <ItemImage id="gregtech:gt.blockmachines:15535"/>

[GTNH Güç Planlayıcısı](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Bu multiblokta değişen tek şey yapıdır, temel işlevselliği öncekiyle aynıdır

## İnşa
<Color id="GREEN">ECE</Color>'nin kademeli bileşeni yoktur. Bakım kapağı ve Egzoz Çıkışı, dişli kutusu kasasına DEĞMEYEN herhangi bir Sağlam Tungsten Çelik Makine Gövdesinin yerini alabilir. Girdi Kapağı/Girdi Kapakları, dişli kutusu kasasına DEĞEN herhangi bir tungsten çeliği türbin gövdesinin yerini alabilir. Dörtlü Girdi Kapağı, gerekli tüm sıvıları yerleştirmek için işe yarayabilir. Dinamo kapağı, yapının sağ tarafında kontrolcünün karşısındaki merkez kasayla sınırlıdır ve 4A'dan büyük olamaz. Ayrıca ekstrem motor emme kasalarının üzerinde hava bulunması zorunludur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15534"/><ItemImage id="gregtech:gt.blockmachines:15534"/>
- 30-33 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 32 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 30 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 12 <ItemLink id="gregtech:gt.blockcasings3:15"/><ItemImage id="gregtech:gt.blockcasings3:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings8:4"/><ItemImage id="gregtech:gt.blockcasings8:4"/>
- 4-7 <ItemLink id="gregtech:gt.blockcasings4:12"/><ItemImage id="gregtech:gt.blockcasings4:12"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1 Dinamo Kapağı (sağ merkez kasa) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Girdi Kapağı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:50" />

### Duvar Paylaşımı
<Color id="GREEN">ECE</Color>'ler kasadan tasarruf etmek için her yüzünü duvar paylaşabilir. Konumu kısıtlı olduğu için buna Girdi Kapağı dahil DEĞİLDİR.

## Kullanım
<Color id="GREEN">ECE</Color>, sınırlı sayıda yanıcı dizel yakıttan güç üretir. Aşağıdaki tablo mevcut seçenekleri ve yoğunluklarını (EU/L) listeler. En popüler seçenekler Jet Yakıtı A ve yüksek oktanlı benzindir. Her ikisi genellikle Evrensel Kimyasal Yakıt Motorunda da kullanılır.
| Dizel Yakıt | EU/L | Varsayılan Hız | Takviyeli Hız |
| --------------- | --------------- | --------------- | --------------- |
| Jet Yakıtı No.3 | 1,824 | 5.98 L/t | 12.0 L/t |
| Jet Yakıtı A | 1,248 | 4.85 L/t | 9.70 L/t |
| Yüksek Oktanlı Benzin | 2,500 | 4.36 L/t | 8.72 L/5 |


<Color id="GREEN">ECE</Color>'nin aşağıda listelenen iki çalışma modu vardır. Makine mevcut girdilere göre aralarında otomatik geçiş yapar. Takviye şiddetle önerilir çünkü maksimum EU/t değerini üçe katlar ve yakıt verimliliğini %100'den %150'ye çıkarır. Sıvı oksijeni sürdürmek zor değildir -- sadece kendine ait bir Vakum Dondurucu <ItemImage id="gregtech:gt.blockmachines:1002"/> veya [Gezegen Gaz Sifonu](./siphon.md) <ItemImage id="gregtech:gt.blockmachines:15559"/> inşa et.

_Varsayılan_
- Girdiler: Yakıt + 8.000 L/saat yağlayıcı.
- Çıktı: %100 yakıt verimliliğinde maksimum 10,900 EU/t.

_Takviyeli_
- Girdiler: Yakıt + 8.000 L/saat yağlayıcı + 40 L/s sıvı oksijen.
- Çıktı: %150 yakıt verimliliğinde maksimum 32,700 EU/t.

<Color id="GREEN">ECE</Color> ayrıca makinenin güç çıktısıyla doğru orantılı kendi verim değerine sahiptir. <Color id="GREEN">ECE</Color>'nin verimi makine çalışırken doğrusal olarak artar ve makine boştayken neredeyse anında sıfıra döner. Maksimum verime ulaşması 25 sn (varsayılan) veya 75 sn (takviyeli) sürer. Mevcut verimi, kontrolcüye bir Taşınabilir Tarayıcı <ItemImage id="gregtech:gt.metaitem.01:32762"/> kullanarak veya WAILA'daki verim değerine bakarak görüntüle.

<Color id="GREEN">ECE</Color> mümkün olduğunca uzun çalışmalıdır ama sonsuza kadar değil, çünkü dinamo kapağı dolduğunda fazladan EU yok edilir. Çözüm, <Color id="GREEN">ECE</Color>'yi Lapotronik Süperkapasitöre veya pil tamponuna bağlı bir RS mandalıyla otomatik açıp kapatmaktır.