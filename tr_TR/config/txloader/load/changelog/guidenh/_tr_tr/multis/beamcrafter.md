---
item_ids:
  - gregtech:gt.blockmachines:3015
navigation:
  title: Işın Üreticisi
  parent: multis.md
  icon: gregtech:gt.blockmachines:3015
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-25
---

# Işın Üreticisi
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3015" />
</GameScene>
<Color id="GREEN">Işın Üreticisi</Color>, herhangi bir başka kaynaktan sağlanan parçacık ışınlarını kullanarak girişlerdeki akışkanları ve sıvıları bombardıman edip başka bir çıktı üreten ZPM kademesinde bir multibloktur.
<br clear="all"/>

## İnşa:
Işın Üreticisi, Işın Hattı'ndan farklı olarak tek bir multibloktur. Oluşturulan ışınları <ItemLink id="gregtech:gt.blockmachines:10503"/><ItemImage id="gregtech:gt.blockmachines:10503"/> içine yönlendirmek için Işın Hattı boruları kullanılır. Bu boruların uzunluğunun makinenin hiçbir özelliğine veya ışınların kendisine etkisi yoktur.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:3015"/><ItemImage id="gregtech:gt.blockmachines:3015"/>
- 224-228 <ItemLink id="gtnhlanth:casing.shielded_accelerator"/><ItemImage id="gtnhlanth:casing.shielded_accelerator"/>
- 26 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:5"/>
- 16 <ItemLink id="gregtech:gt.blockcasings3:10"/><ItemImage id="gregtech:gt.blockcasings3:10"/>
- 2 <ItemLink id="gregtech:gt.blockmachines:10503"/><ItemImage id="gregtech:gt.blockmachines:10503"/>
- 1+ Enerji Kapağı (herhangi bir çarpıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 0+ Giriş Yolu (herhangi bir çarpıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir çarpıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ Çıkış Yolu (herhangi bir çarpıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ Çıkış Kapağı (herhangi bir çarpıştırıcı kasası) <ItemImage id="gregtech:gt.blockmachines:60"/>

## Kullanım:
Sağlanan eşya ve sıvılarla geçerli bir üretim algılanırsa üretim başlar. Işın Üreticisi parçacıkları ancak bu noktada ışın hattı giriş kapakları üzerinden kabul etmeye başlar. Bu ışında doğru parçacıklar varsa üretime ilerleme sağlamak için tüketilirler. Parçacık ışınları kesilirse tarif __durmayacaktır__, ama ilerleme duracaktır. Üretim sürerken, sağlanan parçacık miktarından bağımsız olarak sürekli enerji tüketilir.

Makine parçacıkları tamponlar, ancak bunu yalnızca çalışırken yapar; aksi halde parçacık kabul edemez.

## Yönlendirme:
Işın Üreticisinin yanında, ışınları yönlendirmek için tasarlanmış üç yeni lojistik multiblok vardır. Bunlar <Color id="GREEN">Işın Aynası</Color>, <Color id="RED">Işın Bölücü</Color> ve <Color id="BLUE">Işın Dengeleyici</Color>.
- <Color id="GREEN">Işın Aynası</Color><ItemImage id="gregtech:gt.blockmachines:3016"/> - Bir ışını 90 veya 180 derece döndürmeyi sağlar
- <Color id="RED">Işın Bölücü</Color> <ItemImage id="gregtech:gt.blockmachines:3017"/> - Karışık bir parçacık paketi akışını 4 ayrı yapılandırılabilir hatta bölmeyi sağlar
- <Color id="BLUE">Işın Dengeleyici</Color> <ItemImage id="gregtech:gt.blockmachines:3018"/> - Küçük bir tampon görevi görerek aralıklı yüksek oranlı bir ışını daha düşük miktarlı sabit bir ışına dönüştürmeyi sağlar