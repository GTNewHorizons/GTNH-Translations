---
item_ids:
  - gregtech:gt.blockmachines:15544
navigation:
  title: 주하이 어항
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15544
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 주하이 어항

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15544"/>
</GameScene>
<Color id="GREEN">주하이 어항</Color>은 물고기와 기타 잡다한 전리품의 대량 생산을 위한 IV 티어 멀티블록입니다. <Color id="GREEN">주하이</Color>는 단일블록 물고기 포획기 <ItemImage id="miscutils:blockFishTrap"/>의 직접적인 상위 버전입니다. 오버클럭으로 훨씬 빠르며 $$2 \times (\text{Tier} + 1)$$개의 병렬 처리를 제공하기 때문입니다. 기계의 유일한 입력은 전력이며 출력은 완전히 무작위입니다. 사용 가능한 세 가지 레시피(물고기, 쓰레기, 보물)는 각각 고유한 전리품 테이블을 가지며, 컨트롤러/입력 버스에 특정 프로그래밍 회로를 설정하여 선택합니다. 
<br clear="all"/>

> [!NOTE]
> 구조물 자체만 변경되었으며, 멀티블록의 핵심 기능은 이전과 동일합니다

## 건설
<Color id="GREEN">주하이</Color>에는 티어 부품이 없습니다. 버스/해치는 구조물 어디에서든 모든 케이싱을 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 물은 기계를 초기화하는 일회성 비용이며, 저수조 해치 또는 입력 해치를 통해 구조물에 투입됩니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15544"/><ItemImage id="gregtech:gt.blockmachines:15544"/>
- 160-167 <ItemLink id="miscutils:gtplusplus.blockcasings.3"/><ItemImage id="miscutils:gtplusplus.blockcasings.3"/>
- 12 <ItemLink id="gregtech:gt.sheetmetal:306"/><ItemImage id="gregtech:gt.sheetmetal:306"/>
- 12 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 1+ 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">주하이 어항</Color>은 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 사이에서 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">주하이</Color>는 단일블록 물고기 포획기의 직접적인 상위 버전입니다. 오버클럭으로 훨씬 빠르며 다음 표에서 볼 수 있듯이 $$2 \times (\text{Tier} + 1)$$개의 병렬 처리를 제공하기 때문입니다.
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 |