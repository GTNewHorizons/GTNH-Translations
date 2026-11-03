---
navigation:
  title: "Kademe Atlama"
  icon: gregtech:gt.blockmachines:41
  parent: T_O_P_index.md
  position: -1
---

# Kademe Atlama


**Kademe atlama**, bir multiblok makinenin temel tarif gücü daha yüksek bir kademeye ait olan tarifleri çalıştırmak için daha düşük kademeli Enerji Kapakları kullanabilme yeteneğidir.

Bir multibloğun [nominal gücü](T_O_P_index.md#rated-power) ve [gerilim kademesi](T_O_P_index.md#voltage-tier), Enerji Kapakları tarafından belirlenir. Yalnızca bir Enerji Kapağı takılıyken gerilim kademesi genellikle nominal gücün bir kademe üstündedir; bu 4 katlık bir farktır, ancak nominal güç o daha yüksek gerilim kademesindeki tarifleri çalıştırmak için hâlâ çok düşüktür. Eksik nominal gücü tamamlamak için aynı kademede daha fazla Enerji Kapağı takarsın. İşte bu **kademe atlamadır**. Kademe atlama, **[overclock](overclocking.md)** işleminden farklıdır.

# Çift Kapaklı Kademe Atlama

Aynı kademede iki standart Enerji Kapağı takmak, nominal gücü gerilim kademesiyle eşleşene kadar yükseltir. Buna **çift kapaklı kademe atlama** denir. Aynı kademede iki standart Enerji Kapağı, tam olarak bir kademe üstündeki her tarifi çalıştırmak için yeterli nominal güç ve gerilim kademesini birlikte sağlar.

Bazı multiblokların olağandışı gerilim kademesi kuralları vardır. [Gerilim kademesi](T_O_P_index.md#voltage-tier) altındaki "güçlendirilemez" ve "kısıtlanmamış" durumlara bak.

# Örnek: Elektrikli Yüksek Fırın

<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> örneğini ele alalım. Onunla ilk karşılaştığında genellikle yalnızca LV Enerji Kapakların olur, ancak alüminyum eritmek MV kademesi güç gerektirir.

İki LV Enerji Kapağı taktıktan sonra:

- **[Gerilim kademesi](T_O_P_index.md#voltage-tier)**: $$(32\text{V} + 32\text{V}) / 2 \times 4\text{A} = 128 \text{ EU/t}$$, bu tüm MV tariflerinin temel tarif gücünün üzerindedir. Alüminyum tarifi 120 EU/t gerektirir.
- **[Nominal güç](T_O_P_index.md#rated-power)**: $$32\text{V} \times 2\text{A} + 32\text{V} \times 2\text{A} = 128 \text{ EU/t}$$

Bu durumda Elektrikli Yüksek Fırın kablo kaybına karşı çok hassas hale gelir. Kablo kaybını telafi etmek için kullanılan fazladan akım, fiilen makinenin güç gereksinimini karşılamaya gider:

- Bir Enerji Kapağı yerel güç ağından en fazla 2A kabul edebilir. Kablo kaybı gerilimi 30V'nin altına düşürürse iki Enerji Kapağı birlikte artık tam 120 EU/t alamaz ve makinede güç kesintisi olabilir.
- Üçüncü bir Enerji Kapağı takmak gerilim kademesini yükseltmez: $$(32+32+32)/3 \times 4\text{A} = 128 \text{ EU/t}$$. Yalnızca nominal gücü 192 EU/t'ye çıkarır ve kablo kaybını telafi etmek için ek pay verir.