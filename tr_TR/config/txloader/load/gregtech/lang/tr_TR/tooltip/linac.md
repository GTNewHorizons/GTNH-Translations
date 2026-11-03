Parçacık ışınlarını bir elektrik alanından geçirerek daha yüksek enerjilere hızlandırır
Elektriksel olarak nötr {color_mechanic:Parçacıklar} bu nedenle etkilenmez
{lang:gtnhlanth.tt.beaminfo}
{hr}
Çalışmak için {aqua:Uzunluk * 1,000 {var:fluidUnit}/s} {aqua:Soğutucu} gerektirir, {red:Sıcak Soğutucu} olarak geri döner
{lang:gtnhlanth.tt.coolant.oxygen}
{lang:gtnhlanth.tt.coolant.nitrogen}
{lang:gtnhlanth.tt.coolant.coolant}
{lang:gtnhlanth.tt.coolant.Scoolant}
{hr}
Uzunluğu/gücü artırmak {blue:Çıktı Işın Enerjisini} artırır ancak {dark_green:Çıktı Işın Odaklanmasını} azaltır
{dark_green:Işın Odaklanmasını} daha düşük sıcaklıkta {aqua:Soğutucu} ile daha etkili koru
{hr}
{blue:Çıktı Işın Enerjisi}{color_formula: = max(}{color_note:V}{white:, 50) * 10^}{color_note:IE}
burada {color_note:V}{color_formula: = 0.25 * (Uzunluk - 1) * cbrt({color_eu_usage:{EU/t} Sağlanan})}
ve {color_note:IE}{color_formula: = 1 + min({blue:Girdi Işın Enerjisi}, 7500) / }{blue:Maks Parçacık Enerjisi}
{hr}
{dark_green:Çıktı Işın Odaklanması}{color_formula: = (dark_green:Girdi Işın Odaklanması} + {color_note:Makine Odaklanması})/2} eğer {dark_green:Girdi Işın Odaklanması}{color_formula: > {color_note:Makine Odaklanması}}
{dark_green:Çıktı Işın Odaklanması}{color_formula: = {dark_green:Girdi Işın Odaklanması} * {color_note:Makine Odaklanması}/100} eğer {dark_green:Girdi Işın Odaklanması}{color_formula: <= {color_note:Makine Odaklanması}}
burada {color_note:Makine Odaklanması}{color_formula: = min(90, max(5, (-0.9 * (Uzunluk-1) * 1.1^(0.2 * {aqua:Soğutucu Sıcaklığı}) + 110)))}