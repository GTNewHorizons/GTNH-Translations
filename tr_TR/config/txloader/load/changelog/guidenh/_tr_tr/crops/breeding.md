---
navigation:
  title: Bitki Islahı
  parent: crops.md
  icon: cropsnh:genericSeed
categories:
    - crops
author: Skorched
date: 2026-05-20
---

# Bitki Islahı
Vanilya tohumunu bitki çubuklarına dikerek elde edilebilecek tohum sayısı sınırlıdır. Başka tohumlar üretmenin üç ana yolu vardır ve bunlar bu bölümde ele alınacaktır. "Dünyada" gerçekleşen ıslah yöntemlerinde, bitkinin [yayılma](spreading.md) veya (geçerli bir ıslah düzeni varsayıldığında) ıslah olma şansı 50/50'dir.

## Deterministik Islah
<FloatingImage src="../assets/crops/determine.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    Deterministik bir ıslah örneği
  </ImageAnnotation>
</FloatingImage>
Deterministik ıslah, hedef tohumun bir tür "tarifi" olduğu durumdur. Bu durumda, tarifin gerektirdiği şekilde iki olgun bitki yerleştir ve merkezde hedef bitki için geçerli büyüme koşullarına sahip çift bitki çubuğu bulundur. Geçerli bir deterministik ıslah durumu varsa yeni bitki her zaman ebeveynlerden birinin yayılmış bitkisi veya hedef bitki olur. Havuz mutasyonları gerçekleşmez.
<br clear="all">

## Havuz Islahı
<FloatingImage src="../assets/crops/pools.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    Bir Bitki Mutasyon Havuzu örneği
  </ImageAnnotation>
</FloatingImage>

Bitkilerin çoğunda temel tohumun ıslahı <Color id="GREEN">Havuz Islahı</Color> ile yapılır. Taranmış herhangi bir bitkinin kullanımlarında arama yaparak burada gösterilen sayfayı bulabilirsin; bu sayfa tohumun ait olduğu tüm "havuzları" gösterir. Bu şekilde üretilecek herhangi bir hedef bitki için, hedef bitkiyle aynı havuzdan iki olgun ebeveyni iki yana yerleştirmeli ve deterministik ıslahtaki aynı temel kurulum adımlarını izlemelisin. Doğru planlama yapılmazsa geçerli "çıktı" bitkileri havuzu istediğin bitkiden daha büyük olacağından bu genellikle çok daha az "kesin" bir yöntemdir.
<br clear="all">

## Bitki Islah Makinesi
Daha gelişmiş bitkiler için bir <Color id="BLUE">Bitki Islah Makinesi</Color> <ItemImage id="gregtech:gt.blockmachines:28025" /> kullanmalısın. Bunların çıktıları tamamen deterministiktir, ancak kullanılan makinenin gerilim kademesine bağlı olarak çıktıları yok etme şansı vardır; LV'de %40 başarıyla başlar ve ZPM+ ile %100 olur.

Bitki ıslah makinelerindeki tüm tarifler bir dizi girdi (çoğu zaman yalnızca iki tohum, ancak daha fazla olabilir) ve bir miktar <Color id="GREEN">Zenginleştirilmiş Gübre</Color> alır. Bunun tarifi biraz yanıltıcı olabilir, çünkü hem kademeye hem de çıktı tohumunun istatistiklerine bağlıdır.

Örnek olarak bir <Color id="RED">Bauxia Tohumu</Color> üretmeye çalıştığımızı varsayalım. NEI'de belirtilen tarif Galvania Tohumu + Nickelback Tohumu + Boksit Cevheri + <Color id="GREEN">7560L Zenginleştirilmiş Gübre</Color> şeklindedir.

Gerçek gübre miktarı, aşağıda gösterildiği gibi girdinin istatistiklerine bağlı olarak büyük ölçüde değişebilir:
- 1/1/1 girdiler: <Latex formula="\text{Fertilizer} = 6 \times 144 + (1 + 1 + 1) \times 72 = 1080L" />
- 31/31/31 girdiler: <Latex formula="\text{Fertilizer} = 6 \times 144 + (31 + 31 + 31) \times 72 = 7560L" />

Bu, örneğin bir MV Bitki Islah Makinesinin giriş sıvı yuvasında yalnızca 6.400L depolayabildiğini düşünürsen özellikle önemlidir.

Bu nedenle bu özel amaç için tohumların istatistiklerini "düşürmek" gerekebilir.