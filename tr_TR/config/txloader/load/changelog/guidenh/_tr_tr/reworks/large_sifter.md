---
item_ids:
  - gregtech:gt.blockmachines:15542
navigation:
  title: Büyük Elek
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15542
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Elek

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15542"/>
</GameScene>
<Color id="GREEN">Büyük Elek</Color>, değerli taşları ve mineralleri elemek için HV kademesinde bir multibloktur. <Color id="GREEN">Büyük Elek</Color>, tek bloklu eleğin doğrudan yükseltmesidir; çünkü <Color id="RED">%500</Color> hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%75</Color>'ini kullanır ve gerilim kademesi başına <Color id="GREEN">4</Color> paralel sunar. Başka kullanımı olmayan tozları ve sıvıları pasif olarak elemek önerilir.
<br clear="all"/>

> [!NOTE]
> Bu multibloğun yalnızca yapısı değişti; mekanikler aynı kalıyor

## İnşa
<Color id="GREEN">Büyük Elek</Color>'in kademeli bileşenleri yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15542"/><ItemImage id="gregtech:gt.blockmachines:15542"/>
- 45-59 <ItemLink id="miscutils:gtplusplus.blockcasings.2:5"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:5"/>
- 19 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:6"/>
- 16 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Büyük Elekler</Color> kasa, çerçeve kutusu ve veriyolu/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımına açabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">Büyük Elek</Color>, tek bloklu eleğin doğrudan yükseltmesidir; çünkü %500 hızda çalışır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 4 paralel sunar.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


GTNH'de yalnızca elekte kullanılan ve başka hiçbir amaca hizmet etmeyen birkaç toz ve sıvı vardır. Bunları ME stoklama veriyollarına/kapaklarına veya bölümlenmiş depolama hücreleri ve yapışkan kartlar içeren bir AE2 alt ağına koyman şiddetle önerilir.