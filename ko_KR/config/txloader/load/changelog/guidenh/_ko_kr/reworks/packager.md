---
item_ids:
  - gregtech:gt.blockmachines:15513
navigation:
  title: 아마존 창고 보관소
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15513
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-16
---

# 아마존 창고 보관소

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15513"/>
</GameScene>
<Color id="GREEN">아마존 창고 보관소(AWD)</Color>는 다양한 아이템을 포장하고 포장 해제하는 IV 티어 멀티블록입니다. 단일블록 포장기에서 직접 업그레이드된 기계로, 최대 <Color id="GREEN">900%</Color> 속도로 작동하며 일반적으로 필요한 EU/t의 <Color id="RED">75%</Color>만 소비하고 <Color color="#ed6401">16</Color>개의 병렬 처리를 제공합니다.

<Color id="GREEN">AWD</Color>는 포장 및 포장 해제 레시피를 모두 처리할 수 있으며, 전반적으로 기존 단일블록 기계보다 __훨씬__ 빠릅니다.

<br clear="all"/>

> [!NOTE]
> 멀티블록에는 다음과 같은 변경 사항이 적용되었습니다(구조 제외):
> - 티어별 속도: 레시피 속도가 이제 아이템 파이프 케이싱 티어에 따라 200-900%까지 달라집니다(이전 최대치는 600%)

## 건설
<Color id="GREEN">AWD</Color>에는 티어별 부품이 하나 있습니다. 아이템 파이프 케이싱이 기계의 속도 보너스를 결정합니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 아무런 영향을 주지 않습니다. 버스/해치는 구조 어디에서든 임의의 케이싱을 대체할 수 있습니다. <Color id="RED">멀티 앰프 및 레이저 에너지 해치 </Color>는 지원되지 않지만, 오버클럭을 위해 일반 에너지 해치를 여러 개 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 하위 채널 "item_pipe"와 "glass"로 구조를 시각화/건설하면 해당 부품의 티어를 지정할 수 있습니다.

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15513" /> <ItemImage id="gregtech:gt.blockmachines:15513" />
- 4-15 <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" /> <ItemImage id="miscutils:gtplusplus.blockcasings.3:9" />
- 3 아이템 파이프 케이싱 <ItemImage id="gregtech:gt.blockcasings11:5" />
- 3 티어 유리(아무거나) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 2 <ItemLink id="gregtech:gt.blockframes:32" /> <ItemImage id="gregtech:gt.blockframes:32" />
- 1+ 에너지 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유:
<Color id="GREEN">AWD</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A 이상의 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계가 공유할 수 있습니다.

## 사용법
<Color id="GREEN">AWD</Color>는 단일블록 포장기 및 포장 해제기에서 직접 업그레이드된 기계입니다. 두 종류의 레시피를 모두 처리할 수 있고, 최대 <Color id="GREEN">900%</Color> 속도로 작동하며, 일반적으로 필요한 EU/t의 <Color id="RED">75%</Color>만 소비하고, 다음 표에서 볼 수 있듯이 전압 티어당 <Color color="#ed6401">16</Color>개의 병렬 처리를 제공합니다.
| 티어 | 아이템 파이프 케이싱 | 속도 |
| --------------- | --------------- | --------------- |
| 1 | 주석 | 200% |
| 2 | 황동 | 300% |
| 3 | 일렉트럼 | 400% |
| 4 | 백금 | 500% |
| 5 | 오스뮴 | 600% |
| 6 | 퀀티움 | 700% |
| 7 | 플럭스드 일렉트럼 | 800% |
| 8 | 블랙 플루토늄 | 900% |

----------


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |