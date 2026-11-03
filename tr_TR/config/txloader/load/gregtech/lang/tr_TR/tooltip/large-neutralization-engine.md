Tüm sorunlarını (ç)özer!
{hr}
{color_mechanic:Verimliliği} artırmak için isteğe bağlı olarak {aqua:Baz} verebilirsin:
{aqua:{var:sodium_hydroxide_rate}/min} {aqua:Sodyum Hidroksit} : {color_mechanic:{var:sodium_hydroxide_eff}%}
{aqua:{var:potassium_hydroxide_rate}/min} {aqua:Potasyum Hidroksit} : {color_mechanic:{var:potassium_hydroxide_eff}%}
{aqua:{var:caesium_hydroxide_rate}/min} {aqua:Sezyum Hidroksit} : {color_mechanic:{var:caesium_hydroxide_eff}%}
{aqua:{var:francium_hydroxide_rate}/min} {aqua:Fransiyum Hidroksit} : {color_mechanic:{var:francium_hydroxide_eff}%}
{hr}
Asitleri yakarak {dark_green:Toksik Kalıntı} üretir
{dark_green:Toksik Kalıntı} {dark_aqua:Kapasite}yi aşarsa makine {color_danger:Patlar}
Her tick, {dark_green:Toksik Kalıntı} şu kadar artar: {green:0.05 * Yakıt Yoğunluğu ({EU}/{L})^0.8 * Yakıt Tüketimi ({L}) * rand({var:residue_rand_min}, {var:residue_rand_max})}
Her tick, {dark_green:Toksik Kalıntı} şu kadar azalır: {green:Taban Çürüme * Çürüme Artışı * Toksik Kalıntı^0.08}
{yellow:Multiblok devre dışıyken kalıntı 10 kat daha yavaş çürür}
{hr}
{blue:Çürüme Artışını} artırmak için en fazla {blue:{var:robot_arm_amount_for_decay_boost} Robot Kolu} tak:
{white:Çürüme Artışı =} {green:sqrt(Robot Kolları) * N^(Robot Kolu Kademesi - 1)}; burada {green:N={var:robot_arm_bonus_low}} ({tier-color:arm_tier_low:{VN:arm_tier_low}-}) veya {green:N={var:robot_arm_bonus_high}} ({tier-color:arm_tier_high:{VN:arm_tier_high}+})
Her dakika, tam olarak bir {blue:Robot Kolu}nu yok etme şansı {green:Robot Kolları / (45 * (Robot Kolu Kademesi + 1))} kadardır
{hr}
Yapıda {blue:Taban Çürümeyi} ve {dark_aqua:Kapasite}yi belirleyen {color_mode:3 Kademe} vardır:
{color_mode:T1} : {color_mode:Güçlendirilmiş Cansız Makine Gövdesi} : {blue:{var:tier1_decay}} : {dark_aqua:{var:tier1_capacity}}
{color_mode:T2} : {color_mode:Hassas Sabit Makine Gövdesi} : {blue:{var:tier2_decay}} : {dark_aqua:{var:tier2_capacity}}
{color_mode:T3} : {color_mode:Nihai Durağan Makine Gövdesi} : {blue:{var:tier3_decay}} : {dark_aqua:{var:tier3_capacity}}