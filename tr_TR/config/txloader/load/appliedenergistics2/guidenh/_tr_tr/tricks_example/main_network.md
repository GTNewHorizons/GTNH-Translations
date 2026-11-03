---
navigation:
  parent: ../tricks_example_index.md
  title: Örnek Bir "Ana Ağ"
  icon: appliedenergistics2:tile.BlockController
---

# Örnek Bir "Ana Ağ"

Diğer birçok kurulum bir "Ana Ağ"a atıfta bulunur. Tüm bu [cihazların](../ae2_mechanics/devices.md) nasıl bir araya gelerek işlevsel bir sistem oluşturduğunu da merak ediyor olabilirsin. İşte bir örnek:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/structures/small_base_network.snbt" />

  <BoxAnnotation color="#33dd33" min="3 1 5" max="7 7 9">
  Büyük bir ME Arayüzü ve birleştirici kümesi, üretim kalıpları için bolca yer sağlar.
  Satranç tahtası deseni, arayüzlerin kompakt kalırken birden fazla birleştiriciyi paralel kullanmasını sağlar.
  8'li gruplar kanalların yanlış yönlendirilmesini imkansız hale getirir.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 10 13" max="5 11 14">
  Aslında o kadar büyük bir kontrolcüye ihtiyacın yok; insanların üslerinde gördüğün tüm o devasa halkalar ve küp tasarımları
  çoğunlukla sadece havalı görünmek için.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 12 13" max="4 13 14">
  Her iyi ağda bir enerji hücresi bulunur; oyun tiki başına daha yüksek enerji girdisine izin verir ve
  güç dalgalanmalarını düzgünleştirir.
  </BoxAnnotation>
    
  <BoxAnnotation color="#33dd33" min="4 1 2" max="7 4 4">
  Muhtemelen başka bir modun güç kaynağını kullanmak istersin: bir reaktör, güneş paneli, jeneratör ya da
  her neyse. Titreşim Odaları fena değildir ama AE2 bir modpack içinde kullanılmak ve üssünün
  ana güç jeneratörünü kullanmak üzere tasarlanmıştır.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 1 15" max="8 3 16">
  Cepheler duvarların arkasındaki şeyleri gizlemek için kullanılabilir.
  </BoxAnnotation>
  <BoxAnnotation color="#33dd33" min="3 3 15" max="5 10 16">
  Cepheler duvarların arkasındaki şeyleri gizlemek için kullanılabilir.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8 9 13" max="10 10 14">
  Genel depolaman için o kadar çok sürücü yuvası ve hücreye ihtiyacın yok; 4k veya 16k hücrelerle
  dolu 2-4 Sürücü neredeyse her zaman yeterlidir.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 13" max="7 11 14">
  Yığın depolama için, daha yüksek önceliğe ayarlanmış ayrı sürücülerde belirli eşyalara süzülmüş
  büyük hücreler istersin.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 9 10" max="4 13 11.7">
  Arayüz tabanlı otomatik stoklama.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 10 6" max="5 12 9">
  Şarj cihazı otomasyon kurulumunun birden fazla şarj cihazına mantıksal genişlemesi.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 9 2" max="5 10 5">
  Yazıcıları birbirine bağlamak için boru alt ağlarını kullanan işlemci otomasyonu.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 3" max="7 11 4">
  Yazıcıları birbirine bağlamak için boru alt ağlarını kullanan işlemci otomasyonu.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8.2 9.2 7.2" max="8.8 10 7.8">
  Kablosuz erişim noktası ortada çünkü menzili küresel.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 1 14" max="15 5 16">
  Genellikle büyük işler için 1-2 büyük üretim CPU'su, büyük CPU'lar meşgulken ikincil işleri halletmek için de
  birkaç daha küçük CPU'n bulunur.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 3 5" max="11 4 6">
  Bazen 8'den fazla cihaz varsa (örneğin 8'den fazla yere dağıtım yapılıyorsa) alt ağların kendi kontrolcüsüne
  ihtiyacı olabilir.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="11 1 7" max="14 4 9">
  Kırıktaş çiftliği.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="12 1 10.3" max="14.7 3.7 12.7">
  Suya Atma otomasyonu.
  </BoxAnnotation>

  <IsometricCamera yaw="220" pitch="15" />
</GameScene>