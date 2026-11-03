3 Mod: {light_purple:Hafif} | {blue:Standart} | {dark_green:Ağır}
{gray:{hr}}
{white:Toplam Türbin} Kademesi başına {gold:{var:parallels} Paralel}
{green:{var:speed}% Hız}
{aqua:{var:eu_eff}% EU Kullanımı}
{white:Dev Olmayan Türbinler} daha düşük verimle çalışır...
{white:Yapı} Kademesi başına {var:slots_per_tier} {white:Türbin Yuvası} kazandırır
Çalışmak için {aqua:(Tarif Kademesi * {var:fluid_per_tier} {var:fluid_unit}/s)} {gold:Gazyağı} gerektirir
Bunun yerine {gold:Biyokatalize İtki Sıvısı} vererek {gold:{var:tier2_mult}x} Paralel artışı elde et
{yellow:Hız aşırtmalar Kapak Kademesi + 1 ile sınırlıdır}
{gray:{hr}}
{light_purple:Hafif Mod}:
- {green:+{var:light_speed}% Hız Bonusu}
- Maksimum Tarif Kademesi {aqua:(Gerilim Kademesi - {var:light_offset})}
{blue:Standart Mod}: Normal işleme
{dark_green:Ağır Mod}: {gold:Biyokatalize İtki Sıvısı} gerektirir
- {gold:Paralelleri} {gold:{var:heavy_div}} ile böler
- {red:EU Maliyetini} {red:{var:heavy_eu}} ile çarpar
- {light_purple:Sınırsız Hız Aşırtma}
- Bazı tarifler {dark_green:Ağır Mod} {dark_red:gerektirir}