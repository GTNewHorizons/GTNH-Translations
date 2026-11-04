Parçacıkları yüksek enerjilere hızlandırır ve ardından yeni parçacıklar oluşturmak için çarpıştırır
Elektriksel olarak nötr parçacıklar etkilenmez
{color_electron_volt:Hedef Işın Enerjisini} (en fazla {color_electron_volt:{var:max_energy} {TeV}}) ve {light_purple:maksimum döngü sayısını} ayarla
Her saniye döngü yapar
{hr}
{color_mode:Hızlandırıcı modu}
Işını daha küçük LHC halkasında hızlandırır
Her döngü, {color_electron_volt:Işın Enerjisini} {color_eu_usage:döngüde tüketilen {EU}} * {color_electron_volt:{var:ev_per_eu} {eV}} / {gold:Işın Oranı} kadar artırır
{color_electron_volt:Hedef Işın Enerjisine} veya {light_purple:maksimum döngü sayısına} ulaşılana kadar
{color_electron_volt:Hedef Işın Enerjisine} ulaşılırsa, mevcut {gold:Işın Oranına} {color_formula:{var:rate_gain}} * {gold:Işın Oranı} ekler
{color_formula:{var:nerf_cutoff}} değerinin üzerindeki bir {gold:Işın Oranında}, bunun yerine ({color_formula:{var:rate_gain}} * {gold:Işın Oranı})^{dark_red:{var:nerf_power}} ekler
{color_eu_usage:Güç} maliyeti, {gold:Işın Oranı} başına {VNF:tier} kademesinde {color_amperage:1A} ile başlar ve {light_purple:tamamlanan döngü sayısıyla} karesel olarak artar
{color_eu_usage:P} = ({color_amperage:1A} {VNF:tier}) * {gold:R} * ({light_purple:N}+1)^2
{light_purple:maksimum döngü sayısına} ulaşıldığında otomatik olarak Çarpıştırıcı moduna geçer
{hr}
{color_mode:Çarpıştırıcı modu}
Işını, daha büyük LHC halkasında zıt yönlere giden ve yeni parçacıklar oluşturmak için çarpışan {color_formula:iki} ışına böler
{color_electron_volt:Çarpışma Enerjisi}, {color_electron_volt:Işın Enerjisinin} {color_formula:{var:collision_multiplier}} katıdır
{color_electron_volt:Çarpışma Enerjisi} durgun kütlesini aştığında çıktılarda bir parçacık belirir
{color_name:Süzülmüş Işın Çıkış Kapakları} ve Olasılık Masası, olası çıktıların listesini gösterir ve bunları filtrelemene izin verir
{hr}
{color_mode:Yükseltici Sıvılar}
{color_name:Yükseltici Sıvılar}, {color_formula:{var:nerf_cutoff}} değerinin üzerindeki {gold:Işın Oranları} için {dark_red:ölçekleme üssünü} yükseltir
{color_name:Sıvı yok}: {dark_red:{var:nerf_power}}
{color_name:{fluid:quarkgluonplasma}}: {dark_red:{var:nerf_power_qgp}}
{color_name:{fluid:molten.magmatter}}: {dark_red:{var:nerf_power_magmatter}}
Bir yükselticiyle, {color_electron_volt:Işın Enerjisi} bir anda {color_electron_volt:{var:max_energy} {TeV}} değerine ayarlanır ve her döngüde {gold:Işın Oranı {L}} kadar sıvı tüketilir
Sağlanan {color_name:Yükseltici Sıvı} değişirse, ışın sıfırdan yeniden hızlandırılmalıdır
{hr}
Dört LHC modülü vardır ve modülün üstündeki harfle işaretlenirler:
{aqua:E - Elektromanyetizma}: Yüklü Madde Sensörü ({aqua:CMS})
{dark_green:W - Zayıf Etkileşim}: Gelişmiş Toplam Lepton Asimilasyon Tuzağı ({dark_green:ATLAS})
{white:S - Güçlü Kuvvet}: Mutlak Kafes Entegre Kromodinamik Kapsülleyici ({white:ALICE})
{dark_purple:G - Kütle Çekimi}: Yerelleştirilmiş Ufuk Eğriliği Bağlayıcısı ({dark_purple:LHCb})