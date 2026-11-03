---
navigation:
  title: Multiblok Makineler
  icon: structurelib:item.structurelib.constructableTrigger
  parent: ./gtnh_basics_index.md
---

# Multiblok Makineler

> [!NOTE]
> Bazı bağlantılar, sayfaları şu anda mevcut olmadığı için bozuk. GTNH'nin geliştirilmesine [rehbere katkıda bulunarak](https://github.com/GTNewHorizons/GTNH-Guide-Pack) destek olabilirsin!

Bir **Multiblok**, iki veya daha fazla bloktan inşa edilen bir makinedir. Boyutları küçük Termal Rafinerilerden Tanrıların Ocağı gibi devasa üst yapılara kadar uzanır. Genellikle çok özel bir amaca hizmet ederler ve varsa tek bloklu eşdeğerlerinden her zaman daha iyidirler (yani daha hızlı çalışır, daha iyi tarifler yapar). Çoğu multibloğun kendine özgü kasaları ve yapısı vardır, ancak eşya, sıvı ve enerji giriş/çıkışı (G/Ç) neredeyse evrenseldir. Eşyalar veriyollarıyla, sıvılar kapaklarla, güç ise enerji/dinamo kapaklarıyla aktarılır. Makineyi onarmak için bir bakım kapağı ve kirliliği dışarı atmak için bir egzoz çıkışı da vardır. Hangi veriyollarının/kapakların gerekli olduğunu ve genel yapıya nerede oturduğunu görmek için ipucunu ve/veya <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> öğesini kullan.

> [!IMPORTANT]
> GTNH'deki tüm multibloklar GregTech'ten değildir. Bu sayfadaki bilgilerin hiçbirine uymayan, başka modlardan gelen birkaç tanesi vardır (ör. Railcraft Kazanları ve İzabe Ocakları). Ayrıntılar için kendi sayfalarını ziyaret et.

---

# İnşa

Multibloklar çeşitli şekil, boyut ve kasalarda gelse de eşya, sıvı ve enerji G/Ç'si için ortak birçok bileşen vardır. Aşağıdaki alt bölümler her birinin amacını ve işlevini açıklar. Multiblokların nadiren TÜM bunlara ihtiyaç duyduğunu ve miktarları ile konumlarında kısıtlamalar olabileceğini unutma. Bir multibloğun inşa gereksinimleri hakkında ayrıntılı bilgi için her zaman ipucunu ve <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> öğesini kontrol et.

## Kontrolcü

Kontrolcü multibloğun kalbidir. Tüm yapının yerleşimini ve yönünü olduğu kadar makinenin çalışma ayarlarını da belirler. GUI'yi açmak için kontrolcüye sağ tıkla; GUI'de (1) üstte makinenin adı, (2) makinenin durumu, (3) ses açma/kapama, (4) birkaç yapılandırılabilir parametre, (5) güç paneli ve (6) varsa manuel geçersiz kılmalar bulunur. Yapılandırılabilir parametrelerin ve manuel geçersiz kılmaların her birinin kısa açıklaması aşağıdadır.

- **Yok Etme Modu** - Çıkış veriyolusunda ve/veya çıkış kapağında yer olmadığında multibloğun davranışını belirler. Yalnızca eşyaları, yalnızca sıvıları veya ikisini birden yok etmeyi seç. Hiçbirini Yok Etme, tüm ürünler için yeterli yer olana kadar makineyi geçici olarak duraklatır.
- **Girdi Ayrıştırması** - Farklı giriş yollarındaki KATI bileşenlerin, programlanmış devreler dahil, aynı tarifte kullanılmasını önler. Bu özellikle tarif çakışması ihtimali yüksek multibloklar için kullanışlıdır.
- **Toplu Mod** - Aynı tarifin birden fazla kopyasını tek büyük tarif olarak çalıştırır. Bu, herhangi bir süre indirimi sağlamaz veya makinenin verimini artırmaz. Amacı, tarif kontrolü sayısını azaltarak lag'i düşürmek ve TPS'yi iyileştirmektir.
- **Tarifi Kilitle** - Multibloğun başka tarifler çalıştırmasını önler. Bu, multiblok çalışırken veya istenen tariften önce ayarlanabilir.
- **Yapıyı Güncelle** - Yapı kontrolünü zorlar. Multibloklar zaten periyodik yapı kontrolü yapar, ancak bu birkaç saniye (veya dakika) beklemekten kurtarabilir.
- **Güç Anahtarı** - Multibloğu etkinleştirir veya devre dışı bırakır. Bu, aktif tarifleri KESMEZ.

Güç panelinde iki seçenek vardır. Birincisi, varsayılan olarak mevcut maksimum değere ayarlanan maksimum paralel sayısını belirlemektir. Enerji verimliliği üzerinde mutlak hassasiyet gerektiren çok özel bir senaryo yoksa bunu düşürmenin veya değeri elle ayarlamanın pek bir nedeni yok. İkinci seçenek, sohbetteki mesajı ve kontrolcüye uzaktan baktığında görünen yanıp sönen güç kesintisi simgesini içeren güç kesintisi olaylarını açar/kapatır. Çok oyunculu modda, diğer oyuncuları aynı SpaceProject ekibine davet etmek ve güç kesintisi bilgilerini paylaşmak için ilk komutu kullan. Dünyadaki tüm güç kesintisi simgelerini hemen temizlemek için ikinci komutu kullan.

```
/sp invite <name>
/powerfails clear
```

GUI'ye girmeden makinenin çalışma ayarlarını değiştirmenin birkaç özgün etkileşimi ve kısayolu da var. Bunların hepsi, elinde bir tür GregTech aletiyle kontrolcüye sağ tıklamayı içerir. Bu, aletin dayanıklılığını düşürür, ancak Loki'nin Yüzüğü ile aynı anda birçok makineyi hızlıca yapılandırmak için çok iyi çalışır.

- **İngiliz Anahtarı** - Kontrolcüyü ve dolayısıyla tüm yapıyı döndürür. Yatay olarak çevirmek için eğilip sağ tıkla.
- **Tornavida** - Girdi ayrıştırmasını etkinleştirir/devre dışı bırakır. Ayrıca belirli multiblokların modunu değiştirmek için kullanılır.
- **Tel Kesiciler** - Toplu modu etkinleştirir/devre dışı bırakır.
- **Yumuşak Tokmak** - Makineyi etkinleştirir/devre dışı bırakır.
- **Çekiç** - Ses susturmayı etkinleştirir/devre dışı bırakır.
- **Lehim Demiri** - Kaplamalardan gelen Kızıltaş sinyalinin gücünü (güçlü/zayıf) ayarlar. Bu yalnızca kontrolcülere özgü değildir.

## Veriyolları

<ItemImage id="minecraft:chest" /> **Giriş Yolu** / <ItemImage id="minecraft:chest" /> **Çıkış Yolu**

Giriş ve çıkış yolları sırasıyla KATI bileşenleri yerleştirmek ve çıkarmak içindir. Sıvılar ve gazlar hücreler, kovalar veya benzeri kaplar aracılığıyla sağlanamaz. Giriş yolları bitişik envanterlerden otomatik olarak çekmez, ancak çıkış yolları varsa bitişik envanterlere otomatik olarak iter. Yolun kademesi, mevcut kapasiteyi veya toplam eşya yuvası sayısını belirler:

| Kademe | ULV | LV | MV | HV+ |
|------|-----|----|----|-----|
| Yuva | 1 | 4 | 9 | 16 |

Multiblokta kullanımı olmayan hiçbir bileşenin yoluna girmesini önleyen filtreyi etkinleştirmek/devre dışı bırakmak için bir giriş yoluna tornavidayla sağ tıkla. Sıralama ve sınırlama modunu etkinleştirmek/devre dışı bırakmak için tornavidayla giriş yoluna eğilip sağ tıkla. Sıralama modu eşyaları sürekli en üstteki yuvialara iter, sınırlama modu ise bir eşyanın birden fazla yığınının yoluna girmesini önler. Çıkış yollarının GUI'sinde de onları belirli eşyalara kilitleyen bir filtre vardır (NEI'den sürükle).

- **Süper Veriyolları** - Normal giriş/çıkış yollarının yükseltmesidir, ancak tek farkları yuva kapasiteleridir. Normal veriyollar 16 yuvayla sınırlıyken süper veriyollar 32-160 yuva aralığındadır. Ancak sorun şu ki çok daha pahalıdırlar ve üretim için Kademe+3 normal giriş yolu gerektirirler. Örneğin LV süper veriyolu beş LV konveyör modülü, iki LV motor ve bir EV giriş yolundan üretilir.

- **Stoklama Giriş Yolu (ME)** ve **Çıkış Yolu (ME)** - Normal giriş/çıkış yollarından daha da iyi bir yükseltmedir, çünkü kesintisiz eşya G/Ç'si için doğrudan bir AE2 ağına bağlanırlar. ME kanallarının diğer veriyolları/kapaklar dahil herhangi bir tarafa bağlanmasına izin vermek için tel kesicilerle sağ tıkla. Gelişmiş sürüm, ağdaki herhangi bir eşyayla kendini stoklamasına olanak tanıyan otomatik çekmeyi bile destekler.

## Kapaklar

<ItemImage id="minecraft:cauldron" /> **Girdi Kapağı** / <ItemImage id="minecraft:cauldron" /> **Çıkış Kapağı**

Girdi ve çıkış kapakları sırasıyla SIVI bileşenleri yerleştirmek ve çıkarmak içindir. Girdi kapakları bitişik envanterlerden otomatik olarak çekmez, ancak çıkış kapakları varsa bitişik envanterlere otomatik olarak iter. Kapağın kademesi mevcut kapasiteyi belirler. Girdi kapakları, envanterlerine bir yığın büyük sıvı hücresi koyarak teknik olarak bu miktarlardan çok daha fazlasını "tutabilir".

| Kademe | ULV | LV | MV | HV | EV | IV | ... |
|------|-----|----|----|----|----|----|-----|
| Kapasite | 8.000 L | 16.000 L | 32.000 L | 64.000 L | 128.000 L | 256.000 L | ... |

Buharın ve/veya diğer sıvıların çıktı olarak verilip verilmeyeceğini değiştirmek için bir çıkış kapağına tornavidayla sağ tıkla. Alternatif olarak, onu belirli bir sıvıya kilitlemek için çıkış kapağının GUI'sindeki filtreyi ayarla (NEI'den sürükle).

- **Dörtlü Giriş Kapakları** - Normal giriş kapaklarının bir yükseltmesidir ve aynı kademedeki normal bir girdi kapağının 1/4 kapasitesinde, aynı anda dört farklı sıvı tutabilir. Birden fazla sıvıyı etrafta taşımak için dörtlü sıvı borularıyla güzel bir ikili oluştururlar.

- **Stoklama Girdi Kapağı (ME)** ve **Çıkış Kapağı (ME)** - Normal girdi/çıkış kapaklarından daha da iyi bir yükseltmedir, çünkü kesintisiz sıvı G/Ç'si için doğrudan bir AE2 ağına bağlanırlar. ME kanallarının diğer veriyolları/kapaklar dahil herhangi bir tarafa bağlanmasına izin vermek için tel kesicilerle sağ tıkla. Gelişmiş sürüm, ağdaki herhangi bir sıvıyla kendini stoklamasına olanak tanıyan otomatik çekmeyi bile destekler.

## Enerji ve Dinamo Kapakları

<ItemImage id="minecraft:redstone_block" /> **Enerji Kapağı** / <ItemImage id="minecraft:redstone_block" /> **Dinamo Kapağı**

Bunlar, belirli bir gerilim kademesinde güç yerleştirmek ve çıkarmak içindir. Daha spesifik olarak, standart bir enerji kapağı bir multibloğa 2A'ya kadar güç sağlayabilir ve standart bir dinamo kapağı bir multibloktan 1A'ya kadar güç çekebilir. Bu kapaklarda doğru gerilim ve amperaj kullandığından çok emin ol, aksi halde kablolar yanabilir, bileşenler yok olabilir ve makineler patlayabilir.

- **Tamponlu Dinamo Kapakları** - Standart dinamo kapaklarının küçük bir yükseltmesidir ve bir multibloktan 4A'ya kadar güç çekebilir. Ayrıca gidecek yeri olmadığında güç depolamak için biraz daha büyük bir dahili tamponları vardır. *(2.9 itibarıyla kullanımdan kaldırıldı - bunun yerine 4A Çok Amperli kapak kullan.)*

- **Çok Amperli Kapaklar** - Standart enerji/dinamo kapaklarının bir yükseltmesidir ve bir multibloğa/multibloktan 64A'ya kadar güç aktarabilir. İzin verilip verilmedikleri büyük ölçüde multibloğa bağlıdır.

- **Lazer Kapakları** - Çok daha sonra açılır ve lazer vakum boruları aracılığıyla bir multibloğa/multibloktan milyonlarca amper aktarabilir. Yine, izin verilip verilmedikleri büyük ölçüde multibloğa bağlıdır.

## Bakım Kapağı

<ItemImage id="minecraft:iron_door" /> **Bakım Kapağı**

Bu kapak, bakım sorunlarını onarmak içindir -- her biri multibloğun güç tüketimini %10 artıran rastgele olaylar. Toplamda altı farklı bakım sorunu vardır ve hepsinin aynı anda bulunması multibloğu kapatmaya yeter. Her biri kontrolcüde çok özel bir mesaj oluşturur ve çok özel bir GregTech aletine karşılık gelir. WAILA ayrıca kontrolcüye bakarken kırmızı metinle **SORUNLAR VAR** gösterir.

Bakım sorunlarını, bakım kapağını açıp gerekli aleti eline alıp ortadaki düğmeye sol tıklayarak onar. Bu, her kullanımda az miktarda dayanıklılık ve/veya şarj tüketir.

| Bakım Sorunu | Onaran Alet |
|-------------------|-------------|
| "Boru gevşek" | İngiliz Anahtarı |
| "Vidalar gevşek" | Tornavida |
| "Bir şey sıkışmış" | Yumuşak Tokmak |
| "Kaplamalar çökük" | Çekiç |
| "Devreler yanmış" | Lehim Demiri |
| "Bunun orada olmaması gerek" | Levye |

Her 50 saniyelik çalışma süresinde yeni bir bakım sorununun ortaya çıkma şansı 6.000'de 1'dir. Bu, bakım sorunları arasında ortalama 300.000 saniye veya 83,3 saat çalışma süresi demektir. Devre dışı veya boşta duran multibloklar çalışma süresini artırmaz, dolayısıyla hiçbir bakım sorunu oluşturmaz veya bunların olasılığını artırmaz. Bakım kapağı olmayan multibloklar bu mekaniği tamamen yok sayar.

Aşağıda listelenen birkaç farklı bakım kapağı türü ve onarım yöntemi vardır. Bakım kapakları makineler arasında duvar paylaşımı yapabilir, ancak yine de her biri için ayrı ayrı onarım yapılmalıdır.

- **Alet Çantası (LV)** - En fazla dokuz alet tutar ve bakım kapağına kendi dahili GUI'sinin DIŞINDAN sağ tıklandığında hepsini aynı anda uygular. Mevcut sorun(lar) ne olursa olsun içindeki tüm aletlerin dayanıklılığını ve/veya şarjını tüketir. Lehim demiri için lehim malzemesi de Alet Çantasında saklanabilir ve oradan kullanılabilir. Bir Dynamism Tablet ile otomatikleştirilebilir ve bir bakım kaplaması gerektirir.

- **BrainTech Aerospace Gelişmiş Güçlendirilmiş Koli Bandı (MV)** - Tüm bakım sorunlarını aynı anda çözen tek kullanımlık bir eşya. Bant, bakım kapağının çevresinde görsel olarak belirir, ancak bu gelecekteki bakım sorunlarını önlemez veya oluşma şanslarını azaltmaz.

- **Asa Odağı: Bakım (HV)** - Electromagic Tools'tan yeniden kullanılabilir bir Thaumcraft asa odağıdır ve 25 ignis, 25 terra ve 25 ordo karşılığında tüm bakım sorunlarını aynı anda çözer. Vis indirimleri ve tutumlu odak yükseltmesi bu onarımların maliyetini düşürebilir.

- **Drone Bağlantı Modülü (IV)** - Kapağın menzilinde aktif bir Drone Merkezi varsa tüm bakım sorunlarını otomatik olarak onarır. Kademe 1 ve Kademe 2 drone'lar her saniye düşme ve yok olma şansına sahiptir, ancak bakım sorunlarını düzeltmek tamamen ücretsizdir. Ayrıca bağlı multibloklar üzerinde uzaktan kontrol sağlar; bu, yaygın bir elektrik kesintisinden sonra çok kullanışlıdır.

- **Otomatik Bakım Kapağı (LuV)** - Herhangi bir bakım sorununu 4 koli bandı, 2 yağlayıcı hücresi, 4 çelik vida ve 2 HV devresi karşılığında otomatik olarak onarır. Dahili envanterde toplam dört yuva vardır, yani her eşya türü için bir tane.

- **Otomatik Bantlama Bakım Kapağı (UV)** - Herhangi bir bakım sorununu ücretsiz olarak otomatik onarır. Bakıma kalıcı çözüm.

## Egzoz Çıkışı

<ItemImage id="minecraft:dispenser" /> **Egzoz Çıkışı**

Bu kapak kirliliği makineden dışarı atar. Multibloğun çalışabilmesi için egzoz çıkışının önünde en az bir blok hava olmalıdır. Borular ve kablolar bile engel sayılır. Üretilen kirlilik miktarı multibloğa ve egzoz çıkışının kademesine bağlıdır:

| Kademe | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV |
|------|----|----|----|----|----|-----|-----|----|-----|
| Kirlilik | %100 | %87 | %75 | %62 | %50 | %37 | %25 | %12 | %0 |

Kirlilik devre dışıysa egzoz çıkışları yine de gereklidir, ancak kademeleri artık önemli değildir.

## Duvar Paylaşımı

GregTech multibloklarının benzersiz bir özelliği, kasa, cam, bobin, veriyolu/kapak ve daha fazlasından tasarruf etmek için yapılarının bazı kısımlarını duvar paylaşımı yapabilmeleridir. Birden fazla makinenin aynı bloğu/blokları aynı anda kullanmasına izin vermek için yapıları üst üste bindir. Bunun oyuncuya faydalı olmadığı *çok* az istisna vardır ve bu nedenle ikinci bir [Elektrikli Yüksek Fırın](../tiers/lv/electric-blast-furnace.md) veya ikinci bir Ahenk Gözü inşa ederken olsun, oyunun tamamında son derece kullanışlıdır.

Bakım ve egzoz çıkışlarını paylaşmak her zaman güvenlidir, ancak enerji kapaklarını paylaşırken dikkatli ol çünkü yalnızca 2A'ya kadar güç çekebilirler. Bir multibloğun tariflerinin 1A gücü aşmadığından emin ol ve bakım sorunlarını mümkün olan en kısa sürede onar, aksi halde ek güç maliyeti her iki makinenin de güç kesintisi yaşamasına neden olabilir.

---

# Kullanım

Multibloklar [tek bloklu makinelere](../singleblock/singleblock-index.md) çok benzer şekilde çalışsa da birkaç belirgin fark vardır. Her şeyden önce, multibloklar güç kesintisi yaşadıklarında bileşenleri **yok eder**. Tek bloklularda olduğu gibi tarifi yeniden başlatma yoktur; bileşenler kalıcı olarak kaybolur. Multiblok ayrıca kapanır ve elle yeniden başlatılması gerekir. Bunun olmasını önlemek için enerji depolamanı periyodik olarak kontrol et ve enerji seviyeleri düşükken multiblokları kapat veya kullanmayı bırak. Ayrıca kontrolcünün enerji kapaklarından önce yüklenmemesi için tüm multibloğun chunk yüklü olduğundan emin ol.

## Hız Aşırtma

Bir hız aşırtma, sağlanan güç tarifin gerektirdiğinden en az 1 gerilim kademesi yüksek olduğunda gerçekleşir. Tek bloklular bunu yalnızca daha yüksek kademeli makinelerle başarabilirken multibloklar daha yüksek kademeli ve/veya birden fazla enerji kapağı kullanabilir. Oyuncu hız aşırtma ile ilk kez [Elektrikli Yüksek Fırın](../tiers/lv/electric-blast-furnace.md) kullanırken karşılaşır; 4A LV gücü sağlamak için iki enerji kapağı gerekir, bu da 1A MV gücü simüle eder. İki farklı hız aşırtma türü vardır ve hangisinin kullanıldığı multibloğun kendisine bağlıdır. "Karma" altındakiler aynı tarifte ikisini de kullanabilir veya bir yükseltmeye bağlıdır. "Benzersiz" altındakiler kendi özel kurallarını izler ve iki kategoriye de girmez.

- **Kusurlu Hız Aşırtma** - 2x hız için 4x güç tüketir (4/2). Bu, çoğu multibloğun standart davranışıdır. Örneğin, normalde 128 EU/t ve 60 saniye süren, toplam 153.600 EU harcayan bir tarif düşün. Kusurlu bir hız aşırtma bunu 512 EU/t ve 30 saniyeye çevirir, toplam 307.200 EU. Toplam enerjinin iki katına çıktığına dikkat et; bu, ek hızın her zaman ek güç maliyetine değmeyebileceği anlamına gelir. Alternatif olarak, aynı gerilim kademesinde aynı multibloktan daha fazla inşa et, böylece aynı etkiyi yarı güçle elde et.

- **Kusursuz Hız Aşırtma** - 4x hız için 4x güç tüketir (4/4). Toplam enerji aynı kalır, bu yüzden sağlanan gerilimi/amperajı artırmanın hiçbir dezavantajı yoktur. Kusursuz hız aşırtmaya sahip aynı multibloktan birden fazla inşa etmenin tek nedeni, ek enerji kapakları için yeterli yer olmamasıdır. Çok az multiblok kusursuz hız aşırtmaya izin verir.

Hız aşırtma yalnızca 1 tick'e kadar mümkündür çünkü bu, Minecraft'taki en küçük zaman birimidir, ancak GTNH'deki neredeyse her multiblok, ek hız aşırtmaları simüle etmek için alt tick'lere inebilir veya paralel sayısını karşılık gelen miktarda artırabilir. Tek istisna, dilim başına 1 tick ile sınırlı olan Gelişmiş Montaj Hattı'dır.

## Paraleller

Bir paralel, orijinalle eşzamanlı çalışan bir tarif kopyasıdır. Paraleller, tarifin toplam uzunluğunu artırmadan bir multibloğun verimini ve güç tüketimini artırır. Örneğin iki paralel, aynı anda iki kat girdi işlemek için EU/t'yi ikiye katlar. Toplam EU, kusursuz hız aşırtmalarda olduğu gibi aynı kalır, bu da paralellerin tamamen enerji verimli ve çok güçlü olduğu anlamına gelir. Paralel eklemenin toplu iş boyutunu artırmakla AYNI olmadığını unutma -- ikincisi yalnızca TPS tasarrufu içindir ve multibloğun verimini artırmaz.

- **Toplu İş Boyutu** - Yineleme başına daha fazla tarif, aynı EU/t, daha uzun süre.
- **Paraleller** - Yineleme başına daha fazla tarif, daha yüksek EU/t, aynı süre.

Paraleller enerji indirimlerinden SONRA ve hız aşırtmalardan ÖNCE hesaplanır. Volcanus'ta 16 saniye boyunca 2.000 EU/t tüketen, 8 paralel sunan ve normalde gereken EU/t'nin yalnızca %90'ını kullanan bir tarif düşün. Enerji indirimi önce temel tarifi 16 saniye boyunca 1.800 EU/t'ye düşürür. Maksimum paralel sayısı için yeterli güç varsa multiblok 16 saniye boyunca 8 x 1.800 = 14.400 EU/t tüketir. Hâlâ yeterli güç ve kusursuz hız aşırtma sağlayacak kadar yüksek bobin varsa multiblok 4 saniye boyunca 4 x 14.400 = 57.600 EU/t tüketir. Son olarak, bir kusurlu hız aşırtma güç tüketimini 2 saniye boyunca 4 x 57.600 = 230.400 EU/t'ye çıkarır.

```
EU/t = Base EU/t x EU Usage x Parallels x 4^Overclocks
```

## Sorun Giderme

Bir multiblok çalışmıyorsa ilk yapılacak şey, sorunun ne olduğuna dair ipucu için kontrolcüyü açmaktır. Aşağıda bazı yaygın hata mesajları ve ne anlama gelebilecekleri yer alıyor. Hiçbiri işe yaramazsa, tüm multibloğu <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> ile yeniden inşa etmeden önce ipucunu ve wiki'deki inşa gereksinimlerini yeniden oku.

### \*\* SORUNLAR VAR \*\*

- Bakım Gerekli
  - Bakım Kapağı GUI'sindeki aletleri kullan, **VEYA**
  - Bakım Kapağına Alet Çantasıyla sağ tıkla
    - Tam alet takımına sahip olmalı
    - Lehim demiri şarjlı olmalı
    - Lehim malzemesi gerekli (tüketilebilir)
- Pyrotheum'suz Volcanus - yok olma ve bakım sorunlarına neden olur
- Kriyotheum'suz Kriyojenik Dondurucu - yok olma ve bakım sorunlarına neden olur

### \*\* EKSİK YAPI \*\*

- Multiblok yanlış inşa edilmiş
  - Eksik parçalar - NEI'de kontrolcünün üzerine sol Shift
  - Parçalar yanlış konumda
  - Maksimumları aşıyor veya minimumları karşılamıyor
  - Yanlış kasalar - bazı bloklar görsel olarak benzer
  - Enerji Kapağının kademesi yetersiz
  - Karışık bobin veya kasa türleri
  - Kontrolcü multibloğun iç kısmına bakıyor
  - İçi boş olması gereken bir multibloğun içinde bir şey var
- Yapı tanınmadı
  - Tek chunk'ta inşa edilmemiş veya tamamen chunk yüklenmemiş
  - Kontrolcüyü kır ve yeniden yerleştir

### Açılmıyor

- Güç yok
  - Güç hattında kopukluklar var / bağlı değil
  - Bir kaplama güç aktarımını bir yerde engelliyor
  - Transformatörler düzgün yönlendirilmemiş
  - Enerji Kapağı girişi güce bakmıyor
  - Jeneratör(ler) açık ve bağlı değil
  - Jeneratör(ler)in yakıtı bitti
  - Pil Tamponunda pil yok
  - Piller şarjlı değil
  - Pil ve Tampon kademesi uyuşmuyor
- Yanlış tarif
  - Sıvılar Girdi Kapağında değil
  - Eşyalar Giriş Yolunda değil
  - Giriş Yolunda / Kontrolcüde Programlanmış Devre ayarlanmamış
  - Yanlış bileşenler, meta verilerle doğrula
  - Bobinler/Kasalar/Enerji Kapağı tarif için yetersiz kademede
  - Veriyollarındaki/kapaklardaki kullanılamayan tarif eşyaları tarafından engelleniyor
- Devre dışı
  - Yumuşak Tokmakla vurulmuş
  - Kontrolcüdeki güç düğmesine bas
- Enerji Kapağı yok - güç almak için en az bir Enerji Kapağı ekle
- Yapı yetersiz - multiblok yapılandırması tarifin ihtiyaçlarını karşılamıyor; gaz/sıvı farklı bir konumda çıkış gerektiriyor

### Açılıyor ama Yok Ediyor / Kapanıyor

- Yetersiz güç
  - Yeterli güç üretimi yok - tarifi kontrol et
  - Diğer makineler çok fazla güç kullanıyor
  - Kablo kaybı nedeniyle yeterli güç iletilmiyor
  - Diyot veya transformatör tarafından aşırı sınırlanmış
  - Pil Tamponları pil başına yalnızca 1A verir
  - Tarif hız aşırtma yapıyor, beklenenden fazla güç tüketiyor
  - Tüm Enerji Kapakları güce bağlı değil
  - Güç kabul etmek için yeterli Enerji Kapağı yok (her biri en fazla 2A)
- Egzoz Çıkışı engellenmiş
  - Egzoz çıkışı dışarı bakmıyor
  - Egzoz çıkışının üstünde hava bloğu yok
  - Gelişmiş Egzoz Çıkışları hava filtresi gerektirir
- Eksik Tüketilebilirler
  - Hava Filtreleri ve Türbinler için türbin eşyası
  - Kriyojenik Dondurucu için Kriyotheum
  - Volcanus için Pyrotheum

### Yanlış Çıktı

- Yanlış devre ayarlanmış
- Çoklu veriyolu kurulumunda girdi ayrıştırması etkinleştirilmemiş
- Kaya Kırıcı için Su/Lav koşulları karşılanmamış

### Rastgele Yok Ediyor / Aralıklı Çalışıyor

- Güç kaybı - başka bir makine amperaj için rekabet ediyor veya güç üretimi tutarsız
- İş Tamamlandı - işlenecek bileşen kalmadı veya Hava Filtresi için chunk'larda kirlilik yok

### Daha Fazla Güç Gerekiyor

- Yetersiz Enerji Kapağı kademesi
- Tarif için yetersiz kasa/gövde kademesi

### Taşma

- Bobin / ısı kasası uyuşmazlığı

### Yeterli Çıktı Alanı Yok

- Çıktının tarif için yeterli yuvası yok
- Çıktı dolu/eksik
- Yönlü ürünler için çıkış eksik
  - EYF'nin gaz için üstte, sıvılar için altta bir kapağa ihtiyacı vardır

### Geçerli Tarif Bulunamadı

- Geçerli eşya kombinasyonu yok / yanlış eşya
- Eksik girdi kapağı/yolu