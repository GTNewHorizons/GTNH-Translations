---
item_ids:
  - gregtech:gt.blockmachines:15752
navigation:
  title: L.A.T.E.X.
  parent: multis.md
  icon: gregtech:gt.blockmachines:15752
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-25
---

# L.A.T.E.X.
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15752" />
</GameScene>
<Color id="GREEN">Laminated Application and Termal Enclosure eXpert (LATEX)</Color>, adı her ne kadar ağza dolgun gelse de, kabloları kaplamaya yarayan HV kademesi bir multibloktur. <Color id="GREEN">LATEX</Color>, kablo kaplama için tek bloklu montajcının doğrudan yükseltmesidir; çünkü <Color id="GREEN">%200</Color> hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="RED">%85</Color>'ini kullanır ve gerilim kademesi başına <Color id="BLUE">8</Color> paralel sunar. Ayrıca boru muhafazasının kademesine bağlı olarak eklenen %6.25 kauçuk indirimi ile paralel sayısını ikiye katlamak, %25 daha kauçuk indirimi kazanmak ve çok amperli ve lazer enerji kapaklarını kullanabilme imkânı sunan, kontrolcünün içine elastik tekillik yerleştirme fırsatı da vardır. 
<br clear="all"/>

## İnşaat:
LATEX'in kademeli tek bir bileşeni vardır. Boru muhafazası blokları makinenin toplam kauçuk indirimini belirler. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. Yapının oluşması için cam kademeli olmalıdır; ancak camın makinenin çalışmasına etkisi yoktur. Kontrolcüde elastik tekillik olmadığı sürece çok amperli ve lazer enerji kapakları desteklenmez; ancak overclock için birden fazla normal enerji kapağı kullanılabilir. Bu bileşenlerin kademesini belirtmek için "item_pipe" ve "glass" alt kanallarıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" /><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15752" /><ItemImage id="gregtech:gt.blockmachines:15752"/>
- 14-36 <ItemLink id="gregtech:gt.blockcasings8"/> <ItemImage id="gregtech:gt.blockcasings8"/>
- 32 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 16 <ItemLink id="gregtech:gt.blockframes:649"/><ItemImage id="gregtech:gt.blockframes:649"/>
- 6 Boru Muhafazası (Kademeli)<ItemImage id="gregtech:gt.blockcasings11:5"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80"/>
### Duvar Paylaşımı:
<Color id="GREEN">LATEX</Color> makineleri kasa, cam, çerçeve bloğu ve veriyolu/kapak tasarrufu sağlamak için her bir kenarını paylaşabilir. Hiçbir tarif 1 A'dan fazla güç kullanmaz; bu yüzden <u>__tek__</u> bir enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür. 

## Kullanım:
<Color id="GREEN">LATEX</Color>, kablo kaplama için tek bloklu montajcının doğrudan yükseltmesidir; %200 hızda çalışır, normalde gereken EU/t'nin yalnızca %85'ini kullanır ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 8 paralel sunar. Ayrıca Boru Muhafazasının kademesine bağlı olarak eklenen %6.25 kauçuk polimer indirimi vardır. 

### Paraleller:
|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
|  | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |
| ES | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |

> [!NOTE]
> Burada "ES", kontrolcüde bir Elastik Tekillik bulunduğu anlamına gelir

| Boru Muhafazası   | Kauçuk İndirimi    |
|--------------- | --------------- |
| Kalay   | 6.25%   |
| Pirinç   | 12.50%   |
| Elektrum   | 18.75%   |
| Platin   | 25.00%   |
| Osmiyum   | 31.25%   |
| Kuantinyum   | 37.50%   |
| Fluxlu Elektrum   | 43.75%   |
| Kara Plütonyum   | 50.00%   |


## Elastik Tekillik
<Color id="GREEN">LATEX</Color> kontrolcüsüne bir elastik tekillik yerleştirerek paralel sayısını ikiye katla, %25 daha kauçuk indirimi kazan ve çok amperli ve lazer enerji kapaklarını kullanma imkânının kilidini aç. Bu, en fazla 240 paralel ve %75 kauçuk polimer indirimi demektir. Elastik tekilliğin kendisi bir Dire Üretim Masasında üretilir; ancak onu oluşturan beş tekilliğin tamamı Nötronyum Kompresöründe veya Sözde Kararlı Kara Delik Muhafaza Alanında yapılır. Yani bu yükseltme UV'ye kadar takılamaz ve tekillik makineler arasında paylaşılamaz. Her tekilliğin maliyeti aşağıda listelenmiştir (her biri 113,771,520 L).

- Kauçuk Tekilliği - 12,345 süper yoğun kauçuk levha veya 790,080 tek tek kauçuk levha.
- Silikon Kauçuk Tekilliği - 12,345 süper yoğun silikon kauçuk levha veya 790,080 tek tek silikon kauçuk levha.
- Polivinil Klorür Tekilliği - 12,345 süper yoğun polivinil klorür levha veya 790,080 tek tek polivinil klorür levha.
- Stiren Bütadien Kauçuk Tekilliği - 12,345 süper yoğun stiren bütadien kauçuk levha veya 790,080 tek tek stiren bütadien kauçuk levha.
- Polifenilen Sülfür Tekilliği - 12,345 süper yoğun polifenilen sülfür levha veya 790,080 tek tek polifenilen sülfür levha.