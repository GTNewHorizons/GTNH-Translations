---
navigation:
  title: "Hız Aşırtma"
  icon: gregtech:gt.blockmachines:15410
  parent: T_O_P_index.md
  position: -2
---

# Hız Aşırtma

**Hız aşırtma**, makinenin tarifleri daha kısa sürede tamamlayabilmesi için [nominal gücü](T_O_P_index.md#rated-power) artırmak anlamına gelir. Makinenin nominal gücü (gerçek paralel sayısı x gerçek tarif gücü) değerini yeterli bir katsayıyla, genellikle 4x, aştığında makine bir hız aşırtma kazanır ve tarif süresi kısalır. **[Kademe atlamadan](tierskipping.md)** farklı olarak hız aşırtma birden çok kez gerçekleşebilir.

Hız aşırtmanın [gerilim kademesi](T_O_P_index.md#voltage-tier) ile hiçbir ilgisi yoktur. Daha yüksek kademeli Enerji Kapakları kullanmak tek bir kapağın nominal gücünü artırarak daha fazla hız aşırtmaya olanak tanır; birden fazla Enerji Kapağı istiflemek de benzer bir etki sağlayabilir. Aynı kademeden iki Enerji Kapağı takılan yaygın duruma genellikle **çift kapaklı hız aşırtma** denir.

Hız aşırtmaya başlamadan önce bir Multiblok önce **[paralelleri](parallels.md)** hesaplar ve denemeye çalışır. Hız aşırtma ve yığın modu tamamen ayrı özelliklerdir.

# Hız Aşırtma Türleri

## Kusurlu Hız Aşırtma (4/2)

Bu varsayılan davranıştır. Her hız aşırtma güç çekişini 4 ile çarpar ve süreyi yarıya indirir. Toplam enerji ikiye katlanır, bu yüzden buna **kusurlu hız aşırtma** denir. Çoğu makine bu modu kullanır.

## Kusursuz Hız Aşırtma (4/4)

Her hız aşırtma nominal gücü 4 ile çarpar, süreyi dörtte bire indirir ve toplam enerjiyi değiştirmez. Buna **kusursuz hız aşırtma** denir. Bir örnek <ItemLink id="gregtech:gt.blockmachines:1169" showIcon="left" />.

## Kayıpsız Hız Aşırtma (2/2)

Nominal güç 4x artarken gerçek güç kullanımı yalnızca 2x artar ve süre yarıya iner. Tek bloklu Kütle İmalatçısı buna bir örnektir.

## Özel Hız Aşırtma

Birçok makine yukarıdaki kategorilere tam olarak uymaz. Örneğin:
- <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />: önce Enerji Kapağı kademesine kadar kusurlu hız aşırtmalar kullanır, ardından amperaja dayalı lazer hız aşırtmaları kullanır; burada $$n$$. adım gücü $$(4+0.3n)$$ kadar artırır
- <ItemLink id="gregtech:gt.blockmachines:15410" showIcon="left" />: bir hız aşırtma girdi enerjisini 4 ile çarpar ve süreyi yarıya indirir; bu da kabaca 8/2 hız aşırtma gibi sonuçlanır

## Hız Aşırtma Yapılamayanlar

<ItemLink id="gregtech:gt.blockmachines:15331" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:9402" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:1006" showIcon="left" /> gibi özel amaçlı makineler hız aşırtmaya izin vermez.

# Düşük Güçlü Tariflerde Hız Aşırtma

Gerçek gücü 32 EU/t'nin altında olan her tarif, hız aşırtma hesaplamalarında 32 EU/t olarak kabul edilir. Bu, 1 ila 8 EU/t arasındaki ULV tariflerinin LV gücü olarak kabul edildiği anlamına gelir. ULV standart bir gerilim kademesi olarak kabul edilmez ve kendi kademesi olarak hız aşırtma veya paralel hesaplamalarına katılmaz.

# Tarif Süresinin Hesaplanması

Tarif süresi tick cinsinden ölçülür; bir tick 0,05 saniyedir. Hız aşırtma kayan noktalı değerlerle hesaplanır ve son süre tam sayı tick sayısına aşağı yuvarlanır. Aşağı yuvarlama 0 üretirse 1 tick'e zorlanır. Bu noktada bazı Multibloklar **1tOC** ([1 tick'e ulaştıktan sonra hız aşırtma](parallels.md#overclocking-after-reaching-1-tick-1toc)) tetikler.

Yuvarlama her zaman oyuncunun lehinedir, bu yüzden bazı durumlarda hız aşırtma toplam enerji verimliliğini %100'ün üzerine çıkarabilir.

Örnek - kusurlu hız aşırtma: $$10 \text{ tick} \to 5\text{ tick} \to 2\text{ tick} \to 1 \text{ tick} \to 1\text{ tick}$$

Örnek - kusursuz hız aşırtma: $$40 \text{ tick} \to 10\text{ tick} \to 2\text{ tick} \to 1\text{ tick} \to 1\text{ tick}$$