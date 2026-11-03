---
item_ids:
  - gregtech:gt.blockmachines:13532
quest_ids:
  - ZIotzqvnRiKu1_1Hb9i1dg==
navigation:
  title: Gelişmiş Montaj Hattı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:13532
  position: -5001
---

# Gelişmiş Montaj Hattı

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:13532" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" /> (AAL), eşya boru hattından yararlanarak [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) tariflerini paralel çalıştıran IV kademesinde bir multibloktur; malzemeler gerçek bir Montaj Hattı gibi hepsi bir anda değil, dilim dilim tüketilir. Bu, maksimum paralel sayısının bir tarifteki katı malzeme sayısına karşılık geldiği anlamına gelir. 

AAL, ciddi hız aşırtma ve devasa paralel işlem için çok amperli ve lazer enerji kapaklarını destekler ancak **kademe atlayamaz** ve normal [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) hattına kıyasla otomatikleştirilmesi daha zordur; bu da AAL'i erken oyun ilerlemesi yerine Yıldız Geçidi malzemesi gibi oyun sonu seri üretimine özelleştirir. 

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı Kademe | IV |
| Yapı Boyutu (UxGxY) | 3x5-16x4 |
| Güç | Her tür kapak kullanılabilir, Çok Amperli ve Lazer Kapaklar dahil |
| Hız aşırtma | Benzersiz |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

### Üretim
<RecipesFor id="gregtech:gt.blockmachines:13532" handlerId="gt.recipe.fakeAssemblylineProcess" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gregtech:gt.blockcasings2" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="gregtech:gt.blockcasings2:5" />

<RecipesFor id="gregtech:gt.blockcasings2:9" />

### Yapı
AAL ile [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) arasındaki tek yapısal fark kontrolcüdür. 

AAL döndürülebilir veya çevrilebilir.

Cam herhangi bir kademeden olabilir ve makinenin çalışmasına etkisi yoktur. 

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek için "glass", dilim sayısını belirtmek için "length" alt kanalını kullan $$(\text{Slices} = \text{Length} + 4)$$

#### Temel Yapı (Minimum gereksinimler)
| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" /> | İlk dilim, 3. katman |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir Kademeli Cam | 10, 2. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 8, 3. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-12, 1. katmanın her iki yanı ve 4. katmanın merkezi |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 5, 2. katmanın merkezi |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 5, 3. katmanın merkezi |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Enerji Kapağı">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 1+, Herhangi bir 4. katman Kasası |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, Herhangi bir 1. katman yan kasası |
| <ItemImage id="gregtech:gt.blockmachines:145" noTooltip />Veri Erişim Kapağı | 1, 3. katmanın herhangi bir yanı, ancak ilk dilimde <Color id="red">**DEĞİL**</Color> |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 5, 1. katmanın merkezi |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, Herhangi bir 1. katman yan kasası |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1, Son dilimde herhangi bir 1. katman konumu |

#### Her Ek Dilim

<GameScene interactive={true} wrap="square" align="right" width="170" height="130">
  <Block id="gregtech:gt.blockmachines:71" />
  <Block id="gregtech:gt.blockcasings2" x="-1"/>
  <Block id="gregtech:gt.blockcasings2" x="1"/>
  <Block id="gregtech:gt.blockcasings2:5" y="1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="-1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="1" />
  <Block id="gregtech:gt.blockcasings2:9" y="2" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="-1" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="1" />
  <Block id="gregtech:gt.blockcasings2" y="3"/>
</GameScene>

Her ek dilim (1 uzunluk) şu blokları gerektirir:

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir Kademeli Cam | 2, 2. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 2, 3. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-3, 1. katmanın her iki yanı ve 4. katmanın merkezi |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 1, 2. katmanın merkezi |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 1, 3. katmanın merkezi |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1, 1. katmanın merkezi |

Herhangi bir dilimde 4. katman kasasının yerine <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Enerji Kapakları">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> koyabilir, 1. katmandaki <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> yerine de <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapakları kullanabilirsin.

AAL dilimlerini uzattığında <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolunu son dilime taşıman gerektiğini unutma.

### Duvar Paylaşımı

AAL'ler kasa, cam ve veriyolu/kapak tasarrufu için her bir yanını duvar paylaşabilir. Buna her türlü Girdi Kapağı, bakım kapağı, veri erişim kapağı ve Çıkış Yolu dahildir. Veri erişim kapağını paylaşmak özellikle TPS tasarrufu ve çalıştırmak için gereken [<ItemLink id="gregtech:gt.blockmachines:15313" showIcon="left" />](./data_bank.md) multiblok sayısını azaltmak açısından çok değerlidir.

## Kullanım

<GameScene wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/aal_operation_ponder.snbt" />
  <ImportPonder src="/assets/ponders/multiblocks/aal/aal_operation_ponder.json" />
</GameScene>

AAL, veriyollarının/kapakların içeriği kayıtlı bir veri çubuğuyla eşleştiğinde tıpkı normal [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) gibi işlemeye başlar. Her tarif makinede N dilimden geçmek zorundadır; burada N katı malzeme sayısıdır. Her dilim, giriş yolundaki TEK tür eşyayı işlemek için $$\text{T} = (\text{base duration} / \text{N})$$ saniye harcar ve ardından sıradaki malzeme için bir sonraki dilime geçer. Bu, tüm malzemeler tükenene ve son ürün alınmak üzere çıkış yoluna gönderilene kadar tekrarlanır. Tüm sıvılar işlemenin en başında tüketilir.

AAL, ilk dilim ilk tarifi bitirdiğinde bir sonraki tarifin başlamasına izin vererek paralel işlemeyi destekler. Bu, yeterli kaynak varsa her dilimin aynı anda çalışmasını sağlayan kademeli bir düzen oluşturur.

Bir sonraki dilimin giriş yolunda gereken eşya yoksa mevcut dilim **STUCK** durumuna geçer ve eksik eşya bulunana/geri getirilene kadar tüm makine durur. Kontrolcünün yüzündeki durum ışığı, makinenin STUCK olduğunu belirtmek için turuncuya döner. Sorunun tam olarak nerede olduğunu bulmak için WAILA'yı kullan.

Sağdaki sahne, AAL'in aynı tarifi dilim dilim nasıl aynı anda işlediğini, AAL'in neden takıldığını ve bunun nasıl çözüleceğini gösteriyor.

### Lazer Hız Aşırtmaları

AAL'in enerji tüketimi, paralellerde olduğu gibi etkin dilim sayısı ile temel EU/t'nin çarpımıdır. Ardından AAL, N taneye kadar kusurlu hız aşırtma çalıştırır; burada N, en düşük kademeli enerji kapağının gerilim kademesi ile tarifin gerilim kademesi arasındaki farktır. 

Sonraki hız aşırtmaların hepsi lazer hız aşırtmasıdır; daha fazla güç tüketirler ve kusurlu bir hız aşırtmadan bile daha kötü ölçeklenirler. İlki 4,3 kat güç karşılığında 2 kat hız sağlar ve her ek hız aşırtma güç çarpanını 0,3 artırır; sonsuza kadar ölçeklenir.

- Kusurlu Hız Aşırtmalar - 4,0 kat güç karşılığında 2 kat hız (2/4.0).
- 1. Lazer Hız Aşırtması - 4,3 kat güç karşılığında 2 kat hız (2/4.3).
- 2. Lazer Hız Aşırtması - 4,6 kat güç karşılığında 2 kat hız (2/4.6).
- 3. Lazer Hız Aşırtması - 4,9 kat güç karşılığında 2 kat hız (2/4.9).

Lazer hız aşırtmalarının artan güç maliyeti, enerji kapağını/kapaklarını yükseltmenin makineyi her zaman hız aşırtacağı anlamına gelmez. Her şey tarifin temel EU/t değerine ve maksimum paralel sayısına bağlıdır. 

Örnek olarak UIV alan üreteci tarifini ele alalım. Aynı anda en fazla 14 dilim etkin olabilir ve her biri 15/16A UEV güç tüketerek toplamda 13,1A'ya ulaşır. Bu, 16A'lik bir UEV enerji kapağının tarifin temel maliyetini karşılamaya yettiği ancak hiç lazer hız aşırtma sağlamadığı anlamına gelir. 64A'lik bir enerji kapağına yükseltmek bir lazer hız aşırtma sağlar çünkü bu 13.1 x 4.3 = 56.4A'dan büyüktür; ancak 256A'lik bir enerji kapağına yükseltmek ikinci bir lazer hız aşırtma **SAĞLAMAZ** çünkü bu 56.4 x 4.6 = 259A'dan küçüktür. Aşağıdaki tablo, 15/16A güç tüketen aynı kademedeki tarifler (yani bir UEV lazer enerji kapağına sahip UEV tarifleri) için belirli sayıda lazer hız aşırtma elde etmek üzere gereken amperajı listeler.


| Dilim | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 64 | 256 | 1,024 | 4,096 | 16,384 | 65,536 | 1,048,576 | 4,194,304 | 
| 5 | 64 | 256 | 1,024 | 4,096 | 16,384 | 262,144 | 1,048,576 | 4,194,304 | 
| 6 | 64 | 256 | 1,024 | 4,096 | 16,384 | 262,144 | 1,048,576 | 4,194,304 |
| 7 | 64 | 256 | 1,024 | 4,096 | 65,536 | 262,144 | 1,048,576 | 4,194,304 | 
| 8 | 64 | 256 | 1,024 | 4,096 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 9 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 10 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 | 
| 11 | 64 | 256 | 1,024 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 12 | 64 | 256 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 13 | 64 | 256 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 14 | 64 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 15 | 64 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |
| 16 | 256 | 1,024 | 4,096 | 16,384 | 65,536 | 262,144 | 1,048,576 | 16,777,216 |


## Kaynaklar

- [GTNH Wiki: Gelişmiş Montaj Hattı](https://wiki.gtnewhorizons.com/wiki/Advanced_Assembly_Line)