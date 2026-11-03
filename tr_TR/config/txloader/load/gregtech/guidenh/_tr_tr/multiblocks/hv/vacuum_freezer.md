---
item_ids:
  - gregtech:gt.blockmachines:1002
navigation:
  title: Vakum Dondurucu
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:1002
  position: 10
---

# Vakum Dondurucu

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1002" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> (Vakum Dondurucu, kısaltması VF ve genellikle "dondurucu" olarak anılır) HV kademesinde bir işleme multiblokudur. Sıcak külçelerini daha ileri işlemlerden geçebilecek normal külçelere soğutmak için genellikle [Elektrikli Yüksek Fırın](../lv/electric_blast_furnace.md) ile birlikte kullanılır.

Her Elektrikli Yüksek Fırın ürünü soğutma gerektirmez. Bir üretim hattı kurmadan önce ürünün kullanımlarını NEI'de kontrol et. Fırın zaten normal bir külçe üretiyorsa, ürünün Vakum Dondurucu'dan geçmesi gerekmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı kademe | HV |
| Yapı boyutu | 3×3×3, merkezinde bir hava bloğu ile |
| Güç | Standart Enerji Kapakları; Çok Amperli Enerji Kapakları ve Lazer Enerji Kapakları desteklenmez |
| Hız aşırtma | Standart kusurlu hız aşırtma: her hız aşırtma 4× güç kullanır ve süreyi yarıya indirir |
| İşleme bonusları | Ek hız, güç veya paralel bonusu yok |
| Bakım ve kirlilik | Bakım gerektirir, kirlilik üretmez ve Egzoz Çıkışı gerektirmez |

## Üretim ve İnşa

Kontrolcü ve kasa için mevcut tarifler aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1002" />

<RecipesFor id="gregtech:gt.blockcasings2:1" />

Kontrolcü ön yüzdeki ikinci katmanın merkezinde olacak şekilde içi boş bir 3×3×3 kabuk inşa et. Merkezdeki tek blok hava olarak kalmalıdır; yapının içinde bobin, buz veya soğutucu gerekmez.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1002" showIcon="left" /> | 1, ön yüzdeki ikinci katmanın merkezinde |
| <ItemLink id="gregtech:gt.blockcasings2:1" showIcon="left" /> | En az 16; kalan kasa konumları aşağıda listelenen kapaklar ve yollar ile değiştirilebilir |
| Enerji Kapağı | En az 1, herhangi bir kasa konumunda |
| Bakım Kapağı | 1, herhangi bir kasa konumunda |
| Giriş Yolu veya Girdi Kapağı | Her iki türden en az biri, herhangi bir kasa konumunda |
| Çıkış Yolu veya Çıkış Kapağı | Her iki türden en az biri, herhangi bir kasa konumunda |

Sıcak külçeleri soğutmak için bir Giriş Yolu ve Çıkış Yolu kullan. Sıvı tarifleri için tarifin gerektirdiği Girdi ve Çıkış Kapaklarını tak. Her iki tür arayüz aynı anda takılabilir, ancak yapıda en az 16 gerçek Donmaya Dayanıklı Makine Kasası kalmalıdır; kapaklar ve yollar bu minimuma sayılmaz.

Yalnızca sıcak külçeler için kullanılan, bir Enerji Kapağı, bir Bakım Kapağı, bir Giriş Yolu ve bir Çıkış Yolu bulunan bir makine **21 Donmaya Dayanıklı Makine Kasası** gerektirir. Daha fazla kapak veya yol eklemek gereken kasa bloğu sayısını buna göre azaltır, en az 16'ya kadar.

Yapıyı önizlemek ve inşaya yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Yapı tamamlandığında bir yapı kontrolü çalıştır ve kontrolcünün gösterdiği bakım sorunlarını gidermek için bakım araçlarını kullan.

## Yetenekler

Vakum Dondurucu sıcak külçeleri soğutmanın ötesinde işler yapar. Tarifleri ayrıca belirli gazları sıvılaştırmayı, soğutma hücrelerini yenilemeyi ve plazmaları soğutmayı içerir. Tariflerin gerilim ve girdi/çıktı gereksinimleri farklıdır, bu yüzden bir eşyanın adı tek başına makinenin onu işleyip işleyemeyeceğini belirlemez.

- **Sıcak külçe soğutma**: Elektrikli Yüksek Fırın'dan gelen sıcak külçeleri, Sıcak Nikrom Külçeleri gibi normal karşılıklarına dönüştürür.
- **Sıvı soğutma**: Bir tarifin gerektirdiği gazları veya plazmaları Girdi Kapakları aracılığıyla kabul eder ve ürünleri Çıkış Kapaklarına gönderir.
- **Soğutma hücresi yenileme**: Yalnızca eşleşen bir Vakum Dondurucu tarifi olan hücreler ve bileşenler işlenebilir; her reaktör bileşeni burada onarılamaz.

Yapının kendisi soğutucu tüketmez, ancak tek tek tarifler sıvı girdileri gerektirebilir. NEI'de gösterilen girdileri, çıktıları ve güç kullanımını takip et.

## Güç ve İş Hacmi

HV, makinenin kullanılabilir hale geldiği kademedir, ancak Vakum Dondurucu HV gücüyle sınırlı değildir. Enerji Kapağını yükseltmek kullanılabilir gerilimi artırır ve uygun tarifleri hız aşırtmaya tabi tutar. Ayrıca Multibloklar için geçerli olağan [kademe atlama kurallarına](../../tierskipping_overcloking_parallels/tierskipping.md) uyar.

Vakum Dondurucu'da ısıtma bobini yoktur, bu yüzden Elektrikli Yüksek Fırın'ın ısı indirimlerini veya ısıya dayalı kusursuz hız aşırtmalarını almaz. Her standart kusurlu [hız aşırtma](../../tierskipping_overcloking_parallels/overclocking.md) güç kullanımını dört katına çıkarır ve işlem süresini yarıya indirir, böylece her işlemin tükettiği toplam enerjiyi artırır.

Bir Elektrikli Yüksek Fırın üretim hattını genişlettikten sonra Vakum Dondurucu'nun girdisinde sıcak külçelerin birikip birikmediğini kontrol et. Fırının paralelleri, bobin bonusları ve tarif süresi, gerçek çıktı hızını etkiler. İki makinenin Enerji Kapağı kademesinin aynı olması, iş hacimlerinin de aynı olacağını garanti etmez.

> [!WARNING]
> İşlem sırasında güç kaybı mevcut tarifi iptal eder ve içeri konan girdileri yok eder. Güç ağı, tarifin gerilimini karşılamalı ve makine çalışırken gereken gücü sürekli sağlamalıdır.

## Sıcak Külçe Yönlendirme

Bir Elektrikli Yüksek Fırın hem sıcak külçeler hem de soğutma gerektirmeyen eşyalar üretebilir. Vakum Dondurucu'nun girdisini filtrelemek, normal ürünlerin Giriş Yolu'nu doldurmasını önler.

Normal bir Giriş Yolu tarif filtrelemeyi destekler. Filtreyi açıp kapatmak için Shift basmadan tornavidayla sağ tıkla; Shift ile sağ tıklamak diğer girdi ayarlarını değiştirir. Etkinleştirildiğinde yol yalnızca makinenin tarif haritasının tanıdığı eşyaları kabul eder. Tarif filtreleme, yalnızca sıcak külçeleri kabul etmekle aynı şey değildir, çünkü Vakum Dondurucu başka eşyaları da işleyebilir.

Bir taşıma sistemi seçerken aşağıdaki yönergeleri kullan:

| Taşıma sistemi | Yönlendirme değerlendirmeleri |
| --- | --- |
| GregTech Eşya Boruları | Vakum Dondurucu'da geçerli tarif filtrelemesini etkinleştir ve kalan ürünler için ulaşılabilir başka bir hedef bırak; boru mesafesini ve Kısıtlayıcı Eşya Borularının yönlendirme davranışını hesaba kat |
| Ender IO Eşya Kanalları | Ekleme filtrelerini ve hedef önceliklerini, Vakum Dondurucu soğutma gerektiren eşyaları alırken diğer ürünlerin depolamaya gitmesini sağlayacak şekilde yapılandır |
| AE2 | Belirli sıcak külçeler için filtre uygula; cevher sözlüğü filtrelemesi olan cihazlar sıcak külçeleri eşleştirmek için `ingotHot*` kullanabilir |

Otomasyonu bağladıktan sonra bir sıcak külçe ve bir normal ürünü ayrı ayrı yerleştirip hedeflerini doğrula. Soğutulmuş külçelerin de güvenilir bir çıktı güzergâhı olduğundan emin ol, böylece dolu bir Çıkış Yolu üretimi durduramaz.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Yapı tamamlanmamış | Merkez hava; en az 16 Donmaya Dayanıklı Makine Kasası kalmış; bir Enerji Kapağı, Bakım Kapağı, girdi arayüzü ve çıktı arayüzü mevcut |
| Girdiler girmiyor | Yol, oluşmuş bir makineye ait; tarif filtrelemesi doğru yapılandırılmış; taşıma yönü, filtreler ve öncelikler doğru |
| Girdiler var ama tarif yok | Girdi gerçekten soğutma gerektiriyor; eşya veya sıvı bir tarifle eşleşiyor; Enerji Kapağı yeterli gerilim sağlıyor |
| Çıktı alanı yetersiz | Doğru Çıkış Yolu veya Çıkış Kapağı mevcut, dolu değil ve tarifin çıktısının tamamını tutabiliyor |
| Makine başladıktan hemen sonra duruyor | Daha fazla test malzemesi koymadan önce mevcut gücü, kablo kaybını, enerji tamponlarını ve bakım durumunu kontrol et |

Multiblokların genel işleyişi için [Multiblok Makineleri](../multiblocks_index.md) sayfasına bak. İlerleyen aşamalarda daha yüksek soğutma kapasitesi için Kriyojenik Dondurucu'ya göz at.

## Kaynaklar

- [GTNH Wiki: Vakum Dondurucu](https://wiki.gtnewhorizons.com/wiki/Vacuum_Freezer)