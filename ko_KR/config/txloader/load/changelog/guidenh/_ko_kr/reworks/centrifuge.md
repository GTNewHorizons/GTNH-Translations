---
item_ids:
  - gregtech:gt.blockmachines:15512
navigation:
  title: 산업용 원심분리기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15512
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 산업용 원심분리기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15512"/>
</GameScene>
<Color id="GREEN">산업용 원심분리기 (IC)</Color>는 먼지, 액체 및 기타 아이템을 구성 성분으로 원심분리하기 위한 EV 티어 멀티블록입니다. 단일블록 원심분리기의 직접적인 업그레이드입니다. ZPM 티어에서는 <Color id="RED">Spinmatron-2737</Color>로 대체됩니다.
<br clear="all"/>

> [!NOTE]
> 이 멀티블록의 변경 사항은 비교적 작습니다. 더 큰 기본 구조를 가짐으로써 해치를 배치할 공간이 더 많아졌습니다. 건설 비용과 새로운 디자인을 제외하면, 이 기계의 기능은 변경되지 않았습니다!

## 건설
<Color id="GREEN">산업용 원심분리기</Color>는 단일 유형의 케이싱으로 구성되지만, 구조물에 <Color id="RED">체 격자</Color>와 <Color id="BLUE">에글린 강철 프레임 박스</Color>를 사용합니다. 버스/해치는 구조물의 모든 케이싱을 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 여러 개의 일반 에너지 해치를 사용하여 오버클럭할 수 있습니다. 스크루드라이버로 컨트롤러를 우클릭하면 애니메이션을 비활성화할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조물을 시각화/건설할 수 있습니다.

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15512" /> <ItemImage id="gregtech:gt.blockmachines:15512" />
- 6-32 <ItemLink id="miscutils:miscutils.blockcasings" /> <ItemImage id="miscutils:miscutils.blockcasings" />
- 24 <ItemLink id="miscutils:blockFrameGtEglinSteel" /> <ItemImage id="miscutils:blockFrameGtEglinSteel" />
- 18 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:6" />
- 1+ 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">산업용 원심분리기</Color>는 각 면을 벽 공유하여 케이싱, 프레임 박스, 버스/해치를 절약할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.

## 사용법
<Color id="GREEN">산업용 원심분리기</Color>는 225% 속도로 작동하고, 일반적으로 필요한 EU/t의 90%만 사용하며, 다음 표와 같이 전압 티어당 6개의 병렬 처리를 제공하므로 단일블록 원심분리기의 직접적인 업그레이드입니다.
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |