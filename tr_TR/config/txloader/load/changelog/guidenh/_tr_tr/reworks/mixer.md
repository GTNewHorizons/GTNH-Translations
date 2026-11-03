---
item_ids:
  - gregtech:gt.blockmachines:15566
navigation:
  title: Endüstriyel Karıştırma Makinesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15566
categories:
    - Yapı Yenilemeleri
author: Skorched
date: 2026-05-27
---

# Endüstriyel Karıştırma Makinesi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15566"/>
</GameScene>
<Color id="GREEN">Yeşil Endüstriyel Karıştırma Makinesi</Color>, alaşımları ve diğer toz karışımlarını karıştırmak için IV kademe bir Multibloktur. <Color id="GREEN">Yeşil IMM</Color>, tek bloklu karıştırıcıya ve Buharlı Karıştırıcıya göre doğrudan bir yükseltmedir; çünkü <Color id="RED">Kırmızı %900</Color>'e kadar hızda çalışır ve gerilim kademesi başına <Color id="BLUE">Mavi 8</Color> paralel sunar. UIV+ cam ayrıca <Color id="GREEN">Yeşil IMM</Color>'in normal Enerji Kapakları yerine tek bir çok amperli Enerji Kapağı kullanmasını sağlar. Aynı makine içinde farklı programlanmış devreler kullanmak için <Color id="GREEN">Yeşil IMM</Color>'de Girdi Ayrıştırması etkinleştirilmelidir.

<br clear="all"/>

> [!NOTE]
> Önceki Endüstriyel Karıştırıcıya göre değişiklikler şunlardır (yeni yapı dışında):
> - Kademeli Eşya Boruları: eşya boru muhafazası kademesine bağlı olarak %200-900 hız!
> - Yeni Kasalar: Daha havalı görünüyor!
> - Çok Amperli Kapaklar: Artık Sonsuzluk camı ve sonrasıyla açılıyor!

## Yapım
<Color id="GREEN">Yeşil IMM</Color>'in bir kademeli bileşeni vardır. Eşya boru muhafazası makinenin hız bonusunu belirler. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur, ancak UIV+ cam IMM'in normal Enerji Kapakları yerine tek bir çok amperli Enerji Kapağı kullanmasını sağlar. Yollar/kapaklar yapının herhangi bir yerindeki karıştırıcı kasasının yerini alabilir. Lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal Enerji Kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan ve bu bileşenlerin kademesini belirtmek üzere "item_pipe" ile "glass" alt kanallarını ver.

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15566" /> Kontrolcü <ItemImage id="gregtech:gt.blockmachines:15566" />
- 5-45 <ItemLink id="gregtech:gt.blockcasings12:13" /> <ItemImage id="gregtech:gt.blockcasings12:13" />
- 30 Kademeli Cam (herhangi biri)
- 24 <ItemLink id="gregtech:gt.sheetmetal:316" /> <ItemImage id="gregtech:gt.sheetmetal:316" />
- 10 Eşya Boru Muhafazası <ItemImage id="gregtech:gt.blockcasings11" />
- 5 <ItemLink id="gregtech:gt.blockcasings4:11" /> <ItemImage id="gregtech:gt.blockcasings4:11" />
- 1+ Enerji Kapağı (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir karıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Yeşil IMM'ler</Color> kasa, sac metal ve yol/kapak tasarrufu için her kenarını duvar paylaşımına açabilir. Hiçbir Tarif 1A'dan fazla Güç kullanmaz, bu yüzden çok amperli bir Enerji Kapağı kullanılmadığı sürece <u>__iki__</u> makine arasında <u>__bir__</u> Enerji Kapağı paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">Yeşil IMM</Color>, tek bloklu karıştırıcıya ve Buharlı Karıştırıcıya göre doğrudan bir yükseltmedir; çünkü %900'e kadar hızda çalışır ve aşağıdaki tablolarda görüldüğü gibi gerilim kademesi başına 8 paralel sunar. UIV+ cam ayrıca <Color id="GREEN">Yeşil IMM</Color>'in normal Enerji Kapakları yerine tek bir çok amperli Enerji Kapağı kullanmasını sağlar.

### Paraleller:

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |

### Hız:
| Kademe | Eşya Boru Muhafazası | Hız |
| --------------- | --------------- | --------------- |
| 1 | Kalay | 200% |
| 2 | Pirinç | 300% |
| 3 | Elektrum | 400% |
| 4 | Platin | 500% |
| 5 | Osmiyum | 600% |
| 6 | Kuantinyum | 700% |
| 7 | Yüklenmiş Elektrum | 800% |
| 8 | Siyah Plütonyum | 900% |