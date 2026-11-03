---
item_ids:
  - gregtech:gt.blockmachines:12791
navigation:
  title: Yüksek Sıcaklık Gaz Soğutmalı Reaktör
  parent: multis.md
  icon: gregtech:gt.blockmachines:12791
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-31
---

# Yüksek Sıcaklık Gaz Soğutmalı Reaktör
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12791" />
</GameScene>
<Color id="GREEN">Yüksek Sıcaklık Gaz Soğutmalı Reaktör (HTGR)</Color>, değerli yan ürünleri için TRISO <ItemImage id="kubatech:htgr_item_triso_fuel:1"/> toplarını fisyon yoluyla bozunduran IV kademe bir multibloktur. <Color id="GREEN">HTGR</Color>'ın işlemeye başlaması için en az 100 TRISO topu ve 51.200 L helyumla önceden doldurulması gerekir; ancak maksimum 10.000 TRISO topu ve 512.000 L helyumun altında kalırsan verim düşer ve güç tüketimi artar. İsteğe bağlı olarak IC2 soğutucusu ve/veya damıtılmış su vererek bozunma sürecini büyük ölçüde hızlandırabilir ve maksimum süreyi 1.000 saniyeden yalnızca 10 saniyeye düşürebilirsin. <Color id="GREEN">TRISO</Color>, her işlemin en başında TRISO toplarının %0,14'üne ve helyumun %0,05'ine kadar tüketir; ardından sonraki 10 saniye boyunca 5.000 L/t'ye kadar sıcak soğutucu ve 160.000 L/t buhar üretmek için yalnızca 1.536 EU/t kullanır. Yanmış TRISO topları, orijinal girdilerin çoğunu ve Güneştaşı, indiyum, lutesyum tozu ve lantan gibi birkaç ek çıktıyı geri almak için Endüstriyel Santrifüjde geri dönüştürülebilir. En yüksek yakıt işleme hızı saatte 5.094 TRISO topudur.

Sıcak soğutucu, kızgın buhar üretmek için Termal Kazan <ItemImage id="gregtech:gt.blockmachines:15557"/>, Büyük Isı Eşanjörü <ItemImage id="gregtech:gt.blockmachines:1154"/> veya Whakawhiti Wera XL <ItemImage id="gregtech:gt.blockmachines:31079"/> tarafından kullanılır; süperkritik buhar üretmek için ise Ekstrem Isı Eşanjörü kullanılır. Buhar daha sonra Büyük Buhar Türbinlerinde güç üretmek için kullanılır. Maksimum verimde 111A'nın üzerinde LuV gücü bekleyebilirsin.

<Color id="GREEN">HTGR</Color>, <Color id="RED">Toryum Yüksek Sıcaklık Reaktörüne (THTR)</Color> çok benzer. Fark, <Color id="RED">THTR</Color>'ın çok daha uzun süre çalışması ve neredeyse hiç yan ürün üretmemesidir. Başka bir deyişle, kaynaklar için <Color id="GREEN">HTGR</Color>'ı, güç için <Color id="RED">THTR</Color>'ı kullan. 
<br clear="all"/>

## İnşaat:
<Color id="GREEN">HTGR</Color> dört ayrı yapıdan oluşur. Bu yapıların tam konumları kontrolcüye göre sabittir ve yapının oluşması için dördü de gereklidir. Büyük mor küre reaktördür; üstünde TRISO topları için bir giriş yolu, altında yanmış TRISO topları için bir çıkış yolu bulunur <ItemImage id="kubatech:htgr_item_burned_triso_fuel:3"/>. Ortadaki uzun dikey yapı birincil soğutucu kulesidir; yanında IC2 soğutucusu için bir girdi kapağı, üstünde sıcak soğutucu için bir çıkış kapağı vardır. Kenardaki daha küçük dikey yapı ikincil soğutucu kulesidir; üst kısmına yakın damıtılmış su için bir girdi kapağı, alt kısmına yakın buhar için bir çıkış kapağı vardır. Helyum girdi kapağı, enerji kapağı ve bakım kapağı yalnızca yapının merkezindeki pompanın üzerindeki en üst üç kasaya yerleştirilebilir. <Color id="RED">Çok Amperli ve Lazerli Enerji Kapakları</Color> desteklenmez ve birden fazla normal enerji kapağı olamaz. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:12791"/><ItemImage id="gregtech:gt.blockmachines:12791"/>
- 273 <ItemLink id="gregtech:gt.blockcasings13:3"/><ItemImage id="gregtech:gt.blockcasings13:3"/>
- 272 <ItemLink id="gregtech:gt.blockcasings10:3"/><ItemImage id="gregtech:gt.blockcasings10:3"/>
- 164 <ItemLink id="gregtech:gt.blockframes:81"/><ItemImage id="gregtech:gt.blockframes:81"/>
- 162 <ItemLink id="gregtech:gt.blockcasings13:1"/><ItemImage id="gregtech:gt.blockcasings13:1"/>
- 45 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 41 <ItemLink id="gregtech:gt.blockcasings13:2"/><ItemImage id="gregtech:gt.blockcasings13:2"/>
- 30 <ItemLink id="gregtech:gt.blockcasings2:14"/><ItemImage id="gregtech:gt.blockcasings2:14"/>
- 24 <ItemLink id="gregtech:gt.blockcasings13"/><ItemImage id="gregtech:gt.blockcasings13"/>
- 23 <ItemLink id="gregtech:gt.blockcasings:5"/><ItemImage id="gregtech:gt.blockcasings:5"/>
- 20 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 17 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:10"/><ItemImage id="gregtech:gt.blockcasings2:10"/>
- 2 <ItemLink id="gregtech:gt.blockcasings2:11"/><ItemImage id="gregtech:gt.blockcasings2:11"/>
- 1 <ItemLink id="gregtech:gt.blockcasings2:6"/><ItemImage id="gregtech:gt.blockcasings2:6"/>
- 1 Enerji Kapağı (pompanın üzerindeki herhangi bir üst kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (pompanın üzerindeki herhangi bir üst kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Giriş Yolu (TRISO topları için bir adet) <ItemImage id="gregtech:gt.blockmachines:70" />
- 3 Girdi Kapağı (biri IC2 soğutucusu, biri damıtılmış su, biri helyum için) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1 Çıkış Yolu (yanmış TRISO topları için bir adet) <ItemImage id="gregtech:gt.blockmachines:80" />
- 2 Çıkış Kapağı (biri sıcak soğutucu, biri buhar için) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı:
<Color id="GREEN">HTGR'lar</Color>, yolların/kapakların konum kısıtlamaları ve kontrolcünün döndürülemez veya çevrilemez olması nedeniyle yapılarının önemli bir kısmını duvar paylaşımına açamaz. Reaktör kısmı bile paylaşılamaz çünkü tam olarak simetrik değildir. 

## Kullanım:
<Color id="GREEN">HTGR</Color>'ın aşağıda listelenen iki çalışma modu vardır. Makine boştayken kontrolcüye tornavidayla sağ tıklayarak mod değiştir.

- Normal - TRISO toplarını ve helyumu içinde depolar ve minimum koşullar sağlandığında işlemeye başlar.
- Boşaltma - İçinde depolanan tüm TRISO toplarını çıkış yoluna geri verir.

<Color id="GREEN">HTGR</Color>, reaktörün içindeki TRISO toplarının fisyon bozunmasını stabilize etmek için helyum gazı kullanır. IC2 Soğutucusu ve damıtılmış su isteğe bağlıdır ancak şiddetle önerilir çünkü bozunma sürecini büyük ölçüde hızlandırarak yakıtın daha hızlı tüketilmesini sağlar. Son ürün, orijinal kaynakların bir kısmını ve başka yerlerde kullanılacak birkaç ek kaynağı geri almak için Endüstriyel Santrifüjde geri dönüştürülen yanmış TRISO toplarıdır. Varsa, IC2 soğutucusu sıcak soğutucuya, damıtılmış su ise TRISO topu ve helyum miktarıyla orantılı bir hızda buhara dönüştürülür. 

## Yakıt:
<Color id="GREEN">HTGR</Color> yakıt olarak TRISO toplarını (peletleri DEĞİL) kullanır. Toplamda 9 farklı tür vardır, ancak gerekirse hepsi aynı anda aynı makinede kullanılabilir. İşlemeye başlamak için gereken minimum yakıt miktarı 100 TRISO topudur; ancak maksimum 10.000 TRISO topunun altında kalırsan aşağıdaki denklem ve grafikte görüldüğü gibi makinenin verimi düşer.

TRISO toplarının, yapıldıkları malzemeye göre kendi materyal istatistikleri vardır. NEI ipucunda bu, buradaki gibi üzerine gelerek görebileceğin "Properties: [x], [y], [z]" şeklinde gösterilir: <ItemImage id="kubatech:htgr_item_burnerd_triso_fuel:3"/>. Bu özellikler sırasıyla Temel ($$b$$), Çarpan ($$m$$) ve Üs ($$e$$) olup, bu bölümün devamında ayrıntılandırıldığı gibi güç üretimi ve işlem süresiyle doğrudan ilişkilidir:

Verim, makine çalışırken artırılamaz ve %100'ü aşamaz. Bakım sorunları maksimum verimi her biri %20 azaltır. 

<Latex formula="\text{Efficiency\%} = 0.1 + 0.9 \Biggl( 1 - \Biggl( 1 - \frac{\text{TRISO Balls}}{10,000} \Biggr)^3 \Biggr"/>


<FunctionGraph title="Efficiency of HTGR base on stored TRISO Balls" xRange="0..10000" domain="0..100" xLabel="TRISO Balls" yLabel="Efficiency (%)"> 
<Plot expr="0.1 + 0.9 * (1 - (1 - (x)/(10000))^3) * 100" color="#ff55ff"/>
</FunctionGraph>


<Color id="GREEN">HGTR</Color>'ın verimi, aşağıdaki denklemde görüldüğü gibi her işlemin süresi ve kullanılan materyalin istatistikleriyle doğru orantılıdır.

<Latex formula="\text{Duration (s) } = (100 + (900 \times \text{Efficiency})) \times \eta">
  Burada:
  $$\eta$$: İşlem Süresi Değiştiricisi
</Latex>
<Latex formula="\eta = \frac{1}{e^2}">
  Burada:
  $$\eta$$: İşlem Süresi Değiştiricisi
  $$e$$: Kullanılan TRISO topunun üs istatistiği
</Latex>

<Color id="GREEN">HGTR</Color>'ın verimi ayrıca işlem başına tüketilen/yanan TRISO topu miktarıyla da doğru orantılıdır; bu, aşağıdaki denklemde gösterilmiştir. Bu, işlem başına en fazla 14,15 TRISO topudur; ancak iki değişken de verimle doğrusal olarak ölçeklendiğinden oran (soğutucusuz) süreden bağımsız olarak saatte 51'de sabittir.

<Latex formula="-\text{Balls/Operation} = \text{TRISO Balls} \times \frac{\pi - 3}{100} \times \text{Efficiency}"/>

<Color id="GREEN">HGTR</Color> aynı sayıda yanmış TRISO topu verir. Aşağıdaki tablolarda görüldüğü gibi çeşitli faydalı yan ürünler için TRISO toplarını santrifüjle. Girdilerin çoğu daha fazla yakıt yapmak için geri döner ve başka yerlerde kullanılacak birkaç ek çıktı vardır. En dikkat çekici olarak, Parlak taş TRISO topları Güneştaşı, gümüş TRISO topları indiyum, toryum TRISO topları lutesyum ve sezyum TRISO topları lantan üretir. 

## Soğutucu:
<Color id="GREEN">HGTR</Color>'daki tek zorunlu soğutucu helyumdur. İşlemeye başlamak için minimum helyum miktarı 51.200 L'dir; ancak maksimum 512.000 L'nin altında kalırsan aşağıdaki denklemde görüldüğü gibi makinenin güç tüketimi artar. Maksimum güç tüketimi 61.440 EU/t, minimum güç tüketimi 1.536 EU/t'dir. <Color id="GREEN">HGTR</Color>, her işlemin başında mevcut helyumun tam olarak %0,05'ini tüketir; bu yüzden reaktörün zamanla yavaşça yeniden doldurulması gerekir.

<Latex formula="-\text{EU/t} = 1,536 \times \Biggl( 1 + 39 \times \Biggl( 1 - \frac{\text{Helium} - 51,200}{460,800} \Biggr) \Biggr)"/>

İsteğe bağlı olarak, TRISO toplarının bozunma sürecini büyük ölçüde hızlandırmak için IC2 soğutucusu ve/veya damıtılmış su verebilirsin. IC2 soğutucusu saniyede toplam sürenin %7'sini, damıtılmış su saniyede toplam sürenin %3'ünü atlar; birlikte kullanıldıklarında saniyede toplam sürenin %10'unu atlarlar. Bu, tam 1.000 saniyelik bir işlemin 10 saniyenin altında tamamlanabileceği ve yine de aynı miktarda TRISO topu tüketeceği anlamına gelir. Güç üretimi için son derece verimsiz olsa da bu, üretme ve yan ürün toplama için aşırı derecede kullanışlıdır. Temel saatte 51 TRISO topu, saatte 5.094 TRISO topuna kadar çıkar.

<Color id="GREEN">HGTR</Color>'ın kullandığı IC2 soğutucusu ve damıtılmış su miktarı, aşağıdaki tabloda görüldüğü gibi mevcut TRISO topu miktarına ve mevcut helyum miktarına bağlıdır. IC2 soğutucusu tam 1:1 oranında sıcak soğutucuya, damıtılmış su ise 1:160 oranında buhara dönüştürülür. 

## Güç:
Yüksek sürdürme maliyetlerine rağmen <Color id="GREEN">HGTR</Color>, işlem başına 10 saniyeye kadar etkileyici bir 5.000 L/t sıcak soğutucu ve 160.000 L/t buhar üretir. Yalnızca soğutucunun debisi Toryum Yüksek Sıcaklık Reaktörünün <ItemImage id="gregtech:gt.blockmachines:12733"/> debisinden biraz daha fazla, bir Sıvı Reaktörün çıktısından 72 kat ve bir Derin Dünya Isıtma Pompasının <ItemImage id="gregtech:gt.blockmachines:12729"/> çıktısından 26 kat daha yüksektir. Ayrıca bir Ekstrem Isı Eşanjöründe süperkritik (SC) buhar ve Termal Kazan, Büyük Isı Eşanjörü veya Whakawhiti Wera XL'de kızgın (SH) buhar üretmek için fazlasıyla yeterlidir. Tek sorun, bu kadar çok sıcak soğutucunun çok sayıda ısı eşanjörü ve muazzam miktarda damıtılmış su gerektirmesidir; bu, aşağıdaki tabloda görülebilir. Süperkritik buhar genel olarak daha fazla güç verdiği için, daha fazla makine inşa etmek anlamına gelse de WWXL yerine EHE önerilir.

Dönüşüm Oranları

- 1 L/t Sıcak Soğutucu = 200 L/t SC Buhar (EHE) veya 200 L/t SH Buhar (Termal Kazan, LHE, WWXL)
- 200 L/t SC Buhar = 200 L/t SH Buhar = 200 L/t Buhar
- 160 L/t Buhar = 1 L/t Damıtılmış Su

Sıcak soğutucu ve buhar çıktısı sırasıyla 5.000 L/t ve 160.000 L/t'ye kadar olsa da çıktı hızı, aşağıdaki denklem aracılığıyla kullanılan TRISO toplarının istatistikleriyle doğrudan ilişkilidir:

<Latex formula="\text{Outputs /t} = \text{Base Outputs} \times b\times(m^e)">
  Burada:
    $$b$$: Materyal Temel İstatistiği
    $$m$$: Materyal Çarpan İstatistiği
    $$e$$: Materyal Üs İstatistiği
</Latex>