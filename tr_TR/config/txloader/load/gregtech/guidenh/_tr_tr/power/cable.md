---
navigation:
  title: "Teller ve Kablolar"
  icon: gregtech:gt.blockmachines:1248
  parent: power_index.md
  position: -3
---

# Teller ve Kablolar

**Teller ve kablolar**, bir [yerel güç ağı](enet.md) içindeki verici blokları ve tüketici blokları bağlamak için kullanılan ortamdır. Kendileri güç depolamazlar.

Tellerin üç temel parametresi vardır; hepsi de ipucunda gösterilir.

# Maksimum Gerilim ve Maksimum Akım

**Maksimum gerilim** yalnızca tel malzemesine bağlıdır. Teller, malzemenin temel maksimum akımını çarpan 1x, 2x, 4x, 8x, 12x ve 16x varyantlarında bulunur.

- Maksimum gerilimi çok düşük olan bir tel, daha yüksek gerilimli enerji paketlerini iletemez. Gerilim veya akımdan biri sınırını aşarsa tel yanar.
- Maksimum gerilimi yeterince yüksek olan bir tel, daha düşük gerilimli paketleri güvenle iletebilir.

Akım toplanır: belirli bir tel parçasının taşıdığı akım, içinden geçen tüm akımların toplamıdır. Bir tel parçasının yanıp yanmayacağı, içinden geçen tüm paketler arasındaki en yüksek paket gerilimine bağlıdır.

# Kablo Kaybı Oranı

Güç teller aracılığıyla iletildiğinde akım yol boyunca her yerde aynı kalır, ancak [kablo kaybı](cable_loss.md) nedeniyle gerilim düşebilir.

- Kablo kaybı oranı tel kalınlığına veya akıma bağlı değildir. Yalnızca malzemeye ve telin yalıtımlı olup olmadığına (tel mi kablo mu) bağlıdır. Yalıtımlı kablolar genellikle karşılık gelen çıplak telin kaybının yalnızca yarısına sahiptir.
- Bazı teller sıfır kayba sahiptir ve bu nedenle süperiletken gibi davranır; örneğin 1x Kızıltaş Alaşımı Kablosu, 1x MV Süperiletken Teli ve 1x Sonsuzluk Teli.

# Değiştirme ve Boyama

Bir tür tel veya kablo tutarken, başka bir yerleştirilmiş tel veya kabloya <kbd>Shift</kbd> + <kbd>Sol tık</kbd> yaparak onu doğrudan değiştir. Bağlantı yönleri ve kapaklar korunur. Değiştirmeden sonra eski tel-cihaz bağlantıları kopar ve yeniden bağlanmaları gerekir.

Telleri renklendirmek için sprey kutuları kullanabilirsin. Bu, farklı yerel güç ağlarında farklı gerilimler taşıyan telleri ayırt etmek için kullanışlıdır.