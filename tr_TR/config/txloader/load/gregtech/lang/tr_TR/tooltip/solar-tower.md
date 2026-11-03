Geleceğe Yeşil Enerji katkısı
Isı üretmek için 1-5 halka {white:Güneş Yansıtıcıları} ile çevrele
Daha fazla Güneş Yansıtıcısı daha fazla ısı kazancı ve daha fazla toplam soğutucu akışı demektir
Maksimum 100,000 ısı, ancak buna ulaşmakta hiçbir risk veya tehlike yok
{gray:{hr}}
Her {var:cycle}s {blue:Soğuk Güneş Tuzu}'nu 1:1 oranında {red:Sıcak Güneş Tuzu}'na dönüştürür
Dönüştürülen her 1{var:unit} ısıyı sıfıra ulaşana kadar 1 azaltır
Fazla Soğuk Güneş Tuzu tüketilmez
{gray:{hr}}
Dönüşüm yalnızca {white:ısı >=} {red:{var:threshold}} ve {white:verimlilik =} {aqua:100%} olduğunda gerçekleşir
Verimlilik {aqua:0%} ile başlar ve her 10s'de {aqua:+1%} artar 
{gray:{hr}}
{white:Isı Verimliliği =} {red:1 - (Isı - {var:center})^{var:exp} / {var:coefficient}}, {red:{var:center}} noktasında zirve yapar
{white:Isı/Döngü =} {red:Güneş Yansıtıcıları * Isı Verimliliği * ({var:loss} + 2^(Halka - 1)) - {var:loss}}
{yellow:Isı kazancı yağmurda yarıya iner ve gece devre dışı kalır}