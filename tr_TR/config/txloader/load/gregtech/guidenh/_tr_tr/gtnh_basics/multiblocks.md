---
navigation:
  title: Multiblok Makineleri
  icon: structurelib:item.structurelib.constructableTrigger
  parent: ./gtnh_basics_index.md
---

# Multiblok Makineleri

> [!NOTE]
> Bazı sayfalar şu anda mevcut olmadığı için bazı bağlantılar bozuk. [Rehbere katkıda bulunarak](https://github.com/GTNewHorizons/GTNH-Guide-Pack) GTNH'nin geliştirilmesine destek ol!

Bir **Multiblok**, iki veya daha fazla bloktan inşa edilen bir makinedir. Boyutları küçük Termal Rafinerilerden Forge of the Gods gibi devasa üst yapılara kadar uzanır. Genellikle çok spesifik bir amaca hizmet ederler ve eğer varsa, tek blok karşılıklarından her zaman daha iyidirler (ör. daha hızlı çalışır, daha iyi tarifler). Çoğu multiblokun kendine özgü kasaları ve yapısı vardır, ancak eşya, sıvı ve enerji giriş/çıkışı (I/O) neredeyse evrenseldir. Eşyalar yollar aracılığıyla, sıvılar kapaklar aracılığıyla, güç ise enerji/dinamo kapakları aracılığıyla aktarılır. Ayrıca makineyi onarmak için bakım kapağı ve kirliliği salmak için egzoz çıkışı vardır. Hangi yolların/kapakların gerekli olduğunu ve genel yapıya nerede oturduklarını görmek için ipucunu ve/veya <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

> [!IMPORTANT]
> GTNH'deki tüm multibloklar GregTech'ten değildir. Bu sayfadaki bilgilerin hiçbirine uymayan, diğer modlardan gelen birkaç tanesi vardır (ör. Railcraft Kazanları ve İzabe Ocakları). Daha fazla ayrıntı için kendi sayfalarını ziyaret et.

---

# Yapım

Multibloklar çeşitli şekil, boyut ve kasalarda olsa da eşya, sıvı ve enerji I/O'su için birçok ortak bileşen vardır. Aşağıdaki alt bölümler her birinin amacını ve işlevini açıklar. Multiblokların nadiren bunların TAMAMINI oluşum için gerektirdiğini ve miktarları ile konumları üzerinde kısıtlamalar olabileceğini unutma. Bir multiblokun yapım gereksinimleri hakkında ayrıntılı bilgi için her zaman ipucunu ve <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kontrol et.

## Kontrolcü

Kontrolcü multiblokun kalbidir. Tüm yapının yerleşimini ve yönünü olduğu kadar makinenin çalışma ayarlarını da belirler. GUI'yi açmak için kontrolcüye sağ tıkla; burada (1) üstte makinenin adı, (2) makinenin durumu, (3) bir ses açma/kapama düğmesi, (4) birkaç yapılandırılabilir parametre, (5) güç paneli ve (6) varsa manuel geçersiz kılmalar bulunur. Yapılandırılabilir parametrelerin ve manuel geçersiz kılmaların her birinin kısa bir açıklaması aşağıda verilmiştir.

- **Hiçlik Modu** - Çıkış yolunda ve/veya çıkış kapağında yer olmadığında multiblokun davranışını belirler. Yalnızca eşyaları, yalnızca sıvıları veya ikisini birden yok etmeyi seç. Hiçbir Şeyi Hiçleme, tüm ürünler için yeterli yer olana kadar makineyi geçici olarak duraklat anlamına gelir.
- **Giriş Ayrıştırma** - Farklı giriş yollarındaki KATI bileşenlerin, programlanmış devreler dahil, aynı tarifte kullanılmasını engeller. Bu, tarif çakışması potansiyeli yüksek multibloklar için özellikle kullanışlıdır.
- **Toplu Mod** - Aynı tarifin katlarını tek bir büyük tarif olarak çalıştırır. Bu, hiçbir şekilde zaman indirimi sağlamaz veya makinenin verimini artırmaz. Amacı, tarif kontrol sayısını azaltarak lag'i düşürmek ve TPS'yi iyileştirmektir.
- **Tarifi Kilitle** - Multiblokun başka tarifler çalıştırmasını engeller. Bu, multiblok çalışırken veya istediğin tariften önce ayarlanabilir.
- **Yapıyı Güncelle** - Yapı kontrolünü zorlar. Multibloklar zaten periyodik yapı kontrolü yapar, ancak bu birkaç saniye (veya dakika) beklemekten kurtarır.
- **Güç Anahtarı** - Multibloku etkinleştirir veya devre dışı bırakır. Bu, aktif tarifleri KESMEZ.

Güç panelinde iki seçenek vardır. Birincisi, varsayılan olarak mevcut maksimuma ayarlanan maksimum paralel sayısını belirlemektir. Enerji verimliliği üzerinde mutlak hassasiyet gerektiren çok özel bir senaryo yoksa, bunu düşürmek veya değeri elle ayarlamak için pek bir sebep yoktur. İkinci seçenek, sohbetteki mesajı ve kontrolcüye uzaktan bakıldığında görünen yanıp sönen güç kesintisi simgesini içeren güç kesintisi olaylarını açar/kapatır. Çok oyunculu modda, diğer oyuncuları aynı SpaceProject ekibine davet etmek ve güç kesintisi bilgilerini paylaşmak için ilk komutu kullan. Dünyadaki tüm güç kesintisi simgelerini hemen temizlemek için ikinci komutu kullan.

```
/sp invite <name>
/powerfails clear
```

GUI'ye girmeden makinenin çalışma ayarlarını değiştirmenin birkaç özgün etkileşimi ve kısayolu da vardır. Bunların hepsi elinde bir tür GregTech aleti varken kontrolcüye sağ tıklamayı içerir. Bu, aletin dayanıklılığını azaltır, ancak aynı anda birçok makineyi hızlıca yapılandırmak için Ring of Loki ile çok iyi çalışır.

- **İngiliz Anahtarı** - Kontrolcüyü ve dolayısıyla tüm yapıyı döndürür. Kontrolcüyü yatay olarak çevirmek için eğilerek sağ tıkla.
- **Lehim Demiri** - Giriş ayrıştırmasını açar/kapatır. Ayrıca belirli multiblokların modunu değiştirmek için kullanılır.
- **Tel Makası** - Toplu modu açar/kapatır.
- **Yumuşak Tokmak** - Makineyi açar/kapatır.
- **Çekiç** - Ses susturmayı açar/kapatır.
- **Lehim Demiri** - Kaplamalardan gelen kızıltaş sinyalinin gücünü (güçlü/zayıf) ayarlar. Bu yalnızca kontrolcülere özgü değildir.

## Yollar

<ItemImage id="minecraft:chest" /> **Giriş Yolu** (Sandık simgeli) / <ItemImage id="minecraft:chest" /> **Çıkış Yolu** (Sandık simgeli)

Giriş ve çıkış yolları sırasıyla KATI bileşenleri yerleştirmek ve çıkarmak içindir. Sıvılar ve gazlar hücreler, kovalar veya benzeri kaplar aracılığıyla sağlanamaz. Giriş yolları bitişik envanterlerden otomatik olarak çekmez, ancak çıkış yolları varsa bitişik envanterlere otomatik olarak iteler. Yolun kademesi mevcut kapasiteyi veya toplam eşya yuvası sayısını belirler:

| Kademe | ULV | LV | MV | HV+ |
|------|-----|----|----|-----|
| Yuvalar | 1 | 4 | 9 | 16 |

Multiblokta kullanımı olmayan hiçbir bileşenin yola girmesini engelleyen filtreyi açmak/kapatmak için bir giriş yoluna tornavidayla sağ tıkla. Sıralama ve sınırlama modunu açmak/kapatmak için giriş yoluna tornavidayla eğilerek sağ tıkla. Sıralama modu eşyaları sürekli en üstteki yuvalara iterken, sınırlama modu bir eşyanın birden fazla yığınının yola girmesini engeller. Çıkış yollarının GUI'sinde onları belirli eşyalara kilitlemek için bir filtre de vardır (NEI'den sürükle).

- **Süper Yollar** - Normal giriş/çıkış yollarının bir yükseltmesidir, ancak tek fark yuva kapasiteleridir. Normal yollar 16 yuvayla sınırlıyken süper yollar 32-160 yuva arasında değişir. Ancak sorun şu ki çok daha pahalıdırlar ve üretmek için Kademe+3 normal bir giriş yolu gerektirirler. Örneğin LV süper yol, beş LV konveyör modülü, iki LV motor ve bir EV giriş yolundan üretilir.

- **Stoklayan Giriş Yolu (ME)** ve **Çıkış Yolu (ME)** - Normal giriş/çıkış yollarının daha da iyi bir yükseltmesidir çünkü eşyaların sorunsuz I/O'su için doğrudan bir AE2 ağına bağlanırlar. ME kanallarının diğer yollar/kapaklar dahil herhangi bir tarafa bağlanmasına izin vermek için tel makasıyla sağ tıkla. Gelişmiş sürüm, ağdaki herhangi bir eşyayla kendini stoklamasına olanak tanıyan otomatik çekmeyi bile destekler.

## Kapaklar

<ItemImage id="minecraft:cauldron" /> **Giriş Kapağı** / <ItemImage id="minecraft:cauldron" /> **Çıkış Kapağı**

Giriş ve çıkış kapakları sırasıyla SIVI bileşenleri yerleştirmek ve çıkarmak içindir. Giriş kapakları bitişik envanterlerden otomatik olarak çekmez, ancak çıkış kapakları varsa bitişik envanterlere otomatik olarak iteler. Kapağın kademesi mevcut kapasiteyi belirler. Giriş kapakları, envanterlerine bir yığın büyük sıvı hücresi koyarak teknik olarak bu miktarlardan çok daha fazlasını "tutabilir".

| Kademe | ULV | LV | MV | HV | EV | IV | ... |
|------|-----|----|----|----|----|----|-----|
| Kapasite | 8.000 L | 16.000 L | 32.000 L | 64.000 L | 128.000 L | 256.000 L | ... |

Buhar ve/veya diğer sıvıların çıkıp çıkmayacağını değiştirmek için bir çıkış kapağına tornavidayla sağ tıkla. Alternatif olarak, çıkış kapağının GUI'sindeki filtreyi belirli bir sıvıya kilitlemek için ayarla (NEI'den sürükle).

- **Dörtlü Giriş Kapakları** - Normal giriş kapaklarının bir yükseltmesidir; aynı kademedeki normal bir giriş kapağının kapasitesinin 1/4'ünde aynı anda dört farklı sıvı tutabilir. Birden fazla sıvıyı taşımak için dörtlü sıvı borularıyla güzel bir ikili oluştururlar.

- **Stoklayan Giriş Kapağı (ME)** ve **Çıkış Kapağı (ME)** - Normal giriş/çıkış kapaklarının daha da iyi bir yükseltmesidir çünkü sıvıların sorunsuz I/O'su için doğrudan bir AE2 ağına bağlanırlar. ME kanallarının diğer yollar/kapaklar dahil herhangi bir tarafa bağlanmasına izin vermek için tel makasıyla sağ tıkla. Gelişmiş sürüm, ağdaki herhangi bir sıvıyla kendini stoklamasına olanak tanıyan otomatik çekmeyi bile destekler.

## Enerji ve Dinamo Kapakları

<ItemImage id="minecraft:redstone_block" /> **Enerji Kapağı** / <ItemImage id="minecraft:redstone_block" /> **Dinamo Kapağı**

Bunlar belirli bir voltaj kademesinde güç yerleştirmek ve çıkarmak içindir. Daha spesifik olarak, standart bir enerji kapağı bir multibloka 2A'ya kadar güç sağlayabilir ve standart bir dinamo kapağı bir multibloktan 1A'ya kadar güç çekebilir. Bu kapaklarla doğru voltajı ve amperajı kullanmaya çok dikkat et, aksi hâlde kablolar yanabilir, bileşenler yok olabilir ve makineler patlayabilir.

- **Tamponlu Dinamo Kapakları** - Standart dinamo kapaklarının küçük bir yükseltmesidir ve bir multibloktan 4A'ya kadar güç çekebilir. Ayrıca gidecek yeri olmadığında güç depolamak için biraz daha büyük bir dahili tamponları vardır. *(2.9 itibarıyla kullanımdan kaldırıldı - bunun yerine 4A Çoklu Amper kapağı kullan.)*

- **Çoklu Amper Kapakları** - Standart enerji/dinamo kapaklarının bir yükseltmesidir ve bir multibloka/den 64A'ya kadar güç aktarabilir. İzin verilip verilmedikleri büyük ölçüde multibloka bağlıdır.

- **Lazer Kapakları** - Çok daha sonra açılır ve lazer vakum boruları aracılığıyla bir multibloka/den milyonlarca amper aktarabilir. Yine, izin verilip verilmedikleri büyük ölçüde multibloka bağlıdır.

## Bakım Kapağı

<ItemImage id="minecraft:iron_door" /> **Bakım Kapağı**

Bu kapak, her biri multiblokun güç tüketimini %10 artıran rastgele olaylar olan bakım sorunlarını onarmak içindir. Toplamda altı farklı bakım sorunu vardır ve hepsinin aynı anda bulunması multibloku kapatmaya yeter. Her biri kontrolcüde çok spesifik bir mesaj oluşturur ve çok spesifik bir GregTech aletine karşılık gelir. WAILA ayrıca kontrolcüye bakarken kırmızı metinle **SORUNLARI VAR** gösterir.

Bakım sorunlarını, bakım kapağını açıp gerekli aleti eline alarak ve ortadaki düğmeye sol tıklayarak onar. Bu, her kullanımda az miktarda dayanıklılık ve/veya şarj tüketir.

| Bakım Sorunu | Onarım Aleti |
|-------------------|-------------|
| "Boru gevşek" | İngiliz Anahtarı |
| "Vidalar gevşek" | Tornavida |
| "Bir şey sıkışmış" | Yumuşak Tokmak |
| "Kaplamalar çökük" | Çekiç |
| "Devre yanmış" | Lehim Demiri |
| "Orada olmaması gereken bir şey var" | Levye |

Yeni bir bakım sorununun ortaya çıkması için her 50 saniyelik çalışma süresinde 6.000'de 1 şans vardır. Bu, bakım sorunları arasında ortalama 300.000 saniye veya 83,3 saat çalışma süresi demektir. Devre dışı veya boşta duran multibloklar çalışma süresini artırmaz ve bu nedenle hiçbir bakım sorunu oluşturmaz veya bunların olasılığını artırmaz. Bakım kapağı olmayan multibloklar bu mekaniği tamamen yok sayar.

Aşağıda listelenen birkaç farklı bakım kapağı türü ve onarım yöntemi vardır. Bakım kapakları makineler arasında duvar paylaşabilir, ancak onarımlar yine de her biri için ayrı ayrı yapılmalıdır.

- **Alet Çantası (LV)** - Dokuz alete kadar tutar ve bakım kapağının dahili GUI'sinin DIŞINDAN sağ tıklanması durumunda hepsini aynı anda uygular. Mevcut sorun(lar)dan bağımsız olarak içindeki tüm aletlerin dayanıklılığını ve/veya şarjını tüketir. Lehim demiri için lehim malzemesi de Alet Çantasında saklanabilir ve oradan kullanılabilir. Bir Dynamism Tablet ile otomatikleştirilebilir ve bir bakım kaplaması gerektirir.

- **BrainTech Aerospace Gelişmiş Güçlendirilmiş Koli Bandı (MV)** - Tüm bakım sorunlarını aynı anda çözen tek kullanımlık bir eşya. Bant bakım kapağının etrafında görsel olarak belirir, ancak bu gelecekteki bakım sorunlarını engellemez veya oluşma şanslarını azaltmaz.

- **Wand Focus: Maintenance (HV)** - Electromagic Tools'tan yeniden kullanılabilir bir Thaumcraft asa odağıdır; 25 ignis, 25 terra ve 25 ordo karşılığında tüm bakım sorunlarını aynı anda çözer. Vis indirimleri ve frugal odak yükseltmesi bu onarımların maliyetini azaltabilir.

- **Drone Downlink Module (IV)** - Kapak menzilinde aktif bir Drone Centre varsa tüm bakım sorunlarını otomatik olarak onarır. Kademe 1 ve Kademe 2 dronlar her saniye düşme ve yok olma şansına sahiptir, ancak bakım sorunlarını düzeltmek tamamen ücretsizdir. Ayrıca bağlı multibloklar üzerinde uzaktan kontrol sağlar; bu, geniş çaplı bir elektrik kesintisinden sonra çok kullanışlıdır.

- **Otomatik Bakım Kapağı (LuV)** - 4 koli bandı, 2 yağlayıcı hücresi, 4 çelik vida ve 2 HV devre karşılığında herhangi bir bakım sorununu otomatik olarak onarır. Dahili envanterde toplam dört yuva, yani her eşya türü için bir yuva vardır.

- **Otomatik Bantlama Bakım Kapağı (UV)** - Herhangi bir bakım sorununu ücretsiz olarak otomatik onarır. Bakıma kalıcı çözüm.

## Egzoz Çıkışı

<ItemImage id="minecraft:dispenser" /> **Egzoz Çıkışı**

Bu kapak makineden kirliliği salar. Multiblokun çalışması için egzoz çıkışının önünde en az bir hava bloğu olmalıdır. Borular ve kablolar bile engel sayılır. Üretilen kirlilik miktarı multibloka ve egzoz çıkışının kademesine bağlıdır:

| Kademe | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV |
|------|----|----|----|----|----|-----|-----|----|-----|
| Kirlilik | %100 | %87 | %75 | %62 | %50 | %37 | %25 | %12 | %0 |

Kirlilik devre dışıysa egzoz çıkışları hâlâ gereklidir, ancak kademeleri artık önemli değildir.

## Duvar Paylaşımı

GregTech multibloklarının benzersiz bir özelliği, kasa, cam, bobin, yol/kapak ve daha fazlasından tasarruf etmek için yapılarının parçalarını duvar paylaşma yeteneğidir. Birden fazla makinenin aynı bloğu/blokları aynı anda kullanmasına izin vermek için yapıları basitçe üst üste bindir. Bunun oyuncuya faydalı olmadığı *çok* az istisna vardır ve bu nedenle ikinci bir [Elektrikli Yüksek Fırın](../multiblocks/lv/electric_blast_furnace.md) veya ikinci bir Eye of Harmony inşa ederken olsun, oyunun tamamı boyunca son derece kullanışlıdır.

Bakım ve egzoz çıkışlarını paylaşmak her zaman güvenlidir, ancak enerji kapaklarını paylaşırken dikkatli ol çünkü yalnızca 2A'ya kadar güç çekebilirler. Bir multiblokun tariflerinin 1A gücü aşmadığından emin ol ve bakım sorunlarını mümkün olan en kısa sürede onar, aksi hâlde ek güç maliyeti her iki makinenin de güç kesintisi yaşamasına neden olabilir.

---

# Kullanım

Multibloklar [tek blok makinelere](../singleblock/singleblock_index.md) çok benzer şekilde çalışsa da birkaç belirgin fark vardır. Her şeyden önce, multibloklar güç kesintisi yaşadığında bileşenleri **yok eder**. Tek bloklardaki gibi tarifi yeniden başlatmak yoktur; bileşenler kalıcı olarak kaybolur. Multiblok ayrıca kapanır ve elle yeniden başlatılması gerekir. Bunun olmasını önlemek için enerji depolamanı periyodik olarak kontrol et ve enerji seviyeleri düşükken multiblokları kapat veya kullanmayı bırak. Ayrıca kontrolcünün enerji kapaklarından önce yüklenmesini önlemek için tüm multiblokun chunkloaded olduğundan emin ol.

## Hız Aşırtma

Sağlanan güç, tarifin gerektirdiğinden en az 1 voltaj kademesi yüksek olduğunda hız aşırtma gerçekleşir. Tek bloklar bunu yalnızca daha yüksek kademe makinelerle başarabilir, ancak multibloklar daha yüksek kademe ve/veya birden fazla enerji kapağı kullanabilir. Oyuncu hız aşırtmayla ilk kez [Elektrikli Yüksek Fırın](../multiblocks/lv/electric_blast_furnace.md) kullanırken karşılaşır; 4A LV güç sağlamak ve 1A MV gücü simüle etmek için iki enerji kapağı gerekir. İki farklı hız aşırtma türü vardır ve hangisinin kullanıldığı multiblokun kendisine bağlıdır. "Karma" olanlar aynı tarifte ikisini de kullanabilir veya bir yükseltmeye bağlıdır. "Benzersiz" olanlar kendi özel kurallarını izler ve iki kategoriye de girmez.

- **Kusurlu Hız Aşırtmalar** - 2 kat hız için 4 kat güç tüketir (4/2). Bu, çoğu multiblokun standart davranışıdır. Örneğin, normalde 128 EU/t ve 60 sn süren ve toplamda 153.600 EU harcayan bir tarif düşün. Kusurlu bir hız aşırtma bunu 512 EU/t ve 30 sn'ye, toplamda 307.200 EU'ya çevirir. Toplam enerjinin çift katına çıktığına dikkat et; bu da ekstra hızın her zaman ek güç maliyetine değmeyebileceği anlamına gelir. Alternatif olarak, aynı etkiyi yarı güçle sağlamak için aynı voltaj kademesinde aynı multibloktan daha fazla inşa et.

- **Kusursuz Hız Aşırtmalar** - 4 kat hız için 4 kat güç tüketir (4/4). Toplam enerji aynı kalır, bu yüzden sağlanan voltajı/amperajı artırmanın bir dezavantajı yoktur. Kusursuz hız aşırtmalı aynı multibloktan birden fazla inşa etmenin tek nedeni, ek enerji kapakları için yeterli yer olmamasıdır. Çok az multiblok kusursuz hız aşırtmaya izin verir.

Hız aşırtma yalnızca 1 tick'e kadar mümkündür çünkü bu Minecraft'taki en küçük zaman birimidir, ancak GTNH'deki neredeyse her multiblok ek hız aşırtmaları simüle etmek için alt tickleme yapabilir veya paralel sayısını buna karşılık gelen miktarda artırabilir. Tek istisna, dilim başına 1 tick ile sınırlı olan Gelişmiş Montaj Hattı'dır.

## Paraleller

Bir paralel, orijinaliyle eşzamanlı çalışan bir tarif katıdır. Paraleller, tarifin toplam süresini artırmadan multiblokun verimini ve güç tüketimini artırır. Örneğin iki paralel, aynı anda iki kat girdi işlemek için EU/t'yi ikiye katlar. Kusursuz hız aşırtmalarda olduğu gibi toplam EU aynı kalır; bu da paralellerin mükemmel enerji verimli ve çok güçlü olduğu anlamına gelir. Paralel eklemenin toplu boyutu artırmakla AYNI olmadığını unutma -- ikincisi yalnızca TPS tasarrufu içindir ve multiblokun verimini artırmaz.

- **Toplu Boyut** - Yineleme başına daha fazla tarif, aynı EU/t, daha uzun süre.
- **Paraleller** - Yineleme başına daha fazla tarif, daha yüksek EU/t, aynı süre.

Paraleller enerji indirimlerinden SONRA ve hız aşırtmalardan ÖNCE hesaplanır. Volcanus'ta 16 saniye boyunca 2.000 EU/t tüketen bir tarif düşün; Volcanus 8 paralel sunar ve normalde gereken EU/t'nin yalnızca %90'ını kullanır. Enerji indirimi önce temel tarifi 16 saniyede 1.800 EU/t'ye düşürür. Maksimum paralel sayısı için yeterli güç varsa multiblok 16 saniyede 8 x 1.800 = 14.400 EU/t tüketir. Hâlâ yeterli güç ve kusursuz bir hız aşırtma sağlayacak kadar yüksek bobin varsa multiblok 4 saniyede 4 x 14.400 = 57.600 EU/t tüketir. Son olarak, bir kusurlu hız aşırtma güç tüketimini 2 saniyede 4 x 57.600 = 230.400 EU/t'ye çıkarır.

```
EU/t = Base EU/t x EU Usage x Parallels x 4^Overclocks
```

## Sorun Giderme

Bir multiblok çalışmıyorsa yapılacak ilk şey, neyin yanlış olduğuna dair bir ipucu için kontrolcüyü açmaktır. Aşağıda bazı yaygın hata mesajları ve ne anlama gelebilecekleri yer alıyor. Her şey başarısız olursa, tüm multibloku <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> ile yeniden inşa etmeden önce wiki'deki ipucunu ve yapım gereksinimlerini tekrar oku.

### \*\* SORUNLARI VAR \*\*

- Bakım Gerekiyor
  - Bakım Kapağı GUI'sindeki aletleri kullan, **VEYA**
  - Bakım Kapağına Alet Çantasıyla sağ tıkla
    - Tam alet takımına sahip olmalı
    - Lehim Demiri şarjlı olmalı
    - Lehim malzemesi gerekir (tüketilebilir)
- Pyrotheum olmadan Volcanus - yok olmalara ve bakım sorunlarına neden olur
- Kriyotheum olmadan Cryogenic Freezer - yok olmalara ve bakım sorunlarına neden olur

### \*\* EKSİK YAPI \*\*

- Multiblok yanlış inşa edilmiş
  - Eksik parçalar - NEI'de kontrolcünün üzerine sol Shift ile gel
  - Parçalar yanlış konumda
  - Maksimumları aşıyor veya minimumları karşılamıyor
  - Yanlış kasalar - bazı bloklar görsel olarak benzer
  - Enerji Kapağı kademesi yetersiz
  - Karışık bobin veya kasa türleri
  - Kontrolcü multiblokun içine bakıyor
  - İçi boş olması gereken bir multiblokun içinde bir şey var
- Yapı tanınmadı
  - Tek bir chunk'ta inşa edilmemiş veya tamamen chunkloaded değil
  - Kontrolcüyü kır ve yerine koy

### Açılmıyor

- Güç yok
  - Güç hattında kopukluklar var / bağlı değil
  - Bir kaplama bir yerde güç iletimini engelliyor
  - Transformatörler doğru yönde değil
  - Enerji Kapağı girişi güce bakmıyor
  - Jeneratör(ler) açık ve bağlı değil
  - Jeneratör(ler)in yakıtı bitti
  - Pil Tamponunda pil yok
  - Piller şarjlı değil
  - Pil ve Tampon kademesi uyuşmuyor
- Yanlış tarif
  - Sıvılar Giriş Kapağında değil
  - Eşyalar Giriş Yolunda değil
  - Programlanmış Devre Giriş Yolunda / Kontrolcüde ayarlanmamış
  - Yanlış bileşenler, metadata ile doğrula
  - Bobinler/Kasalar/Enerji Kapağı tarif için yetersiz kademede
  - Yollardaki/kapaklardaki kullanılamayan tarif eşyaları tarafından engelleniyor
- Devre dışı
  - Yumuşak Tokmakla vurulmuş
  - Kontrolcüdeki güç düğmesine bas
- Enerji Kapağı yok - güç kabul etmek için en az bir Enerji Kapağı ekle
- Yapı yetersiz - multiblok yapılandırması tarifin ihtiyaçlarını karşılamıyor; gaz/sıvı farklı bir konumda çıkış gerektiriyor

### Açılıyor sonra Yok Ediyor / Kapanıyor

- Yetersiz güç
  - Yeterli güç üretimi yok - tarifi kontrol et
  - Diğer makineler çok fazla güç kullanıyor
  - Kablo kaybı nedeniyle yeterli güç iletilmiyor
  - Diyot veya transformatör tarafından fazla sınırlanmış
  - Pil Tamponları pil başına yalnızca 1A çıkış verir
  - Tarif hız aşırtıyor, beklenenden fazla güç tüketiyor
  - Tüm Enerji Kapakları güce bağlı değil
  - Güç kabul etmek için yeterli Enerji Kapağı yok (her biri en fazla 2A)
- Egzoz Çıkışı engellenmiş
  - Egzoz dışa bakmıyor
  - Egzozun üstünde hava bloğu yok
  - Gelişmiş Egzoz Çıkışları hava filtreleri gerektirir
- Eksik Tüketilebilirler
  - Hava Filtreleri ve Türbinler için türbin eşyası
  - Cryogenic Freezer için Kriyotheum
  - Volcanus için Pyrotheum

### Yanlış Çıktı

- Yanlış devre ayarlanmış
- Çoklu yol kurulumunda giriş ayrıştırma etkin değil
- Rock Breaker için Su/Lav koşulları karşılanmadı

### Rastgele Yok Ediyor / Aralıklı Çalışıyor

- Güç kaybı - başka bir makine amper için yarışıyor veya güç üretimi tutarsız
- İş Bitti - işlenecek bileşen kalmadı veya Hava Filtresi için chunk'larda kirlilik yok

### Daha Fazla Güç Gerekiyor

- Enerji Kapağı kademesi yetersiz
- Tarif için kasa/gövde kademesi yetersiz

### Taştı

- Bobin / ısı kasaları uyuşmuyor

### Yeterli Çıkış Alanı Yok

- Çıkışta tarif için yeterli yuva yok
- Çıkış dolu/eksik
- Yönlü ürünler için çıkış eksik
  - EYF'nin gaz için üstte bir kapağa ve sıvılar için altta bir kapağa ihtiyacı var

### Geçerli Tarif Bulunamadı

- Geçerli eşya kombinasyonu yok / yanlış eşya
- Giriş kapağı/yolu eksik