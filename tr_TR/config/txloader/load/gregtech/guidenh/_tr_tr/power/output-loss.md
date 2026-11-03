---
navigation:
  title: "İletim İç Direnci"
  icon: gregtech:gt.blockmachines:21
  parent: power-index.md
  position: -6
---

# İletim İç Direnci

Jeneratörler, [pil tamponları](distribution.md#battery-buffers), [transformatörler](distribution.md#transformers) ve benzeri bloklar dahil tüm [verici blokları](enet.md), EU çıktısı verirken **iç direnç kaybı** yaşar. Bu kayıp doğrudan dahili EU tamponundan düşülür ve çıktı gerilimini veya akımını etkilemez.

> [!IMPORTANT]
> İç direnç kaybı, bir jeneratörün yakıt verimliliğiyle aynı şey değildir. Yakıt verimliliğinin üzerine eklenen ayrı bir çarpımsal kayıptır.

# Mekanizma

Herhangi bir verici blok, $$8 \times 4^{\text{tier index}} \text{ EU}$$ içeren bir standart gerilimli enerji paketi üretmek için dahili EU tamponundan her zaman $$8 \times 4^{\text{tier index}} \text{ V} + 2^{\text{tier index} - 1} \text{ EU}$$ tüketir.

Bu, LV standart geriliminde iletim yapan herhangi bir bloğun çarpımsal olarak yalnızca $$\frac{32}{33}$$ gerçek verimliliğe sahip olduğu anlamına gelir. Bunun üzerindeki her gerilim kademesinde mutlak verimlilik kaybı yarıya iner.

| Çıktı Gerilimi | Çıktı Paketi | Dahili Tampon Maliyeti | Kayıp Enerji | Gerçek Verimlilik |
|----------------|---------------|----------------------|-------------|-------------------|
| LV (32 V) | 32 EU | 33 EU | 1 EU | 96.97% |
| MV (128 V) | 128 EU | 130 EU | 2 EU | 98.48% |
| HV (512 V) | 512 EU | 516 EU | 4 EU | 99.24% |
| EV (2,048 V) | 2,048 EU | 2,056 EU | 8 EU | 99.62% |
| IV (8,192 V) | 8,192 EU | 8,208 EU | 16 EU | 99.81% |

Kayıp küçük olduğundan ve çıktı gerilimini değiştirmediğinden, yüksek gerilimde genellikle bunu önemsemen gerekmez.

Örnek: Bir Basit Buhar Türbini 32 EU/t çıktı verdiğinde iç direnç kaybı 1 EU/t'dir, dolayısıyla gerçek buhar maliyeti 33 EU/t üzerinden hesaplanmalıdır. Gelişmiş bir Buhar Türbini 32 EU/t çıktı verdiğinde iç direnç kaybı 0.5 EU/t'dir, yani daha verimlidir.