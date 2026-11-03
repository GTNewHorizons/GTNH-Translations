---
navigation:
  title: "Kademe Atlama"
  icon: gregtech:gt.blockmachines:41
  parent: T_O_P_index.md
  position: -1
---

# Kademe Atlama


**Kademe atlama**, bir multiblok makinenin temel tarif gücü daha yüksek bir kademeye ait olan tarifleri çalıştırmak için daha düşük kademeli Enerji Kapakları kullanabilme yeteneğidir.

Bir multibloğun [anma gücü](T_O_P_index.md#rated-power) ve [gerilim kademesi](T_O_P_index.md#voltage-tier) Enerji Kapakları tarafından belirlenir. Yalnızca bir Enerji Kapağı takılıyken gerilim kademesi genellikle anma gücünün bir kademe üstündedir, yani 4x fark vardır, ancak anma gücü o daha yüksek gerilim kademesinde tarif çalıştırmak için hâlâ çok düşüktür. Eksik anma gücünü telafi etmek için aynı kademede daha fazla Enerji Kapağı takarsın. İşte bu **kademe atlamadır**. Kademe atlama, **[overclock](overclocking.md)** işleminden farklıdır.

# Çift Kapaklı Kademe Atlama

Aynı kademede iki standart Enerji Kapağı takmak, anma gücünü gerilim kademesiyle eşleşene kadar yükseltir. Buna **çift kapaklı kademe atlama** denir. İki standart aynı kademe Enerji Kapağı, tam olarak bir kademe üstteki her tarifi çalıştırmak için birlikte yeterli anma gücü ve gerilim kademesi sağlar.

Bazı multiblokların olağandışı gerilim kademesi kuralları vardır. [Gerilim kademesi](T_O_P_index.md#voltage-tier) altındaki "güçlendirilemez" ve "kısıtlamasız" durumlara bak.

# Örnek: Elektrikli Yüksek Fırın

Örnek olarak <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> al. Onunla ilk karşılaştığında genellikle yalnızca LV Enerji Kapakların olur, ancak alüminyum eritmek MV kademesi güç gerektirir.

İki LV Enerji Kapağı taktıktan sonra:

- **[Gerilim kademesi](T_O_P_index.md#voltage-tier)**: $$(32\text{V} + 32\text{V}) / 2 \times 4\text{A} = 128 \text{ EU/t}$$, bu tüm MV tariflerinin temel tarif gücünün üzerindedir. Alüminyum tarifi 120 EU/t gerektirir.
- **[Anma gücü](T_O_P_index.md#rated-power)**: $$32\text{V} \times 2\text{A} + 32\text{V} \times 2\text{A} = 128 \text{ EU/t}$$

Bu durumda Elektrikli Yüksek Fırın kablo kaybına karşı çok hassas hale gelir. Kablo kaybını telafi etmek için kullanılan her ek akım, aslında makinenin güç gereksinimini karşılamaya harcanır:

- Bir Enerji Kapağı yerel güç ağından en fazla 2A kabul edebilir. Kablo kaybı gerilimi 30V'nin altına düşürürse iki Enerji Kapağı birlikte artık tam 120 EU/t almaz ve makine güç kesintisi yaşayabilir.
- Üçüncü bir Enerji Kapağı takmak gerilim kademesini yükseltmez: $$(32+32+32)/3 \times 4\text{A} = 128 \text{ EU/t}$$. Yalnızca anma gücünü 192 EU/t'ye çıkarır ve kablo kaybını telafi etmek için ek pay sağlar.