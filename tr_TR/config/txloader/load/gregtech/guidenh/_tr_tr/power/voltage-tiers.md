---
navigation:
  title: "Gerilim Kademeleri"
  icon: gregtech:gt.metaitem.01:32598
  parent: power_index.md
  position: -1
---

# Gerilim Kademeleri

GTNH, ilerlemeyi bir dizi gerilim kademesine böler. Gerilim kademeni ilerletmek, paketin teknolojik ilerlemeyi ölçtüğü başlıca yollardan biridir.

Aşağıdaki tablo her kademenin gerilim aralığını gösterir. **Standart gerilim**, her kademenin üst bağlı değeridir. Çoğu durumda, her kademe yükselişi standart gerilimi 4 ile çarpar. Bir kademenin standart gerilimi genellikle $$2 \times 4^n \text{ V}$$ olur; burada $$n$$ **kademe indeksidir**: ULV 0, LV 1 ve böyle devam eder.

| Kademe İndeksi | Kısaltma | Tam Ad | Gerilim Aralığı (V) | Standart Gerilim (V) |
|------------|---------|-----------|-------------------|----------------------|
| 0 | ULV | Ultra Düşük Gerilim | 1-8 | 8 |
| 1 | LV | Düşük Gerilim | 9-32 | 32 |
| 2 | MV | Orta Gerilim | 33-128 | 128 |
| 3 | HV | Yüksek Gerilim | 129-512 | 512 |
| 4 | EV | Ekstrem Gerilim | 513-2,048 | 2,048 |
| 5 | IV | Çılgın Gerilim | 2,049-8,192 | 8,192 |
| 6 | LuV | Akılalmaz Gerilim | 8,193-32,768 | 32,768 |
| 7 | ZPM | Sıfır Noktası Modülü Gerilimi | 32,769-131,072 | 131,072 |
| 8 | UV | Nihai Gerilim | 131,073-524,288 | 524,288 |
| 9 | UHV | Son Derece Nihai Gerilim | 524,289-2,097,152 | 2,097,152 |
| 10 | UEV | Aşırı Nihai Gerilim | 2,097,153-8,388,608 | 8,388,608 |
| 11 | UIV | Çılgınca Nihai Gerilim | 8,388,609-33,554,432 | 33,554,432 |
| 12 | UMV | Mega Nihai Gerilim | 33,554,433-134,217,728 | 134,217,728 |
| 13 | UXV | Genişletilmiş Mega Nihai Gerilim | 134,217,729-536,870,912 | 536,870,912 |
| 14 | MAX | Maksimum Gerilim | 536,870,913-2,147,483,640 | - |

Kademe indeksi genellikle bobin ısısı ve maksimum paralel sayısı gibi multiblok hesaplamalarında kullanılır.