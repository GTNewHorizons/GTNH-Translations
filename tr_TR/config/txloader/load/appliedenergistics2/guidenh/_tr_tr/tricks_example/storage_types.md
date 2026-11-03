---
navigation:
  parent: ../tricks_example_index.md
  title: Depolama Türleri ve Ağ Düzeni
  icon: appliedenergistics2:tile.BlockDrive
---

# Çeşitli Depolama Türleri ve Ağını Düzenli Tutmak

Filtreleri, [bölümlemeleri](../items_blocks/cell_workbench.md) ve [depolama önceliğini](../ae2_mechanics/import_export_storage.md#storage-priority)
kullanarak farklı türde şeyler için birkaç depolama kademesi kurabilirsin.

Depolama türleri genellikle şunlardır:
* Genel depolama, birkaç ila birkaç bin adet sahip olduğun rastgele her şey için. 4k veya 16k gibi küçük [hücreler](../items_blocks/storage_cells.md)
kullanır.
* Yığın depolama, birkaç binden fazla sahip olduğun her şey için, örneğin kırıktaş veya demir. 256k gibi büyük hücreler
veya MEGA eklentisindeki hücreler kullanır.
* Çiftliklerde yerel depolama, [Özelleştirilmiş Yerel Depolama](specialized_local_storage.md) bölümünde anlatıldığı gibi. Certus çiftliği örnekleri yüksek sürümlü Budding Certus bloklarına bağlıdır ve 1.7.10'a taşınmamıştır.

Öncelikler şöyle ayarlanır: eşyalar ana ağa atıldığında ağ önce onları özelleştirilmiş
yığın veya yerel depolamada saklamayı dener; bu yapılamazsa (filtreler ve bölümlemeler nedeniyle) eşyaları genel depolamaya koyar.
Bu, eşyaların bir depolamadan diğerine ETKİN OLARAK TAŞINMAYACAĞI, ancak ağa girip çıkarken "göç edeceği" anlamına gelir.
Eşyaları etkin olarak taşımak için bir <ItemLink id="appliedenergistics2:tile.BlockIOPort" /> kullan.

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="../assets/structures/network_storage_types.snbt" />

  <BoxAnnotation color="#33dd33" min="0 0 4" max="1 1.3 5">
  Yığın Depolama. Bu durumda çekmece gibi yüksek kapasiteli bir depolama üzerinde filtrelenmiş bir depolama veriyolu. Bu depolama veriyolu
  kömüre filtrelenmiştir. Yüksek önceliğe sahiptir, böylece kömür ağa girdiğinde bu depolama veriyoluna gider ve kömür
  ağdan çekildiğinde *burası hariç her yerden* çekilir, böylece kömür bu çekmeceye "göç eder".

  ÖNEMLİ NOT: Çekmeceler gibi büyük optimize edilmiş envanterler bunun için uygundur, ancak devasa sandıklar gibi
  çok sayıda yuvaya sahip büyük *optimize edilmemiş* envanterler depolama veriyollarıyla kullanıldığında performans açısından berbattır.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 0 4" max="3 1 5">
  Yığın Depolama. Bu durumda yüksek öncelikli bir sürücüde bölümlenmiş 256k'lık bir hücre. Bu hücre kırıktaşa ve
  demire bölümlenmiştir. Eşit Dağıtım Kartı vardır, böylece tamamen kırıktaşla dolup demire
  yer bırakmaz. Sürücü yüksek önceliğe sahiptir, böylece kırıktaş veya demir ağa girdiğinde bu depolama veriyoluna gider
  ve kırıktaş veya demir ağdan çekildiğinde *burası hariç her yerden* çekilir, böylece kırıktaş ve demir bu hücreye "göç eder".
  </BoxAnnotation>

  <BoxAnnotation color="#33dddd" min="4 0 4" max="5 1 5">
  Genel Depolama. Bu durumda 16k hücrelerle dolu bir sürücü. Bu hücreler bölümlenmemiştir. Sürücü nötr önceliğe sahiptir
  (bu durumda 0), böylece bir şey ağa girdiğinde önce özelleştirilmiş yığın veya yerel depolamaya gider
  ve bir şey ağdan çekildiğinde önce buradan çekilir, böylece özelleştirilmiş depolaması olan eşyalar doğal olarak
  genel depolamadan "göç eder".
  </BoxAnnotation>

  <BoxAnnotation color="#88ff88" min="7 0 4" max="8 1 5">
  Bu İo Bağlantı Noktası ağı düzenli tutmada önemli bir rol oynar. Depolama önceliği eşyaları *etkin olarak*
  taşımadığından, Genel Depolamada kullanılan hücreler, özelleştirilmiş depolamada yeri olan eşyaları o depolamaya taşımak için
  düzenli olarak bir İo bağlantı noktasından "karıştırılmalıdır". Bu, depolamayı "birleştirir" ve eşyaların
  birden fazla yerde saklanmadığından emin olur.
  </BoxAnnotation>

  <BoxAnnotation color="#dd3333" min="10 0 1" max="11 1 2">
  Bir canavar çiftliğinde yerel depolama. Bu sürücüde, tutmak istediğin düşüşlere (kemik ve ok gibi) bölümlenmiş hücreler var.
  Sürücünün kendisine öncelik verilmez, çünkü önceliği etkileyen şey alt ağa ana ağdan erişen depolama veriyoludur.
  Hücrelerde eşit dağıtım kartları ve taşma yok etme kartları vardır.
  </BoxAnnotation>

  <BoxAnnotation color="#dd3333" min="9 1 1" max="10 2.3 2">
  Bir canavar çiftliğinde yerel depolama. Bu depolama veriyolu - arayüz kurulumu, ana ağın bu alt ağın depolamasına erişmesini sağlar.
  Depolama veriyoluna yüksek öncelik verilir ve alt ağdaki hücrelerde saklanan şeylere filtrelenir.

  ÖNEMLİ: Alt ağdaki çöp kutusu kurulumu nedeniyle bu depolama veriyolunu filtrelediğinden emin ol, yoksa
  *ağa giren her bir eşyayı, sıvıyı vb. çöpe atmaya* başlar!
  </BoxAnnotation>

  <BoxAnnotation color="#dd3333" min="8 0 1" max="9 1.3 2">
  Bir canavar çiftliğinde yerel depolama. Bir madde yoğunlaştırıcısı üzerindeki bu depolama veriyolu, sürücüden daha düşük önceliğe ayarlanmıştır. Bu,
  sürücüdeki hücrelere giremeyen canavar düşüşlerinin buraya taşacağı ve imha edileceği anlamına gelir. Bu önemlidir,
  çünkü alt ağın çoğu kırık yaylar gibi rastgele çöplerle dolup tıkanmasını önler.
  </BoxAnnotation>

  <BoxAnnotation color="#dd33dd" min="10.7 1 7" max="12 2.3 8">
  Bir karpuz çiftliğinde yerel depolama. Bu kurulum, çeşitli certus çiftliği örneklerinde kullanılan benzer bir yöntemi kullanır. Alt ağdaki bir depolama veriyolu
  yetiştirilen şeyi bir varile ekler. Ana ağdaki başka bir depolama veriyolu (karpuz
  dilimlerine filtrelenmiş ve yüksek öncelikli) ana ağa yetiştirilen şeylere erişim sağlar.
  </BoxAnnotation>

  <IsometricCamera yaw="270" pitch="30" />
</GameScene>