---
navigation:
  title: "Güç"
  icon: gregtech:gt.metaitem.01:32518
  parent: /index.md
  position: 8
---

# Güç

GregTech güç sistemi EU (Enerji Birimi) kullanır. Merkezinde [yerel güç ağı](enet.md) (GT-Enet) bulunur; enerji üretimi, taşınması, depolanması, tüketimi ve dönüştürülmesi bunun etrafında kuruludur.

- Enerji üretim yöntemleri için üretim genel bakışına bak.
- Ağ düzeni ve taşıma önerileri için güç depolama ve taşıma bölümüne bak.
- Makine kademesi atlama, overclock ve paralellik için **[Kademe Atlama, Overclock ve Paralellik](../tierskipping-overcloking-parallels/T-O-P-index.md)** bölümüne bak.

# Gerilim ve Akım

EU, enerji paketleri olarak iletilir. Enerji paketlerinin sayısı her zaman bir tam sayıdır.

## Gerilim

Gerilim, her paketin ne kadar EU taşıdığını açıklar ve volt (V) cinsinden ölçülür. $$1\text{ V} = 1\text{ EU}/\text{packet}$$.

Gerilim, tek bir enerji paketinin boyutunu açıklar ve jeneratör ile makine ilerlemesini belirler ([gerilim kademelerine](voltage-tiers.md) bak).

## Akım

Akım, birim zamanda kaç enerji paketinin aktarıldığını açıklar ve amper (A) cinsinden ölçülür. $$1\text{ A} = 1\text{ packet}/\text{tick}$$.

Tek bir tick'te aktarılan enerji paketi sayısı her zaman bir tam sayı olduğundan, anlık akım da her zaman bir tam sayıdır. Ortalama akım, anlık akımın ortalamasıdır, bu yüzden genellikle kesirlidir.

## Güç

Güç, gerilim ile akımın çarpımıdır: $$P = UI$$. Birim zamanda ne kadar enerji üretildiğini, iletildiğini veya tüketildiğini açıklar ve EU/t cinsinden ölçülür. $$1\text{ EU/t} = 1\text{ V} \times 1\text{ A}$$.

Enerji, gücün zamanla (tick) çarpımıdır ve EU cinsinden ölçülür.

GT güç sistemi gerçek dünyadaki elektrik davranışına yakındır. [Kablo kaybını](cable-loss.md) ve [iletim iç direncini](output-loss.md) hesaba kattığında bile enerjinin korunumu geçerliliğini korur.