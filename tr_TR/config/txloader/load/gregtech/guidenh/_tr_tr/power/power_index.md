---
navigation:
  title: "Güç"
  icon: gregtech:gt.metaitem.01:32518
  parent: /index.md
  position: 8
---

# Güç

GregTech güç sistemi EU (Enerji Birimleri) kullanır. Çekirdeği [yerel güç ağı](enet.md) (GT-Enet) olup güç üretimi, taşınması, depolanması, tüketimi ve dönüşümü bunun etrafında kuruludur.

- Güç üretim yöntemleri için üretim genel bakışına bak.
- Ağ düzeni ve taşıma tavsiyeleri için güç depolama ve taşıma bölümüne bak.
- Makine kademe atlama, hız aşırtma ve paraleller için **[Kademe Atlama, Hız Aşırtma ve Paraleller](../tierskipping_overcloking_parallels/T_O_P_index.md)** sayfasına bak.

# Gerilim ve Akım

EU, enerji paketleri halinde iletilir. Enerji paketlerinin sayısı her zaman bir tam sayıdır.

## Gerilim

Gerilim, her paketin ne kadar EU taşıdığını volt (V) cinsinden tanımlar. $$1\text{ V} = 1\text{ EU}/\text{packet}$$.

Gerilim, tek bir enerji paketinin boyutunu tanımlar ve jeneratör ile makine ilerlemesini belirler (bkz. [gerilim kademeleri](voltage_tiers.md)).

## Akım

Akım, birim zamanda kaç enerji paketinin aktarıldığını amper (A) cinsinden tanımlar. $$1\text{ A} = 1\text{ packet}/\text{tick}$$.

Tek bir tick içinde aktarılan enerji paketlerinin sayısı her zaman bir tam sayı olduğundan, anlık akım da her zaman bir tam sayıdır. Ortalama akım, anlık akımın ortalaması olduğu için genellikle kesirlidir.

## Güç

Güç, gerilim ile akımın çarpımıdır: $$P = UI$$. Birim zamanda ne kadar enerjinin üretildiğini, iletildiğini veya tüketildiğini EU/t cinsinden tanımlar. $$1\text{ EU/t} = 1\text{ V} \times 1\text{ A}$$.

Enerji, gücün zamanla (tick) çarpımıdır ve EU cinsinden ölçülür.

GT güç sistemi gerçek dünyadaki elektriksel davranışa yakındır. [Kablo kaybını](cable_loss.md) ve [iletim iç direncini](output_loss.md) hesaba kattığında bile enerjinin korunumu geçerlidir.