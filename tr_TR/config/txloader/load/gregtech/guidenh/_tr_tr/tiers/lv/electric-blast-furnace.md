---
item_ids:
    gregtech:gt.blockmachines:1000
navigation:
    title: Elektrikli Yüksek Fırın
    parent: ./tier-lv-index.md
    icon: gregtech:gt.blockmachines:1000
quest_ids:
    - AAAAAAAAAAAAAAAAAAAATQ
---

# Elektrikli Yüksek Fırın

<GameScene interactive={true} wrap="square" align="right" width="380" height="300" >
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_ponder.json" />
</GameScene>

## <ItemImage id="gregtech:gt.blockmachines:1000"/> Elektrikli Yüksek Fırın

```filetree
|-- **Source**:         [GregTech5u](https://github.com/GTNewHorizons/GT5-Unofficial/blob/master/src/main/java/gregtech/common/tileentities/machines/multi/MTEElectricBlastFurnace.java)
|-- **Machine Type**:   Blast Furnace
|-- **Kademe**:           [LV](./tier-lv-index.md)
|-- **Details**
|   |-- **Size**:                   3x3x4
|   |-- **Energy Hatches**:         Standard
|   |-- **[Overclocks](../../tierskipping-overcloking-parallels/overclocking.md)**: Imperfect
|   \-- **Pollution**:              400 gibbl/s
|-- [Wiki Page](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)
\-- Quest: <QuestLink id="AAAAAAAAAAAAAAAAAAAATQ==" />
```

<ItemImage id="gregtech:gt.blockmachines:1000" /> **Elektrikli Yüksek Fırın** (**EYF**), tozları standart fırınlardan daha yüksek ısıda külçelere eritmek için kullanılan [LV](./tier-lv-index.md)
kademe bir [multibloktur](/gtnh-basics/multiblocks.md).

EYF, <ItemImage id="gregtech:gt.blockmachines:140" /> Tuğlalı Yüksek Fırın'ın doğrudan yükseltmesidir; çünkü yanabilir yakıtlar yerine elektrikle çalışır ve daha yüksek kademe malzemeleri işleyebilir.

Yapıdaki ısıtma bobinleri makinenin ısı kapasitesini, enerji kapağı/kapakları ise gerilimi belirler. Yeni tariflerin kilidini açmak ve makineyi [hız aşırtma](../../tierskipping-overcloking-parallels/overclocking.md) yapmak için ikisini de yükselt.

EYF, egzoz çıkışından kirlilik salma, ara sıra bakım gerektirme ve güç kesintisinde malzemeleri yok etme gibi standart multiblok davranışlarını izler.
Eşyalar ve sıvılar sırasıyla veriyolları ve kapaklar aracılığıyla yerleştirilir/çıkarılır.

<RecipesFor id="gregtech:gt.blockmachines:1000" input="gregtech:gt.blockcasings:11" />

# İnşaat
EYF, üst ve alt katmanlarda <ItemImage id="gregtech:gt.blockcasings:11" /> **Isı Geçirmez Makine Gövdeleri**, ortadaki iki katmanda ise ısıtma bobinleriyle inşa edilir.

Isıtma bobinleri makinenin ısı kapasitesini belirler ve yapının oluşması için hepsi aynı kademede olmalıdır.

Veriyolları/kapaklar yalnızca alt katmandaki kasaların yerini alabilir; bunun istisnası üst orta kasayla sınırlı olan egzoz çıkışıdır.
Bir diğer istisna, alt katmanda sıvıları, üst katmanda ise gazları toplayan çıkış kapağıdır. Geri kazanılan gaz miktarı egzoz çıkışının kademesine bağlıdır.

EYF, enerji kapağının [gerilim kademesinde](../../power/voltage-tiers.md) çalışır ancak iki enerji kapağıyla bir sonraki gerilim kademesine hız aşırtma yapabilir.

Isıtma bobinlerinin kademesini belirtmek için "coil" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Gerekli                                                                                     |
|:--------------------------------------------------------------------------------------------|
| 1 <ItemImage id="gregtech:gt.blockmachines:1000" /> **Elektrikli Yüksek Fırın** (kontrolcü) |
| 16 <ItemImage id="gregtech:gt.blockcasings5" /> **Isıtma Bobini**[^one]                     |
| 0-15 <ItemImage id="gregtech:gt.blockcasings:11" /> **Isı Geçirmez Makine Gövdesi**       |
| 1+ <ItemImage id="gregtech:gt.blockmachines:41" /> **Enerji Kapağı** (herhangi bir alt kasa) |
| 1 <ItemImage id="gregtech:gt.blockmachines:90" /> **Bakım Kapağı** (herhangi bir alt kasa)  |
| 1 <ItemImage id="gregtech:gt.blockmachines:91" /> **Susturucu Kapağı** (üst orta kasa)      |
| 0+ <ItemImage id="gregtech:gt.blockmachines:71" /> **Giriş Yolu** (herhangi bir alt kasa) |
| 0+ <ItemImage id="gregtech:gt.blockmachines:51" /> **Girdi Kapağı** (herhangi bir alt kasa) |
| 0+ <ItemImage id="gregtech:gt.blockmachines:81" /> **Çıkış Yolu** (herhangi bir alt kasa) |
| 0+ <ItemImage id="gregtech:gt.blockmachines:61" /> **Çıkış Kapağı** (herhangi bir üst/alt kasa) |
[^one]: Bu **KADEMELİ** bir bileşendir.

> [!WARNING]
> Çok amperli ve lazer enerji kapakları desteklenmez.

## Duvar Paylaşımı

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right" >
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

EYF'ler kasa, ısıtma bobini ve veriyolu/kapaktan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir.
EYF'leri yan yana üst üste bindirmek en etkili yöntemdir ve şiddetle önerilir; çünkü önemli miktarda
ısıtma bobininden tasarruf sağlar ve ek EYF'lerin maliyetini düşürür.

Örneğin dörtlü paylaşılan bir EYF, tam 64 yerine yalnızca 42 ısıtma bobini gerektirir.
Tek dezavantajı, yapının/yapıların oluşması için hepsinin aynı kademede olması gerektiğinden ısıtma bobinlerini yükseltmenin zorluğudur.

Bakım kapağı, çıkış yolu ve girdi kapağını paylaşmak da oldukça faydalıdır; ancak enerji kapaklarını paylaşma; çünkü EYF sık sık daha yüksek bir gerilim kademesine hız aşırtma yapılmalıdır ve bu, iki enerji kapağından maksimum 4A kullanır. Bunu iki makine arasında bölmek mümkün değildir ve birinin güç kesintisi yaşamasına neden olur.

Lojistiğini makinenin altından geçirmek zorunda kalmadan veriyollarına ve kapaklara kolayca erişmek için kontrolcü bloğunu anahtarla 90 derece döndürüp dörtlü EYF'yi yanlamasına inşa etmeyi seçebilirsin.

> [!CAUTION]
> GregTech multiblokları için güç kesintisine, hatta ++**patlamaya**++ yol açabilecek birkaç olası tehlike vardır.
> * EYF'yi yağmura maruz bırakma.
> * Egzoz çıkışını herhangi bir blok, kablo veya boruyla kapatma.
> * Enerji kapaklarının gerilim kademesini aşma.
> * Tarif boyunca istikrarlı güç sağla.
> * Hiçlik koruması etkinse çıkışlar için yer olduğundan emin ol.

# Kullanım
Yapı oluştuğunda ve tüm bakım sorunları giderildiğinde EYF sonunda kullanıma hazırdır. Ancak oyuncunun yalnızca LV enerji kapaklarına erişimi olmasına rağmen LV tarifi yoktur; <ItemImage id="gregtech:gt.metaitem.01:11305" /> çelik ve <ItemImage id="gregtech:gt.metaitem.01:11019" /> alüminyum işlemek en az MV güç gerektirir.

Çözüm, makineyi bir sonraki gerilim kademesine [hız aşırtma](../../tierskipping-overcloking-parallels/overclocking.md) yapmak için yapıya iki enerji kapağı yerleştirmektir. Enerji kapakları normalde yalnızca 1A güç çeker, ancak bunun gibi durumlar için 2A'ya kadar çekebilirler. Bu, iki enerji kapağının 4A güç, yani bir sonraki gerilim kademesinin 1A'sına eşdeğer güç çekebileceği anlamına gelir.

Sürekli 4A güç sağlamak, yakınlarda en az dört [tek blok](../../singleblock/singleblock-index.md) <ItemImage id="gregtech:gt.blockmachines:1115" /> buhar türbini gerektirir. Çelik ve alüminyum tarifleri yalnızca 120 EU/t tüketir, bu yüzden bir miktar kablo kaybı olabilir ama çok fazla değil.

Aşağıda bu güç gereksinimlerini karşılamanın ve EYF'yi çalıştırmanın iki yöntemi var. İkisi de oyuncunun, amper veya mesafeden bağımsız olarak sıfır kablo kaybına sahip süper iletken kabloları **KULLANMADIĞINI** varsayar.

## Yöntem 1: Kablo Kaybını En Aza İndir
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

Kayıpları en aza indirmek için enerji kapaklarının yakınına <u>dört</u> buhar türbini yerleştir.
* Yalnızca dört buhar türbini gerekir.
* Başka hiçbir şeye güç sağlayamaz.
* Daha düşük kablo kaybı.

## Yöntem 2: Kablo Kaybını Tamponla
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

Herhangi bir kaybı fazladan türbinlerle karşılamak için enerji kapaklarının yakınına 4+ yuvalı bir <ItemImage id="gregtech:gt.blockmachines:171" /> Pil Tamponu yerleştir.
* Beş veya daha fazla buhar türbini gerekir.
* Piller ve yüksek amperli kablolar gerekir.
* Diğer makinelere güç sağlayabilir.
* Daha yüksek kablo kaybı.

## Isı Kapasitesi
Yapıya yerleştirilen ısıtma bobinleri EYF'nin ısı kapasitesini ve dolayısıyla hangi tarifleri çalıştırabileceğini belirler. Mevcut ısı kapasitesini görmek için kontrolcüye bir <ItemImage id="gregtech:gt.metaitem.01:32762" /> Taşınabilir Tarayıcı kullan, bir tarifin minimum ısı kapasitesini görmek için [NEI](/introduction/introduction-index.md) kullan.

Örneğin kupronikel bir EYF 1.801K ısı kapasitesine sahiptir; bu, çelik (1.000K) ve alüminyum (1.300K) eritmek için fazlasıyla yeterlidir ama <ItemImage id="gregtech:gt.metaitem.01:11856" /> Solar Kalite silisyum (2.273K) için **YETERLİ DEĞİLDİR**. Ayrıca MV'nin ötesindeki her gerilim kademesi için +100K ısı bonusu vardır; aşağıdaki grafikte görüldüğü gibi:

<LineChart title="Isı Bonusu" categories="LV,MV,HV,EV,IV,LuV,ZPM,UV,UHV,UEV,UIV,UMV,UXV,MAX,MAX+" yAxisUnit="K" width="600">
  <Series name="Isı" data="0,0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300" color="#E15759"/>
</LineChart>

Bir tarifin minimum ısı kapasitesini aşmak iki ayrı bonus sağlar. Birincisi, üzerindeki her 900K için %5 enerji indirimidir (**çarpımsal**). İkincisi, üzerindeki her 1.800K için bir [kusursuz hız aşırtma](../../tierskipping-overcloking-parallels/overclocking.md#perfect-overclocking-44)'dır. İkincisi özellikle güçlüdür çünkü EYF normalde aynı güç için yarı etkili olan kusurlu hız aşırtmalar çalıştırır.

> [!NOTE]
> *Kusurlu Hız Aşırtma* - 2x hız için 4x güç tüket (4/2).
> *Kusursuz Hız Aşırtma* - 4x hız için 4x güç tüket (4/4).

Örneğin <ItemImage id="TConstruct:materials:12" /> **Ham Alüminyum** (1.300K) eritmeyi HV güç ve <ItemImage id="gregtech:gt.blockcasings5:2" /> **Nikrom Bobinler** ile düşün. Azotlu temel tarif, 60 saniye boyunca 120 EU/t hızında 144.000 EU tüketir. EYF'nin ısı kapasitesi 3.701K, yani tarifin minimum ısı kapasitesinin tam 2.401K üzerindedir. Bu, iki adet %5 enerji indirimi ve bir adet kusursuz hız aşırtma olduğu anlamına gelir. Sonuç, 15 saniye boyunca 120 EU/t x 0.95 x 0.95 x 4 = 434 EU/t hızında yalnızca 130.200 EU tüketen bir tariftir.

> [!TIP]
> * Birden fazla giriş yolu/kapağı olabilir; bu, çeşitli sıvı girdilerini (ör. hidrojen, oksijen, azot, helyum) tutmak için faydalı olabilir. EV'de açıldıktan sonra dörtlü girdi kapağı da çok iyi çalışır.
> * Talep arttıkça ek EYF'ler inşa etmen şiddetle önerilir. GTNH'de tarif süreleri oyuncuyu altyapısını genişletmeye zorlamak için kasıtlı olarak uzundur.
> * Aynı malzeme için genellikle birden fazla tarif vardır; bu yüzden sana en uygun olanı bulmak için [NEI](/introduction/introduction-index.md) içinde ara sıra gezin. Örneğin çoğu külçenin eritme sürelerini kısaltmak için her bir soy gazla tarifi vardır ve çelik, önemli bir süre ve enerji indirimi için demir tozu yerine ferforje demir tozundan üretilebilir.
> * Ferforje demir tozu eriten bir MV EYF, çelik üretmek için 48 Tuğlalı Yüksek Fırın kadar hızlıdır ve bunun ötesine hız aşırtma yapabilir.

# Sorun Giderme
## Eksik Yapı
Tüm minimum gereksinimleri karşıladığını kontrol et (kasa sayısı, bir bakım kapağı, bir egzoz çıkışı ve bir veya daha fazla enerji kapağı). EYF'de her şey varsa kontrolcünün GUI'si içinde yapı kontrolünü zorlamayı dene. Ayrıca EYF'nin içinde görünmez bir ışık bloğu gibi hiçbir şey olmadığını kontrol et.

## Çalışmıyor
Tarifin doğru olduğunu kontrol et (eşyalar, sıvılar ve programlanmış devre). Ayrıca egzoz çıkışının bir blok, kablo veya boruyla kapatılmadığını kontrol et. Bu sorun, EYF hiç güç almıyorsa bile ortaya çıkabilir. Kabloların bağlı olduğunu ve buhar türbinlerinin doğru yöne baktığını kontrol et.

## Bir saniye çalışıp kapanıyor ve malzemeleri yok ediyor
Yeterli EU sağlandığını kontrol et. Muhtemelen çok fazla kablo kaybı vardır ya da yeterli buhar türbini yoktur. Ayrıca gelişmiş susturucularda hava filtresi olduğunu kontrol et.

## Yeterli çıkış alanı yok.
Çıkış yolunun/kapağının dolu olmadığını kontrol et. Tarif ayrıca, yapının alt katmanında çıkış kapağı gerektiren sıvı çıkışlarının aksine, yapının üst katmanında çıkış kapağı gerektiren bir gaz çıkarmaya çalışıyor olabilir. Çıkışlardan biri özellikle önemli değilse eşyalar, sıvılar veya her ikisi için hiçlik modunu etkinleştirmeyi dene.