---
item_ids:
  - gregtech:gt.blockmachines:15536
navigation:
  title: Naquadah Yakıt Rafinerisi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15536
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Naquadah Yakıt Rafinerisi
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15536"/>
</GameScene>
<Color id="GREEN">Naquadah Yakıt Rafinerisi (NFR)</Color>, neredeyse yalnızca Büyük Naquadah Reaktörü (LNR) <ItemImage id="gregtech:gt.blockmachines:15537"/> tarafından güç üretmek için kullanılan Mk-III+ naquadah bazlı sıvı yakıtları üretmeye yarayan UHV kademe bir multobloktur. Tüm yakıtların, daha verimli üretim sağlayan ancak daha pahalı materyaller gerektiren en az bir alternatif tarifi vardır. <Color id="GREEN">NFR</Color> girdi gerilimini artırarak hız aşırtılamaz; bunun yerine alan kısıtlama bobinleri yükseltilerek hız aşırtılır. Dört kademe mevcuttur ve her biri yeni tarifler açar, daha düşük kademe tarifler için ek bir kusursuz hız aşırtma yapar ve 4 paralel sunar. 

NFR dahil güç planlaması için bir elektronik tablo [burada](https://docs.google.com/spreadsheets/d/1FTFdfmY_UWbTbFOyNzARKeI90pbHvPBH6M3JHJmaC-E/edit?gid=589078529#gid=589078529) bulunabilir.
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı hariç) aşağıdaki değişiklikler yapıldı:
> - Serbest Kapak Yerleşimi: Kapaklar artık camın bitişiğindeki konumlarla sınırlı değil.
> - Daha Fazla Paralel: Artan bobin maliyetini telafi etmek için bobin kademesi başına +4 Paralel

## İnşaat
<Color id="GREEN">NFR</Color>'nin kademeli tek bir bileşeni vardır. Alan kısıtlama bobinleri mevcut tarifleri, kusursuz hız aşırtma sayısını ve paralel sayısını belirler. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir naquadah yakıt rafinerisi kasasının yerini alabilir. <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir, ancak girdi gerilimini artırmak makineyi hız aşırtmaz. Bakım kapağı yoktur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan; tek bir kümede tutulan projektör sayısı bobinlerin kademesini belirler. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15536"/><ItemImage id="gregtech:gt.blockmachines:15536"/>
- 0-483 <ItemLink id="GoodGenerator:FRF_Casings"/><ItemImage id="GoodGenerator:FRF_Casings"/>
- 192 <ItemLink id="GoodGenerator:fieldRestrictingGlass"/><ItemImage id="GoodGenerator:fieldRestrictingGlass"/>
- 124 <ItemLink id="gregtech:gt.blockcasings8:5"/><ItemImage id="gregtech:gt.blockcasings8:5"/>
- 72 Alan Kısıtlama Bobini (Kademeli)<ItemImage id="GoodGenerator:FRF_Coil_1"/>
- 64 <ItemLink id="GoodGenerator:radiationProtectionSteelFrame"/><ItemImage id="GoodGenerator:radiationProtectionSteelFrame"/>
- 1+ Enerji Kapağı (herhangi bir rafineri kasası) <ItemImage id="gregtech:gt.blockmachines:40" />
- 0+ Giriş Yolu (herhangi bir rafineri kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir rafineri kasası) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (herhangi bir rafineri kasası) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">NFR</Color>'ler kasa, cam ve yol/kapaklardan tasarruf etmek için her kenarını duvar paylaşımında kullanabilir. EU/t miktarları sabit olduğu için buna enerji kapağı da dahildir, ancak alan kısıtlama bobinleri DAHİL DEĞİLDİR. 

## Kullanım
Tüm <Color id="GREEN">NFR</Color> tariflerinin bir minimum kademe alan kısıtlama bobini vardır. Her kademe 4 paralel sunar ve minimumun üzerindeki her kademe ek bir kusursuz hız aşırtma sağlar. Örneğin, Mk-IV naquadah bazlı sıvı yakıt en az 2. kademe bobinler gerektirir, ancak 4. kademe bobinlere sahip bir <Color id="GREEN">NFR</Color> bu tarifi 16 paralel ve iki kusursuz hız aşırtma ile çalıştırabilir. Bu nedenle, her zaman mümkün olan en yüksek kademe bobinlere yükseltmen önerilir. 