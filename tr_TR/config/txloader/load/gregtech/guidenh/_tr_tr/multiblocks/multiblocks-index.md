---
navigation:
  title: "Multiblok Makineleri"
  icon: structurelib:item.structurelib.constructableTrigger
  parent: /index.md
  position: 9
categories:
  - Makineler
---

# Multiblok Makineleri

**Multiblok makineler**, birden fazla bloktan inşa edilen makinelerdir. Boyutları kompakt <ItemLink id="gregtech:gt.blockmachines:1169" showIcon="left" />'lerden devasa <ItemLink id="gregtech:gt.blockmachines:15411" showIcon="left" />'lere kadar uzanır. GregTech multibloklarının her zaman bir **kontrolcü bloğu** vardır, genellikle belirli bir amaca hizmet ederler ve karşılık gelen [tek blok makine](../singleblock/singleblock-index.md) varsa her zaman ondan daha hızlı veya daha verimlidirler. Yalnızca [hız aşırtma](../tierskipping-overcloking-parallels/overclocking.md) yapabilen [tek blok makinelerin](../singleblock/singleblock-index.md) aksine, multibloklar ayrıca **[kademe atlama](../tierskipping-overcloking-parallels/tierskipping.md)** ve **[paraleller](../tierskipping-overcloking-parallels/parallels.md)** kullanabilir.

Çoğu multiblokun kendine özgü kasaları ve yapıları olsa da, eşya, sıvı ve güç giriş/çıkışları **işlevsel kapaklar** aracılığıyla neredeyse evrenseldir. Multiblok yapılarını önizlemek ve hızlıca inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullanabilirsin.

# Kategoriler

## Buharlı Makineler

Yalnızca yedi buharlı multiblok vardır:
<ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" />,
<ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" />, ve
<ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" />.
Buharlı tek blokların yapamadığı Santrifüj, Karıştırıcı ve Cevher Yıkama Tesisi tariflerini çalıştırabilirler.

- Buhar almak için **Buhar Kapakları** kullan; her kapakta 64.000 L tampon bulunur.
- Bakım gerektirmezler.
- Buhar tariflerini sabit %125 hızda ve %62,5 buhar maliyetiyle çalıştırırlar.
- Sabit olarak en fazla 8 paralel sınırına sahiptirler.

## Elektrikli Makineler

Elektrikli multibloklar birçok biçimde gelir ve güç almak için **Enerji Kapakları** kullanır. Bakım gerektirirler, ancak Enerji Kapaklarını daha yüksek kademeli olanlarla değiştirerek onları yükseltebilirsin.

- [Vakum Dondurucu](./vacuum_freezer.md): Sıcak külçeleri soğutur ve belirli sıvıları ve soğutucu hücrelerini işler.
- [Damıtma Kulesi](./distillation_tower.md): Bir sıvıyı tek seferde tüm fraksiyonlarına ayırır ve her birini kendine ayrılmış bir katmanda çıkarır.

# Yapı

## Kontrolcü Bloğu

GregTech multibloklarının her zaman bir kontrolcü bloğu vardır ve kontrolcünün ön yüzü tüm yapının yönünü belirler.

- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /><kbd>Sağ tık</kbd> ön yüz -> yapıyı döndür.
- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /><kbd>Sağ tık</kbd> başka bir yüz (GT 3x3 somun anahtarı kurallarıyla) -> kontrolcünün baktığı yönü değiştir.
- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> -> yapıyı aynala.

Bazı kontrolcüler yukarı veya aşağı bakabilir. <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> gibi birkaç makine yalnızca yatay olarak bakabilir.

## Önizleme ve İnşa

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan:

- Kontrolcüye <kbd>Sağ tık</kbd> -> hologramı önizle.
- Kontrolcü üzerinde <kbd>Shift</kbd> + <kbd>Sağ tık</kbd> basılı tut -> envanterindeki uygun blokları otomatik yerleştir.
- Havaya <kbd>Sağ tık</kbd> -> alt kanalı yapılandır.

## Kapaklar

Çoğu multiblok, giriş/çıkış için ortak işlevsel kapaklar kullanır. Kapaklar kademeler halinde gelir (ULV'den UHV+'a kadar) ve her kademe farklı kapasite veya iş hacmi sağlar.

| Kapak Türü | Amaç |
|------------|---------|
| Giriş Yolu / Çıkış Yolu | Eşyalar |
| Giriş Kapağı / Çıkış Kapağı | Sıvılar |
| Enerji Kapağı / Dinamo Kapağı | Güç |
| Buhar Kapağı | Buhar (yalnızca buharlı multibloklar) |
| Bakım Kapağı | Bakım sorunlarını giderir |
| Egzoz Çıkışı | Kirliliği tahliye eder |

Yapı minimum kasa sayısını hâlâ karşıladığı sürece, genellikle istediğin kadar kapak yerleştirebilirsin, ancak Bakım Kapakları genellikle bir taneyle sınırlıdır. Ucuz kapaklar çoğu zaman pahalı yapı bloklarının yerini alabilir.

## Paylaşım

GregTech multiblokları genellikle **duvar paylaşımına** izin verir: iki makine aynı duvardaki yapı bloklarını ve kapakları paylaşabilir.

- **Bakım Kapakları**, **Giriş Yolları**, **Giriş Kapakları** ve **Egzoz Çıkışları** paylaşılabilir.
- **Çıkış Yollarını** veya **Çıkış Kapaklarını** paylaşırken dikkatli ol, çünkü taşma çıkışları yok edebilir.
- **Enerji Kapaklarını** paylaşırken de dikkatli ol: genellikle bir Enerji Kapağı ikiden fazla makine tarafından paylaşılmamalı ve çift kapaklı kademe atlaması için kullanılan Enerji Kapakları paylaşılmamalıdır.

## Yapı Kontrolleri

Multibloklar yapılarının tamamlanıp tamamlanmadığını sürekli olarak yeniden kontrol etmez:

- Kontrolcü ilk kez yerleştirildiğinde -> yapı 100 tick sonra kontrol edilir.
- Yakındaki bir blok güncellendiğinde -> 50 ticklik bir geri sayım başlar ve her yeni güncelleme bu geri sayımı sıfırlar.
- Arayüzdeki "Yapı Kontrolünü Güncelle" düğmesine bastığında -> yapı 1 tick sonra kontrol edilir.

Bu gecikme penceresi içinde yapıyı kırıp geri yüklemek **sıcak değişimi** mümkün kılar. Bir Matter Manipulator (MK I veya üstü) bu tür sıcak değişimleri 1 tick içinde tamamlayabilir.

# Grafiksel Kullanıcı Arayüzü

Arayüzü açmak için kontrolcü bloğuna <kbd>Sağ tık</kbd> yap. Çoğu makine standart GregTech arayüzünü kullanır. ZPM ve sonrasındaki bazı oyun sonu makineleri TecTech tarzı arayüzü kullanır.

## GregTech Tarzı Arayüz

Sağ taraftaki düğmeler temel açma/kapama seçeneklerini sunar:

| Düğme | İşlev |
|--------|----------|
| Güç paneli | Paralel yapılandırmasını ve güç kesintisi olay ayarlarını açar |
| Yapı kontrolünü güncelle | Yapı kontrolünü zorlar |
| Güç anahtarı | Makineyi açar veya kapatır; kapatılırsa mevcut tarifin bitmesine izin verilir |

Orta sol alan en az dört yapılandırma seçeneği sunar, ancak her makine hepsine izin vermez:

- **Yok Etme Modu**: hiçbir şeyi yok etme / yalnızca eşyaları / yalnızca sıvıları / ikisini de.
- **Giriş Ayrıştırması**: farklı Giriş Yollarındaki eşyaların aynı tarifte kullanılmasını engeller.
- **Toplu Mod**: tarif kontrollerini ve TPS maliyetini azaltmak için aynı tarifin tekrarlanan kopyalarını birleştirir.
- **Tarifi Kilitle**: makinenin başka tarifler çalıştırmasını engeller.

Araç kısayolları (kontrolcüye <kbd>Sağ tık</kbd>, dayanıklılık harcar):

- <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> -> yapıyı döndür.
- <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> -> giriş ayrıştırmasını aç/kapat / bazı makine modlarını değiştir.
- <ItemLink id="gregtech:gt.metatool.01:26" showIcon="left" /> -> toplu modu aç/kapat.
- <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> -> gücü aç/kapat.
- <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> -> sesi kapat/aç.

## TecTech Tarzı Arayüz

Yalnızca birkaç ZPM ve sonrası makine bunu kullanır, örneğin <ItemLink id="gregtech:gt.blockmachines:15300" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15311" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:14003" showIcon="left" />.

Onu tanımlayan özellik gösterge ışığı sistemidir:
- Yanıp sönen mavi: parametre çok düşük.
- Yeşil: normal.
- Yanıp sönen turuncu: parametre çok yüksek.
- Önemli bir parametrenin ışığına genellikle sol tıklayarak ayarı değiştirebilirsin.

TecTech makineleri **taşmada her zaman yok eder**, bu yüzden güvenli yok etme düğmesinin pratikte bir etkisi yoktur. Parametre depolama kartları ayarları bir TecTech makinesinden diğerine kopyalayabilir.

# Bakım

## Bakım Sorunları

Yalnızca yapısı <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> gerektiren multibloklar bakım ister. Kontrolcü yerleştirildiğinde altı bakım sorununun tamamı varsayılan olarak mevcuttur ve makine çalışmadan önce giderilmelidir.

| Sorun | Araç |
|---------|------|
| "Bir boru gevşek." | Somun Anahtarı |
| "Bazı vidalar gevşek." | Tornavida |
| "Bir şey sıkışmış." | Yumuşak Tokmak |
| "Plakalar bükülmüş." | Sert Çekiç |
| "Bir şey buraya ait değil." | Levye |
| "Devre kısa devre yapmış." | Lehim Demiri (10k EU + 1 lehim malzemesi harcar) |

**Nasıl ortaya çıkarlar**: her 1000 ticklik kesintisiz çalışmada rastgele bir bakım sorununun oluşması için 1/6000 şans vardır. Bu da ortalama olarak yaklaşık her 83,3 saatte bir sorun demektir.

**Ceza**: her bakım sorunu güç kullanımını %10 artırır. Altısı da mevcutsa makine kapanır. Bazı makinelerin özel cezaları vardır; örneğin <ItemLink id="gregtech:gt.blockmachines:32013" showIcon="left" /> bir bakım sorunu ortaya çıktığında kinetik enerjisini anında sıfıra düşürür.

## Onarım Yöntemleri

| Aşama | Yöntem |
|-------|--------|
| LV | Gerekli tüm araçları ve lehimi içeren bir Alet Çantası ile Bakım Kapağına <kbd>Sağ tık</kbd> yap |
| MV | FAL-84 Güçlendirilmiş Koli Bandı ile onar |
| HV | Asa Odağı: Bakım (vis harcar) |
| IV | Toplu yönetim için Drone Downlink Module ve Drone Centre |
| LuV | Otomatik Bakım Kapağı (malzeme harcar) |
| UV | Hata Ayıklama Bakım Kapağı (ücretsiz otomatik bakım) |

Bir Bakım Kapağına bir kez önceden bakım yapabilirsin. Makine bu durumu okuduktan sonra kapağın etkin bakım durumunu temizler ve ardından bir ek tamponlanmış bakım durumu depolar. Daha sonra bir bakım sorunu ortaya çıktığında kapak, onu düzeltmek için tamponlanmış bir bakım durumunu otomatik olarak harcar.

# Tarif Algılama

Bir multiblok açıldığında, eşleşen bir tarif aramak için tüm kapaklarını tarar. Buradaki kilit kavram **giriş grubudur**: aynı giriş grubunda olmayan malzemeler asla tek bir tarifte birleştirilmez.

## Giriş Ayrıştırması

Giriş ayrıştırması etkinleştirildiğinde, her Giriş Yolu tüm Giriş Kapaklarıyla ve kontrolcünün envanter yuvalarıyla birlikte bağımsız bir giriş grubu oluşturur. Bu, farklı yollardaki malzemelerin yanlışlıkla istenmeyen bir tarife karışmasını önlemek için çok kullanışlıdır.

## Tarif Önceliği

Farklı giriş grupları arasındaki tarif kontrolleri, kontrol edilebilir bir öncelik sırasını izler.
1. **Desen giriş kapakları/yolları** (<ItemLink id="gregtech:gt.blockmachines:2715" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:2714" showIcon="left" />) normal kapaklara göre önceliklidir.
2. **Tablo ile işaretlenmiş** normal giriş kapakları ve yolları. <ItemLink id="gregtech:gt.metaitem.01:32468" showIcon="left" /> arayüzünde gösterilen sıraya göre öncelik siyahtan beyaza doğru azalır.
3. Giriş Yolları, Giriş Kapaklarına göre önceliklidir.
4. Fiziksel konum: önden arkaya, yukarıdan aşağıya, soldan sağa.

> [!TIP]
> Kapakları Tablo ile işaretlemek, tarif yürütme sırasını kontrol etmenin bir yoludur.

# Tarif Yürütme

## Kademe Atlama

Bkz. **[Kademe Atlama](../tierskipping-overcloking-parallels/tierskipping.md)**.

Aynı kademeden iki Enerji Kapağını 4A sağlamak için kullanmak, makinenin voltaj kademesinin beklediği nominal güce ulaşmasını ve tarifleri bir kademe yukarıda çalıştırmasını sağlar. Buna **çift kapaklı kademe atlama** denir. Bunu muhtemelen ilk kez <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> ile kullanacaksın.

IV'ten itibaren bazı makineler artık kademe atlayamaz, örneğin <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" />.

## Paraleller

Bkz. **[Paraleller](../tierskipping-overcloking-parallels/parallels.md)**.

Paraleller, makinenin aynı zaman aralığında aynı tarifin birden çok kopyasını işleme yeteneğidir. [Tek blok makineler](../singleblock/singleblock-index.md) bunu yapamaz.

Genel olarak, pratikte her $$4^n$$ maksimum paralel, yaklaşık olarak $$n$$ kusursuz hız aşırtmaya eşdeğerdir. Paraleller yalnızca aynı tarif için geçerlidir.

## Hız Aşırtma

Bkz. **[Hız Aşırtma](../tierskipping-overcloking-parallels/overclocking.md)**.

Standart 4/2 kusurlu hız aşırtmaların yanı sıra, bazı multibloklar 4/4 kusursuz hız aşırtmayı da destekler ve bazıları özel hız aşırtma kuralları kullanır. Multibloklar 1 tickin ötesine de hız aşırtabilir (1tOC).

Hesaplama sırası: önce paraleller, sonra hız aşırtmalar (önce kusursuz, sonra kusurlu).

## Toplu Mod

Toplu mod, aynı tarifin tekrarlanan kopyalarını tek bir büyük tarifte birleştirir. **Süre indirimi sağlamaz ve paralel eklemez**. Tek amacı tarif kontrol sıklığını azaltmak ve TPS maliyetini düşürmektir.

Toplu mod etkinleştirildiğinde makine, tarif süresini 128 ticke uzatmaya çalışır. Bu, birim zaman başına çıktıyı değiştirmez. Buharlı multibloklar toplu modu kullanamaz.

# Arızalar

[Tek blok makinelerin](../singleblock/singleblock-index.md) aksine, bir multiblok arızalandığında **tarifi tamamen iptal eder ve girdileri geri vermez**.

| Arıza | Çözüm |
|---------|-----|
| "Yapı tamamlanmamış." | Eksik yapı bloklarını kontrol et |
| "Egzoz Çıkışı, Bakım Kapağı veya benzeri eksik." | Gerekli kapağı ekle |
| "Makine hasarı nedeniyle kapatıldı." | Tüm bakım sorunlarını gider |
| "Tarif daha fazla güç gerektiriyor." | Enerji Kapaklarının sayısını ve mevcut amperajı kontrol et |
| "Tarifin başlaması için daha yüksek voltaj gerekiyor." | Voltaj kademesinin yeterince yüksek olup olmadığını kontrol et |
| "Eşya/sıvı çıkışı için yeterli alan yok." | Daha fazla Çıkış Yolu veya Çıkış Kapağı ekle |
| "Enerji eksikliği nedeniyle kapatıldı." | Güç kaynağını kontrol et |

Bir arıza meydana geldiğinde, boyuttaki güç kesintisi uyarı simgelerini kaldırmak için `/powerfails clear` veya güç kesintisi bilgilerini paylaşmak için `/sp invite <playerID>` komutunu kullanabilirsin.

# Patlamalar

[Tek blok makinelerde](../singleblock/singleblock-index.md#explosions) olduğu gibi, bir multibloktaki **dahili EU tamponu olan enerjili herhangi bir kapak** yağmurda veya karda patlayabilir. Kontrolcü blokları, yapı blokları ve güç tamponlamayan kapaklar yağmurda veya karda patlamaz. Bir Enerji Kapağına aşırı voltaj vermek de patlamaya neden olabilir.