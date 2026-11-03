---
navigation:
  title: Kanallar
  parent: /ae2_mechanics_index.md
  icon: appliedenergistics2:item.ItemMultiPart:56
---

# Kanallar

## Kanallar Nedir?

Kanallar, bir AE2 [ME Ağı](me_network_connections.md) içindeki cihazlar tarafından tüketilen bir kaynaktır. Bir ME ağı, ağa bağlı depolama ve diğer ağ hizmetleri sağlayan [cihazları](devices.md) desteklemek için kanalları kullanır. Kablolarda kullanılabilir kanal sayısı sınırlıdır: her kablo yalnızca belirli sayıda kanal taşıyabilir. Kanal kullanan bir cihazı kabloyla ağa bağladığında, o cihaz kabloda bir kanal kaplar. Kablo kanallarını tükettiğinde, yeni eklenen cihazlar artık ME ağına bağlanamaz.

<GameScene zoom="4" showBackground={false} width="300" rotateX={20} rotateY={-75}>
  <ImportStructure src="../assets/structures/channels_channel_count.snbt" />
  <LineAnnotation
  points="0.35 0.65 5; 0.35 0.65 4.5;0.35 1.5 4.5"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.35 0.5 5; 0.35 0.5 3.5;0.35 1.5 3.5"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.35 0.35 5; 0.35 0.35 2.5;0.35 1.5 2.5"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.65 0.35 5; 0.65 0.35 4.65;2.5 0.35 4.65"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.65 0.65 5; 0.65 0.65 4.65;1.5 0.65 4.65"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.65 0.35 5; 0.65 0.35 4.35;2.5 0.35 4.35"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.65 0.65 5; 0.65 0.65 4.35;1.5 0.65 4.35"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.5 5; 0.5 0.5 4.5;2.5 0.5 4.5"
  color="#00ff00"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.55 5;0.5 0.55 4.6"
  color="#ff0000"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.55 4.4;0.5 0.55 4"
  color="#ff0000"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.55 3.6;0.5 0.55 3.2"
  color="#ff0000"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.55 2.8;0.5 0.55 2.4"
  color="#ff0000"
  thickness="1"
  alwaysOnTop={true}>
  </LineAnnotation>
  <LineAnnotation
  points="0.5 0.55 2;0.5 0.55 0.5"
  color="#ff0000"
  thickness="1"
  alwaysOnTop={true}>
  Kablodaki 8 kanalın tamamı kullanıldığı için Sürücü kanal alamıyor. 
  </LineAnnotation>
  <DiamondAnnotation pos="0.5 0.55 2" color="#ff0000">
    Kablodaki 8 kanalın tamamı kullanıldığı için Sürücü kanal alamıyor. 
  </DiamondAnnotation>
</GameScene>

Normal kablolar 8 kanal taşıyabilirken kalın kablolar 32 kanal taşıyabilir. Kanal kullanımını gözlemlemenin kolay bir yolu, kanal kullanımını dokuları ve ışıklarıyla gösteren [Akıllı Kabloları](../items_blocks/cables.md#Smart Cable) kullanmaktır.


# Kanal Yönlendirmesi

Bir <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> içeren ME ağında kanallar üç adımda yönlendirilir:

1. Kanal, bitişik cihazdan en yakın normal kabloya en kısa yolu izler; bu kablo Cam Kablo, Kaplamalı Kablo veya Akıllı Kablo olabilir.
2. Ardından o normal kablo boyunca en yakın kalın kabloya devam eder.
3. Son olarak o kalın kablo boyunca ME Kontrolcüsüne gider.

En kısa yol zaten doluysa bazı cihazlar ihtiyaç duydukları kanalları alamayabilir.

Kanalları istediğin yoldan gitmeye zorlamak için kablo renklendirmesini, <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" showIcon="left"/>, ve <ItemImage id="appliedenergistics2:item.ItemMultiPart:120" yOffset="2" /><ItemLink id="appliedenergistics2:item.ItemMultiPart:120"/> kullanabilirsin. Renk, kanal önceliğini etkilemez. Yalnızca farklı renkteki kabloların birbirine bağlanmasını engeller; bu da kanal yönlendirmesini kontrol etmeye yardımcı olur.

> [!NOTE]
> Renksiz (Fluix) kablolar her renkteki kabloya bağlanabilir.

Örneğin aşağıdaki düzenekte kablolar bir döngü oluşturur. Kanallar her zaman en kısa yolu kullanmaya çalıştığından bazı Sürücüler kanal kaybedip çevrimdışı olur.

<GameScene zoom="2" showBackground={false} width="200" rotateX={90} rotateY={-90}>
    <ImportStructure src="../assets/structures/channels_channel_loop1.snbt" />
</GameScene>

Bu, kanal yollarını kablo renkleri, Kuvars Fiber ve Kablo Çapalarıyla dikkatlice sınırlandırarak düzeltilebilir. Ağ yapıları olabildiğince az döngü ve belirsiz örgü yolu içeren ağaç benzeri yapılar olmalıdır.

<GameScene zoom="2" showBackground={false} width="200" rotateX={90} rotateY={-90}>
    <ImportStructure src="../assets/structures/channels_channel_loop2.snbt" />
</GameScene>


# Ağ Tasarımı

Yukarıda açıklandığı gibi ME ağları dallanan ağaçlar olarak tasarlanmalıdır. Kanalları kontrolcüden dışarı taşıyan ana gövde olarak kalın kablolar kullan, ardından cihazları beslemek için kalın hattan normal kablolar ayır. Her normal kablo grubu en fazla 8 cihaza hizmet etmelidir. Daha fazlasına ihtiyacın varsa kalın kablodan başka bir normal kablo dalı ayır.

Aşağıda <Color id="RED">kötü yapılandırılmış</Color> bir ağ örneği var. Döngülerle doludur: kablolar döngüler oluşturur ve cihazlar arasında doğrudan kanal aktarımı da döngüler yaratır. Sonuç, okunması ve çözümlenmesi zor olan ve kanal alamadıkları için bazı bileşenleri muhtemelen çevrimdışı bırakan bir ağdır.

<GameScene zoom="4" showBackground={false} width="400" rotateX={30} rotateY={100}>
    <ImportStructure src="../assets/structures/channels_bad_design.snbt" />
</GameScene>

İşte <Color id="GREEN">iyi yapılandırılmış</Color> bir ağ örneği:
<GameScene zoom="2" showBackground={false} width="400" rotateY={-115} rotateX={30}>
    <ImportStructure src="../assets/structures/channels_good_design.snbt" />
    <BoxAnnotation min="11 0 8" max="13 1 5" color="#00ff1a" thickness="1">
      Bölümleri ayırmak için farklı kablo renkleri kullan; böylece daha kolay tanımlanır ve yanlışlıkla bağlanma olasılıkları azalır.
    </BoxAnnotation>
    <BoxAnnotation min="5 0 4" max="3 4 6" color="#00ff1a" thickness="1">
      Bu normal kablo 8 Arayüz için tam olarak 8 kanal taşıyor. Burada kanal sıkıntısı da atık da yok çünkü Moleküler Birleştiricilerin kendisi kanal kullanmaz.
    </BoxAnnotation>
</GameScene>

# Ad-Hoc Ağlar

Bir <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> olmayan ağ ad-hoc bir ağdır. Kanal kullanan en fazla 8 cihazı destekleyebilir. 8 cihazı aşarsan yalnızca fazladan cihazların çevrimdışı olması yerine tüm ağ çöker. Bu noktada ya bazı cihazları kaldırmalı ya da bir ME Kontrolcüsü eklemelisin.

Normal kontrolcü tabanlı bir ağdan farklı olarak, ad-hoc ağdaki Akıllı Kablolar o belirli kablodan geçen kanal sayısını değil, tüm ağda kullanılan toplam kanal sayısını gösterir.

Pratikte ad-hoc ağdaki her cihaz, tüm ağdaki her kabloda bir kanal kaplar. Bu, bir ME Kontrolcüsünün kanalları en kısa yola göre ayırmasından tamamen farklıdır. Başka bir deyişle, kullanılan tüm kanallar tüm ad-hoc ağa eşit şekilde yayılır ve yönlendirilmiş bir kanal yolu kavramı gerçekte yoktur.

<FloatingImage src="../assets/images/channels_normal_network.png"  wrap="top-bottom" align="left"  displayWidth="300" title="Normal Ağ" >
  <ImageAnnotation>
  Normal Ağ
  </ImageAnnotation>
</FloatingImage>
<FloatingImage src="../assets/images/channels_ad_hoc_network.png"  wrap="top-bottom" align="left"  displayWidth="300" title="Ad-Hoc Ağ" >
  <ImageAnnotation>
  Ad-Hoc Ağ
  </ImageAnnotation>
</FloatingImage>