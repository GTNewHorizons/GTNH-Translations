---
navigation:
  title: "Kablo Kaybı"
  icon: gregtech:gt.metatool.01:26
  parent: power_index.md
  position: -5
---

# Kablo Kaybı

**Kablo kaybı**, güç [teller ve kablolar](cable.md) üzerinden iletildiğinde ortaya çıkabilecek ek güç maliyetidir. GT [yerel güç ağı](enet.md) için çekirdek bir mekaniktir. Oyunun başlarında makine gerilimleri düşük olduğundan kablo kaybını kontrol etmek çok önemlidir. Gerilim kademeleri yükseldikçe kablo kaybı daha az önem kazanır.

# Kayıp Oranı

Her [tel ve kablonun](cable.md) bir kablo kayıp oranı parametresi vardır (ipucunda "loss/m/amp: x V" olarak gösterilir). Bu kayıp oranı $$\rho$$ ve tel uzunluğu $$L$$ olsun. O zaman bir paketin telden geçmesinden sonraki gerçek giriş gerilimi şudur:

$$U_{\text{input}} = U_{\text{output}} - \rho L_{\text{wire}}$$

Telde kaybedilen güç:

$$P_{\text{cable loss}} = I \rho L_{\text{wire}}$$

Yani kablo kaybı kayıp oranı, akım ve tel uzunluğuyla doğru orantılıdır. Tel uzunluğu, kayıp oranı ve iletilen güç aynı kaldığında, iletim gerilimini yükseltmek akımı düşürür ve böylece kablo kaybını dolaylı olarak azaltır. **İletim gerilimindeki her kademe artışı kablo kaybını dörtte bire indirir**.

Örnek: herhangi bir Kalay Kablo 1 V/m kayıp oranına sahiptir. 32V 2A güç 2 m Kalay Kablo üzerinden geçerse varış noktasında 30V 2A olur ve yol boyunca kablo kaybı 4 EU/t'dir.

[Gücü Güvenilir Sağlama](enet.md#providing-power-reliably) bölümü yalnızca sıfır kayıp durumunu ele alır. Kablo kaybı mevcutken önce tüketicinin aldığı gerçek paket gerilimini hesapla, sonra mantığın geri kalanını değiştirmeden uygula.

Kablo kaybı gerilimi düşürdüğünde, kaybedilen gücü giriş akımını artırarak telafi edebilirsin. Ancak akım, ne telin maksimum akımını ne de tüketicinin maksimum giriş akımını aşamaz. Akımı artırmak hâlâ yeterli değilse daha düşük kayıplı tel, daha yüksek akımlı tel veya daha kısa bir iletim yolu gerekir.