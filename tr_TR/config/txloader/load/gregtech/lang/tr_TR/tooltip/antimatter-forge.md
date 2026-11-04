{light_purple:Boyutlar dahil değil!}
Protomaddeyi antimaddeye dönüştürür
Görüntülemeyi kapatmak için tornavida kullan
Pasif olarak {var:base_consumption} + ({dark_aqua:Antimadde} * 1000)^(1.5 - {green:{bold:{underline:M}}}) {EU/t} tüketir
Boşken tüketim her tick %1 azalır
Antimadde üretmek için döngü başına aktif olarak ({dark_aqua:Antimadde} * {var:active_base_mult})^(1.5 - {dark_purple:{bold:{underline:G}}}) {EU} kullanır
{hr}
Her saniye döngü yapar
Her döngüde, 16 antimadde kapağındaki en düşük antimadde miktarı kaydedilir
En düşük miktardan fazlasına sahip tüm kapaklar {red:farkın yarısını kaybeder!}
{red:Antimaddenin %10'unu yok eder}, döngü sırasında enerjisi/protomaddesi biterse
Kapak başına temel üretim, her döngüde (1/16) * ({dark_aqua:Antimadde}^(0.5 + {gold:{bold:{underline:C}}})) antimaddedir
Her kapak, kapak başına temel üretimi, ortalaması 0.2 + {aqua:{bold:{underline:A}}} ve varyansı 1 olan normal dağılımdan çekilen rastgele bir sayıyla çarpar
Toplam antimadde kazancı negatif olabilir!
{hr}
Antimadde üretimini iyileştirmek için stabilizasyon sıvılarıyla beslenebilir
Her stabilizasyon aynı anda sıvılardan yalnızca birini kullanabilir
{green:{bold:{underline:M}}}{green:anyetik Stabilizasyon} (Döngü başına {dark_aqua:Antimadde}^0.5 {L} sıvı tüketir)
1. {fluid:molten.tengampurified} = {green:0.1}
2. {fluid:temporalfluid} = {green:0.2}
3. {fluid:molten.magmatter} = {green:0.3}
{dark_purple:{bold:{underline:G}}}{dark_purple:ravite Stabilizasyonu} (Döngü başına {dark_aqua:Antimadde}^0.5 {L} sıvı tüketir)
1. {fluid:molten.spacetime} = {dark_purple:0.05}
2. {fluid:spatialfluid} = {dark_purple:0.10}
3. {fluid:molten.eternity} = {dark_purple:0.15}
{gold:{bold:{underline:M}}}{gold:uhafaza Stabilizasyonu} (Döngü başına {dark_aqua:Antimadde}^(2/7) {L} sıvı tüketir)
1. {fluid:molten.shirabon} = {gold:0.05}
2. {fluid:molten.magnetohydrodynamicallyconstrainedstarmatter} = {gold:0.10}
{aqua:{bold:{underline:A}}}{aqua:ktivasyon Stabilizasyonu} (Döngü başına {dark_aqua:Antimadde}^(1/3) {L} sıvı tüketir)
1. {fluid:naquadah based liquid fuel mkv (depleted)} = {aqua:0.05}
2. {fluid:naquadah based liquid fuel mkvi (depleted)} = {aqua:0.10}