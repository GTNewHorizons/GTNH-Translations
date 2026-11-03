---
item_ids:
  - gregtech:gt.blockmachines:31087
quest_ids:
  - AAAAAAAAAAAAAAAAAAADZg
navigation:
  title: Buhar Ocağı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31087
  position: -501
---
# Buhar Ocağı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok fırındır. Eşyaları partiler halinde eritmek için buhar kullanır ve aynı tarifin aynı anda en fazla sekiz kopyasını işler. Patlatma ve Tütsüleme modları, uygun metal ve yemek tariflerini ayrıca hızlandırabilir.

Buhar Ocağının aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Elektrik gücü tüketmez, ancak kazanın sürekli buhar sağlaması gerekir.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | Buhar; kontrolcü tarifi bir Yüksek Basınçlı Buhar Fırını ve diğer malzemeler gerektirir |
| Boyutlar | 3×3×3; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| İşleme modları | Fırın, Patlatma ve Tütsüleme; kabul edilen eşyalar seçilen tarif haritasına bağlıdır |
| Paraleller | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı artırmaz |
| İşleme bonusları | Fırın modunda temel yapı, tek bloklu bronz Buhar Fırınının hızının %125'inde ve paralel başına buhar tüketim hızının %62,5'inde çalışır |
| Yükseltmeler ve overclock | Yüksek basınçlı yapı hızı ve buhar tüketim hızını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31087" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı bronz bileşenleri, yüksek basınçlı yapı ise bunların çelik karşılıklarını kullanır. **Dört yapı bileşeninin tümü de aynı kademeden olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda altı; alt ve orta katmanlardaki kasa konumları aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az iki gerçek kasa kalmalıdır |
| Dişli Kutusu | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Dört; üst katmanın her kenarının ortasında |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Dört; alt katmanın her kenarının ortasında |
| Külhan | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Üç; orta katmanın sol, sağ ve arka yüzlerinin ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" /> | Aynı kontrolcü | Bir; ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir; bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir; bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir; bir kasanın yerine |

Kasa veya kapak için dokuz konum vardır. Gerekli üç arayüzü kurmak altı kasa bırakır. Eklenen her yol bir kasa daha değiştirir. Kapaklar Dişli Kutusu, Boru Muhafazası veya Külhanın yerini alamaz.

### Katman Katman İnşa

Önce alt katmanı, ardından kontrolcüyü içeren orta katmanı ve son olarak üstteki dört Dişli Kutusunu inşa et. Önizlemedeki boş konumların kasa ile doldurulması gerekmez. Yapı ne cam ne de Isıtma Bobini gerektirir.

Boru bağlantıları için uygun kasa konumlarına Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını yerleştir. Sıradan elektrikli makine Giriş ve Çıkış Yolları buharlı sürümlerin yerini alamaz. Bakım ve Egzoz Çıkışları gerekmez.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Destekli inşadan sonra kapakları tak ve yapıyı kontrol et.

## Kullanımlar ve İşleme Modları

Buhar Ocağı fırın tariflerini toplu halde işleyerek taş, cam, doğrudan eritilmiş malzemeler ve pişmiş yemek gibi eşyalar üretebilir. Farklı girdiler farklı ürünler verebilir. Eritmeden önce, özellikle bir cevher işleme zincirinden gelen ara ürünleri kullanmadan önce NEI'yi kontrol et.

**Fırın → Patlatma → Tütsüleme → Fırın** sırasıyla geçiş yapmak için kontrolcüye bir <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> ile sağ tıkla. GUI'deki mod düğmesini de kullanabilirsin. Waila ve kontrolcü arayüzü geçerli modu gösterir.

| Mod | Kabul edilen tarifler | Aynı yapı kademesindeki Fırın moduna göre değişim |
| --- | --- | --- |
| Fırın | Sıradan fırın tarifleri | Temel hız ve buhar tüketim hızı |
| Patlatma | Et Futurum Patlatma Fırınının kabul ettiği metal tarifleri | İki kat hız ve buhar tüketim hızı |
| Tütsüleme | Et Futurum Tütsücüsünün kabul ettiği yemek tarifleri | İki kat hız ve buhar tüketim hızı |

Patlatma ve Tütsüleme yalnızca kendi tarif haritalarındaki eşyaları işler; otomatik olarak Fırın moduna geri dönmezler. Fırın tarifi olan bir eşya işlenmiyorsa önce seçili modu kontrol et. Tek başına metal veya yemek eşyası olmak, özel modda bir tarif olduğunu garanti etmez.

> [!NOTE]
> Buradaki Patlatma, Minecraft 1.14+ ile gelen Patlatma Fırını işlemesine karşılık gelir. Bir [Elektrikli Yüksek Fırın](./electric_blast_furnace.md) veya Tuğlalı Yüksek Fırının yerini alamaz. Isı veya Isıtma Bobini mekaniği yoktur ve Patlatmayı seçmek Elektrikli Yüksek Fırın tariflerini etkinleştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, buharlı Giriş Yolu ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. Girdi için uygun modu seç ve Çıkış Yolunda yer bırak.
4. Makineyi etkinleştir ve az miktarda malzeme ver. Ürünleri ve depolanan buharı izle.
5. Malzeme girdisini ve paralel sayısını artırmadan önce sürekli buhar sağlandığını doğrula.

## Buhar Beslemesi ve Verim

Buhar Ocağı aynı anda **aynı tarifin** en fazla sekiz kopyasını işler. Tek bir çevrimde sekiz farklı eşyayı birlikte işlemez. Gerçek paralel sayısı ayrıca malzeme miktarlarına, çıkış alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Fırın modunda temel yapı, tek bloklu bronz Buhar Fırınının hızının %125'inde çalışır ve tek bloklu fırının süresinin yaklaşık %80'i kadar sürer. Paralel başına buhar tüketim hızı, o fırının buhar tüketim hızının %62,5'idir. Bu bonuslar birleştiğinde aynı eşya için toplam buhar tüketiminin yaklaşık %50'si elde edilir. Birden fazla paralel çalıştırmak yine de makinenin anlık buhar talebini artırır.

Aşağıdaki karşılaştırma, temel olarak **Fırın modundaki temel yapıyı, aynı paralel sayısıyla** kullanır:

| Yapı ve mod | İşleme hızı | Buhar tüketim hızı |
| --- | --- | --- |
| Temel yapı, Fırın | 1× | 1× |
| Temel yapı, Patlatma veya Tütsüleme | 2× | 2× |
| Yüksek basınçlı yapı, Fırın | 2× | 2× |
| Yüksek basınçlı yapı, Patlatma veya Tütsüleme | 4× | 4× |

Mod ve yüksek basınç bonusları üst üste biner. İkisi de hızı ve buhar tüketim hızını birlikte artırır, esas olarak verimi iyileştirir. Eşya başına tüketilen toplam buharı tekrar yarıya indirmezler. Gerçek süre ve tüketim ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Kazanları ve boruları yalnızca Buhar Kapağının 64.000 L kapasitesine güvenmek yerine **çalışma sırasındaki buhar tüketim hızına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim hızını kontrol etmek ve sürekli işleme sırasında depolanan buharın düşmeye devam edip etmediğini izlemek için Waila kullan. Bir arayüz L/t kullanıyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Besleme yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini genişlet veya boruları iyileştir.

> [!WARNING]
> İşleme sırasında buharın tükenmesi, tüketilen malzemeleri geri vermeden mevcut işlemi iptal eder. Yüksek basınca yükseltmeden veya daha hızlı bir mod seçmeden önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. Ancak **tablodaki tüm Bronz Kaplama Tuğlalar, Bronz Dişli Kutuları, Bronz Boru Muhafazaları ve Bronz Külhanlar çelik karşılıklarıyla değiştirilmelidir**. Yalnızca kasaları veya Külhanları değiştirmek ya da iki kademeden bileşenleri karıştırmak kademe kontrolünden geçmez.

Yükseltmeden önce işlemeyi ve malzeme girdisini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınç kademesini bildirdiğini doğrula.

Yüksek basınç ayrı bir buhar sıvısı değil, bir yapı kademesidir. Makine yine sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı yollar yeniden kullanılabilir. Elektrikli Enerji Kapağı gerekmez. Yükseltme hızı ve buhar tüketim hızını ikiye katlar, maksimum ise sekiz paralel olarak kalır.

## Otomasyon ve Sıralama

Buharlı Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik olarak malzeme çekmez veya ürünleri onlara itmez. Bir yolun yanına sandık koymak taşımayı otomatikleştirmez.

- **Girdi:** Malzemeleri Giriş Yolunun ön yüzünden yerleştirmek için huniler, GT Eşya Boruları, Konveyör Modülleri, Eşya Kanalları veya benzeri ekipman kullan.
- **Çıktı:** Ürünleri Çıkış Yolunun ön yüzünden borular, kanallar veya Konveyör Modülleriyle etkin biçimde çek, ardından depolamaya veya bir sonraki makineye gönder.
- **Buhar:** Kazan çıktısını Buhar Kapağına ulaştırmak için sıvı boruları kullan. Eşya yolları buhar alamaz.
- **Sıralama:** Taşıma ekipmanını amaçlanan malzemelere göre filtrele; böylece mevcut modun işleyemediği eşyalar giriş yuvalarını doldurmaz.

Metalleri, yemekleri ve diğer malzemeleri sık sık aynı anda işlemen gerekiyorsa ayrı makineler kullan veya malzeme değiştirirken modu değiştir. Daha fazla Giriş Yolu eşya tamponunu artırır ancak paralel sınırını yükseltmez. Daha fazla Çıkış Yolu çıkış tıkanıklıklarını azaltabilir.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Eksik yapı | Kontrolcü ikinci katmanın ön ortasında; dört Dişli Kutusu, dört Boru Muhafazası ve üç Külhan doğru konumlarda |
| Yapı kademesi uyuşmuyor | Kasalar, Dişli Kutuları, Boru Muhafazaları ve Külhanlar aynı kademeden olmalı; yükseltmeden sonra kalan bronz bileşenleri kontrol et |
| Buhar Kapağı veya yol eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş ve Çıkış Yolu; yanlış kapak türlerini kontrol et |
| Yolları ekledikten sonra yapı oluşmuyor | En az iki gerçek kasa kalmalı; yollar Dişli Kutusu, Boru Muhafazası veya Külhanın yerini alamaz |
| Malzemeler var ama tarif bulunamıyor | Doğru mod, o modda eşya için geçerli bir tarif ve yeterli çıkış alanı |
| Depolanan buhara rağmen başladıktan sonra duruyor | Yeterli sürekli besleme, boru kısıtlamaları veya paylaşılan besleme ve paralel sayısının, yüksek basınç kademesinin ya da daha hızlı modun kazan kapasitesini aşıp aşmadığı |
| Yolun yanındaki sandık eşya aktarmıyor | Buharlı yollar eşyaları otomatik olarak çekmez veya itmez; etkin taşıma ekipmanını, bağlantı yüzlerini, yönleri ve filtreleri kontrol et |
| Sekizden az tarif işleniyor | Aynı tarif için yeterli malzeme, GUI paralel sınırı ve tüm ürünler için çıkış alanı |
| Yükseltmeden sonra buhar tüketimi artıyor | Yüksek basınç tüketim hızını ikiye katlar ve Patlatma veya Tütsüleme tekrar ikiye katlayabilir; buhar beslemesini buna göre artır |

Genel yapı kontrolleri ve araç kontrolleri için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Buhar Ocağı](https://wiki.gtnewhorizons.com/wiki/Steam_Hearth)