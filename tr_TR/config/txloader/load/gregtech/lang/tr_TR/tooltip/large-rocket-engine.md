Güç üretmek için {color_key:Rocket Fuel} yakar (min {var:min_fuel} {L}/s)
{white:Dynamo Hatch} boyutu dışında güç çıktısında üst sınır yoktur
Ancak yakıt verimliliğini düşüren {color_eu_usage:{var:cap1} {EU/t}} ve {color_eu_usage:{var:cap2} {EU/t}} (takviyesiz) değerlerinde yumuşak sınırlar vardır
{color_danger:Do not insert Rocket Fuel while disabled - it will be voided on start!}
{hr}
Yanma süreci bazı ek girdiler gerektirir:
Saatte {color_amount:{var:lubricant_amount}L} {white:{var:lubricant}} (takviyeli ise x{var:boost})
Tick başına mevcut {EU/t} değerinin {color_amount:{var:air_percent}%} kadarı {white:Air} olarak (yalnızca hava giriş kapaklarından)
Takviye için tick başına mevcut {EU/t} değerinin {color_amount:{var:coolant_percent}%} kadarı {white:{var:coolant}} olarak (isteğe bağlı)
{hr}
Hava bir an tükenirse makine kapanır ve elle yeniden başlatılması gerekir
Takviye, yumuşak sınırları {aqua:{var:cap1_boosted} {EU/t}} ve {aqua:{var:cap2_boosted} {EU/t}} değerlerine çarpar
Mevcut güç çıktısına göre ısınması {var:warmup_min}-{var:warmup_max} saniye sürer
{hr}
Her {aqua:{var:pollution_unit} {EU/t}} için {dark_purple:{var:pollution}} kirlilik üretir