---
item_ids:
  - gregtech:gt.blockmachines:15545
navigation:
  title: Yosun Çiftliği
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15545
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Yosun Çiftliği

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15545"/>
</GameScene>
<Color id="GREEN">Yosun Çiftliği</Color>, farklı yosun türleri yetiştirmek için MV kademesinde bir multibloktur. <Color id="GREEN">Yosun Çiftliği</Color> çalışmak için güç dışında hiçbir girdi gerektirmez ve kirlilik üretmez. Her döngünün süresi ile üretilen yosunun türü/miktarı enerji kapağının kademesine bağlıdır. Birçok çıktı garantili değildir, bunun yerine %90 ihtimalle üretilir. İsteğe bağlı olarak, bir Giriş Yolundan kompost vererek makinenin kademesini bir artırabilirsin. 

<br clear="all"/>

> [!NOTE]
> Multoblokta (yapısal değişiklikler hariç) şu değişiklikler yapıldı:
> - Kademeli Cam: Artık yapının bir gereksinimi - UMV camı üstündeki tüm kademelerin kilidini açar
> - Güç: Yapı artık __GÜÇ GEREKTİRİYOR__
> - Hız: Döngü başına hız ve çıktı miktarları artık yapıdaki makine kasaları yerine güce bağlı

## İnşa
<Color id="GREEN">Yosun Çiftliği</Color>'nin bir kademeli bileşeni vardır. Cam, enerji kapağının maksimum kademesini belirler. UMV kademesindeki cam tüm kısıtlamaları kaldırır. Veriyolları/kapaklar yapının herhangi bir yerindeki yosun kasasının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez ve yalnızca BİR normal enerji kapağı olabilir. Su, makineyi ilk çalıştırmak için tek seferlik bir maliyettir ve yapıya bir rezervuar kapağı veya Girdi Kapağı aracılığıyla konur. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/> <ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Duvar Paylaşımı
<Color id="GREEN">Yosun Çiftlikleri</Color> kasa, cam ve veriyolu/kapak tasarrufu için her bir yanını duvar paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığından <u>__iki__</u> makine arasında <u>__tek__</u> bir enerji kapağı paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Yosun Çiftliği</Color> çalışmak için güç dışında hiçbir girdi gerektirmez ve kirlilik üretmez. Her döngünün süresi ile üretilen yosunun türü/miktarı enerji kapağının kademesine bağlıdır. Birçok çıktı garantili değildir, bunun yerine %90 ihtimalle üretilir. Örneğin, bir HV Yosun Çiftliği her zaman 1 kahverengi yosun üretir ve %90 ihtimalle 4 tane daha üretir; döngü başına toplam 5 ve saniyede ortalama 0,066.

LuV ve üzeri için iyileşen ölçeklemeye dikkat et. Tarif süresi her kademede 10 saniye azalmak yerine yarıya iner; bu da üretilen ortalama yosun miktarını büyük ölçüde artırır. En son kademe şu anda elde edilemez çünkü UXV'nin üzerinde üretilebilir enerji kapağı yok. 

İsteğe bağlı olarak, bir Giriş Yolundan GT++ kompostu verilerek makinenin kademesi yapay olarak bir artırılabilir. Örneğin bir MV Yosun Çiftliği kahverengi yosun üretebilir ve tarif süresi 80 sn'den 70 sn'ye düşebilir. İşlem başına gereken kompost miktarı her kademede ikiye katlanır ve en fazla 128'e ulaşır.

Yosunun kendisi başlıca ExxonMobil Kimya Tesisi <ItemImage id="gregtech:gt.blockmachines:998"/> içinde metan, sülfürik asit, etilen ve amonyak için yenilenebilir bir alternatif olarak kullanılır. Kahverengi yosun ayrıca MAR-Ce-M200 külçelerini eritmek için lityum klorür yapımında, kırmızı yosun ise prizmarin parçaları yapımında kullanılır.