Arıların için ideal yuva
{color_mode:Giriş Modu}:
- Güç tüketmez, kraliçeleri dahili tamponda depolamak için onları {color_name:Giriş Yolu} içine koy
{hr}
{color_mode:Çıkış Modu}:
- Güç tüketmez, arıları {color_name:Çıkış Yolu} içine geri verir
- {color_note:Dikkat, arılarını kolayca yok edebilirsin}
{hr}
{color_mode:Çalışma Modu}:
- {color_mechanic:Normal}:
  - Her işlem başına {color_time:{var:normal_seconds}s}, {color_amount:{var:bee_acceleration}x} arı hızı
  - Kraliçe başına {color_amperage:1} {VNF:normalTier} amper kullanır
  - {color_amount:8} üretim yükseltmesi ve {color_name:Genetik Dengeleyici} uygulanır
  - Mükemmel bir ortam simüle eder
  - {color_key:Kraliyet Jölesi} her jöle için {color_amount:{var:jelly_bonus}%} çıktı verir, {color_amount:{var:max_jelly_bonus}%} değerine kadar (her çalışmada arı başına tüketilir)
- {color_mechanic:Swarmer}:
  - Yalnızca {color_amount:1} kraliçe, yavaşça {color_name:Ignoble Princesses} üretir
  - İşlem başına {color_amount:{var:swarmer_jelly_cost}} {color_key:Kraliyet Jölesi}
  - {color_time:{var:swarmer_seconds}s} temel süre, {color_amperage:1} {VNF:swarmerTier} amper
  - {color_mechanic:Hız aşırtma yapabilir}
{hr}
Kontrolcüye {color_name:Tornavida} ile sağ tıklayarak {color_mode:modu} (Giriş/Çıkış/Çalışma) değiştir
Kontrolcüye {color_name:Tornavida} ile Shift-sağ tıklayarak {color_mechanic:çalışma modunu} (Normal/Swarmer) değiştir