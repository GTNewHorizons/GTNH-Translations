---
navigation:
  title: "Güç Dağıtımı"
  icon: gregtech:gt.blockmachines:15300
  parent: power_index.md
  position: -7
---

# Güç Dağıtımı

Gerilim dönüşümü, akım sınırlama ve enerji depolamayı bir araya getirerek birden fazla [yerel güç ağı](enet.md) birbirine bağlanabilir. Bu işlevlere sahip cihazlar genellikle farklı yerel güç ağları arasında köprü görevi görür: hem tüketici blokları hem de verici blokları olarak çalışır, bir ağdan dahili EU tamponları aracılığıyla güç alıp başka bir ağa güç verirler.

# Trafolar

> [!WARNING]
> Güç verilmişken trafo modunu değiştirmek, trafonun hemen patlamasına neden olur.

Trafolar, iletim kayıplarını azaltmak, daha yüksek kademeli makineleri çalıştırmak ve daha fazlası için gerilimi değiştirir. Bir trafo gücü yalnızca gerilimler arasında dönüştürdüğü için, gerilimdeki değişikliklere genellikle akımda da değişiklikler eşlik eder.

**Tek bloklu trafolar** gerilimi bir kademe yükseltebilir veya düşürebilir; akım ise 4 kat değişir. 1 yüksek gerilim yüzü ve 5 düşük gerilim yüzü vardır. <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> tutarken <kbd>Sağ tıkla</kbd> ile yükseltme modu ve düşürme modu arasında geçiş yap. Yüksek gerilim yüzü daire ile, düşük gerilim yüzleri kareler ile işaretlenmiştir ve renkler ipucunda gösterilen kademe rengiyle eşleşir. Varsayılan düşürme modunda yüksek gerilim yüzü girdi, düşük gerilim yüzleri çıktıdır; yükseltme modunda yön tersine döner.

- Maksimum girdi gerilimi: girdi yüzüne karşılık gelen kademenin standart gerilimi.
- Çıktı gerilimi: çıktı yüzüne karşılık gelen kademenin standart gerilimi.
- Maksimum akım: ipucundaki amperaj değeri düşük gerilim yüzlerinin maksimum akımıdır; yüksek gerilim yüzü bu amperajın dörtte birini destekler.

**Enerji Dağıtıcısı** düşük gerilimdeki aşırı yüksek akımı yüksek gerilime dönüştüren bir başka tek bloklu cihazdır.

**Aktif Trafo** (<ItemLink id="gregtech:gt.blockmachines:15300" showIcon="left" />) bir multiblok trafodur. Güç G/Ç'si olarak Enerji Kapakları ve Dinamo Kapakları kullanır. Güç iletimi etkinleştirilmiş TecTech makineleri de aktif trafo olarak görev yapabilir.

# Kablo Diyotları

**Kablo diyotları** akımın yönünü kısıtlar ve paketlerin yalnızca girdi tarafından çıktı tarafına gitmesine izin verir. Ayrıca küçük bir dahili EU tamponu içerirler, böylece sınırlı miktarda gerilim yumuşatması sağlarlar.

Kablo diyotları farklı kademelerde ve akım sınırlarında gelir. İpucu, izin verilen maksimum gerilimi ve maksimum geçiş akımını gösterir. Bu değerlerden birini aşarsan diyot yanar.

# Pil Tamponları

Pil Tamponları düşük gerilimde en yaygın depolama cihazlarıdır ve uyumlu kademedeki pilleri gerektirirler:

- Maksimum girdi gerilimi: karşılık gelen kademenin nominal gerilimi.
- Maksimum girdi akımı: 2A x pil sayısı.
- Çıktı gerilimi: karşılık gelen kademenin nominal gerilimi.
- Maksimum çıktı akımı: 1A x pil sayısı.

Depolama cihazları aynı anda güç alıp verebilir. Pil Tamponlarının girdi ve çıktı akım sınırları farklı olduğundan, dolaylı bir akım sınırlama yöntemi olarak da kullanılabilirler. Daha fazla depolama seçeneği için güç depolama ve taşımaya bak.