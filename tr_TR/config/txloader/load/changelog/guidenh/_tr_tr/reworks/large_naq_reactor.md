---
item_ids:
  - gregtech:gt.blockmachines:15537
navigation:
  title: Büyük Naquadah Reaktörü
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15537
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Naquadah Reaktörü

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15537"/>
</GameScene>
<Color id="GREEN">Büyük Naquadah Reaktörü (LNR)</Color>, naquadah bazlı sıvı yakıtlardan güç üreten ZPM kademesi bir multibloktur. <Color id="GREEN">LNR</Color> yakıtı doğrudan EU'ya dönüştürür, ısınma süresi yoktur ve türbin kullanmaz. Tek zorluk giriş gereksinimlerini karşılamaktır: Girdi kapaklarında herhangi bir anda YALNIZCA TEK tür yakıt olabilir ve güç çıkışı için <Color id="GREEN">LNR</Color>'ye 2.400 L/s sıvı hava beslenmelidir. İsteğe bağlı olarak makinenin verimliliğini artırmak için bir soğutucu ve/veya makinenin genel verimini artırmak için uyarılmış bir sıvı besleyebilirsin. Tek bir <Color id="GREEN">LNR</Color>, (en yüksek kademe sıvılarla) 665B EU/t'ye kadar üretebilir; bu da daha yüksek gerilim kademelerine çok iyi ölçeklendiği anlamına gelir. <Color id="GREEN">LNR</Color>'nin yerini Dyson Sürüsü Yer Ünitesi <ItemImage id="gregtech:gt.blockmachines:14001"/> veya Yarı Kararlı Antimadde Stabilizasyon Sıralayıcısı (SSASS) <ItemImage id="gregtech:gt.blockmachines:32027"/> alır.

Naquadah bazlı sıvı yakıtın (naq yakıtı) ilk iki kademesi sırasıyla Füzyon Reaktöründe ve Büyük Kimyasal Reaktörde üretilir. Kalan dört kademenin tamamı, yeni tariflerin kilidini açmak için gelişmiş alan kısıtlama bobinleri kullanan [Naquadah Yakıt Rafinerisi](./naq_refinery.md) içinde üretilir. Mk-V yakıtı ayrıca yıldız yakıtı üretmek için kullanılır ve tükenmiş Mk-V ile Mk-VI yakıtları SSASS tarafından aktivasyon stabilizasyonu için kullanılır. Nötron Aktivatörü <ItemImage id="gregtech:gt.blockmachines:32013"/> naq yakıtının bozunmasını önemli ölçüde hızlandırabilir, ancak hiç güç üretmez.

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Bu multiblokun yalnızca yapısı değişti, mekanikler aynı kalıyor

## İnşa
<Color id="GREEN">LNR</Color>'nin kademeli bileşeni yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir naquadah reaktör kasasının yerini alabilir. Dört farklı giriş sıvısını tutmak için bir stoklama girdi kapağı şiddetle önerilir. Ciddi güç üretimi için çok amperli ve lazer dinamo kapakları desteklenir, ancak birden fazla olamaz. Dinamo kapağı mevcut güç çıkışının %100'ünü destekleyemezse <Color id="GREEN">LNR</Color> kapanır, bu yüzden yüksek amperli bir lazer dinamo kapağı kullanmak neredeyse zorunludur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15537"/><ItemImage id="gregtech:gt.blockmachines:15537"/>
- 130-141 <ItemLink id="gregtech:gt.blockcasings13:15"/><ItemImage id="gregtech:gt.blockcasings13:15"/>
- 81 <ItemLink id="GoodGenerator:MAR_Casing"/><ItemImage id="GoodGenerator:MAR_Casing"/>
- 32 <ItemLink id="GoodGenerator:radiationProtectionSteelFrame"/><ItemImage id="GoodGenerator:radiationProtectionSteelFrame"/>
- 1 Dinamo Kapağı (herhangi bir reaktör kasası) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir reaktör kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Girdi Kapağı (herhangi bir reaktör kasası) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (herhangi bir reaktör kasası) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<FloatingImage src="../assets/reworks/lnr_wallshare.png" displayWidth="128" align="right">
  <ImageAnnotation>
    Duvar paylaşımlı çift reaktör örneği
  </ImageAnnotation>
</FloatingImage>
<Color id="GREEN">LNR</Color>, kasa, çerçeve kutusu ve veriyolu/kapak tasarrufu yapmak için her bir yanını veya yapının merkezindeki küreyi duvar paylaşımıyla kullanabilir. Buna, aynı anda 2-4 makineyi destekleyecek kadar verim varsa lazer dinamo kapağı da dahildir. Yukarıdaki görsel iki makineyi gösterir, ancak istenirse kalan eksene üçüncü bir makine yerleştirilebilir (lazer aynası gerektirir).

## Kullanım
Diğer jeneratör multibloklarına kıyasla <Color id="GREEN">LNR</Color>'yi kullanmak çok basittir. <Color id="GREEN">LNR</Color> yakıtı doğrudan EU'ya dönüştürür, ısınma süresi yoktur ve türbin kullanmaz. Tek zorluk aşağıdaki giriş gereksinimlerini karşılamaktır:

- Girdi kapaklarında herhangi bir anda YALNIZCA BİR tür yakıt olabilir, aksi halde makine PATLAR.
- Güç çıkışı için <Color id="GREEN">LNR</Color>'ye 2.400 L/s sıvı hava beslenmelidir, aksi halde yakıt yok edilir.
- Dinamo kapağı mevcut güç çıkışının %100'ünü destekleyecek kadar büyük olmalıdır, aksi halde makine kapanır.

## Soğutucu
İsteğe bağlı olarak <Color id="GREEN">LNR</Color>'nin verimliliğini artırmak için bir soğutucu sağlanabilir. Aşağıdaki sıvıların her biri, yakıt tüketim oranını artırmadan veya tarifin süresini kısaltmadan mevcut EU/t'yi çarpar. Soğutucu kesinlikle makineye fayda sağlar. Üst üste binmedikleri için birden fazla soğutucu türü olamaz.

| Soğutucu | Verimlilik | Miktar |
| --------------- | --------------- | --------------- |
| IC2 Soğutucu | %105 | 1.000 L/s |
| Süper Soğutucu | %150 | 1.000 L/s |
| Kriyotheum | %275 | 1.000 L/s |
| Takyon Zengin Zamansal Sıvı | %500 | 20 L/s |

## Güçlendirici
İsteğe bağlı olarak <Color id="GREEN">LNR</Color>'nin verimini artırmak için bir güçlendirici sağlanabilir. Aşağıdaki sıvıların her biri, paralellere benzer şekilde mevcut EU/t'yi ve tüketilen yakıt miktarını çarpar. Bu, oksijen veya soğutucu tüketimini artırmaz. Güçlendiriciler kesinlikle fazladan makine yığmaktan tasarruf sağlar. Üst üste binmedikleri için birden fazla güçlendirici türü olamaz.

| Güçlendirici | Çarpan | Miktar |
| --------------- | --------------- | --------------- |
| Eriyik Sezyum | 2x | 180 L/s |
| Eriyik Uranyum-235 | 3x | 180 L/s |
| Eriyik Naquadah | 4x | 20 L/s |
| Eriyik Atomik Ayrıştırma Katalizörü | 16x | 20 L/s |
| Uzamsal Olarak Genişletilmiş Sıvı | 64x | 20 L/s |