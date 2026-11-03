---
item_ids:
  - gregtech:gt.blockmachines:15550
navigation:
  title: Cevher Yıkama Tesisi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15550
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Cevher Yıkama Tesisi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15550"/>
</GameScene>
<Color id="GREEN">Cevher Yıkama Tesisi (OWP)</Color>, ezilmiş cevherleri yıkamak veya basit yıkama yapmak için kullanılan bir EV kademe multibloğudur. Yıkama ile basit yıkama arasındaki fark, ikincisinin belirgin şekilde daha hızlı olması ama cevherlerden hiçbir yan ürün üretmemesidir. <Color id="GREEN">OWP</Color>, tek bloklu cevher yıkayıcı ve basit yıkayıcıya doğrudan bir yükseltmedir; çünkü her iki tarif türünü de işleyebilir, <Color id="RED">%500</Color> hızla çalışır ve her gerilim kademesi için <Color id="BLUE">4</Color> paralel sunar. 
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı hariç) aşağıdaki değişiklikler yapılmıştır:
> - Ayrıştırma: Bu multiblok __artık__ kimyasal banyo tariflerini işlemez. Bunun yerine [Industrial Chemical Bath](./chem_bath.md) sayfasına bak

## İnşaat
<Color id="GREEN">OWP</Color>'nin kademeli bileşenleri yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı bulunabilir. Su, makineyi ilk çalıştırmak için tek seferlik bir maliyettir ve yapıya bir rezervuar kapağı veya girdi kapağı aracılığıyla verilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15550"/><ItemImage id="gregtech:gt.blockmachines:15550"/>
- 70-85 <ItemLink id="miscutils:gtplusplus.blockcasings.2:4"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:4"/>
- 15 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">OWP</Color>'ler kasa ve yol/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımıyla kullanabilir. Buna su sağlayan rezervuar kapağı da dahildir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden bir enerji kapağını iki makine arasında paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">OWP</Color>, tek bloklu cevher yıkayıcı ve basit yıkayıcıya doğrudan bir yükseltmedir; çünkü her iki tarif türünü de işleyebilir, %500 hızla çalışır ve her gerilim kademesi için 4 paralel sunar.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


<Color id="GREEN">OWP</Color>'nin aşağıda listelenen iki çalışma modu vardır. Modları kontrolcünün GUI'sinde değiştir. Cevher yıkayıcı modu, çok hızlı olduğu ve yan ürün ürettiği için cevher işleme düzeneklerinde özellikle kullanışlıdır.

- Cevher Yıkayıcı - Ezilmiş cevherleri her biri 200L su ile yıkar. Yan ürün üretir.
- Basit Yıkayıcı - Ezilmiş cevherleri ve saf olmayan tozları her biri 100L su ile yıkar. Yan ürün üretmez.