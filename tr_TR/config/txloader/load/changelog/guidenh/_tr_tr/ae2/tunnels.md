---
item_ids:
  - appliedenergistics2:item.ItemTunnelPattern
navigation:
  title: Tünel Kalıpları
  parent: ae2.md
  icon: appliedenergistics2:item.ItemTunnelPattern
categories:
    - Applied Energistics 2
author: Skorched
date: 2026-05-27
---

# Tünel Kalıpları
Bir yükseltme aldığında tüm kalıplarındaki devre kartlarını ya da EYF koruyucu gazını güncellemekten yoruldun mu? 2.9'da bununla başa çıkmanın yeni bir yolu geliyor:

## AE2 Tünel Kalıpları!

<Color id="GREEN">Tünel Kalıpları</Color> yeni bir **yalnızca girdi** kalıp tipidir. Tekrarı azaltmak ve çok sayıda kalıp içeren düzenekleri yönetmeyi kolaylaştırmak için tasarlanmışlardır. Girdisi olup çıktısı olmayan bir işleme kalıbı kodladığında, o bir Tünel Kalıbı olur. Her biri güvenilir şekilde referans verilebilmesi için benzersiz bir ID alır.

__Başka bir kalıbın girdilerine__ bir <Color id="GREEN">Tünel Kalıbı</Color> koyarak modüler kalıp yapı taşları olarak kullanılabilirler. Üretim sırasında ME sistemin bir kalıbın girdilerinde Tünel Kalıbı bulursa, ağındaki ME Arayüzlerinde bu Tünel Kalıbını arar ve __girdilerini mevcut tarife ekler__. Kalıp bulunamazsa, Tünel Kalıbı eşyasının kendisine geri döner.

Tünel Kalıplarını __zincirleyebilirsin__ de: bir Tünel Kalıbının girdileri olarak istediğin kadar Tünel Kalıbı ve normal bileşen karışımını ayarlayabilirsin. Bu sayede, birçok tarifte paylaşılabilen ve sonradan kolayca değiştirilebilen __kullanılabilir girdi grupları__ tanımlayabilirsin. Tünel Kalıbının bileşenlerini, ona referans veren kalıpların <u>__hiçbirini__</u> değiştirmek zorunda kalmadan serbestçe yeniden adlandırabilir veya değiştirebilirsin!

Bu özelliği kullanmanın harika bir örneği, çok bloklu sözde üretim tariflerine kademeli camları, bobinleri ya da tam girdi/çıktı kapakları ve veri yolu setlerini dahil etmek veya EYF üretimlerine asal gazları eklemek için kullanmaktır. Daha fazla kullanım alanı hâlâ keşfediliyor!