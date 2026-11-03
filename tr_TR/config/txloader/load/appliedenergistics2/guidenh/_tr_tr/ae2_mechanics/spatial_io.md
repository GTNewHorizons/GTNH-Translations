---
navigation:
  parent: /ae2_mechanics_index.md
  title: Uzamsal İo
  icon: appliedenergistics2:tile.BlockSpatialPylon
---

# Uzamsal İo

Uzamsal İo, dünyandaki fiziksel uzay hacimlerini kesip yapıştırmanın bir yoludur. <ItemLink id="appliedenergistics2:tile.BlockSpatialPylon" showIcon="left"/> ve <ItemLink id="appliedenergistics2:tile.BlockSpatialIOPort" showIcon="left"/> bloklarından oluşan bir multiblok yapı sayesinde tanımlı bir uzay hacmini bir Uzamsal Depolama Hücresine sıkıştırmanı, yanında taşımanı ve depolanan içeriği herhangi bir yerde serbest bırakmanı sağlar. End portalı çerçevelerini bile taşıyabilirsin!

Uzamsal Pilonlar blokları ve varlıkları taşıyabilir; bu da depolama hücrelerini boyutlar arasında taşıyacak araçlara sahipsen ve Uzamsal İo sistemini otomatikleştirebiliyorsan, Uzamsal Pilonları oyuncular dahil canlı varlıkları boyutlar arasında ışınlamak için bile kullanabileceğin anlamına gelir. Ancak Uzamsal Pilonların enerji maliyetinin oldukça yüksek olduğunu unutma. Enerji üretiminin kısıtlı olduğu dönemlerde işletme maliyetini önceden hesaplaman en iyisidir.

# Uzamsal Pilon Multiblok Yapısı
Uzamsal İo'nun çalışması tanımlı bir alan gerektirir ve bu alanın hacmi, kullanılan Uzamsal Depolama Hücresinin hacmine eşit veya ondan küçük olmalıdır.

Etki alanı Uzamsal Pilon blokları tarafından tanımlanır. Tüm Uzamsal Pilonlar aynı ME Ağında olmalıdır; bir alt ağ kullanman önerilir. 1\*1\*n (n > 1) bitişik Uzamsal Pilon bloğu kullanmak bir Uzamsal Pilon sütunu oluşturabilir. Birden fazla sütun 1 blok kalınlığında kare bir kabuk oluşturur ve içindeki boşluk Uzamsal İo sistemi için etki alanıdır. Başka bir deyişle, Uzamsal İo'nun etki alanı, tüm Uzamsal Pilon multiblok yapısının sınırlarından bir blok daha küçüktür.

Uzamsal İo multiblok sisteminin inşası şu kurallara uyar:
  * Her Uzamsal Pilon sütunu en az 2 Uzamsal Pilon bloğundan oluşmalı ve sütun düz bir çizgi olmalıdır.
  * Tüm Uzamsal Pilon sütunları aynı ME Ağında olmalıdır ve her sütun 1 kanal kaplar.
  
<GameScene zoom="2" rotateY={200} height="200"  >
    <ImportStructure src="../assets/structures/spatial_io_spatial_pylons_rule.snbt" />
    <BoxAnnotation min="3 0 0" max="5 1 1" color="#EE3333" thickness="1">
      Bu Uzamsal Pilon sütunu koyu kırmızıdır, bu da onun enerjisiz olduğunu gösterir. Bu sahnede ikisini ayırt etmek zor olabilir, ancak oyun içinde çok daha belirgindir.
    </BoxAnnotation>
</GameScene>

  * Etki alanı, tüm Uzamsal Pilon sistemi boyunca maksimum ve minimum X, Y ve Z koordinatlarındaki Uzamsal Pilon blokları tarafından tanımlanır.
  * Tanımlanabilecek en küçük etki alanı 1\*1\*1'dir.
  * Tüm Uzamsal Pilon sütunları kare kabuk üzerinde yer almalıdır. Kabuğun içindeki etki alanında etkin Uzamsal Pilon sütunu bulunamaz.
  * Geçerli Uzamsal Pilon dokuları birbirine bağlanır.
    * Noktalı mor doku geçersiz bir Uzamsal Pilon yapısını belirtir.
    * Koyu kırmızı Uzamsal Pilonlar enerjisiz olduklarını belirtir.
    * Parlak kırmızı Uzamsal Pilonlar geçerli bir Uzamsal Pilon yapısını, ancak multiblok yapısının geçerli bir etki alanı oluşturmadığını belirtir.
    * Parlak mor Uzamsal Pilonlar multiblok yapısının tamamen oluştuğunu belirtir.

<GameScene zoom="2"  width ="300" height="200" rotateY={225} >
    <ImportStructure src="../assets/structures/spatial_io_spatial_pylons_rule2.snbt" />
    <Block id="appliedenergistics2:tile.BlockCableBus" nbt='{__guidenh_encoded_keys_v1:[0:{v:{id:"appliedenergistics2:item.ItemMultiPart",Count:1b,Damage:36s},k:"def:6"},1:{v:{},k:"extra:6"}],id:"BlockCableBus",hasRedstone:2}' x="2" z="2"/>
    <BoxAnnotation min="5 0 0" max="0 5 5" color="#EE3333" thickness="1" alwaysOnTop={true}>
      Kırmızı kutu Uzamsal Pilon yapısının sınırlarını gösterir ve etki alanı "kabuğun" içinde yer alır.
    </BoxAnnotation>
    <BoxAnnotation min="4 1 1" max="1 4 4" color="#00ff00" thickness="1">
      Yeşil kutu Uzamsal İo etki alanıdır. Bu alana aynı ağa bağlı yeni bir Uzamsal Pilon sütunu yerleştirmek, geçersiz bir Uzamsal Pilon multiblok yapısıyla sonuçlanır.
    </BoxAnnotation>
</GameScene>

# Uzamsal İo Bağlantı Noktası
<ItemLink id="appliedenergistics2:tile.BlockSpatialIOPort" showIcon="left"/> Uzamsal İo işlemleri için kontrol terminalidir. Multiblok yapısının istatistiksel bilgilerini gösterir.

Tüm sistemi kurduktan sonra bir Uzamsal İo işlemi yürütmek istersen, giriş yuvasına bir Uzamsal Depolama Hücresi koy ve Uzamsal İo Bağlantı Noktasına bir Kızıltaş darbesi gönder; Uzamsal İo sistemi ardından etkinleşir. Etki alanındaki tüm blokların ve varlıkların, kendin dahil, hücrenin içine depolanacağını unutma. Kaçma yolun yoksa Uzamsal Depolama Hücresi boyutunda - karanlık, özelliksiz bir alan - mahsur kalırsın. Bunu arkadaşlarına şaka yapmak için kullanabilirsin!

# Enerji Tüketimi
Uzamsal İo Bağlantı Noktasının her etkinleştirilmesi, gereken enerjiyi tek seferde tüketir. Değer Uzamsal İo Bağlantı Noktasında listelenir, bu yüzden önceden yeterli [Enerji Hücresi](../items_blocks/energy_cells.md) hazırla.

Tek bir Uzamsal İo işleminin enerji tüketimi, etki alanının hacmiyle hızla artar ve enerji verimliliği katsayısından etkilenir. Enerji üretiminin kısıtlı olduğu dönemlerde enerji üretimini iyileştirmek akıllıca bir seçimdir.

Basitçe söylemek gerekirse, enerji verimliliği multiblok yapısını oluşturan Uzamsal Pilon sayısıyla pozitif ilişkilidir, ancak enerji verimliliğinin güç tüketimini azaltma etkisi logaritmik olarak düşer. Bu, maksimum azaltmayı elde etmenin son derece yüksek enerji verimliliği gerektirdiği, bunun da daha fazla Uzamsal Pilon bloğu gerektirdiği anlamına gelir. Enerji tüketimini Enerji Hücrelerinin ve Uzamsal Pilon bloklarının üretim maliyetleriyle birlikte düşündüğünde, genellikle %50~60 verimlilik civarında bir dengeye ulaşılır.

# Tam Çalışır Yapı
Multiblok yapısının tüm kurallarını anladıysan, aşağıdaki yapının geçerli ve çalışır olduğunu görebilirsin.

<GameScene zoom="2" width="300" rotateY={200} >
    <ImportStructure src="../assets/structures/spatial_io_mess.snbt" />
    <BoxAnnotation min="7 0 8" max="0 5 0" color="#EE3333" thickness="1">
    </BoxAnnotation>
    <BoxAnnotation min="6 1 7" max="1 4 1" color="#00ff00" thickness="1">
    </BoxAnnotation>
</GameScene>

Ancak fazlasıyla dağınık ve yeterince sade değil. Pratikte aşağıdaki yapı tasarımlarına başvurabilirsin:
<GameScene zoom="2" width="300" rotateY={200} >
    <ImportStructure src="../assets/structures/spatial_io_simple.snbt" />
    <BoxAnnotation min="9 0 0" max="5 4 4" color="#EE3333" thickness="1">
    </BoxAnnotation>
    <BoxAnnotation min="8 1 1" max="6 3 3" color="#00ff00" thickness="1">
    </BoxAnnotation>
    <BoxAnnotation min="4 0 0" max="0 4 4" color="#EE3333" thickness="1">
    </BoxAnnotation>
    <BoxAnnotation min="3 1 1" max="1 3 3" color="#00ff00" thickness="1">
    </BoxAnnotation>
</GameScene>

Daha yüksek enerji verimliliğine sahip bir yapı:

<GameScene zoom="2" width="300" rotateY={-135} >
    <ImportStructure src="../assets/structures/spatial_io_efficiency.snbt" />
    <BoxAnnotation min="6 0 6" max="0 5 0" color="#EE3333" thickness="1">
    </BoxAnnotation>
    <BoxAnnotation min="5 1 5" max="1 4 1" color="#00ff00" thickness="1">
    </BoxAnnotation>
</GameScene>

Her şey hazır olduğuna göre, hadi Uzamsal İo'yu etkinleştirelim!

<GameScene zoom="2" width="400" height="275" rotateY={30}>
    <ImportStructure src="../assets/structures/spatial_io_working.snbt" />
    <ImportPonder src="../assets/ponder/spatial_io_working.json" />
</GameScene>

# Uzamsal Depolama Hücresi Boyutu
Uzamsal Pilonun çalışma prensibi, seçilen alandaki tüm uzayı [Uzamsal Depolama Hücresi](../items_blocks/spatial_cells.md) içindeki aynı boyuttaki bir uzayla takas etmektir. Yeni bir Uzamsal Depolama Hücresi ilk kez kullanıldığında, hücre hacim özellikleriyle tam olarak eşleşen bir boyut oluşturur. Başka bir deyişle, her yeni Uzamsal Depolama Hücresini hava bloklarıyla dolu olarak düşünebilirsin; Uzamsal Pilon ilk kez uzamsal takas için kullanıldığında, depolama hücresinden karşılık gelen boyuttaki hava hacmini takas eder.

<Color id="RED">Bir Uzamsal Depolama Hücresi kullanıldıktan sonra sıfırlayamaz, biçimlendiremez veya boyutunu ayarlayamazsın. Farklı bir boyut kullanmak istersen yeni bir hücre üretmelisin.</Color>

<GameScene zoom="2" width="400" height="200" rotateY={200} offsetX={-80} allowLayerSlider={false} gridButtonEnabled={false}>
    <ImportStructure src="../assets/structures/spatial_io_dimension.snbt" />
    <BoxAnnotation min="-3 2 -2" max="-6 5 1" color="#EE3333" thickness="1">
    Uzamsal Depolama Hücresi Boyutu
    </BoxAnnotation>
    <ImportPonder src="../assets/ponder/spatial_io_dimension.json" />
</GameScene>