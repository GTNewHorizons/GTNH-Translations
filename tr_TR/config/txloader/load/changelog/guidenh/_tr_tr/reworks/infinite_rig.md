---
item_ids:
  - gregtech:gt.blockmachines:15567
navigation:
  title: Sonsuz Sıvı Sondaj Kulesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15567
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Sonsuz Sıvı Sondaj Kulesi
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15567"/>
</GameScene>
<Color id="GREEN">Sonsuz Sıvı Sondaj Kulesi (IFDR)</Color>, ana kayanın altındaki büyük sıvı rezervuarlarını çıkarmak için kullanılan UHV kademe bir multibloktur. Sıvı rezervuarları 8x8 normal chunk boyutundadır ve özellikle gezegenler veya boyutlar arasında sıvının hem türü hem de miktarı açısından önemli ölçüde değişir. Rezervuarları araştır ve bilgilerini, bir araştırmacı tarayıcısıyla ana kayaya sağ tıklayarak ya da sismik araştırıcı kullanarak Journey Map'e ekle. <Color id="GREEN">IFDR</Color>, tüm bir rezervuar boyunca sonsuz miktarda sıvı toplayabilir. Sıvının çıkarılma hızı, minimumun üzerindeki gerilim kademesi sayısına ve çalışma aralığındaki kalan sıvı miktarına bağlıdır. Sıvıları üssüne/üssünden uzun menzilli sıvı boru hatları, ME kuantum halkaları veya ender tanklarla taşı.
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı: 
> - Artırılmış Paralel: UHV üzerindeki her enerji kademesi için +2 Paralel

## İnşa
<Color id="GREEN">IFDR</Color>'nin kademeli bileşeni yoktur. Maden borularını kontrolcüye ve/veya bir giriş yoluna yerleştir. Maden borusu fiziksel olarak yapının merkez bloğunun altında dünyada belirir ve ana kayaya doğru dümdüz inerken yolundaki her şeyi yok eder. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez ve yalnızca BİR normal enerji kapağına izin verilir. <Color id="GREEN">IFDR</Color>'nin her kademesi ayrıca çalışmak için minimum bir gerilim gerektirir. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Makinenin yağmurda patlamasını önlemek için üstünü kapatmayı unutma! Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15567"/><ItemImage id="gregtech:gt.blockmachines:15567"/>
- 90-103 <ItemLink id="gregtech:gt.blockcasings8:2"/><ItemImage id="gregtech:gt.blockcasings8:2"/>
- 38 <ItemLink id="gregtech:gt.blockframes:129"/><ItemImage id="gregtech:gt.blockframes:129"/>
- 20 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings8:7"/><ItemImage id="gregtech:gt.blockcasings8:7"/>
- 12 <ItemLink id="tectech:gt.blockcasingsTT:3"/><ItemImage id="tectech:gt.blockcasingsTT:3"/>
- 9 <ItemLink id="gregtech:gt.blockcasings9"/><ItemImage id="gregtech:gt.blockcasings9"/>
- 8 <ItemLink id="gregtech:gt.sheetmetal:397"/><ItemImage id="gregtech:gt.sheetmetal:397"/>
- 1 Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0-1 Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">IFDR</Color>'ler kasa, çerçeve kutusu ve veriyolu/kapaktan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. <Color id="GREEN">IFDR</Color> yalnızca 0,875A güç tüketir, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
Etkinleştirildiğinde <Color id="GREEN">IFDR</Color> önce maden borusunu/borularını ana kayaya doğru dümdüz indirir. Bu, makinenin mevcut y seviyesine bağlı olarak birkaç saniye sürebilir. Gerekirse işlemi hemen durdurmak için kontrolcünün GUI'sindeki "maden borularını iptal et ve geri çek" düğmesine bas. Yapıya çıkış yolu eklenemez, bu yüzden maden boruları kontrolcünün içindeki yuvaya geri döner. Maden borularının indirilmesi veya geri çekilmesi sırasında sıvı toplanmaz.

Neredeyse tükenmiş sıvı rezervuarlarını/chunk'ları yok saymak için programlanmış devreler kullan. İşlem (döngü) başına litre, programlanmış devre numarasından düşük olduğunda <Color id="GREEN">IFDR</Color> otomatik olarak durur ve maden borularını geri çeker.

<Color id="GREEN">Sonsuz Sıvı Sondaj Kulesi</Color>, diğer kuleler arasında benzersizdir; çünkü aşağıdaki tabloda görüldüğü gibi UHV üzerindeki her enerji kapağı kademesi için 2 paralel sunar. Güç paneli yalnızca bir paralel listeleyebilir ama pompa hızı buna göre artmalıdır.

|   | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |
| Paralel | 1 | 3 | 5 | 7 | 9 | 11 | 13 |