---
navigation:
  title: Aşırı Dolu Pota Nerfi
  parent: magic.md
  icon: Thaumcraft:blockMetalDevice
categories:
    - Büyü Değişiklikleri
date: 2026-06-10
---

Thaumcraft'ın <ItemLink id="Thaumcraft:blockMetalDevice"/> <ItemImage id="Thaumcraft:blockMetalDevice"/> artık <Color id="RED">esansı yok edecek</Color>; <Color id="RED">ne kadar aşırı doluysa</Color> o kadar hızlı. <Color id="BLUE">200</Color> toplam esanstan başlayarak artık toplam esansın <Color id="RED">bir yüzdesini</Color> çürütecek ve bileşik aspektleri parçalama eğiliminde olacak. Bu yüzde, <Color id="BLUE">1000</Color> toplam esansta saniyede <Color id="RED">%4.2</Color>'ye yavaşça yükselir; bu, <Color id="BLUE">100</Color> olan orijinal yumuşak sınırın 10 katıdır.

<FunctionGraph xMax="1200" width="380" title="Saniyede Ayrışan Esans" xLabel="Potadaki Esans" yLabel="Saniyede Ayrışan Esans">
  <Function expr="0.2" color="#4488FF" label="Taşmasız çürüme (0.2 / s)" domain="0..100"/>
  <Function expr="4.2" color="#44FF44" label="Orijinal taşma çürümesi (4.2 / s)" domain="100..200"/>
  <Function expr="4.2 + 0.000042x^2" color="#FFFF22" label="Ölçeklenen taşma çürümesi (4.2 + 0.000042x^2 / s)" domain="200..1000"/>
  <Function expr="4.2 + 0.042x" color="#FF2222" label="Maksimum taşma çürümesi (4.2 + 0.042x / s)" domain="1000..1200"/>
</FunctionGraph>