Sıcak sıvılar: {color_hot:{fluid:lava}}, {color_hot:{fluid:ic2hotcoolant}}, {color_hot:{fluid:molten.solarsalthot}}
Soğutulduğu sıvılar: {color_cold:{fluid:ic2pahoehoelava}}, {color_cold:{fluid:ic2coolant}}, {color_cold:{fluid:molten.solarsaltcold}}
{color_name:Damıtılmış Su} sıvısını {color_steam:Buhar} hâline dönüştürür
Sıcak sıvı girdisi {color_note:SH eşiğine} ulaştığında bunun yerine yarısı kadar {color_steam:Aşırı Isıtılmış Buhar} üretir
{color_danger:Damıtılmış su olmadan {var:explode_seconds} saniye sonra patlar}
{hr}
{color_hot:{fluid:lava}}: SH eşiği {color_hot:{var:lava_threshold} {L}/s}, maks girdi {color_hot:{var:lava_max_input} {L}/s}, maks çıktı {color_steam:{var:lava_max_output} {L}/t SH Buharı}
{color_hot:{fluid:ic2hotcoolant}}: SH eşiği {color_hot:{var:coolant_threshold} {L}/s}, maks girdi {color_hot:{var:coolant_max_input} {L}/s}, maks çıktı {color_steam:{var:coolant_max_output} {L}/t SH Buharı}
{color_hot:{fluid:molten.solarsalthot}}: SH eşiği {color_hot:{var:salt_threshold} {L}/s}, maks girdi {color_hot:{var:salt_max_input} {L}/s}, maks çıktı {color_steam:{var:salt_max_output} {L}/t SH Buharı}
{hr}
Kontrolcüdeki bir {color_name:Programlanmış Devre}, {var:min_circuit} değerinin üzerindeki her değer için SH eşiğini {color_amount:{var:threshold_reduction}%} düşürür ve buhar çıktısını {color_loss:{var:steam_penalty}%} azaltır