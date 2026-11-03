---
item_ids:
  - gregtech:gt.blockmachines:31087
navigation:
  title: Buharlı Ocak
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31087
  position: 1
quest_ids:
  - AAAAAAAAAAAAAAAAAAADZg
---

# Buharlı Ocak

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" />, Buhar çağında kullanılabilen bir Multiblok fırındır. Eşyaları partiler hâlinde eritmek için buhar kullanır ve aynı tarifin sekiz kopyasına kadarını tek seferde işler. Eritme (Blasting) ve Tütsüleme (Smoking) modları, uygun metal ve yemek tariflerini ayrıca hızlandırabilir.

Buharlı Ocak'ın, aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Elektrik gücü tüketmez, ancak kazanın sürekli buhar sağlaması gerekir.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi bir Yüksek Basınçlı Buhar Fırını ve diğer materyalleri gerektirir |
| Boyutlar | 3×3×3, kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| İşleme modları | Fırın, Eritme (Blasting) ve Tütsüleme (Smoking); kabul edilen eşyalar seçili tarif haritasına bağlıdır |
| Paralel işlem | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı artırmaz |
| İşleme avantajları | Fırın modunda temel yapı, tek blok bronz Buhar Fırını'nın hızının %125'inde ve paralel başına buhar tüketim oranının %62,5'inde çalışır |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim oranını Çift katına çıkarır; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31087" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı bronz bileşenler kullanır, yüksek basınçlı yapı ise bunların çelik karşılıklarını kullanır. **Dört yapı bileşeni türünün tümü aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda altı adet; alt ve orta katmanlardaki kasa konumları aşağıdaki kapaklar veya yollar ile değiştirilebilir, ancak en az iki gerçek kasa kalmalıdır |
| Dişli Kutusu | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Dört adet, üst katmanın her kenarının ortasında |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Dört adet, alt katmanın her kenarının ortasında |
| Külhan | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Üç adet, orta katmanın sol, sağ ve arka kenarlarının ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |

Kasa veya kapak için dokuz konum vardır. Gerekli üç arayüzü kurmak altı kasa Yaprakları bırakır. Her ek yol bir kasa daha değiştirir. Kapaklar Dişli Kutuları, Boru Muhafazaları veya Külhanların yerine geçemez.

### Katman Katman İnşa

Önce alt katmanı, ardından kontrolcüyü içeren orta katmanı ve son olarak üstteki dört Dişli Kutusunu inşa et. Önizlemedeki boş konumların kasalarla doldurulması gerekmez. Yapı ne cam ne de Isıtma Bobinleri gerektirir.

Kolay boru bağlantıları için Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını uygun kasa konumlarına yerleştir. Sıradan elektrikli makine Giriş ve Çıkış Yolları buharlı sürümlerin yerine geçemez. Bakım ve Egzoz Çıkışı gerekmez.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademe 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Destekli inşanın ardından kapakları yerleştir ve yapıyı kontrol et.

## Kullanım ve İşleme Modları

Buharlı Ocak, fırın tariflerini toplu olarak işleyebilir; taş, cam, doğrudan eritilen materyaller ve pişmiş yemek gibi eşyalar üretir. Farklı girdiler farklı ürünler verebilir. Erirmeden önce, özellikle cevher işleme zincirinden gelen ara ürünleri kullanmadan önce NEI'yi kontrol et.

Modları **Fırın → Eritme (Blasting) → Tütsüleme (Smoking) → Fırın** sırasında geçirmek için kontrolcüye <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> ile sağ tıkla. GUI'deki mod düğmesini de kullanabilirsin. Waila ve kontrolcü arayüzü mevcut modu gösterir.

| Mod | Kabul edilen tarifler | Aynı yapı kademesindeki Fırın moduna göre değişim |
| --- | --- | --- |
| Fırın | Sıradan fırın tarifleri | Temel hız ve buhar tüketim oranı |
| Eritme (Blasting) | Et Futurum Yüksek Fırını'nın kabul ettiği metal tarifleri | Çift hız ve buhar tüketim oranı |
| Tütsüleme (Smoking) | Et Futurum Tütsüleyicisi'nin kabul ettiği yemek tarifleri | Çift hız ve buhar tüketim oranı |

Eritme ve Tütsüleme yalnızca kendi tarif haritalarındaki eşyaları işler; otomatik olarak Fırın moduna geri dönmezler. Fırın tarifi olan bir eşya işlenmiyorsa önce seçili modu kontrol et. Yalnızca metal veya yemek eşyası olmak, özel modda bir tarifi olduğunu garanti etmez.

> [!NOTE]
> Buradaki Eritme, Minecraft 1.14+ ile gelen Yüksek Fırın işlemesine karşılık gelir. Bir [Elektrikli Yüksek Fırın](../lv/electric_blast_furnace.md) veya Tuğla Yüksek Fırın'ın yerini alamaz. Isı veya Isıtma Bobini mekaniği yoktur ve Eritme'yi seçmek Elektrikli Yüksek Fırın tariflerini aktifleştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı ile buharlı Giriş ve Çıkış Yollarının takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. Girdi için uygun modu seç ve Çıkış Yolunda boş yer bırak.
4. Makineyi aktifleştir ve az miktarda malzeme ver. Ürünleri ve depolanan buharı izle.
5. Malzeme girdisini ve paralel sayısını artırmadan önce sürekli buhar beslemesini doğrula.

## Buhar Beslemesi ve İşlem Kapasitesi

Buharlı Ocak aynı anda **aynı tarifin** en fazla sekiz kopyasını işler. Bir döngüde sekiz farklı eşyayı birlikte işlemez. Gerçek paralel sayısı ayrıca malzeme miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Fırın modunda temel yapı, tek blok bronz Buhar Fırını'nın hızının %125'inde çalışır ve süresinin yaklaşık %80'ini alır. Paralel başına buhar tüketim oranı, o fırının oranının %62,5'idir. Bu avantajların birleşmesi, aynı eşya için toplam buhar tüketiminin yaklaşık %50'sini verir. Birden fazla paralel çalıştırmak yine de makinenin anlık buhar talebini artırır.

Aşağıdaki karşılaştırma, temel olarak **Fırın modundaki temel yapıyı ve aynı paralel sayısını** kullanır:

| Yapı ve mod | İşleme hızı | Buhar tüketim oranı |
| --- | --- | --- |
| Temel yapı, Fırın | 1× | 1× |
| Temel yapı, Eritme veya Tütsüleme | 2× | 2× |
| Yüksek basınçlı yapı, Fırın | 2× | 2× |
| Yüksek basınçlı yapı, Eritme veya Tütsüleme | 4× | 4× |

Mod ve yüksek basınç avantajları birleşir. İkisi de hızı ve buhar tüketim oranını birlikte artırır, esas olarak işlem kapasitesini iyileştirir. Eşya başına tüketilen toplam buharı tekrar yarıya indirmezler. Gerçek süre ve tüketim tick ve tam sayı yuvarlamasından da etkilenir.

Kazanları ve boruları yalnızca Buhar Kapağının 64.000 L kapasitesine güvenmek yerine **çalışma sırasındaki buhar tüketim oranına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim oranını görmek ve sürekli işleme boyunca depolanan buharın düşmeye devam edip etmediğini izlemek için Waila kullan. Bir arayüz L/t kullanıyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru kapasitesini karşılaştırırken aynı birimleri kullan. Besleme yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini genişlet veya boruları iyileştir.

> [!WARNING]
> İşleme sırasında buharın bitmesi, tüketilen malzemeleri geri vermeden mevcut işlemi iptal eder. Yüksek basınca yükseltmeden veya daha hızlı bir mod seçmeden önce buhar üretimini ve boru kapasitesini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. Ancak **tüm Bronz Kaplamalı Tuğlalar, Bronz Dişli Kutuları, Bronz Boru Muhafazaları ve Bronz Külhanlar tablodaki çelik karşılıklarıyla değiştirilmelidir**. Yalnızca kasaları veya Külhanları değiştirmek ya da iki kademeden bileşenleri karıştırmak kademe kontrolünü başarısız kılar.

Yükseltmeden önce işlemeyi ve malzeme girdisini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınç kademesini bildirdiğini doğrula.

Yüksek basınç ayrı bir buhar sıvısı değil, bir yapı kademesidir. Makine yine sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı yollar yeniden kullanılabilir. Elektrikli Enerji Kapağı gerekmez. Yükseltme hızı ve buhar tüketim oranını Çift katına çıkarır, maksimum ise sekiz paralel olarak kalır.

## Otomasyon ve Sıralama

Buharlı Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Yanlarındaki sandıklardan malzemeleri otomatik olarak çekmez veya ürünleri onlara itmez. Bir yolun yanına sandık koymak taşımayı otomatikleştirmez.

- **Girdi:** Eşyaları Giriş Yolunun ön yüzünden vermek için huniler, GT Eşya Boruları, Konveyör Modülleri, Eşya Kanalları veya benzeri ekipman kullan.
- **Çıktı:** Borular, kanallar veya Konveyör Modülleri ile Çıkış Yolunun ön yüzünden aktif olarak çek ve ürünleri depolamaya veya bir sonraki makineye gönder.
- **Buhar:** Kazan çıktısını Buhar Kapağına ulaştırmak için sıvı boruları kullan. Eşya yolları buhar alamaz.
- **Sıralama:** Amaçlanan malzemeler için taşıma ekipmanını filtrele, böylece mevcut modun işleyemeyeceği eşyalar giriş yuvalarını doldurmaz.

Metalleri, yemekleri ve diğer materyalleri sık sık aynı anda işlemen gerekiyorsa ayrı makineler kullan veya malzeme değiştirirken modu değiştir. Daha fazla Giriş Yolu eşya tamponunu artırır ancak paralel sınırını yükseltmez. Daha fazla Çıkış Yolu çıktı tıkanıklıklarını azaltabilir.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yapı | Kontrolcü ikinci katmanın ön ortasında mı; dört Dişli Kutusu, dört Boru Muhafazası ve üç Külhanın konumları doğru mu |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutuları, Boru Muhafazaları ve Külhanların tümü aynı kademede olmalı; yükseltmeden sonra kalan bronz bileşenleri kontrol et |
| Eksik Buhar Kapağı veya yol | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş ve Çıkış Yolu; yanlış kapak türlerini kontrol et |
| Yol ekledikten sonra yapı bozuluyor | En az iki gerçek kasa kalmalı; yollar Dişli Kutuları, Boru Muhafazaları veya Külhanların yerine geçemez |
| Malzemeler var ama tarif bulunamıyor | Doğru mod, eşyanın o modda geçerli bir tarifi ve yeterli çıktı alanı |
| Depolanan buhara rağmen başladıktan sonra duruyor | Yeterli sürekli besleme, boru kısıtlamaları veya paylaşılan besleme ve paralel sayısı, yüksek basınç kademesi ya da daha hızlı modun kazan kapasitesini aşıp aşmadığı |
| Yolun yanındaki sandık eşya taşımıyor | Buharlı yollar eşyaları otomatik çekmez veya itmez; aktif taşıma ekipmanını, bağlantı yüzlerini, yönlerini ve filtreleri kontrol et |
| Sekizden az tarif işleniyor | Aynı tarif için yeterli malzeme, GUI paralel sınırı ve tüm ürünler için çıktı alanı |
| Yükseltmeden sonra buhar tüketimi artıyor | Yüksek basınç tüketim oranını Çift katına çıkarır ve Eritme veya Tütsüleme bunu tekrar Çift katına çıkarabilir; buhar beslemesini buna göre artır |

Genel yapı kontrolleri ve araç kullanımı için [Multibloklar Makineleri](../multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Steam Hearth](https://wiki.gtnewhorizons.com/wiki/Steam_Hearth)