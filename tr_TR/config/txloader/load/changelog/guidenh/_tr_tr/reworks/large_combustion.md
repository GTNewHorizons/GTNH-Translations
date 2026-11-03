---
item_ids:
  - gregtech:gt.blockmachines:15533
navigation:
  title: Büyük Yanmalı Motor
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15533
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Yanmalı Motor
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15533"/>
</GameScene>
<Color id="GREEN">Büyük Yanmalı Motor (LCE)</Color>, yanıcı yakıtlardan güç üretmek için kullanılan EV kademe bir multibloktur. <Color id="GREEN">LCE</Color>, tek bloklu yanmalı jeneratörlerin doğrudan yükseltmesidir çünkü çok daha yüksek yakıt verimliliğine sahiptir ve 1A'dan fazla güç çıktısı verebilir. Ancak <Color id="GREEN">LCE</Color>'nin çalışması için 1.000 L/h yağlayıcı ile beslenmesi gerekir ve isteğe bağlı olarak makineyi güçlendirmek için 40 L/s oksijen verilebilir. Güçlendirme şiddetle önerilir çünkü maksimum güç çıktısını üçe katlar ve yakıt verimliliğini yüzde 100'den yüzde 150'ye çıkarır. Güç, makinenin arkasındaki 4A dinamo kapağından alınır. Makine çalışırken dinamo kapağını kırma, yoksa patlar. Lapotronik Süperkapasitöre <ItemImage id="gregtech:gt.blockmachines:13106"/> bağlı bir RS mandalı ile <Color id="GREEN">LCE</Color>'yi otomatik açıp kapatarak yakıttan tasarruf et. <Color id="GREEN">LCE</Color>'nin yerini IV'te Ekstrem Yanmalı Motor <ItemImage id="gregtech:gt.blockmachines:15534"/> ve Evrensel Kimyasal Yakıt Motoru <ItemImage id="gregtech:gt.blockmachines:15535"/> alır. 

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Yalnızca yapının kendisi değişti, multiblokun çekirdek işlevselliği öncekiyle aynı

## Yapım
<Color id="GREEN">LCE</Color>'nin kademeli bileşenleri yoktur. Bakım Kapağı ve Egzoz Çıkışı, dişli kutusu kasasına temas ETMEYEN herhangi bir dengeli titanyum makine gövdesinin yerine geçebilir. Girdi kapağı(ları), dişli kutusu kasasına temas EDEN herhangi bir dengeli titanyum makine gövdesinin yerine geçebilir. Gerekli tüm sıvıları koymak için dörtlü girdi kapağı işe yarayabilir. Dinamo Kapağı, yapının sağ tarafında kontrolcünün karşısındaki orta kasayla sınırlıdır ve 4A'dan büyük olamaz. Ayrıca motor emme kasalarının önünde zorunlu hava boşluğu vardır. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15533"/><ItemImage id="gregtech:gt.blockmachines:15533"/>
- 21 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 19 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 10-15 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 8 <ItemLink id="gregtech:gt.blockcasings4:13"/><ItemImage id="gregtech:gt.blockcasings4:13"/>
- 4 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 1 Dinamo Kapağı (sağ orta kasa) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Girdi Kapağı (dişli kutusunun yanında olmayan herhangi bir titanyum kasa) <ItemImage id="gregtech:gt.blockmachines:50" />

### Duvar Paylaşımı
<Color id="GREEN">LCE</Color>'ler kasa, çerçeve kutusu ve veri yolu/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşabilir. Konum kısıtlaması nedeniyle buna girdi kapağı dahil DEĞİLDİR. 

## Kullanım
<Color id="GREEN">LCE</Color>, yanıcı dizel yakıtlardan güç üretir. En popüler seçenekler hafif yakıt, dizel ve setan takviyeli dizeldir. Jet Yakıtı A ve yüksek oktanlı benzin de oldukça yaygındır, ancak bunlar genellikle bunun yerine Ekstrem Yanmalı Motorda veya Evrensel Kimyasal Yakıt Motorunda kullanılır. Son iki yakıt o kadar yüksek enerji değerlerine sahiptir ki varsayılan modda kullanılamazlar. 

<Color id="GREEN">LCE</Color>'nin aşağıda listelenen iki çalışma modu vardır. Makine mevcut girdilere göre aralarında otomatik geçiş yapar. Güçlendirme şiddetle önerilir çünkü maksimum EU/t'yi üçe katlar ve yakıt verimliliğini yüzde 100'den yüzde 150'ye çıkarır. Oksijeni sürdürmek zor değildir--sadece bir şeker pancarı veya şalgam çiftliği kur ve şekeri elektroliz et.

_Varsayılan_
- Girdiler: Yakıt + 1.000 L/h yağlayıcı
- Çıktı: Yüzde 100 yakıt verimliliğinde maksimum 2.048 EU/t.

_Güçlendirilmiş_
- Girdiler: Yakıt + 1.000 L/h yağlayıcı + 40 L/s oksijen
- Çıktı: Yüzde 150 yakıt verimliliğinde maksimum 6.144 EU/t.

<Color id="GREEN">LCE</Color>'nin ayrıca makinenin güç çıktısıyla doğru orantılı kendi verimlilik değeri vardır. <Color id="GREEN">LCE</Color>'nin verimliliği makine çalışırken doğrusal olarak artar ve makine boştayken neredeyse anında yüzde sıfıra geri döner. Maksimum verimliliğe ulaşmak 33 sn (varsayılan) veya 100 sn (güçlendirilmiş) sürer. Mevcut verimliliği kontrolcüye bir Taşınabilir Tarayıcı kullanarak veya WAILA'daki verimlilik değerine bakarak görebilirsin.

<Color id="GREEN">LCE</Color> mümkün olduğunca uzun süre çalışmalı ama sonsuza kadar değil, çünkü dinamo kapağı dolduğunda fazladan EU boşa gider. Çözüm, Lapotronik Süperkapasitöre veya pil tamponuna bağlı bir RS mandalı ile <Color id="GREEN">LCE</Color>'yi otomatik açıp kapatmaktır.