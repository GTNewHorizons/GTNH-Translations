---
navigation:
  title: "Paraleller"
  icon: gregtech:gt.blockmachines:31041
  parent: T_O_P_index.md
  position: -3
---

# Paraleller


**Paraleller**, bir multiblok makinenin aynı tarifin birden fazla kopyasını aynı zaman aralığında işleme yeteneğidir. Tek bloklu makineler bu yeteneğe sahip değildir.

Bir makine paralel çalıştığında, güç çekişi (gerçek paralel sayısı x gerçek tarif gücü) olur, tüm girdi tüketimi ve çıktı üretimi gerçek paralel sayısıyla çarpılır ve tarif süresi değişmez.

Paraleller uygulandıktan sonra multiblok, [nominal gücün](T_O_P_index.md#rated-power) hâlâ yeterli olduğunu varsayarak **[hız aşırtmayı](overclocking.md)** hesaplar ve denemeye çalışır. Paraleller ve yığın modu tamamen ayrı özelliklerdir.

# Maksimum Paralel

Multibloklarda bir paralel yapılandırma penceresi vardır ve maksimum paralel sayısı elle düşürülebilir.

- Özel bir notu olmayan makineler, <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> gibi, varsayılan olarak 1 paralele sahiptir
- <ItemLink id="gregtech:gt.blockmachines:15517" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15518" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15516" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15515" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15569" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" /> sabit olarak en fazla 256 paralel sınırına sahiptir
- Çoğu makine maksimum paralel sayısını gerilimden veya bir yapı bileşeninin kademesinden hesaplar. Bir ipucu "her gerilim kademesi $$x$$ paralel sağlar" dediğinde, bu, tüm Enerji Hatch'lerinin gerilim girdilerinin toplamından hesaplanır ve 15 (MAX+) ile sınırlandırılır

Yalnızca <ItemLink id="gregtech:gt.blockmachines:1003" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:1132" showIcon="left" /> tarifler arası paralellere sahiptir; yani tek bir paralel yığın birden çok farklı tarif içerebilir.

Pratikte gerçek paralel sayısındaki darboğaz genellikle makinenin maksimum paralel sınırıdır.

# 1 Tick'e Ulaştıktan Sonra Hız Aşırtma (1tOC)

Hız aşırtma gerçek tarif süresini 1 tick'in altına düşürecekse, tarif süresi 1 tick'e sabitlenir ve fazladan hız aşırtma ek bir paralel çarpanına dönüştürülür. Buna **1tOC** denir.

$$\text{1tOC telafi faktörü} = \left\lceil\frac{1 \text{ tick}}{\text{gerçek süre (kayan nokta)}}\right\rceil$$

Bu telafi faktörü, makinenin maksimum paralel sayısını karşılık gelen çarpan kadar artırır. Sonuç yukarı yuvarlandığı için her zaman oyuncunun yararınadır.

1tOC'yi desteklemeyen makineler:
- Tüm tek bloklu makineler
- <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15410" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:5001" showIcon="left" />

# Paraleller ile Kusursuz Hız Aşırtmalar Arasındaki Denklik

**[Paraleller](parallels.md)**, kusursuz hız aşırtmaların eşdeğeri olarak değerlendirilebilir. Maksimum $$n$$ paralel sayısına sahip bir makine, kusurlu hız aşırtmaları kusursuz olanlara dönüştürmek için $$\log_4{n}$$ fırsata sahip olmakla etkin olarak eşdeğerdir; bu da makineyi $$\sqrt{n}$$ kat hızda çalıştırır.