---
navigation:
  title: 과충전된 도가니 너프
  parent: magic.md
  icon: Thaumcraft:blockMetalDevice
categories:
    - 마법 변경 사항
date: 2026-06-10
---

Thaumcraft의 <ItemLink id="Thaumcraft:blockMetalDevice"/> <ItemImage id="Thaumcraft:blockMetalDevice"/>는 이제 <Color id="RED">더 많이 과충전될수록</Color> <Color id="RED">에센티아를 제거</Color>하는 속도가 더 빨라집니다. 총 에센티아가 <Color id="BLUE">200</Color>부터 시작하면, 이제 <Color id="RED">총 에센티아의 일정 비율</Color>을 감소시키며, 복합 측면을 분해하는 쪽으로 치우칩니다. 이 비율은 총 에센티아가 <Color id="BLUE">1000</Color>일 때 초당 <Color id="RED">4.2%</Color>까지 천천히 증가하며, 이는 기존 소프트캡인 <Color id="BLUE">100</Color>의 10배입니다.

<FunctionGraph xMax="1200" width="380" title="Essentia Decomposed / s" xLabel="Essentia in Crucible" yLabel="Essentia Decomposed / s">
  <Function expr="0.2" color="#4488FF" label="Non-overflow decay (0.2 / s)" domain="0..100"/>
  <Function expr="4.2" color="#44FF44" label="Original overflow decay (4.2 / s)" domain="100..200"/>
  <Function expr="4.2 + 0.000042x^2" color="#FFFF22" label="Scaling overflow decay (4.2 + 0.000042x^2 / s)" domain="200..1000"/>
  <Function expr="4.2 + 0.042x" color="#FF2222" label="Max overflow decay (4.2 + 0.042x / s)" domain="1000..1200"/>
</FunctionGraph>