---
item_ids:
  - gregtech:gt.blockmachines:3015
navigation:
  title: 빔 제작기
  parent: multis.md
  icon: gregtech:gt.blockmachines:3015
categories:
    - 새로운 멀티블록
author: Skorched
date: 2026-05-25
---

# 빔 제작기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3015" />
</GameScene>
<Color id="GREEN">빔 제작기</Color>는 ZPM 티어 멀티블록으로, 다른 어떤 공급원에서 제공되는 입자 빔을 사용해 입력부의 유체와 액체를 충돌시켜 다른 산출물을 제작합니다.
<br clear="all"/>

## 건설:
빔 제작기는 빔라인과 달리 단일 멀티블록입니다. 빔라인 파이프는 생성된 빔을 <ItemLink id="gregtech:gt.blockmachines:10503"/><ItemImage id="gregtech:gt.blockmachines:10503"/>로 유도하는 데 사용됩니다. 이 파이프의 길이는 기계나 빔 자체의 어떤 속성에도 영향을 주지 않습니다.

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:3015"/><ItemImage id="gregtech:gt.blockmachines:3015"/>
- 224-228 <ItemLink id="gtnhlanth:casing.shielded_accelerator"/><ItemImage id="gtnhlanth:casing.shielded_accelerator"/>
- 26 티어 유리 (아무거나) <ItemImage id="bartworks:BW_GlasBlocks:5"/>
- 16 <ItemLink id="gregtech:gt.blockcasings3:10"/><ItemImage id="gregtech:gt.blockcasings3:10"/>
- 2 <ItemLink id="gregtech:gt.blockmachines:10503"/><ItemImage id="gregtech:gt.blockmachines:10503"/>
- 1+ 에너지 해치 (충돌기 케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 0+ 입력 버스 (충돌기 케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ 입력 해치 (충돌기 케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ 출력 버스 (충돌기 케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ 출력 해치 (충돌기 케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:60"/>

## 사용법:
제공된 아이템과 유체로 유효한 제작이 감지되면 제작이 시작됩니다. 오직 이 시점에서만 빔 제작기가 빔라인 입력 해치를 통해 입자를 받아들이기 시작합니다. 이 빔에 올바른 입자가 존재하면, 해당 입자는 소모되어 제작 진행에 기여합니다. 입자 빔이 중단되어도 레시피는 __중단되지 않습니다__, 다만 진행은 멈춥니다. 제작이 진행되는 동안에는 제공되는 입자량과 관계없이 에너지가 지속적으로 소모됩니다.

기계는 입자를 버퍼링하지만, 작동 중일 때만 가능하며, 그렇지 않으면 입자를 받아들일 수 없습니다.

## 라우팅:
빔 제작기와 함께, 빔 라우팅을 위해 설계된 세 가지 새로운 물류 멀티블록이 있습니다. 그것은 <Color id="GREEN">빔 반사경</Color>, <Color id="RED">빔 분할기</Color>, <Color id="BLUE">빔 안정기</Color>입니다.
- <Color id="GREEN">빔 반사경</Color><ItemImage id="gregtech:gt.blockmachines:3016"/> - 빔을 90도 또는 180도 회전시킬 수 있습니다.
- <Color id="RED">빔 분할기</Color> <ItemImage id="gregtech:gt.blockmachines:3017"/> - 혼합된 입자 패킷 흐름을 4개의 개별 구성 가능한 라인으로 분할할 수 있습니다.
- <Color id="BLUE">빔 안정기</Color> <ItemImage id="gregtech:gt.blockmachines:3018"/> - 작은 버퍼 역할을 하여, 간헐적인 고속 빔을 더 낮은 양의 일정한 빔으로 변환할 수 있게 합니다.