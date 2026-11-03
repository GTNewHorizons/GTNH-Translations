---
navigation:
  parent: ../tricks_example_index.md
  title: Otomatik Ayarlı Kırıktaş Jeneratörü
  icon: minecraft:cobblestone
---

# Otomatik Ayarlı Kırıktaş Jeneratörü

Bir kırıktaş jeneratörünün otomasyonu basittir; sadece bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> kısmını standart bir vanilya
manuel kırıktaş jeneratörüne doğrult. Ancak bunu yapmak sonunda ağını kırıktaşla tıkar, bu yüzden biraz düzenleme
istenir.

Yok etme düzlemleri (<ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> gibi davranırlar) bu şekilde çalıştığından, kızıltaş kartlı bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> kısmını
doğrudan bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> kısmına bakacak şekilde koyamayız (çünkü arada depolama olmadan doğrudan içe aktarmadan dışa aktarmaya
geçemezsin). Biraz daha dolambaçlı gitmemiz gerekiyor.

<ItemLink id="appliedenergistics2:item.ItemMultiPart:80" /> kısımları, ağının parçalarını kızıltaş sinyalleriyle bağlamana ve ayırmana izin verir, ancak bunu yaptıklarında
ağ yeniden başlar. Basit bir çözüm var: anahtar veri yolunu bir [alt ağ](../ae2_mechanics/subnetworks.md)
üzerine koy, böylece yalnızca alt ağı yeniden başlatsın.

Kendi kendine yeten bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> [alt ağı](../ae2_mechanics/subnetworks.md)
ana ağdaki bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kısmına itebilir. Anahtar veri yolu, alt ağı bir
kuvars fibere bağlar ve ayırır, düzlemlere giden gücü keser.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/regulated_cobble_gen.snbt" />

  <BoxAnnotation color="#dddddd" min="3 2 2" max="7 2.3 3">
  (1) Yok Etme Düzlemleri: Yapılandırılacak GUI yok, ancak güç çekişini azaltmak için Verimlilik ve Kırılmazlık ile büyülenebilirler.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 2" max="2.3 3 3">
  (2) Depolama Veri Yolu: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 2.3 2" max="2.7 2.7 2.3">
  (3) Anahtar Veri Yolu: Anahtar veri yolunun ana ağda değil,
  alt ağda olması çok önemli.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 2.3" max="2.7 3.3 2.7">
  (4) Seviye Verici: Kırıktaş ve istenen miktarla yapılandırılmış, "Seviyeler sınırın altına düştüğünde yay" olarak ayarlanmış.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 3" max="2 3 2">
  (5) Arayüz: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 2.5 1.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> kısımlarının (1) yapılandırılacak bir GUI'si yoktur, ancak güç çekişini azaltmak için Verimlilik ve Kırılmazlık ile büyülenebilirler.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:80" /> (3) kuvars fiberin ana ağ tarafında değil, alt ağ tarafında olmalı; yoksa ana
  ağ her açılıp kapandığında yeniden başlar.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (4) istenen eşya ve miktarla yapılandırılmış ve "Seviyeler sınırın altına düştüğünde yay" olarak ayarlanmıştır.
* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (5) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

1. Kırıktaş jeneratörü bir miktar kırıktaş üretir.
2. <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> kısımları kırıktaşı kırar.
3. <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> kırıktaşı <ItemLink id="appliedenergistics2:tile.BlockInterface" /> içinde depolar ve ana ağa gönderir.
4. Ana ağdaki kırıktaş miktarı ayarlanan miktarı aştığında, <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> sinyal
   göndermeyi durdurur ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:80" /> kısmını kapatır.
5. Bu, alt ağa giden gücü keser ve yok etme düzlemlerinin çalışmasını durdurur.