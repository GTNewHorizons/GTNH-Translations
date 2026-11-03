İşlem başına {color_name:Yakıt}'ın en fazla {color_amount:{var:fuel_percent}%} kadarını kullanır
Çalışmaya başlamak için en az {color_amount:{var:min_helium}%} {color_key:Helyum} gerekir
{color_key:Helyum}, maksimum kapasitede eşanjör verimliliğini doğrusal olarak {color_amount:100%} değerine kadar artırır
Reaktör her işlemde depoladığı {color_key:Helyum}un {color_amount:{var:helium_lost}%} kadarını kaybeder
{color_eu_usage:{var:power} {EU/t}} kullanır, {color_key:Helyum} eksik olduğunda {color_amount:{var:power_penalty}x} kadar artar
{hr}
İşlem süresi reaktörün dolum seviyesine göre ölçeklenir
{color_amount:{var:min_time}s} ile {color_amount:{var:max_time}s} arasında
Bu değerin {color_amount:10%} kadarı sabittir, {color_amount:90%} kadarı {aqua:y = 1 - (1 - x)^3} formülünü izler ({white:x} % dolum seviyesidir)
Bakım sorunları her sorun için verimliliği {color_amount:20%} düşürür
{hr}
{color_key:Soğutucu}, {color_key:Su} veya ikisini birden sağlamak tarifi hızlandırır:
saniyede toplam tarif süresinin {color_amount:{var:coolant_speedup}%} / {color_amount:{var:water_speedup}%} / {color_amount:{var:total_speedup}%} kadarı
Maksimum bonus için gereken sıvı miktarı, {color_key:TRISO Küreleri} sayısıyla ölçeklenir
{color_amount:{var:coolant_per_ball}} {color_key:Soğutucu}/tick/küre ve {color_amount:{var:water_per_ball}} {color_key:Damıtılmış Su}/tick/küre