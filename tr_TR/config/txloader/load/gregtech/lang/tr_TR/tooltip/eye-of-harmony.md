Boyutlararası mühendislik kullanarak içi dışından daha büyük bir uzay-zaman cebi oluşturur.
Sertifikalı Zaman Lordu yönetmeliklerine uygundur.
{gold:{hr}}
Her biri {green:9} kademeli üç farklı Alan Jeneratöründen oluşur:
{blue:Uzay-Zaman Sıkıştırması}: Maksimum Tarif Kademesini belirler, tarifin üzerindeki her kademe için {green:-3%} işlem süresi (çarpımsal)
{blue:Zaman Genleşmesi}: her kademe için {green:-50%} tarif süresi (çarpımsal), her kademe için {green:-9.25%} tarif başarı şansı (toplamsal)
{blue:Stabilizasyon}: her kademe için {green:+5%} tarif başarı şansı (toplamsal), her kademe için {green:-5%} verim (toplamsal)
Daha düşük kademeli stabilizasyon jeneratörleri ayrıca toplam {EU} çıktısını azaltır,
T1 Ham ile {green:-40%} ile başlar ve her kademe için {green:+5%} artar (toplamsal)
{gold:{hr}}
Yerleştirmek ve tarifi ayarlamak için {blue:Gezegen Bloğu} ile kontrolcüye sağ tıkla
Temel tarif başarı şansı {green:(S)} Gezegen Kademesine bağlıdır
Başarı durumunda NEI'de listelenen her şeyi çıktı olarak verir. Sıvılar için temel verim, herhangi bir cezadan önce {green:100%} ile başlar
Başarısızlık durumunda {green:Spacetime}{color_formula: = S * 14,400 * 2^(Gezegen Kademesi)} ve varsa {EU} çıktısını verir
Pity, birkaç ardışık başarısızlıktan sonra başarıyı garanti eder ancak başarı veya tarif değişikliğinde sıfırlanır
{gold:{hr}}
Boştayken kendi iç tamponuna sürekli {blue:Hidrojen} ve {blue:Helyum} alır ve tarif başladığında hepsini tüketir
Bir tarif için gereken minimum miktarı aşmak, tarif başarı şansını ve verimi büyük ölçüde azaltır
{green:Taşma Oranı}{color_formula: = (Depolanan Sıvı / Min Sıvı) - 1}
{green:Ceza%}{color_formula: = 1 - exp(-(30 * Taşma Oranı)^2)}
{gold:{hr}}
{yellow:Sahibinin kablosuz ağından doğrudan {EU} tüketir}
Giriş yolundaki {color_name:Programlanmış Devre} ile istediğin aşırı hızlandırma sayısını ayarla
{EU} çıktısı sabittir ve aşırı hızlandırma sayısıyla ölçeklenmez
{gold:{hr}}
Paralel eklemek için bir giriş yolundan {blue:Astral Dizi Üreticileri (AA)} yerleştir (maks {blue:8,637})
Her biri başarılı olup olmayacağını belirlemek için bağımsız olarak değerlendirilir
{green:Paralel Üs (PE)}{color_formula: = floor(log(8 * AA) / log(1.7))}
{green:Paraleller}{color_formula: = 2^(PE)}
{gold:{hr}}
Paralel çalıştırırken artık pity yoktur ve güç değişir:
{green:{EU} Girdisi}{color_formula: = Temel {EU} Girdisi * 4^OC * 2.3^PE * 1.63 / 20.7}
{green:{EU} Çıktısı}{color_formula: = Temel {EU} Çıktısı * 2.3^(PE-1) / 9}
Ayrıca {blue:Hidrojen} ve {blue:Helyum} yerine {blue:Yoğunlaştırılmış Ham Yıldız Plazma Karışımı} tüketir:
{green:Ham Yıldız Plazması}{color_formula: = 12.4 / 10^6 * Helyum Miktarı * Paraleller}