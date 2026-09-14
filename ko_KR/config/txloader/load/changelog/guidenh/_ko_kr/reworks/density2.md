---
item_ids:
  - gregtech:gt.blockmachines:15547
navigation:
  title: 밀도^2
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15547
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 밀도^2

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15547"/>
</GameScene>
<Color id="GREEN">밀도^2</Color>는 폭발물로 판과 분진을 압축하는 IV 티어 멀티블록입니다. <Color id="GREEN">밀도^2</Color>는 200% 속도로 작동하고, 오염을 절반만 배출하며, 전압 티어 두 개마다 병렬 처리 하나를 제공하므로 내파 압축기 <ItemImage id="gregtech:gt.blockmachines:1001"/>의 직접적인 업그레이드입니다. <Color id="GREEN">밀도^2</Color>는 UHV 티어에서 [전기 내파 압축기](./eic.md) <ItemImage id="gregtech:gt.blockmachines:15563"/>로 대체됩니다. 
<br clear="all"/>

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일합니다

## 건설
<Color id="GREEN">밀도^2</Color>에는 티어별 부품이 없습니다. 버스/해치는 구조물 어디에서든 모든 텅스텐강 기계 케이싱을 대체할 수 있습니다. <Color id="RED">다중 앰프 및 레이저 에너지 해치</Color>는 지원되지 않습니다. 하지만 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설하십시오. 

### 요구 사항:
- <ItemLink id="gregtech:gt.blockmachines:15547"/><ItemImage id="gregtech:gt.blockmachines:15547"/> 1개
- <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/> 80개
- <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/> 50-60개
- <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/> 24개
- <ItemLink id="gregtech:gt.sheetmetal:86"/><ItemImage id="gregtech:gt.sheetmetal:86"/> 4개
- <ItemLink id="gregtech:gt.blockframes:86"/><ItemImage id="gregtech:gt.blockframes:86"/> 4개
- 에너지 해치 1개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 출력 버스 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">밀도^2 기계들</Color>은 케이싱, 프레임 박스, 정제 흑연 블록, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 단, 흑연 구체 전체는 포함되지 않습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나의__</u> 에너지 해치를 <u>__두__</u> 기계 사이에서 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">밀도^2</Color>는 오염을 절반만 배출하고, 두 배 빠르게 작동하며, 다음 표에서 볼 수 있듯이 전압 티어 두 개마다 병렬 처리 하나를 제공하므로 내파 압축기 <ItemImage id="gregtech:gt.blockmachines:1001"/>의 직접적인 업그레이드입니다.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 7 | 7 | 8 | 8 |


내파 압축기 레시피는 모두 LV이며, 아래 나열된 폭발물 중 하나를 필요로 합니다. 폭발물의 수량은 종류와 레시피에 따라 달라집니다. 화약통은 다른 것들보다 훨씬 많은 수량이 필요하지만, 화약은 탄소, 황, 초석으로 매우 쉽게 제작할 수 있습니다. TNT와 산업용 TNT는 대부분 목타르 및/또는 중질 연료를 증류하여 얻는 톨루엔입니다. 다이너마이트는 대부분 글리세롤로, 씨앗/생선 기름에서 얻을 수 있는 재생 가능 자원입니다. 하지만 가장 좋고 가장 재생 가능한 방법은 폭발성 꿀벌을 사용하여 산업용 TNT를 대량으로 직접 자동 생성하는 것입니다 -- 화학 공정이 필요하지 않습니다.

- 화약통
- TNT
- 다이너마이트
- 산업용 TNT