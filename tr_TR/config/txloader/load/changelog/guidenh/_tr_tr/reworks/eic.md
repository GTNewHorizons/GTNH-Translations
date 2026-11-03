---
item_ids:
  - gregtech:gt.blockmachines:15563
navigation:
  title: Elektrikli Patlama Kompresörü
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15563
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Elektrikli Patlama Kompresörü
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15563"/>
</GameScene>
<Color id="GREEN">Elektrikli Patlama Kompresörü (EIC)</Color>, plakaları ve tozları elektrikle sıkıştırmak için kullanılan bir UHV kademesi multibloktur. <Color id="GREEN">EIC</Color>, patlayıcı tüketmediği, tarif sürelerini 1 saniyeden 1 tick'e düşürdüğü ve 256'ya kadar paralel sunabildiği için Patlama Kompresörü <ItemImage id="gregtech:gt.blockmachines:1001"/> ve Density^2 <ItemImage id="gregtech:gt.blockmachines:15547"/> makinelerinin doğrudan yükseltmesidir. <Color id="GREEN">EIC</Color> aynı zamanda manyetik hidrodinamik olarak kısıtlanmış yıldız maddesi (MHDCSM) parçalarını üretebilen tek makinedir ve bu nedenle UXV'ye ilerlemek için zorunludur, ancak mümkün olan en kısa sürede inşa edilmesi şiddetle önerilir. 

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapıldı:
> - Cam: Yapıda artık cam olduğu için bu da başka bir kademeli bileşendir. UMV camı kısıtlamaları kaldırır.

## İnşaat
<Color id="GREEN">EIC</Color>'nin iki kademeli bileşeni vardır. Muhafaza blokları paralel sayısını, cam ise enerji kapağının maksimum kademesini belirler. UMV kademesi camı tüm kısıtlamaları kaldırır. Veriyolları/kapaklar yapının herhangi bir yerindeki naquadah güçlendirilmiş bloğun yerine geçebilir. Ciddi overclock için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir, ancak <Color id="GREEN">EIC</Color> yalnızca bir kademe atlayabilir. Muhafaza bloklarının ve camın kademesini belirtmek üzere sırasıyla "piston_block" ve "glass" alt kanallarıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15563"/><ItemImage id="gregtech:gt.blockmachines:15563"/>
- 230-247 <ItemLink id="gregtech:gt.blockreinforced:10"/><ItemImage id="gregtech:gt.blockreinforced:10"/>
- 36 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 24 Muhafaza Bloğu (Kademeli) <ItemImage id="gregtech:gt.blockmetal5:2"/>
- 22 Kademeli Cam <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 10 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 2 <ItemLink id="gregtech:gt.blockframes:324"/><ItemImage id="gregtech:gt.blockframes:324"/>
- 1+ Enerji Kapağı (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir güçlendirilmiş blok) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">EIC</Color>'ler kasa ve veriyolu/kapaklardan tasarruf etmek için her bir yüzlerini duvar paylaşımına açabilir. Buna yapının sol ve sağındaki kanatların üç katmanının tamamı da dahildir. Konumlarındaki kısıtlama nedeniyle muhafaza blokları buna DAHİL DEĞİLDİR. 

## Kullanım
<Color id="GREEN">EIC</Color> tariflerinin çoğu UEV geriliminde derecelendirilmiştir ve yalnızca 1 tick uzunluğundadır. Bu, <Color id="GREEN">EIC</Color>'nin inanılmaz hızlı olduğu ve hiç patlayıcı kullanmadığı halde şaşırtıcı derecede enerji verimli olduğu anlamına gelir. Daha yüksek kademeler ayrıca aşağıdaki tabloda görüldüğü gibi önemli sayıda paralel ekler. 

| Kademe | Muhafaza Bloğu | Paralel |
| --------------- | --------------- | --------------- |
| 1 | Nötronyum Bloğu | 1 |
| 2 | Sonsuzluk Bloğu | 4 |
| 3 | Aşkın Metal Bloğu | 16 |
| 4 | Uzayzaman Bloğu | 64 |
| 5 | Universium Bloğu | 256 |

Ancak <Color id="GREEN">EIC</Color> yalnızca bir kademe atlayabilir. Örneğin bir tarif MAX geriliminde derecelendirilmişse, <Color id="GREEN">EIC</Color>'nin onu çalıştırmak için en az 4A UXV enerji kapağına ihtiyacı vardır. Ne kadar UMV amper olursa olsun asla yeterli olmaz. Bu sınırlama, sonsuzluk nanitleriyle eriyik halindeki MHDCSM üretmeye çalışırken en belirgin halini alır. 
<RecipeFor id="gregtech:gt.metaitem.99:583" input="gregtech:gt.metaitem.03:4141"/>