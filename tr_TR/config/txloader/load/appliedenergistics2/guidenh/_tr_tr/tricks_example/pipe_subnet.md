---
navigation:
  parent: /tricks_example_index.md
  title: Eşya/Sıvı "Boru" Alt Ağı
  icon: appliedenergistics2:item.ItemMultiPart:220
---

# Eşya/Sıvı "Boru" Alt Ağı

AE2 [cihazlarıyla](../ae2_mechanics/devices.md) bir eşya ve/veya sıvı borusunu taklit etmenin basit bir yöntemi; kısacası, bir eşya veya sıvı borusunu ne için kullanıyorsan onun için işe yarar.
Buna bir üretimin sonucunu bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> içine geri döndürmek de dahildir.

Bunu başarmanın genellikle iki farklı yöntemi vardır:

## İçe Aktarma Veriyolu -> Depolama Veriyolu

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) İçe Aktarma Veriyolu: Filtrelenebilir.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) Depolama Veriyolu: Filtrelenebilir. Bu (ve hedef olmasını istediğin diğer depolama veriyolları)
    ağdaki tek depolama olmalıdır.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    Kaynak
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    Hedef
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Kaynak envanterdeki <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (1) eşyaları veya sıvıyı içe aktarır ve bunları [ağ deposuna](../ae2_mechanics/import_export_storage.md) depolamaya çalışır.
Ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2) olduğundan (bu yüzden bu bir alt ağdır ve ana ağında değildir), eşyalar veya sıvı
hedef envantere konur ve böylece aktarılmış olur. Enerji bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" /> üzerinden sağlanır.
Hem içe aktarma veriyolu hem de depolama veriyolu filtrelenebilir, ancak filtre uygulanmazsa düzen erişebildiği her şeyi aktarır.
Bu düzen birden fazla içe aktarma veriyolu ve birden fazla depolama veriyolu ile de çalışır.

## Depolama Veriyolu -> Dışa Aktarma Veriyolu

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/storage_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) Depolama Veriyolu: Filtrelenebilir. Bu (ve kaynak olmasını istediğin diğer depolama veriyolları)
    ağdaki tek depolama olmalıdır.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) Dışa Aktarma Veriyolu: Filtrelenmelidir.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    Kaynak
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    Hedef
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Hedef envanterdeki <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> filtresindeki eşyaları [ağ deposundan](../ae2_mechanics/import_export_storage.md) çekmeye çalışır.
Ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> olduğundan (bu yüzden bu bir alt ağdır ve ana ağında değildir), eşyalar veya sıvı
kaynak envanterden çekilir ve böylece aktarılmış olur. Enerji bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" /> üzerinden sağlanır.
Dışa aktarma veriyolları çalışmak için filtrelenmek zorunda olduğundan, bu düzen yalnızca dışa aktarma veriyolunu filtrelediğinde çalışır.
Bu düzen birden fazla depolama veriyolu ve birden fazla dışa aktarma veriyolu ile de çalışır.

## Çalışmayan Bir Düzen (İçe Aktarma Veriyolu -> Dışa Aktarma Veriyolu)

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dd3333" thickness="1">
    İçe Aktarma Veriyolu: Ağda depolama olmadığından içe aktarabileceği bir yer yok.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dd3333" thickness="1">
    (2) Dışa Aktarma Veriyolu: Ağda depolama olmadığından dışa aktarabileceği bir şey yok.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
    Kaynak
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
    Hedef
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Yalnızca bir içe aktarma ve bir dışa aktarma veriyolundan oluşan bir düzen çalışmaz. İçe aktarma veriyolu kaynak envanterden çekmeye
ve eşyaları veya sıvıyı ağ deposuna depolamaya çalışır. Dışa aktarma veriyolu ağ deposundan çekmeye ve
eşyaları veya sıvıyı hedef envantere koymaya çalışır. Ancak bu ağın **depolaması olmadığından** içe aktarma veriyolu içe aktaramaz
ve dışa aktarma veriyolu dışa aktaramaz, bu yüzden hiçbir şey olmaz.

## Tek Yüzden Girdi ve Çıktı

Girdi alabilen ve çıktısı tek yüzden çekilebilen bir makinen olduğunu düşün. (Bir <ItemLink id="appliedenergistics2:tile.BlockCharger" /> gibi.)
2 boru alt ağı yöntemini birleştirerek hem malzemeleri içeri itebilir hem de sonucu dışarı çekebilirsin:

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_export_pipe.snbt" />
  <BoxAnnotation min="4 1 1" max="5 1.3 2" color="#dddddd" thickness="1">
    (1) İçe Aktarma Veriyolu: Filtrelenebilir.
  </BoxAnnotation>
  <BoxAnnotation min="2 1 1" max="3 1.3 2" color="#dddddd" thickness="1">
    (2) Depolama Veriyolu: Filtrelenebilir. Bu (ve eşya itip çekmek istediğin diğer depolama veriyolları)
    ağdaki tek depolama olmalıdır.
  </BoxAnnotation>
  <BoxAnnotation min="2 0 1" max="3 1 2" color="#dddddd" thickness="1">
    (3) İçine İtmek ve Ondan Çekmek İstediğin Şey: Bu durumda bir Şarj Cihazı.
  </BoxAnnotation>
  <BoxAnnotation min="0 1 1" max="1 1.3 2" color="#dddddd" thickness="1">
    (4) Dışa Aktarma Veriyolu: Filtrelenmelidir.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
    Kaynak
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
    Hedef
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Arayüzler

İçe aktarma ve dışa aktarma veriyollarının yanı sıra eşyaları [ağ deposuna](../ae2_mechanics/import_export_storage.md) iten
ve oradan çeken [cihazlar](../ae2_mechanics/devices.md) da varmış!
Burada ilgili olan <ItemLink id="appliedenergistics2:tile.BlockInterface" />. Arayüzün stoklamak üzere ayarlanmadığı bir eşya yerleştirilirse arayüz onu
ağ deposuna iter; bundan içe aktarma veriyolu -> depolama veriyolu borusuna benzer şekilde yararlanabiliriz. Bir arayüzü
bir eşyayı stoklamak üzere ayarlamak, onu ağ deposundan çeker; depolama veriyolu -> dışa aktarma veriyolu borusuna benzer. Arayüzler
bazı şeyleri stoklayıp bazılarını stoklamayacak şekilde ayarlanabilir; böylece bir nedenden dolayı bunu yapmak istersen depolama veriyolları üzerinden uzaktan itme ve çekme yapabilirsin.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/interface_pipes.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    Arayüz
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    Depolama Veriyolu
  </BoxAnnotation>
  <BoxAnnotation min="3.7 0 2" max="4 1 3" color="#dddddd" thickness="1">
    Depolama Veriyolu
  </BoxAnnotation>
  <BoxAnnotation min="0 1 2" max="1 1.3 3" color="#dddddd" thickness="1">
    Arayüz
  </BoxAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Birden Çoka ve Çoktan Bire (ve çoktan çoka)

Elbette yalnızca bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> veya <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> veya <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> kullanmak zorunda değilsin

<GameScene zoom="3" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/many_to_many_pipe.snbt" />
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Birden Fazla Yere Tedarik Etme

Tüm bunlardan, malzemeleri bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> içinden bir makine dizisi veya bir makinenin birkaç farklı yüzü gibi
birçok farklı konuma göndermenin bir yöntemini çıkarabiliriz.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/fluid_interface_storage.snbt" />
  <BoxAnnotation min="2.7 0 1" max="3 1 2" color="#dddddd" thickness="1">
    Arayüz (düz olmalı, tam blok değil)
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 4" color="#dddddd" thickness="1">
    Depolama Veriyolları
  </BoxAnnotation>
  <BoxAnnotation min="0 0 0" max="1 1 4" color="#dddddd" thickness="1">
    Kalıpla tedarik etmek istediğin yerler (birden fazla makine veya 1 makinenin birden fazla yüzü)
  </BoxAnnotation>
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>