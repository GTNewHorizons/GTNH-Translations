---
navigation:
  title: "Yerel Güç Ağı (Enet)"
  icon: tectech:item.em.EuMeterGT
  parent: power_index.md
  position: -4
---

# Yerel Güç Ağı (GT-Enet)

[Teller ve kablolar](cable.md) etrafında kurulu **yerel güç ağı** (GT-Enet), GTNH genelinde kullanılan ana kablolu güç taşıma sistemidir.

Bir yerel güç ağı içinde enerji paketleri, tek bloklu makinelerin ve Enerji Kapaklarının dahili EU tamponları arasında hareket eder. Bu, makinelerin tarif çalıştırırken enerji harcama kurallarından ayrıdır. İkincisinin ayrıntılı davranışı **[Kademe Atlama, Overclock ve Paraleller](../tierskipping_overcloking_parallels/T_O_P_index.md)** sayfasında ele alınır.

# Ağ Yapısı

Yerel bir güç ağının üç parçası vardır:

- **Verici bloklar**: EU tamponlarından enerji paketleri çıkarır. Örnekler arasında tek bloklu jeneratörler, [trafoların](distribution.md#transformers) veya pil tamponlarının çıkış tarafı ve Dinamo Kapakları bulunur. Çıkardıkları paketlerin gerilimi genellikle kademelerinin standart gerilimidir.
- **Teller** ([teller ve kablolar](cable.md)): enerji paketlerini taşır ve [kablo kaybı](cable_loss.md) yoluyla gerilimlerini düşürebilir. Teller EU depolamaz.
- **Tüketici bloklar**: enerji paketlerini EU tamponlarına alır. Örnekler arasında tek bloklu makineler, trafoların veya pil tamponlarının giriş tarafı ve Enerji Kapakları bulunur. Kabul ettikleri maksimum paket gerilimi genellikle kademelerinin standart gerilimidir.

# İstek ve İtme Davranışı

Oyun açısından yerel güç ağları bir **istek ve itme** sistemi kullanır. Düzeneğin güvenli olduğunu varsayarsak:

- Güç aktarımı temelde **verici bloğun EU tamponundan doğrudan tüketici bloğunun EU tamponuna** bir aktarımdır.
- Bir verici blok, tamponları dolu olmayan tüketicileri kontrol eder ve gerektiğinde kendi tamponundan onlara enerji paketleri iter.
- Bir vericinin tamponlanmış EU'yu paketlere dönüştürürken ödediği ek [iletim iç direnci](output_loss.md) ve her paket tellerden geçerken ödenen [kablo kaybı](cable_loss.md) dışında hiçbir güç boşuna harcanmaz.

# Gücü Güvenli Sağlama

Güvenli olmayan düzeneklerin yıkıcı sonuçları vardır:

- Bir tüketici bloğun giriş gerilimi maksimum giriş gerilimini aşarsa tüketici **anında patlar**. LV Ark Ocağını MV paketlerle besleme; bunun yerine daha fazla LV jeneratör kullan veya gerilimi bir [trafo](distribution.md#transformers) ile düşür.
- Bir tel, maksimum geriliminin üzerinde gerilim veya maksimum akımının üzerinde akım taşırsa tel **yanıp yok olur** ve yerine ateş gelir.

Akım toplanır: bir tel parçasının taşıdığı akım, içinden geçen tüm akımların toplamıdır. Bir yerel güç ağında oluşabilecek maksimum akım, o ağdaki tüm verici blokların toplam maksimum çıkış akımını aşamaz. Bir telin yanıp yanmayacağı, içinden geçen tüm paketler arasındaki en yüksek paket gerilimine bağlıdır.

# Gücü Güvenilir Sağlama

Verici bloklar ve tüketici blokların her birinin kendi maksimum çıkış akımı ve maksimum giriş akımı vardır. Her tick'te bir vericinin itebileceği veya bir tüketicinin kabul edebileceği enerji paketi sayısının bir sınırı vardır.

Güvenilir güç beslemesinin amacı basittir: tüketici bloklar tamponlarını dolu tutacak ve güç kesintilerini önleyecek kadar paket her zaman almalıdır.

Tüketicinin aldığı paket geriliminin sabit olduğunu varsayarsak ihtiyaç duyduğu ortalama giriş akımı şöyledir:

$$I_{\text{required input}} = \frac{P_{\text{recipe}}}{U_{\text{input}}}$$

Güvenilir güç için gerekli koşullar şunlardır:

- Tüm tüketici blokların ihtiyaç duyduğu ortalama giriş akımının toplamı, verici bloklardan sağlanabilen toplam maksimum çıkış akımını aşmamalıdır.
- Her tüketici bloğun ihtiyaç duyduğu ortalama giriş akımı, o bloğun kendi maksimum giriş akımını aşmamalıdır.

Güç yetersizse tek bloklu makineler güç kesintisi yaşar ve ilerlemelerini kaybeder; multibloklar ise güç kesintisi yaşar, ilerlemelerini kaybeder ve girdilerini kalıcı olarak yok eder. Güç beslemesinin yeterli olduğundan emin ol.

# Faydalı Araçlar

Herhangi bir güç verilen blok veya tel üzerinde GT EU Meter ya da taşınabilir tarayıcı kullanarak elektriksel bilgilerini görüntüle.

Özellikle şu iki değere dikkat et:
- Dahili EU tamponunu gösteren **Depolanan Enerji**.
- Maksimum giriş/çıkış gerilimini ve akımını gösteren **Maks. Giriş/Çıkış**.