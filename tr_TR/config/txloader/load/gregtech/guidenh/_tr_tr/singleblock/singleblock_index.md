---
navigation:
  title: "Tek Blok Makineleri"
  icon: gregtech:gt.blockmachines:106
  parent: /index.md
  position: 10
---

# Tek Blok Makineleri

Tek blok makineleri yalnızca bir bloktan oluşur. Kullanım alanları dardır ve varsa eşdeğer [Multibloklar](../multiblocks/multiblocks_index.md) makinesinden her zaman daha yavaş veya daha verimsizdir. Yüksek basınçlı buhar makineleri hariç yükseltilemezler; bu yüzden onları değiştirmek her zaman yeni bir makine üretmek anlamına gelir. Yine de erken ilerleme için gereklidirler ve bazıları oyun boyunca işe yarar. EV'den IV'e kadar, çoğu [Multibloklar](../multiblocks/multiblocks_index.md) makinesi kullanılabilir hale geldiğinde, oyuncular yavaş yavaş tek blok makinelerden uzaklaşır.

# Makine Yönü

Her tek blok makinesi, ister buharlı ister elektrikli olsun, iki özel yüze ve dört sıradan yüze sahiptir. Yönünü <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> ile, GregTech 3x3 İngiliz anahtarı kurallarını kullanarak değiştirebilirsin.

- **Ön yüz**: görsel olarak en belirgin yüz ve yalnızca yatay olarak yönlendirilebilir. Hiçbir şekilde eşya, sıvı, buhar veya güç girişi ya da çıkışı yapamaz.
  - İngiliz anahtarını elinde tut, ardından bir yan yüze <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yaparak ön yüz yönünü değiştir.
- **Çıktı yüzü**: siyah zemin üzerinde küçük beyaz çerçeveli bir bağlantı noktası bulunan yüz.
  - Buhar makinelerinde bu, kullanılmış buhar basıncını serbest bırakan egzoz menfezidir.
  - Elektrikli makinelerde bu, ürünleri dışarı atmak için kullanılan eşya çıktısı yüzüdür.
  - İngiliz anahtarını elinde tut, ardından bir yan yüze <kbd>Sağ tık</kbd> yaparak çıktı yüzünü değiştir.
- **Diğer tüm yüzler**: kalan dört yüz eşdeğerdir ve eşya, sıvı, buhar veya güç girişi ya da çıkışı yapabilir.

# Buhar Makineleri

Tek blok buhar makineleri buharla çalışır ve buhar çağında yoğun olarak kullanılır. Buhar, kazanlar tarafından üretilir. Her standart sürümün çelikten yapılmış bir yüksek basınçlı sürümü vardır.

Buhar makineleri patlamaz, yağmur ve kara dayanıklıdır ve açık havada güvenle yerleştirilebilir.

## Kategoriler

Yalnızca altı tek blok buhar makinesi vardır ve her birinin standart ve yüksek basınçlı sürümü bulunur:

| İşlev | Standart | Yüksek Basınçlı |
|----------|----------|---------------|
| Fırın | <ItemLink id="gregtech:gt.blockmachines:103" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:104" showIcon="left" /> |
| Alaşım İzabesi | <ItemLink id="gregtech:gt.blockmachines:118" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:119" showIcon="left" /> |
| Kompresör | <ItemLink id="gregtech:gt.blockmachines:115" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:116" showIcon="left" /> |
| Öğütücü | <ItemLink id="gregtech:gt.blockmachines:106" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:107" showIcon="left" /> |
| Özütleyici | <ItemLink id="gregtech:gt.blockmachines:109" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:110" showIcon="left" /> |
| Dövme Çekiç | <ItemLink id="gregtech:gt.blockmachines:112" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:113" showIcon="left" /> |

## Grafik Kullanıcı Arayüzü

- **Buhar ölçeri**: sol üstte, dahili buhar tamponunu gösterir. Tüm buhar makinelerinin 16.000 L dahili tamponu vardır.
- **Depolama yuvaları**: alttaki iki yuva, özel bir davranışları yok.
- **Sessize alma düğmesi**: sağ üstte. Makineye <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak da açıp kapatabilirsin.

Buhar makineleri otomatik çıktıyı desteklemez.

## Güç

Makine, ön yüz ve egzoz yüzü dışındaki dört yüzden buhar kabul ederek dahili tamponunu doldurur. LV kademesi tariflerini 4 L buhar = 1 EU oranıyla çalıştırır; bu %50 verim demektir. Bronz makineler bir LV tarifinin normal süresinin iki katı sürede çalışır.

| Makine Türü | Buhar Maliyeti (L/t) | Süre |
|--------------|------------|----------|
| Buhar makinesi | 2x | 2x |
| Yüksek basınçlı buhar makinesi | 4x | 1x |

Yüksek basınçlı sürüm buharı iki kat hızda tüketir ve tarif süresini yarıya indirir; etkili biçimde bir 2/2 kayıpsız [hız aşırtma](../tierskipping_overcloking_parallels/overclocking.md) gerçekleştirir.

Makineyi <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak duraklatabilir veya devam ettirebilirsin.

## Eşya Taşıma ve Egzoz

Ön ve egzoz yüzleri dışındaki dört yüz giriş veya çıktı yapabilir. Buhar makineleri eşyaları kendi başlarına dışarı atamaz, bu yüzden ürünleri çıkarmak için hunilere veya başka bir taşıma sistemine ihtiyacın olur.

Egzoz menfezi bir buhar makinesinin çıktı yüzüdür. Her tarif tamamlandıktan sonra makine egzozunu bu yüzden tahliye etmelidir. Menfez tıkanırsa makine tarifi tamamlayamaz. Bir tarif tamamlandığında menfezin yanında durmak oyuncuya 3,5 kalp hasar verir.

## Arızalar

- Egzoz menfezi tıkalı -> bir arıza simgesi belirir ve egzoz tahliye edilene kadar makine devam etmez.
- Buhar tamponu boş -> bir arıza simgesi belirir. Buhar tamponu kısa süre sonra yeniden dolarsa makine tarifi yeniden dener. Buhar beslemen temelde yetersizse makine tekrar tekrar arızalanabilir, tüm ilerlemeyi kaybedebilir ve buharı boşa harcayabilir.

# Elektrikli Makineler

> [!WARNING]
> Tek blok elektrikli makineler patlayabilir. [Patlamalar](#patlamalar) bölümünü dikkatlice oku.

Tek blok elektrikli makineler LV'de üretilmesi zorunlu ilk makinelerdir. Belirli kullanımları, sabit gerilim kademeleri vardır ve yükseltildiklerinde tamamen değiştirilmeleri gerekir.

## Grafik Kullanıcı Arayüzü

Elektrikli makinenin GUI'si buharlı olandan daha karmaşıktır:

- **Eşya giriş/çıkış yuvaları**: ilerleme çubuğunun solunda ve sağında bulunan açık renkli yuvalar.
- **Sıvı giriş/çıkış yuvaları**: eşya yuvalarının altındaki koyu yuvalar. Kapları elinde tutarken onlarla doğrudan etkileşime geçebilirsin: <kbd>Sol tık</kbd> eşleşen tüm sıvı kaplarını doldurur veya boşaltır, <kbd>Sağ tık</kbd> ise yalnızca bir kabı işler.
- **Güç yuvası**: aynı gerilimdeki aletleri veya pilleri kabul eder. Dahili tampon yeterince dolduğunda onları şarj eder; tampon azaldığında onlardan çekebilir. Normal depolama yuvası olarak da kullanılabilir.
- **Veri yuvası**: yalnızca tarayıcılar, yazıcılar ve fotokopi makineleri gibi özel makinelerde görünür.
- **Entegre devre yuvası**: sağ altta. Devre numarasını artırmak veya azaltmak için <kbd>fare tekerleğini</kbd> kaydır veya tıkla; <kbd>Shift</kbd> + <kbd>Sol tık</kbd> seçici GUI'sini açar; <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> temizler.
- **Otomatik çıktı anahtarları**: sol alttaki iki düğme. Aktifleştirildiğinde makine eşya veya sıvı dışarı atabilir. Buhar makinelerinde bu özellik yoktur.
- **Sessize alma düğmesi**: sağ üstte. Makineye <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak da açıp kapatabilirsin.

## Güç

Elektrikli makineler EU ile çalışır. Makine geriliminin EU cinsinden 64 katına eşit küçük bir dahili EU tamponuna sahiptirler; bu, standart gerilimde 1A'nın 3,2 saniyede tükettiği miktardır. Örneğin bir LV makinesi 2.048 EU depolarken bir HV makinesi 32.768 EU depolar.

Makineler tamponlarını doldurmak için yerel güç ağından sürekli olarak enerji paketleri ister. Maksimum giriş akımları:

$$\text{Maximum Input Current} = \left\lfloor\frac{\text{Recipe Rated Power} \times 2}{\text{Machine Operating Voltage}}\right\rfloor + 1 \text{ A}$$

- Çoğu tek blok makinesi: en fazla 2A.
- Termal Santrifüj: en fazla 4A.
- Ark Fırını: en fazla 6A.

Makineyi <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> ile <kbd>Sağ tık</kbd> yaparak duraklatabilir veya devam ettirebilirsin.

## Hız Aşırtma

Tek blok elektrikli makineler 4/2 kusurlu hız aşırtma kullanır: her hız aşırtma güç tüketimini 4 ile çarpar ve tarif süresini yarıya indirir, böylece toplam enerji iki katına çıkar. Tek blok Kütle İmalatçısı tek istisnadır ve 2/2 kayıpsız hız aşırtma kullanır.

Tam sistem için **[Hız Aşırtma](../tierskipping_overcloking_parallels/overclocking.md)** bölümüne bak.

## Lojistik

Ön yüz dışındaki beş yüzün tamamı çıktı verebilir. Ön yüz ve çıktı yüzü dışındaki dört yüz giriş yapabilir.

- **Otomatik çıktı**: GUI'deki otomatik çıktı anahtarını aktifleştir; çıktı yüzü eşya veya sıvı dışarı atabilir.
- **Çıktı yüzünden girişe izin ver**: <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> tut ve açıp kapatmak için ön yüze veya çıktı yüzüne <kbd>Sağ tık</kbd> yap.
- **Girdi süzme**: bir tornavida tut ve aktifleştirmek için ön yüze veya çıktı yüzüne <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yap. Aktifleştirildiğinde girdi eşyaları tarif haritasına göre süzülür.
- **Girdi yığma**: <ItemLink id="Forestry:solderingIron" showIcon="left" /> tut ve aktifleştirmek için ön yüze <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> yap; bu, aynı yuvada birden fazla eşya türüne izin verir.

## Arızalar

Dahili EU tamponu tükendiğinde makine arızalanır. Tarif ilerlemesi kaybolur ancak girdi durumu korunur. Tampon kısa süre sonra yeniden dolarsa makine tarifi yeniden dener. Güç beslemesinin kendisi yetersizse makine tekrar tekrar arızalanabilir, ilerlemeyi kaybedebilir ve EU'yu boşa harcayabilir.

## Patlamalar

Tek blok elektrikli makineler aşağıdaki durumlarda patlayabilir:

- **Aşırı gerilim**: kendi gerilimlerinin üzerinde bir enerji paketi alırlarsa anında patlarlar. Örneğin bir LV makinesine MV paketleri beslemek.
- **Ateş**: makine kapasitesinin %20'sinden fazla EU depoluyorsa her tick bir kez 1/1000 şansla kontrol yapar. Herhangi bir taraf ateşteyse makine patlar.
- **Yağmur veya kar**: makine EU depoluyorsa yine her tick bir kez 1/1000 şansla kontrol yapar. Yağmur sırasında anında patlama şansı 1/10, alev alma şansı 9/10'dur; gök gürültülü fırtınalarda anında patlama şansı 1/3'tür.
- Bir patlama, depolanan tüm EU'yu bağlı her tele veya bitişik her makineye IV kademesi güç olarak salar; bu da zincirleme patlamalara yol açabilir veya yakındaki tellere aşırı yük bindirebilir.
- [Multibloklar](../multiblocks/multiblocks_index.md) makinelerindeki güç kapakları da aynı nedenlerle alev alabilir veya patlayabilir.