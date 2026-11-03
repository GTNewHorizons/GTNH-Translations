---
item_ids:
  - gregtech:gt.blockmachines:1002
navigation:
  title: Vakum Dondurucu
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1002
  position: -3001
---
# Vakum Dondurucu
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1002" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> (Vakum Dondurucu, kısaca VF ve çoğu zaman "dondurucu") HV kademesinde çalışan bir işleme multibloğudur. Sıcak külçelerini daha ileri işlemeden geçebilecek normal külçelere soğutmak için genellikle [Elektrikli Yüksek Fırın](./electric_blast_furnace.md) ile birlikte kullanılır.

Her Elektrikli Yüksek Fırın ürünü soğutma gerektirmez. Bir üretim hattı kurmadan önce ürünün kullanımlarını NEI'de kontrol et. Fırın zaten normal bir külçe üretiyorsa bunun Vakum Dondurucudan geçmesi gerekmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | HV |
| Yapı boyutu | 3×3×3; merkezde bir hava bloğu |
| Güç | Standart Enerji Kapakları; Çok Amperli Enerji Kapakları ve Lazer Enerji Kapakları desteklenmez |
| Hız aşırtma | Standart kusurlu hız aşırtma: her hız aşırtma 4× güç kullanır ve süreyi yarıya indirir |
| İşleme bonusları | Ek hız, güç veya paralel bonusu yok |
| Bakım ve kirlilik | Bakım gerektirir, kirlilik üretmez ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü ve kasa için güncel tarifler aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1002" />

<RecipesFor id="gregtech:gt.blockcasings2:1" />

Kontrolcü ön yüzdeki ikinci katmanın ortasında olacak şekilde içi boş bir 3×3×3 kabuk inşa et. Merkezdeki tek blok hava olarak kalmalıdır; yapının içinde bobin, buz veya soğutucu gerekmez.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> | 1; ön yüzdeki ikinci katmanın ortasında |
| <ItemLink id="gregtech:gt.blockcasings2:1" showIcon="left" /> | En az 16; kalan kasa konumları aşağıda listelenen kapaklar ve yollarla değiştirilebilir |
| Enerji Kapağı | En az 1; herhangi bir kasa konumunda |
| Bakım Kapağı | 1; herhangi bir kasa konumunda |
| Giriş Yolu veya Girdi Kapağı | İki türden en az biri; herhangi bir kasa konumunda |
| Çıkış Yolu veya Çıkış Kapağı | İki türden en az biri; herhangi bir kasa konumunda |

Sıcak külçeleri soğutmak için bir Giriş Yolu ve Çıkış Yolu kullan. Sıvı tarifleri için tarifin gerektirdiği Girdi ve Çıkış Kapaklarını tak. İki tür arayüz aynı anda takılabilir, ancak yapı en az 16 gerçek Dona Dayanıklı Makine Kasası tutmalıdır; kapaklar ve yollar bu minimuma sayılmaz.

Yalnızca sıcak külçeler için kullanılan, bir Enerji Kapağı, bir Bakım Kapağı, bir Giriş Yolu ve bir Çıkış Yolu olan bir makine **21 Dona Dayanıklı Makine Kasası** gerektirir. Daha fazla kapak veya yol eklemek gereken kasa bloğu sayısını buna göre azaltır, en az 16'ya kadar.

Yapıyı önizlemek ve inşaya yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Tamamlandığında bir yapı kontrolü çalıştır ve kontrolcünün gösterdiği bakım sorunlarını çözmek için bakım araçlarını kullan.

## Yetenekler

Vakum Dondurucu sıcak külçeleri soğutmaktan fazlasını yapar. Tarifleri ayrıca belirli gazları sıvılaştırmayı, soğutucu hücrelerini yenilemeyi ve plazmaları soğutmayı içerir. Tarifler farklı gerilim ve giriş/çıkış gereksinimlerine sahiptir, bu nedenle yalnızca bir eşyanın adı makinenin onu işleyip işleyemeyeceğini belirlemez.

- **Sıcak külçe soğutma**: Elektrikli Yüksek Fırından gelen sıcak külçeleri (ör. Sıcak Nikrom Külçeleri) normal karşılıklarına dönüştürür.
- **Sıvı soğutma**: Tarifin gerektirdiği gazları veya plazmaları Girdi Kapakları aracılığıyla alır ve ürünleri Çıkış Kapaklarına gönderir.
- **Soğutucu hücresi yenileme**: Yalnızca eşleşen bir Vakum Dondurucu tarifi olan hücreler ve bileşenler işlenebilir; her reaktör bileşeni burada onarılamaz.

Yapının kendisi soğutucu tüketmez, ancak tek tek tarifler sıvı girdileri gerektirebilir. NEI'de gösterilen girdileri, çıktıları ve güç kullanımını izle.

## Güç ve Verim

Makine HV kademesinde kullanılabilir hale gelir, ancak Vakum Dondurucu HV gücüyle sınırlı değildir. Enerji Kapağını yükseltmek kullanılabilir gerilimi artırır ve uygun tarifleri hız aşırtmaya tabi tutar. Ayrıca olağan multiblok [kademe atlama kurallarına](/tierskipping_overcloking_parallels/tierskipping.md) uyar.

Vakum Dondurucuda ısıtma bobini yoktur, bu nedenle Elektrikli Yüksek Fırının ısı indirimlerini veya ısıya dayalı kusursuz hız aşırtmalarını almaz. Her standart kusurlu [hız aşırtma](/tierskipping_overcloking_parallels/overclocking.md) güç kullanımını dörde katlar ve işleme süresini yarıya indirir; bu da her işlemin tükettiği toplam enerjiyi artırır.

Bir Elektrikli Yüksek Fırın üretim hattını genişlettikten sonra Vakum Dondurucunun girişinde sıcak külçelerin birikip birikmediğini kontrol et. Fırının paralelleri, bobin bonusları ve tarif süresi, gerçek çıktı hızını etkiler. İki makinenin Enerji Kapağı kademesinin eşleşmesi, verimin de eşleşeceğini garanti etmez.

> [!WARNING]
> İşleme sırasında güç kaybı mevcut tarifi iptal eder ve yerleştirilen girdileri yok eder. Güç ağının tarifin gerektirdiği gerilimi karşılaması ve makine çalışırken gereken gücü sürekli sağlaması gerekir.

## Sıcak Külçe Yönlendirmesi

Bir Elektrikli Yüksek Fırın hem sıcak külçeler hem de soğutma gerektirmeyen eşyalar üretebilir. Vakum Dondurucunun girişini filtrelemek, normal ürünlerin Giriş Yolunu doldurmasını önler.

Normal bir Giriş Yolu tarif filtrelemeyi destekler. Filtreyi açıp kapatmak için Shift basmadan bir Tornavidayla sağ tıkla; Shift+sağ tık diğer giriş ayarlarını değiştirir. Etkinleştirildiğinde yol yalnızca makinenin tarif haritasının tanıdığı eşyaları kabul eder. Tarif filtrelemesi yalnızca sıcak külçeleri kabul etmekle aynı değildir, çünkü Vakum Dondurucu başka eşyaları da işleyebilir.

Bir taşıma sistemi seçerken aşağıdaki yönergeleri kullan:

| Taşıma sistemi | Yönlendirme değerlendirmeleri |
| --- | --- |
| GregTech Eşya Boruları | Vakum Dondurucuda geçerli tarif filtrelemesini etkinleştir ve kalan ürünler için erişilebilir başka bir hedef bırak; boru mesafesini ve Kısıtlayıcı Eşya Borularının yönlendirme davranışını hesaba kat |
| Ender IO Eşya Kanalları | Ekleme filtrelerini ve hedef önceliklerini yapılandır; Vakum Dondurucu soğutma gerektiren eşyaları alsın, diğer ürünler depolamaya gitsin |
| AE2 | Belirli sıcak külçeler için filtrele; cevher sözlüğü filtrelemesi olan cihazlar sıcak külçeleri eşleştirmek için `ingotHot*` kullanabilir |

Otomasyonu bağladıktan sonra bir sıcak külçe ve bir normal ürünü ayrı ayrı yerleştir ve hedeflerini doğrula. Soğutulmuş külçelerin de güvenilir bir çıkış rotası olduğundan emin ol; böylece dolu bir Çıkış Yolu üretimi durduramaz.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Yapı tamamlanmamış | Merkez hava; en az 16 Dona Dayanıklı Makine Kasası kalmış; bir Enerji Kapağı, Bakım Kapağı, giriş arayüzü ve çıkış arayüzü mevcut |
| Girdiler girmiyor | Yol oluşmuş bir makineye ait; tarif filtrelemesi doğru yapılandırılmış; taşıma yönü, filtreler ve öncelikler doğru |
| Girdiler var ama tarif yok | Girdi gerçekten soğutma gerektiriyor; eşya veya sıvı bir tarifle eşleşiyor; Enerji Kapağı yeterli gerilim sağlıyor |
| Yetersiz çıkış alanı | Doğru Çıkış Yolu veya Çıkış Kapağı var, dolu değil ve tarifin tüm çıktısını tutabiliyor |
| Makine başladıktan hemen sonra duruyor | Daha fazla test malzemesi koymadan önce mevcut gücü, kablo kaybını, enerji tamponlarını ve bakım durumunu kontrol et |

Genel multiblok çalışması için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak. İlerleyen aşamalarda daha yüksek soğutma kapasitesi için Kriyojenik Dondurucuya göz at.

## Kaynaklar

- [GTNH Wiki: Vakum Dondurucu](https://wiki.gtnewhorizons.com/wiki/Vacuum_Freezer)