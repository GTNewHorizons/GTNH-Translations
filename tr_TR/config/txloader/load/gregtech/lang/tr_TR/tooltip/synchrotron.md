Parçacık ışınlarını, göreli Larmor etkisiyle foton ışını üretene kadar hızlandırır
Elektriksel olarak nötr §5parçacıklar§7 ve 25'in altında §2Odaklanmaya§7 sahip olan ışınlar bu nedenle etkilenmez
{lang:gtnhlanth.tt.beaminfo}
{gray:{hr}}
Çalışmak için §f32,000 {var:fluidUnit}/s§7 §bsoğutucu§7 gerektirir, §csıcak soğutucu olarak geri döner
{lang:gtnhlanth.tt.coolant.oxygen}
{lang:gtnhlanth.tt.coolant.nitrogen}
{lang:gtnhlanth.tt.coolant.coolant}
{lang:gtnhlanth.tt.coolant.Scoolant}
{gray:{hr}}
Gücü artırmak §6Çıktı Işın Oranını artırır
§2Işın Odaklanmasını§7 daha düşük sıcaklıkta §bsoğutucu ile daha etkili koru
§dAnten Kasalarının§7 kademesini artırmak makinenin verimliliğini iyileştirir
Aşağıdaki formüllerdeki §9enerjiler§7 tamamen keV cinsinde olmalıdır
{gray:{hr}}
§9Çıktı Işın Enerjisi§f = §eIR§f * §eGüç Ölçek Faktörü
burada §eIR§f = (§9Girdi Işın Enerjisi§f)^(1.13 * (§dAnten Kademesi§f)^(4/9)) / 40,000,000
ve §eGüç Ölçek Faktörü§f = 1 - 0.15^(§3Sağlanan Toplam EU/t§f / (30,384 * (§dAnten Kademesi§f)^2.5))
{gray:{hr}}
§2Çıktı Işın Odaklanması§f = (§2Girdi Işın Odaklanması§f + §eMakine Odaklanması§f)/2.5§7 eğer §2Girdi Işın Odaklanması§f > §eMakine Odaklanması
§2Çıktı Işın Odaklanması§f = §2Girdi Işın Odaklanması§f * §eMakine Odaklanması§f/100§7 eğer §2Girdi Işın Odaklanması§f <= §eMakine Odaklanması
burada §eMakine Odaklanması§f = max(10, min(90, 1.5^(12 - §bSoğutucu Sıcaklığı§f/40)))
{gray:{hr}}
§6Çıktı Işın Oranı§f = floor(2.5^(§dAnten Kademesi§f) * sqrt(§3Sağlanan Toplam EU/t§f) * §6Girdi Işın Oranı§f/15,000)