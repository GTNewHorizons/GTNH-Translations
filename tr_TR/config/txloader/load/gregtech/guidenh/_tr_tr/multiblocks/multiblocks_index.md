---
navigation:
  title: "Multiblok Makineleri"
  icon: structurelib:item.structurelib.constructableTrigger
  parent: /index.md
  position: 9
categories:
  - Makineleri
---

# Multiblok Makineleri

**Multiblok makineleri**, birden çok bloktan inşa edilen makinelerdir. Boyutları kompakt <ItemLink id="gregtech:gt.blockmachines:1169" showIcon="left" /> makinelerden devasa <ItemLink id="gregtech:gt.blockmachines:15411" showIcon="left" /> makinelere kadar uzanır. GregTech multibloklarının her zaman bir **kontrolcü bloğu** vardır, genellikle belirli bir amaca hizmet ederler ve varsa karşılık gelen [tek bloklu makineden](../singleblock/singleblock_index.md) her zaman daha hızlı veya daha verimlidirler. [Yalnızca hız aşırtma](../tierskipping_overcloking_parallels/overclocking.md) yapabilen [tek bloklu makinelerin](../singleblock/singleblock_index.md) aksine, multibloklar ayrıca **[kademe atlama](../tierskipping_overcloking_parallels/tierskipping.md)** ve **[paraleller](../tierskipping_overcloking_parallels/parallels.md)** kullanabilir.

Çoğu multiblokun benzersiz kasaları ve yapıları olsa da eşya, sıvı ve güç G/Ç'si **işlevsel kapaklar** aracılığıyla neredeyse evrenseldir. Multiblok yapılarını önizlemek ve hızlıca inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullanabilirsin.

# Kategoriler

## Buhar Makineleri

Sekiz buharlı multiblok vardır:
<ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" />, ve
<ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" />.
Buharlı tek bloklu makinelerin çalıştıramadığı Santrifüj, Mikser ve Cevher Yıkama Tesisi tariflerini çalıştırabilirler.

- Buhar almak için **Buhar Kapakları** kullan; kapak başına 64.000 L tampon vardır.
- Bakım gerektirmezler.
- Buhar tariflerini sabit %125 hız ve %62,5 buhar maliyetiyle çalıştırırlar.
- Sabit maksimum 8 paralele sahiptirler.

- [Buhar Ocağı](./steam/steam_hearth.md): Eşyaları partiler halinde eritir, Patlatma ve Tütsüleme modlarını destekler ve yüksek basınçlı bir yapıya yükseltilebilir.
- [Buhar Kaynaştırıcı](./steam/steam_alloy_smelter.md): Alaşımlar yapar ve kalıplama tariflerini partiler halinde işler; sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır.
- [Buhar Presi](./steam/steam_presser.md): Plakalar ve Uzun Çubuklar yapar ve cevherleri partiler halinde işler; sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır.
- [Buhar Karıştırıcı](./steam/steam_mixer.md): Tozları ve sıvıları partiler halinde karıştırır; hücreler yerine sıvı kullanan tarifler, sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır.
- [Buhar Ayrıştırıcı](./steam/steam_centrifuge.md): Cevher tozlarını arındırır ve Yapışkan Reçineyi partiler halinde işler; sekiz paralel, sıvı çıktıları ve yüksek basınçlı yapı yükseltmesi vardır.
- [Buhar Öğütücü](./steam/steam_grinder.md): Cevherleri ve malzemeleri partiler halinde öğütür; sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır; yalnızca tarifin ilk eşya çıktısını üretir.
- [Buhar Kompresörü](./steam/steam_compressor.md): Malzemeleri bloklara sıkıştırır ve Sıkıştırılmış Hava Hücreleri üretir; sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır.
- [Buhar Arındırıcı](./steam/steam_washer.md): Mineralleri partiler halinde yıkar; Cevher Yıkayıcı ve Basit Yıkayıcı modları, sekiz paralel ve yüksek basınçlı yapı yükseltmesi vardır.

## Elektrik Makineleri

Elektrik multiblokları birçok biçimde gelir ve güç almak için **Enerji Kapakları** kullanır. Bakım gerektirirler, ancak Enerji Kapaklarını daha yüksek kademeli olanlarla değiştirerek onları yükseltebilirsin.

- [Elektrik Yüksek Fırını](./lv/electric_blast_furnace.md): Alüminyum ve yüksek sıcaklık malzemelerini işlemek için Isıtma Bobinlerini kullanır ve erken iki kapaklı kademe atlamayı sunar.
- [Vakum Dondurucu](./hv/vacuum_freezer.md): Sıcak külçeleri soğutur ve belirli sıvıları ve soğutucu hücrelerini işler.
- [Damıtma Kulesi](./hv/distillation_tower.md): Bir sıvıyı tüm fraksiyonlarına aynı anda ayırır ve her birini ayrı bir katmanda çıkarır.
- [Temiz Oda](./hv/cleanroom.md): Dahili makinelerin belirli devre ve diğer tarifleri çalıştırması için temiz bir çevre sağlar; işleme başlamadan önce %100 temizliğe ulaş.

# Yapı

## Kontrolcü Bloğu

GregTech multibloklarının her zaman bir kontrolcü bloğu vardır ve kontrolcünün ön yüzü tüm yapının yönünü belirler.

- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /><kbd>Sağ tık</kbd> ön yüze -> yapıyı döndür.
- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /><kbd>Sağ tık</kbd> başka bir yüze (GT 3x3 İngiliz anahtarı kurallarını kullanarak) -> kontrolcünün baktığı yönü değiştir.
- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> -> yapıyı aynala.

Bazı kontrolcüler yukarı veya aşağı bakabilir. <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> gibi birkaç makine yalnızca yatay olarak bakabilir.

## Önizleme ve İnşa

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan:

- Kontrolcüye <kbd>Sağ tık</kbd> -> hologramı önizle.
- <kbd>Shift</kbd> + kontrolcünün üzerinde <kbd>Sağ tık</kbd> basılı tut -> envanterindeki eşleşen blokları otomatik olarak yerleştir.
- Havada <kbd>Sağ tık</kbd> -> alt kanalı yapılandır.

## Kapaklar

Çoğu multiblok, G/Ç için ortak işlevsel kapaklar kullanır. Kapaklar kademeler halinde gelir (ULV'den UHV+'a kadar) ve her kademe farklı kapasite veya işlem hacmi sağlar.

| Kapak Türü | Amaç |
|------------|---------|
| Giriş Yolu / Çıkış Yolu | Eşyalar |
| Giriş Kapağı / Çıkış Kapağı | Sıvılar |
| Enerji Kapağı / Dinamo Kapağı | Güç |
| Buhar Kapağı | Buhar (yalnızca buharlı multibloklar) |
| Bakım Kapağı | Bakım sorunlarını gider |
| Egzoz Çıkışı | Kirliliği tahliye et |

Yapı hâlâ minimum kasa sayısını karşıladığı sürece genellikle istediğin kadar kapak yerleştirebilirsin, ancak Bakım Kapakları genellikle bir taneyle sınırlıdır. Ucuz kapaklar genellikle pahalı yapı bloklarının yerini alabilir.

## Paylaşım

GregTech multiblokları genellikle **duvar paylaşımına** izin verir: iki makine aynı duvardaki yapı bloklarını ve kapakları paylaşabilir.

- **Bakım Kapakları**, **Giriş Yolları**, **Giriş Kapakları** ve **Egzoz Çıkışları** paylaşılabilir.
- **Çıkış Yollarını** veya **Çıkış Kapaklarını** paylaşırken dikkatli ol, çünkü taşma çıktıları yok edebilir.
- **Enerji Kapaklarını** paylaşırken de dikkatli ol: genellikle bir Enerji Kapağı ikiden fazla makine tarafından paylaşılmamalıdır ve çift kapaklı kademe atlama için kullanılan Enerji Kapakları paylaşılmamalıdır.

## Yapı Kontrolleri

Multibloklar yapılarının tamamlanıp tamamlanmadığını sürekli olarak yeniden kontrol etmez:

- Kontrolcü ilk kez yerleştirildiğinde -> yapı 100 tik sonra kontrol edilir.
- Yakındaki bir blok güncellendiğinde -> 50 tiklik bir geri sayım başlar ve her yeni güncelleme bu geri sayımı sıfırlar.
- GUI'deki "Yapı Kontrolünü Güncelle" düğmesine bastığında -> yapı 1 tik sonra kontrol edilir.

Yapıyı bu gecikme aralığı içinde kırıp yeniden kurmak **sıcak değiştirmeyi** etkinleştirir. Bir Madde Manipülatörü (MK I veya üstü) bu tür sıcak değiştirmeleri 1 tik içinde tamamlayabilir.

# Grafik Kullanıcı Arayüzü

GUI'yi açmak için kontrolcü bloğuna <kbd>Sağ tık</kbd> yap. Çoğu makine standart GregTech GUI'sini kullanır. ZPM'den itibaren bazı geç oyun makineleri TecTech tarzı GUI'yi kullanır.

## GregTech Tarzı GUI

Sağ taraftaki düğmeler temel aç/kapat seçeneklerini sunar:

| Düğme | İşlev |
|--------|----------|
| Güç paneli | Paralel yapılandırma ve güç arızası olay ayarlarını açar |
| Yapı kontrolünü güncelle | Bir yapı kontrolünü zorlar |
| Güç anahtarı | Makineyi açar veya kapatır; kapatılırsa mevcut tarifin bitmesine izin verilir |

Orta sol alan en az dört yapılandırma seçeneği sunar, ancak her makine hepsine izin vermez:

- **Hiçlik Modu**: Hiçbir Şeyi Hiçleme / yalnızca eşyalar / yalnızca sıvılar / ikisi de.
- **Giriş Ayrıştırması**: farklı Giriş Yollarındaki eşyaların aynı tarifte kullanılmasını önler.
- **Toplu Mod**: tarif kontrollerini ve TPS maliyetini azaltmak için aynı tarifin tekrarlanan kopyalarını birleştirir.
- **Tarifi Kilitle**: makinenin başka tarifler çalıştırmasını önler.

Alet kısayolları (kontrolcüye <kbd>Sağ tık</kbd>, dayanıklılık tüketir):

- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> -> yapıyı döndür.
- <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> -> giriş ayrıştırmasını aç/kapat / bazı makine modlarını değiştir.
- <ItemLink id="gregtech:gt.metatool.01:26" showIcon="left" /> -> toplu modu aç/kapat.
- <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> -> gücü aç/kapat.
- <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> -> sessize al/sesi aç.

## TecTech Tarzı GUI

Yalnızca birkaç ZPM ve sonrası makine bunu kullanır; örneğin <ItemLink id="gregtech:gt.blockmachines:15300" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15311" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:14003" showIcon="left" />.

Onu tanımlayan özellik gösterge ışığı sistemidir:
- Mavi yanıp sönüyor: parametre çok düşük.
- Yeşil: normal.
- Turuncu yanıp sönüyor: parametre çok yüksek.
- Anahtar bir parametrenin ışığına genellikle ayarı değiştirmek için sol tıklanabilir.

TecTech makineleri taşma durumunda **her zaman yok eder**, bu yüzden güvenli hiçlik düğmesinin pratikte bir etkisi yoktur. Parametre depolama kartları ayarları bir TecTech makinesinden diğerine kopyalayabilir.

# Bakım

## Bakım Sorunları

Yalnızca yapısı <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> gerektiren multibloklar bakım gerektirir. Kontrolcü yerleştirildiğinde altı bakım sorununun tamamı varsayılan olarak mevcuttur ve makine çalışmadan önce giderilmelidir.

| Sorun | Alet |
|---------|------|
| "Bir boru gevşek." | İngiliz Anahtarı |
| "Bazı vidalar gevşek." | tornavida |
| "Bir şey sıkışmış." | Yumuşak Tokmak |
| "Plakalar bükülmüş." | Sert Çekiç |
| "Buraya ait olmayan bir şey var." | Levye |
| "Devrede kısa devre var." | Lehim Demiri (10k EU + 1 lehim malzemesi tüketir) |

**Nasıl ortaya çıkarlar**: her 1000 tik sürekli çalışmada rastgele bir bakım sorunu oluşturma şansı 1/6000'dir. Ortalama olarak bu, yaklaşık her 83,3 saatte bir sorun demektir.

**Ceza**: her bakım sorunu güç kullanımını %10 artırır. Altısı da mevcutsa makine kapanır. Bazı makinelerin özel cezaları vardır; örneğin <ItemLink id="gregtech:gt.blockmachines:32013" showIcon="left" /> bir bakım sorunu ortaya çıktığında kinetik enerjisini anında sıfıra düşürür.

## Onarım Yöntemleri

| Aşama | Yöntem |
|-------|--------|
| LV | Gerekli tüm aletleri ve lehimi içeren bir Alet Çantasıyla Bakım Kapağına <kbd>Sağ tık</kbd> yap |
| MV | FAL-84 Güçlendirilmiş Koli Bandı ile onar |
| HV | Asa Odağı: Bakım (vis tüketir) |
| IV | Toplu yönetim için Drone Bağlantı Modülü ve Drone Merkezi |
| LuV | Otomatik Bakım Kapağı (malzeme tüketir) |
| UV | Hata Ayıklama Bakım Kapağı (ücretsiz otomatik bakım) |

Bir Bakım Kapağına bir kez önceden bakım yapabilirsin. Makine bu durumu okuduktan sonra kapağın etkin bakım durumunu temizler ve ardından bir ek tamponlanmış bakım durumu depolar. Daha sonra bir bakım sorunu ortaya çıktığında kapak, sorunu gidermek için otomatik olarak bir tamponlanmış bakım durumunu tüketir.

# Tarif Algılama

Bir multiblok açıldığında, eşleşen bir tarif aramak için tüm kapaklarını tarar. Buradaki kilit kavram **giriş grubu**dur: aynı giriş grubunda olmayan malzemeler asla tek bir tarifte birleştirilmez.

## Giriş Ayrıştırması

Giriş Ayrıştırması etkinleştirildiğinde, her Giriş Yolu tüm Giriş Kapakları ve kontrolcünün envanter yuvalarıyla birlikte bağımsız bir giriş grubu oluşturur. Bu, farklı yollardaki malzemelerin yanlışlıkla istenmeyen bir tarife karışmasını önlemek için çok kullanışlıdır.

## Tarif Önceliği

Farklı giriş grupları arasındaki tarif kontrolleri kontrol edilebilir bir öncelik sırasını izler.
1. **Desen giriş kapakları/yolları** (<ItemLink id="gregtech:gt.blockmachines:2715" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:2714" showIcon="left" />) normal kapaklara göre önceliklidir.
2. **Tablo rengiyle boyanmış** normal giriş kapakları ve yolları. <ItemLink id="gregtech:gt.metaitem.01:32468" showIcon="left" /> GUI'sinde gösterilen sırayı izleyerek öncelik siyahtan beyaza doğru azalır.
3. Giriş Yolları, Giriş Kapaklarına göre önceliklidir.
4. Fiziksel konum: önden arkaya, yukarıdan aşağıya, soldan sağa.

> [!TIP]
> Kapakları tablo rengiyle boyamak, tarif yürütme sırasını kontrol etmenin bir yoludur.

# Tarif Yürütme

## Kademe Atlama

Bkz. **[Kademe Atlama](../tierskipping_overcloking_parallels/tierskipping.md)**.

Aynı kademeden iki Enerji Kapağı kullanarak 4A sağlamak, makinenin voltaj kademesinin beklediği nominal güce ulaşmasını ve tarifleri bir kademe yukarıda çalıştırmasını sağlar. Buna **çift kapaklı kademe atlama** denir. Bunu muhtemelen ilk kez <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> ile kullanacaksın.

IV'ten itibaren bazı makineler artık kademe atlayamaz; örneğin <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" />.

## Paraleller

Bkz. **[Paraleller](../tierskipping_overcloking_parallels/parallels.md)**.

Paraleller, makinenin aynı zaman aralığında aynı tarifin birden çok kopyasını işleme yeteneğidir. [Tek bloklu makineler](../singleblock/singleblock_index.md) bunu yapamaz.

Genel olarak, maksimum paralel sayısının her $$4^n$$ katı, pratikte kabaca $$n$$ kusursuz hız aşırtmaya eşdeğerdir. Paraleller yalnızca aynı tarife uygulanır.

## Hız Aşırtma

Bkz. **[Hız Aşırtma](../tierskipping_overcloking_parallels/overclocking.md)**.

Standart 4/2 kusurlu hız aşırtmaların yanı sıra bazı multibloklar 4/4 kusursuz hız aşırtmayı da destekler ve bazıları özel hız aşırtma kuralları kullanır. Multibloklar 1 tik'in altına da (1tOC) hız aşırtabilir.

Hesaplama sırası: önce paraleller, sonra hız aşırtmalar (önce kusursuz, sonra kusurlu).

## Toplu Mod

Toplu Mod, aynı tarifin tekrarlanan kopyalarını tek büyük bir tarifte birleştirir. **Zaman indirimi sağlamaz ve paralel eklemez**. Tek amacı tarif kontrol sıklığını azaltmak ve TPS maliyetini düşürmektir.

Toplu Mod etkinleştirildiğinde makine tarif süresini 128 tik'e uzatmaya çalışır. Bu, birim zaman başına çıktıyı değiştirmez. Buharlı multibloklar Toplu Mod'u kullanamaz.

# Arızalar

[Tek bloklu makinelerin](../singleblock/singleblock_index.md) aksine, bir multiblok arızalandığında **tarifi tamamen iptal eder ve girdileri geri vermez**.

| Arıza | Çözüm |
|---------|-----|
| "Yapı tamamlanmamış." | Yapıda eksik blok olup olmadığını kontrol et |
| "Egzoz Çıkışı, Bakım Kapağı veya benzeri eksik." | Gerekli kapağı ekle |
| "Makine hasarı nedeniyle kapatıldı." | Tüm bakım sorunlarını gider |
| "Tarif daha fazla güç gerektiriyor." | Enerji Kapaklarının sayısını ve mevcut amperajı kontrol et |
| "Tarifin başlaması için daha yüksek voltaj gerekiyor." | Voltaj kademesinin yeterince yüksek olup olmadığını kontrol et |
| "Eşya/sıvı çıktısı için yeterli alan yok." | Daha fazla Çıkış Yolu veya Çıkış Kapağı ekle |
| "Enerji eksikliği nedeniyle kapatıldı." | Güç kaynağını kontrol et |

Bir arıza olduğunda, boyuttaki güç arızası uyarı simgelerini kaldırmak için `/powerfails clear` veya güç arızası bilgilerini paylaşmak için `/sp invite <playerID>` kullanabilirsin.

# Patlamalar

[Tek bloklu makinelerde](../singleblock/singleblock_index.md#explosions) olduğu gibi, bir multibloktaki herhangi bir **dahili EU tamponu olan enerji verilmiş kapak** yağmurda veya karda patlayabilir. Kontrolcü blokları, yapı blokları ve güç tamponlamayan kapaklar yağmurda veya karda patlamaz. Bir Enerji Kapağına aşırı voltaj vermek de patlamaya neden olabilir.