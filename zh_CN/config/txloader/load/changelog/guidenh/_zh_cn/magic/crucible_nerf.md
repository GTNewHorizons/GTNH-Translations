---
navigation:
  title: Overfilled Crucible Nerf
  parent: magic.md
  icon: Thaumcraft:blockMetalDevice
categories:
    - Magic Changes
date: 2026-06-10
---

Thaumcraft's <ItemLink id="Thaumcraft:blockMetalDevice"/> <ItemImage id="Thaumcraft:blockMetalDevice"/> will now <Color id="RED">remove essentia</Color> more quickly the <Color id="RED">more overfilled</Color> it is. Starting at <Color id="BLUE">200</Color> total essentia, it will now decay a <Color id="RED">percent of the total essentia</Color>, with a bias toward breaking down compound aspects. This percent slowly increases to <Color id="RED">4.2%</Color> per second at <Color id="BLUE">1000</Color> total essentia, 10x the original softcap of <Color id="BLUE">100</Color>.

<FunctionGraph xMax="1200" width="380" title="Essentia Decomposed / s" xLabel="Essentia in Crucible" yLabel="Essentia Decomposed / s">
  <Function expr="0.2" color="#4488FF" label="Non-overflow decay (0.2 / s)" domain="0..100"/>
  <Function expr="4.2" color="#44FF44" label="Original overflow decay (4.2 / s)" domain="100..200"/>
  <Function expr="4.2 + 0.000042x^2" color="#FFFF22" label="Scaling overflow decay (4.2 + 0.000042x^2 / s)" domain="200..1000"/>
  <Function expr="4.2 + 0.042x" color="#FF2222" label="Max overflow decay (4.2 + 0.042x / s)" domain="1000..1200"/>
</FunctionGraph>