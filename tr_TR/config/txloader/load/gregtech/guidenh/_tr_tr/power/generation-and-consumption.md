---
navigation:
  title: "Güç Üretimi ve Tüketimi"
  icon: gregtech:gt.blockmachines:1120
  parent: power-index.md
  position: -2
---

# Güç Üretimi ve Tüketimi

# Üretim

Jeneratörler, kaynakları güce dönüştüren veya özel koşullarda görünüşte yoktan güç üreten makinelerdir.

**Tek bloklu jeneratörler** çıktılarını önce dahili bir EU tamponunda depolar (boyutu ipucunda gösterilir), ardından kademelerinin standart geriliminde 1A'ya kadar çıkış verir. Tek bloklu jeneratörler talebe göre güç üretir: yakıtı yalnızca dahili EU tamponunda yeterli yer kaldığında tüketir. Onlara israfı dert etmeden yakıt verebilirsin.

**Multiblok jeneratörlerde** çıktı, tam yapılandırmalarına göre belirlenir; çıkış gerilimi ve akımı ise Dinamo Kapaklarıyla sınırlıdır. Multiblok jeneratörler talebe göre güç üretmez: Dinamo Kapaklarının dahili kapasitesini aşan enerji yok edilir.

# Tüketim

> [!WARNING]
> Bir tüketici bloğa aşırı gerilim uygulamak patlamaya neden olur.

EU alan ve tüketen cihazlara topluca makine denir. Bir makine yalnızca gerilimi azami giriş geriliminden büyük olmayan enerji paketlerini kabul edebilir; bu genellikle kademesinin standart gerilimidir. Bir makineye aşırı gerilim uygulamak onu anında patlatır.

Makineler yalnızca güç gereksinimi kendi nominal güçlerine eşit veya daha az olan tarifleri çalıştırabilir. Tarif gücü, ilgili kademenin standart geriliminde genellikle en fazla $$\frac{15}{16}\text{ A}$$'dir. Bu özel değere tarifin standart gücü denir.

**[Tek bloklu makineler](../singleblock/singleblock-index.md)** LV'de kullanılabilir hale gelir. Önce enerji paketlerini talebe göre dahili EU tamponlarına alır, ardından tarif çalıştırırken sürekli EU tüketir. Azami giriş akımı genellikle 2A'dır; Termal Santrifüj 4A ve Ark Ocağı 6A ile istisnadır.

**[Multiblok makineler](../multiblocks/multiblocks-index.md)** gücü genellikle Enerji Kapakları üzerinden alır. Standart Enerji Kapakları 2A'ya kadar kabul eder. Çok Amperli Enerji Kapakları nominal amperajlarının 1,25 katına kadar kabul eder.

Bir makinenin dahili tamponundaki enerji tükendiğinde tarifi yürütmeyi durdurur ve **güç kesintisine** girer. Tek bloklu makineler tarif ilerlemesini kaybeder ama girdi durumlarını korur; multibloklar hem tarif ilerlemesini hem de girdilerini kaybeder. [Gücü güvenilir şekilde sağladığından](enet.md#providing-power-reliably) emin ol.