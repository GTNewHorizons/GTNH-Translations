---
navigation:
  title: "Kablo Kaybı"
  icon: gregtech:gt.metatool.01:26
  parent: power-index.md
  position: -5
---

# Kablo Kaybı

**Kablo kaybı**, güç [teller ve kablolar](cable.md) üzerinden iletildiğinde ortaya çıkabilecek ek güç maliyetidir. GT [yerel enerji ağı](enet.md) sisteminin temel bir mekaniğidir. Oyunun başlarında makine gerilimleri düşük olduğu için kablo kaybını kontrol etmek çok önemlidir. Gerilim kademeleri yükseldikçe kablo kaybı daha az önemli hale gelir.

# Kayıp Oranı

Her [tel ve kablonun](cable.md) bir kablo kayıp oranı parametresi vardır (ipucunda "loss/m/amp: x V" olarak gösterilir). Kayıp oranı $$\rho$$ ve tel uzunluğu $$L$$ olsun. Bir paket telden geçtikten sonra gerçek giriş gerilimi şöyledir:

$$U_{\text{input}} = U_{\text{output}} - \rho L_{\text{wire}}$$

Tele kaybedilen güç:

$$P_{\text{cable loss}} = I \rho L_{\text{wire}}$$

Yani kablo kaybı kayıp oranı, akım ve tel uzunluğuyla orantılıdır. Tel uzunluğu, kayıp oranı ve iletilen güç aynı kalırsa iletim gerilimini yükseltmek akımı düşürür ve dolayısıyla kablo kaybını dolaylı olarak azaltır. **İletim gerilimindeki her kademe artışı kablo kaybını dörtte bire indirir**.

Örnek: herhangi bir Kalay Kablonun kayıp oranı 1 V/m'dir. 32V 2A güç 2 m Kalay Kablodan geçerse hedefte 30V 2A olur ve yol boyunca kablo kaybı 4 EU/t'dir.

[Gücü Güvenilir Sağlama](enet.md#providing-power-reliably) bölümü yalnızca sıfır kayıp durumunu ele alır. Kablo kaybı varken önce tüketicinin aldığı gerçek paket gerilimini hesapla, ardından mantığın geri kalanını değiştirmeden uygula.

Kablo kaybı gerilimi düşürdüğünde kaybedilen gücü giriş akımını artırarak telafi edebilirsin. Ancak akım ne telin maksimum akımını ne de tüketicinin maksimum giriş akımını aşabilir. Akımı artırmak yine de yetmiyorsa daha düşük kayıplı tel, daha yüksek akımlı tel veya daha kısa bir iletim yolu gerekir.