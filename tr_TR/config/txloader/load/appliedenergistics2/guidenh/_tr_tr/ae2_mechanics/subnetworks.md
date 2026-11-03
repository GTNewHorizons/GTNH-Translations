---
navigation:
  parent: /ae2_mechanics_index.md
  title: Alt Ağlar
  icon: appliedenergistics2:item.ItemMultiPart:140
---

# Alt Ağlar

<GameScene width="600" height="400" zoom={4} rotateX={25} rotateY={-45}>
  <ImportStructure src="../assets/structures/subnet_demonstration.snbt" />

  <DiamondAnnotation pos="1.5 2.5 9.5" color="#00ff00">
  Montajcı çıktılarını varile taşır.
  </DiamondAnnotation>

  <DiamondAnnotation pos="1.5 2.5 8.5" color="#00ff00">
  Üstteki Süper Tank'ın sıvılarını alttakine taşır.
  </DiamondAnnotation>

  <DiamondAnnotation pos="1.5 2.5 7.5" color="#00ff00">
  Kızıltaş P2P alt ağı, kızıltaş bloğunun \
  gücünü kızıltaş lambasına iletir.
  </DiamondAnnotation>

  <DiamondAnnotation pos="1.5 2.5 6.5" color="#00ff00">
  Varilin içeriğini bir eşya yok etme hücresine taşır.
  </DiamondAnnotation>

  <DiamondAnnotation pos="1.5 2.5 5.5" color="#00ff00">
  Arayüz-Depolama Veriyolu etkileşimini kullanarak \
  ana ağın erişebileceği yerel bir alt depolama \
  görevi gören alt ağ.
  </DiamondAnnotation>

  <DiamondAnnotation pos="2.5 0.5 3.5" color="#00ff00">
  Bir kalıbın içeriğini EYF'nin girişlerine taşıyan, \
  ardından çıktıyı kalıpların geldiği aynı arayüzden \
  ana ağa geri veren EYF otomatik üretim alt ağı.
  </DiamondAnnotation>
</GameScene>

"Alt ağ" oldukça gevşek tanımlanmış bir terim; yine de bir alt ağın ana ağını destekleyen veya küçük bir iş yapan herhangi bir [ağ](./me_network_connections.md) olduğu söylenebilir. Başlangıçta genellikle kontrolcü gerektirmeyecek kadar küçüktürler; ancak AE2 sistemine multibloklar girdiğinde bu çok hızlı değişir.

Başlıca 3 kullanım alanı şunlardır:

* [Cihazların](./devices.md) hangi depolamaya erişebileceğini kısıtlamak (örneğin cevher işleme alt ağının ürünlerini ana ağına boşaltmasını istemezsin ama yine de onları ana ağdan görmek istersin).
* Ana ağda kanal tasarrufu yapmak; örneğin kalıplı bir arayüzün çıktısını birkaç makinedeki birkaç depolama veriyoluna bağlı bir arayüze vermek, birkaç makineye arayüz koyup birkaç kanal kullanmak yerine (ana ağdan) 1 kanal kullanır. 
* Kalın kablolardan ve alandan tasarruf etmek; 32 ana ağ kanalını tek bir [P2P](./p2p_tunnels.md) taşıyıcı alt ağı kanalında paketleyerek uzun mesafelerde verimli kanal taşımacılığı yapmak.

Alt ağ oluştururken [ağ bağlantılarını](./me_network_connections.md) takip etmek çok önemlidir.
Çoğu zaman insanlar arayüz, veriyolu ve benzeri şeylerden karmaşık bir yığın oluşturup bunun bir alt ağ olmasını bekler;
oysa tüm cihazlar hâlâ çeşitli tam blok cihazlar üzerinden ana ağa bağlıdır.

> [!NOTE]
> Farklı renkteki kabloların alt ağ oluşturmakla ilgisi yoktur; tek farkları birbirlerine bağlanmamalarıdır.

Alt ağların bazı kullanım durumları şunlardır:

* <Color id="BLUE"> Soyutlama</Color>. Karmaşık bir üretim işleminin tüm ayrıntılarını alt ağından yönet; böylece ana ağının bakış açısından
  tüm fabrika tek bir makine gibi "görünür".
* <Color id="GREEN"> Paralellik</Color>. Yavaş bir makineyi yavaş makinenin 10 kopyasıyla değiştir. Ana ağının bakış açısından hiçbir şey değişmez
  ve fazladan kanal bile kullanmazsın.
* <Color id="YELLOW"> Multiblok kalıplama</Color>. Tüm malzemelerini bir alt ağda kolayca aynı giriş veriyollarına/kapaklarına gönder.

Bazı örnekler şunlardır:

* Bir eşya veya sıvı borusu gibi eşya ya da sıvıları bir kaptan diğerine aktarmak için kurulmuş bir içe aktarma veriyolu ve depolama veriyolu.
* Bir yok etme düzlemi ve depolama veriyolu; böylece yok etme düzleminin kırdığı şeyleri koyabileceği tek yer depolama veriyolu olur ve düzlemi filtreleyebilirsin.
* Bir arayüz ve oluşturma düzlemi; böylece arayüze eklenen her şey oluşturma düzlemine itilir ve dünyaya yerleştirilir/bırakılır.
* Ana ağdan Arayüz üzerindeki Depolama Veriyolu etkileşimiyle erişilebilen özel bir depolama sistemi; böylece bir çiftliğin çıktısını ana depolamanı sonsuza dek taşırmadan saklayabilirsin.
* Ve benzerleri

Alt ağ oluştururken <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" showIcon="left" /> çok işine yarar. Ağlar arasında onları birbirine bağlamadan
güç aktarır; böylece her yere enerji alıcıları ve güç kabloları koymadan alt ağlara güç verebilirsin.