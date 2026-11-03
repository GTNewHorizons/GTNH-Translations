---
item_ids:
  - gregtech:gt.blockmachines:15559
navigation:
  title: Gezegen Gaz Sifonu
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15559
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Gezegen Gaz Sifonu
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15559"/>
</GameScene>
<Color id="GREEN">Gezegen Gaz Sifonu (PGS)</Color>, Jüpiter, Satürn, Uranüs ve Neptün gaz devlerinden sonsuz miktarda gaz toplamak için IV kademe bir multibloğdur. <Color id="GREEN">PGS</Color>, gezegenlerin yüzeyinin çok üzerindeki bir uzay istasyonundan çalışması dışında bir Sıvı Sondaj Kulesine <ItemImage id="gregtech:gt.blockmachines:149"/> benzer. Her gaz devinde dört farklı gaz vardır, ancak aynı anda yalnızca biri çıkarılabilir. <ItemImage id="gregtech:gt.blockmachines:149"/> derinliğini ve dolayısıyla hangi gazın çıkarılacağını değiştirmek için giriş yolundaki programlanmış devre değerini ayarla. Isıtma bobinlerini ve/veya enerji kapağını yükselterek makinenin çıkarma oranını (L/s) artır.

<br clear="all"/>

> [!NOTE]
> Multibloğa (yapı dışında) aşağıdaki değişiklikler yapıldı:
> Bobin Kademelendirmesi: Daha yüksek kademeli bobinler kademe başına +%10 hız bonusu verir (toplanır)
> İki Katına Çıkan Temel Hız: Temel işleme hızı eski yapıya göre iki katına çıkarıldı
> WAILA Yükseltmesi: Kontrolcünün üzerine gelmek artık mevcut hız bonusunu ve bobin kademesini gösterir

## İnşa
<Color id="GREEN">PGS</Color>'nin tek kademeli bir bileşeni vardır. Isıtma bobinleri makinenin hız bonusunu belirler. Veriyolları/kapaklar yapının herhangi bir yerindeki sifon kasasının yerine geçebilir, ancak enerji kapağı dahil her birinden tam olarak bir tane olmalıdır. Çok amperli ve lazer enerji kapakları desteklenmez. Giriş yolundaki madencilik boruları kontrolcü tarafından asla tüketilmez veya dünyaya yerleştirilmez, bu yüzden <Color id="GREEN">PGS</Color>'nin aşağıdaki gaz devine doğrudan görüş hattına ihtiyacı yoktur. Isıtma bobinlerinin kademesini belirtmek için "coil" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15559"/><ItemImage id="gregtech:gt.blockmachines:15559"/>
- 184 <ItemLink id="gtnhintergalactic:gassiphoncasing"/><ItemImage id="gtnhintergalactic:gassiphoncasing"/>
- 93 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 12 Isıtma Bobini (Kademeli) <ItemLink id="gregtech:gt.blockcasings5:13"/><ItemImage id="gregtech:gt.blockcasings5:13"/>
- 6 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:88"/><ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:88"/>
- 1 Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
PGS kasa, ısıtma bobini ve veriyolu/kapaktan tasarruf etmek için her bir kenarını duvar paylaşımıyla kullanabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığından <u>__tek__</u> bir enerji kapağı <u>__iki__</u> hatta <u>__dört__</u> makine arasında paylaşılabilir.

## Uzay İstasyonları
<Color id="GREEN">PGS</Color> bir gaz devinin yörüngesindeki bir uzay istasyonunda inşa edilmelidir. <Color id="BLUE">Uzay İstasyonları</Color>, uzaya bir roket fırlatıp bir gezegene tıklayarak ve ekranın sağ tarafında "Buraya bir Uzay İstasyonu oluşturulabilir!" yazan yerdeki CREATE düğmesine basarak inşa edilir. Gaz devlerinin her biri için uzay istasyonu maliyeti aşağıda listelenmiştir. Oyuncunun düğmeye basabilmesi için gerekli materyalleri envanterinde (sırt çantasında veya sıkıştırılmış sandıkta değil) bulundurması gerekir. Uzay istasyonu daha sonra Galaksi Haritasında gezegenin yörüngesinde, bir ay gibi bir uydu olarak görünür.

- Jüpiter - 1 EV Makine Gövdesi, 4 EV Devresi, 6 Cam Panel, 231 Dekoratif Nikel Bloğu
- Satürn - 1 LuV Makine Gövdesi, 4 LuV Devresi, 6 Cam Panel, 231 Dekoratif Mithril Bloğu
- Uranüs - 1 LuV Makine Gövdesi, 4 LuV Devresi, 6 Cam Panel, 231 Dekoratif Tungsten Bloğu
- Neptün - 1 ZPM Makine Gövdesi, 4 ZPM Devresi, 6 Cam Panel, 231 Dekoratif Adamantit Bloğu

NEI'de veya Galaksi Haritasında görünmese de her gaz deviyle ilişkili bir kademe vardır. Roketlerinin kademesi çok düşükse oyuncu, herhangi bir roketle uzay istasyonu oluşturabilmesine rağmen bir gaz devinin uzay istasyonunu göremez veya oraya gidemez.

<Color id="BLUE">Uzay İstasyonları</Color> başlangıçta çok küçüktür ve son derece garip bir yerçekimi etkisine sahiptir. Ancak oyuncu onları istediği kadar büyütebilir ve uzaya uçup gitmemek için birkaç duvar/çatı inşa edebilir. Uzay istasyonlarında oksijen de yoktur, bu yüzden birkaç yedek oksijen tüpü veya daha kalıcı bir çözüm için bir oksijen toplayıcı ve oksijen kompresörü getir. Bir uzay istasyonundan ayrılmak için fırlatma rampasından roket fırlat. Dolu bir roket gidiş-dönüş uçuşu için fazlasıyla yeterli yakıta sahiptir, ancak her ihtimale karşı bir yakıt yükleyici ve biraz ekstra roket yakıtı getirmek fena fikir olmayabilir.

## Kullanım
<Color id="GREEN">PGS</Color>, Jüpiter, Satürn, Uranüs ve Neptün gaz devlerinden sonsuz miktarda gaz toplar. Ancak aynı anda yalnızca bir gaz toplayabilir, her gaz için minimum bir gerilim kademesi vardır ve overclock yalnızca enerji kapağının kendisi yükseltilerek yapılabilir. <Color id="GREEN">PGS</Color>'nin derinliğini ve dolayısıyla gaz devinden hangi gazın çıkarılacağını değiştirmek için giriş yolundaki programlanmış devre değerini ayarla.

Derinlik ayrıca makinenin girdilerini de belirler. Giriş yolunda gereken madencilik borusu sayısı $$\text{Depth} \times 64$$ ve temel EU/t $$\text{Depth} \times 4^{T+2}$$; burada $$T$$ gaz devinin kademesidir. Örneğin Jüpiter'de helyum pompalamak 128 madencilik borusu gerektirir ve temel güç tüketimi 2.048 EU/t yani 1A EV'dir. Overclock'lar gerilimden bağımsız olarak amper sayısını her zaman aynı tutar.

Gazın çıkarılma oranı (L/s), aşağıdaki tablolarda görüldüğü gibi gaz devine, gaz türüne ve mevcut güce bağlıdır. <Color id="GREEN">PGS</Color> %200 hızda çalışır ve ısıtma bobini kademesi başına +%10 hız bonusu kazanır, ancak ikincisi listelenen oranlara DAHİL DEĞİLDİR.

| Isıtma Bobini   | Hız    |
|--------------- | --------------- |
| Bakır-Nikel   | %210   |
| Kantal   | %220   |
| Nikrom   | %230   |
| TPV-Alaşım   | %240   |
| HSS-G   | %250   |
| HSS-S   | %260    |
| Naquadah   | %270   |
| Naquadah Alaşımı   | %280   |
| Trinyum   | %290   |
| Yüklenmiş Elektrum   | %300   |
| Uyandırılmış Drakonyum   | %310   |
| Sonsuzluk   | %320   |
| Hipojen   | %330   |
| Ebedi   | %340   |