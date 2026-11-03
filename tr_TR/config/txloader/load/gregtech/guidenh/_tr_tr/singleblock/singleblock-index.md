---
navigation:
  title: "Tek Blok Makineleri"
  icon: gregtech:gt.blockmachines:106
  parent: /index.md
  position: 10
---

# Tek Blok Makineleri

Tek blok makineler yalnızca tek bir bloktan oluşur. Kullanım alanları dardır ve varsa eşdeğer [Multibloklar makinesinden](../multiblocks/multiblocks_index.md) her zaman daha yavaş ya da daha verimsizdirler. Yüksek basınçlı buhar makineleri dışında yükseltilemezler, bu yüzden onları değiştirmek her zaman yeni bir makine üretmek anlamına gelir. Buna rağmen erken ilerleme için hayati önemdedirler ve bazıları oyunun tamamı boyunca işe yaramaya devam eder. EV'den IV'e kadar, çoğu [Multibloklar makineleri](../multiblocks/multiblocks_index.md) kullanılabilir hâle geldiğinde oyuncular yavaş yavaş tek blok makinelerden uzaklaşır.

# Makine Yönü

Buharlı ya da elektrikli olsun, her tek blok makinenin iki özel yüzü ve dört sıradan yüzü vardır. GregTech 3x3 İngiliz anahtarı kurallarını kullanarak yönünü <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> ile değiştirebilirsin.

- **Ön yüz**: görsel olarak en belirgin yüz olup yalnızca yatay olarak yönlendirilebilir. Eşya, sıvı, buhar veya güç girişi ya da çıktısı hiç yapamaz.
  - Bir İngiliz anahtarı tutup bir yan yüze <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yaparak ön yüzün yönünü değiştir.
- **Çıktı yüzü**: siyah arka plan üzerinde küçük beyaz çerçeveli bir bağlantı noktası bulunan yüz.
  - Buharlı makinelerde bu, harcanmış buhar basıncını dışarı atan egzoz menfezidir.
  - Elektrikli makinelerde bu, ürünleri dışarı atmak için kullanılan eşya çıktısı yüzüdür.
  - Bir İngiliz anahtarı tutup bir yan yüze <kbd>Sağ tık</kbd> yaparak çıktı yüzünü değiştir.
- **Diğer tüm yüzler**: kalan dört yüz eşdeğerdir ve eşya, sıvı, buhar veya güç alıp verebilir.

# Buharlı Makineler

Tek blok buharlı makineler buharla çalışır ve buhar çağında yoğun olarak kullanılır. Buhar, kazanlar tarafından üretilir. Her standart sürümün çelikten yapılmış karşılık gelen bir yüksek basınçlı sürümü vardır.

Buharlı makineler patlamaz, yağmura ve kara dayanıklıdır ve açık havaya güvenle yerleştirilebilir.

## Kategoriler

Yalnızca altı tek blok buharlı makine vardır ve her birinin standart ile yüksek basınçlı sürümü bulunur:

| İşlev | Standart | Yüksek Basınçlı |
|----------|----------|---------------|
| Fırın | <ItemLink id="gregtech:gt.blockmachines:103" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:104" showIcon="left" /> |
| Alaşım İzabesi | <ItemLink id="gregtech:gt.blockmachines:118" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:119" showIcon="left" /> |
| Kompresör | <ItemLink id="gregtech:gt.blockmachines:115" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:116" showIcon="left" /> |
| Öğütücü | <ItemLink id="gregtech:gt.blockmachines:106" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:107" showIcon="left" /> |
| Ekstraktör | <ItemLink id="gregtech:gt.blockmachines:109" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:110" showIcon="left" /> |
| Dövme Çekiç | <ItemLink id="gregtech:gt.blockmachines:112" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:113" showIcon="left" /> |

## Grafiksel Kullanıcı Arayüzü

- **Buhar ölçeri**: sol üstte, dahili buhar tamponunu gösterir. Tüm buharlı makinelerin 16.000 L dahili tamponu vardır.
- **Depolama yuvaları**: alttaki iki yuva, özel bir davranışları yoktur.
- **Sessize alma düğmesi**: sağ üstte. Makineye <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak da açıp kapatabilirsin.

Buharlı makineler otomatik çıktıyı desteklemez.

## Güç

Makine, ön yüz ve egzoz yüzü dışındaki dört yüzden buhar kabul ederek dahili tamponunu doldurur. LV seviyesindeki tarifleri 4 L buhar = 1 EU oranıyla, yani %50 verimlilikle çalıştırır. Bronz makineler bir LV tarifinin normal süresinin iki katını alır.

| Makine Türü | Buhar Maliyeti (L/t) | Süre |
|--------------|------------|----------|
| Buharlı makine | 2x | 2x |
| Yüksek basınçlı buharlı makine | 4x | 1x |

Yüksek basınçlı sürüm buharı iki kat hızda tüketir ve tarif süresini yarıya indirir; etkili olarak bir 2/2 kayıpsız [hız aşırtma](../tierskipping-overcloking-parallels/overclocking.md) gerçekleştirir.

Makineye <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak onu duraklatabilir veya devam ettirebilirsin.

## Eşya Taşımacılığı ve Egzoz

Ön ve egzoz yüzleri dışındaki dört yüz giriş veya çıktı yapabilir. Buharlı makineler eşyaları kendi başlarına dışarı atamaz, bu yüzden ürünleri almak için hunilere veya başka bir taşıma sistemine ihtiyacın var.

Egzoz menfezi bir buharlı makinenin çıktı yüzüdür. Her tarif tamamlandıktan sonra makine egzozunu o yüzden dışarı vermek zorundadır. Menfez tıkanırsa makine tarifi tamamlayamaz. Bir tarif tamamlandığında menfezin yanında durmak oyuncuya 3,5 kalp hasar verir.

## Arızalar

- Egzoz menfezi tıkalı -> bir arıza simgesi belirir ve egzoz boşaltılana kadar makine devam etmez.
- Buhar tamponu boş -> bir arıza simgesi belirir. Buhar tamponu kısa süre sonra yeniden dolarsa makine tarifi yeniden dener. Buhar beslemen temelde yetersizse makine tekrar tekrar arızalanabilir, tüm ilerlemeyi kaybedebilir ve buharı boşa harcayabilir.

# Elektrikli Makineler

> [!WARNING]
> Tek blok elektrikli makineler patlayabilir. [Patlamalar](#patlamalar) bölümünü dikkatlice oku.

Tek blok elektrikli makineler, LV'de mutlaka üretilmesi gereken ilk makinelerdir. Belirli kullanım alanları ve sabit gerilim seviyeleri vardır ve yükseltildiklerinde tamamen değiştirilmeleri gerekir.

## Grafiksel Kullanıcı Arayüzü

Elektrikli makinenin arayüzü buharlı olandan daha karmaşıktır:

- **Eşya girdisi/çıktısı yuvaları**: ilerleme çubuğunun solundaki ve sağındaki açık renkli yuvalar.
- **Sıvı girdisi/çıktısı yuvaları**: eşya yuvalarının altındaki koyu renkli yuvalar. Elinde kap varken bunlarla doğrudan etkileşebilirsin: <kbd>Sol tık</kbd> eşleşen tüm sıvı kaplarını doldurur veya boşaltır, <kbd>Sağ tık</kbd> ise yalnızca bir kabı işler.
- **Güç yuvası**: aynı gerilimdeki araçları veya bataryaları kabul eder. Dahili tampon yeterince dolduğunda onları şarj eder; tampon azaldığında onlardan çekebilir. Normal bir depolama yuvası olarak da kullanılabilir.
- **Veri yuvası**: yalnızca tarayıcılar, yazıcılar ve fotokopi makineleri gibi özel makinelerde görünür.
- **Entegre devre yuvası**: sağ altta. Devre numarasını artırmak veya azaltmak için <kbd>fare tekerleğini</kbd> kaydır ya da tıkla; <kbd>Shift</kbd> + <kbd>Sol tık</kbd> seçim arayüzünü açar; <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> temizler.
- **Otomatik çıktı düğmeleri**: sol alttaki iki düğme. Etkinleştirildiğinde makine eşya veya sıvı dışarı atabilir. Buharlı makinelerde bu özellik yoktur.
- **Sessize alma düğmesi**: sağ üstte. Makineye <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak da açıp kapatabilirsin.

## Güç

Elektrikli makineler EU ile çalışır. Makine geriliminin 64 katına eşit, EU cinsinden küçük bir dahili tamponları vardır; bu, standart gerilimde 1A'nın 3,2 saniyede tükettiği miktardır. Örneğin bir LV makine 2.048 EU, bir HV makine ise 32.768 EU depolar.

Makineler tamponlarını doldurmak için yerel güç ağından sürekli enerji paketleri talep eder. Maksimum giriş akımları şudur:

$$\text{Maximum Input Current} = \left\lfloor\frac{\text{Recipe Rated Power} \times 2}{\text{Machine Operating Voltage}}\right\rfloor + 1 \text{ A}$$

- Çoğu tek blok makine: en fazla 2A.
- Termal Santrifüj: en fazla 4A.
- Ark Fırını: en fazla 6A.

Makineye <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak onu duraklatabilir veya devam ettirebilirsin.

## Hız Aşırtma

Tek blok elektrikli makineler 4/2 kusurlu hız aşırtmalar kullanır: her hız aşırtma güç tüketimini 4 ile çarpar ve tarif süresini yarıya indirir, böylece toplam enerji iki katına çıkar. Tek blok Kütle İmalatçısı tek istisnadır ve 2/2 kayıpsız hız aşırtmalar kullanır.

Tam sistem için **[Hız Aşırtma](../tierskipping-overcloking-parallels/overclocking.md)** bölümüne bak.

## Lojistik

Ön yüz dışındaki beş yüzün tamamı çıktı verebilir. Ön ve çıktı yüzü dışındaki dört yüz giriş alabilir.

- **Otomatik çıktı**: arayüzdeki otomatik çıktı düğmesini etkinleştir; çıktı yüzü eşya veya sıvı dışarı atabilir.
- **Çıktı yüzünden girişe izin ver**: <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> tutup ön yüze veya çıktı yüzüne <kbd>Sağ tık</kbd> yaparak açıp kapat.
- **Girdi süzme**: bir tornavida tutup ön yüze veya çıktı yüzüne <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yaparak etkinleştir. Etkinleştirildiğinde girdi eşyaları tarif haritasına göre süzülür.
- **Girdi yığınlama**: <ItemLink id="Forestry:solderingIron" showIcon="left" /> tutup ön yüze <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yaparak etkinleştir; aynı yuvada birden fazla eşya türü bulunabilir.

## Arızalar

Dahili EU tamponu tükendiğinde makine arızalanır. Tarif ilerlemesi kaybolur ama girdi durumu korunur. Tampon kısa süre sonra yeniden dolarsa makine tarifi yeniden dener. Güç beslemesinin kendisi yetersizse makine tekrar tekrar arızalanabilir, ilerlemeyi kaybedebilir ve EU harcayabilir.

## Patlamalar

Tek blok elektrikli makineler aşağıdaki durumlarda patlayabilir:

- **Aşırı gerilim**: kendi gerilimlerinin üzerinde bir enerji paketi alırlarsa anında patlarlar. Örneğin bir LV makineye MV paketleri beslemek.
- **Ateş**: makine kapasitesinin %20'sinden fazla EU depoluyorsa her tick'te bir kez 1/1000 şansla kontrol eder. Herhangi bir tarafı ateş içindeyse makine patlar.
- **Yağmur veya kar**: makine EU depoluyorsa yine her tick'te bir kez 1/1000 şansla kontrol eder. Yağmur sırasında anında patlama şansı 1/10, alev alma şansı 9/10'dur; gök gürültülü fırtınalarda anında patlama şansı 1/3'tür.
- Bir patlama, depolanan tüm EU'yu IV seviyesi güç olarak her bağlı tele veya bitişik makineye boşaltır; bu da zincirleme patlamalara yol açabilir veya yakındaki telleri aşırı yükleyebilir.
- [Multibloklar makinelerindeki](../multiblocks/multiblocks_index.md) güç verilmiş kapaklar da aynı nedenlerle alev alabilir veya patlayabilir.