Girdiler: {color_hot:Lav}, {color_hot:Sıcak Soğutucu}, {color_hot:Sıcak Güneş Tuzu} veya {color_hot:Plazma}
Çıktılar: {color_cold:Pahoehoe Lav}, {color_cold:IC2 Soğutucu}, {color_cold:Soğuk Güneş Tuzu} veya {color_cold:Eriyik Metal}
Bu süreçte damıtılmış suyu {color_steam:SH Buhar} veya {color_steam:SC Buhar} hâline dönüştürür
Sıcak sıvının girdi hızı belirli bir {color_mechanic:eşiğin} üstündeyse {color_steam:SC Buhar} çıktısı verir
{color_danger:Damıtılmış suyu biterse anında patlar}
{hr}
{color_hot:Lav} | SC Eşiği {color_mechanic:80,000 {L}/s} | Maks Girdi {color_hot:160,000 {L}/s} | Maks Çıktı {color_steam:640,000 {L}/t SC Buhar}
{color_hot:Sıcak Soğutucu} | SC Eşiği {color_mechanic:8,000 {L}/s} | Maks Girdi {color_hot:128,000 {L}/s} | Maks Çıktı {color_steam:1,280,000 {L}/t SC Buhar}
{color_hot:Sıcak Güneş Tuzu} | SC Eşiği {color_mechanic:1,600 {L}/s} | Maks Girdi {color_hot:3,200 {L}/s} | Maks Çıktı {color_steam:160,000 {L}/t SC Buhar}
{hr}
{color_hot:Plazma} girdi hızından bağımsız olarak her zaman {color_steam:Yoğun SC Buhar} verir
Maks girdi ve çıktı hızları plazmanın yoğunluğuna bağlıdır ({EU}/{L})
{hr}
Kontrolcüdeki bir devre, buhar maliyeti karşılığında SC eşiğini düşürür
1'in üzerindeki her devre için {color_mechanic:-150 {L}/s} SC Eşiği ve {color_steam:-1.5%} buhar çıktısı