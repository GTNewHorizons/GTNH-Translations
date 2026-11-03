---
navigation:
  title: "Enerji Üretimi ve Tüketimi"
  icon: gregtech:gt.blockmachines:1120
  parent: power_index.md
  position: -2
---

# Enerji Üretimi ve Tüketimi

# Üretim

Jeneratörler, kaynakları enerjiye dönüştüren veya özel koşullar altında görünüşte yoktan enerji üreten makinelerdir.

**Tek bloklu jeneratörler** önce çıktılarını dahili bir EU tamponunda depolar (boyutu araç ipucunda gösterilir), ardından kademelerinin standart geriliminde 1A'ya kadar çıkış verir. Tek bloklu jeneratörler talebe göre enerji üretir: yakıtı yalnızca dahili EU tamponunda yeterli yer kaldığında tüketirler. İsraf endişesi duymadan onlara yakıt besleyebilirsin.

**Multiblok jeneratörlerde** çıktı, tam yapılandırmaları tarafından belirlenir; çıkış gerilimi ve akımı ise Dinamo Kapakları tarafından sınırlanır. Multiblok jeneratörler talebe göre enerji üretmez: Dinamo Kapaklarının dahili kapasitesini aşan enerji yok edilir.

# Tüketim

> [!WARNING]
> Bir tüketici bloğa aşırı gerilim uygulamak patlamaya neden olur.

EU alan ve tüketen bloklara topluca makine denir. Bir makine yalnızca gerilimi maksimum giriş geriliminden büyük olmayan enerji paketlerini kabul edebilir; bu genellikle kademesinin standart gerilimidir. Bir makineye aşırı gerilim uygulamak onu anında patlatır.

Makineler yalnızca güç gereksinimi kendi nominal gücüne eşit veya daha az olan tarifleri çalıştırabilir. Tarif gücü genellikle ilgili kademenin standart geriliminde en fazla $$\frac{15}{16}\text{ A}$$ olur. Bu özel değere tarifin standart gücü denir.

**[Tek bloklu makineler](../singleblock/singleblock_index.md)** LV'de kullanılabilir hale gelir. Önce talebe göre enerji paketlerini dahili EU tamponlarına alır, sonra tarif çalıştırırken sürekli EU tüketirler. Maksimum giriş akımı genellikle 2A'dır; Termal Santrifüj 4A ve Ark Fırını 6A ile istisnadır.

**[Multiblok makineler](../multiblocks/multiblocks_index.md)** genellikle gücü Enerji Kapakları üzerinden alır. Standart Enerji Kapakları 2A'ya kadar kabul eder. Çok Amperli Enerji Kapakları, nominal amperajlarının 1,25 katına kadar kabul eder.

Bir makinenin dahili tamponundaki enerji tükendiğinde, tarifi yürütmeyi durdurur ve **enerji kesintisine** girer. Tek bloklu makineler tarif ilerlemesini kaybeder ama giriş durumlarını korur; multibloklar hem tarif ilerlemesini hem de girdilerini kaybeder. [Gücü güvenilir şekilde sağladığından](enet.md#providing-power-reliably) emin ol.