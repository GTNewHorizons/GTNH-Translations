---
item_ids:
  - gregtech:gt.blockmachines:15516
navigation:
  title: 메가 증류탑
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15516
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 메가 증류탑

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15516"/>
</GameScene>
<Color id="GREEN">메가 증류탑 (MDT)</Color>은 유체를 모든 구성 분획으로 동시에 대량 증류하거나, 단일 분획을 증가된 속도로 증류하기 위한 LuV 티어 멀티블록입니다. 이 구조는 중앙의 거대한 탑과 그 옆의 파이프로 이루어져 있으며, 구조에 "조각"을 추가하여 높이를 늘릴 수 있습니다. 증류탑 모드일 경우 출력 순서는 레시피의 NEI 미리보기를 따르며, 출력 수가 구조의 최소 높이를 결정합니다. <Color id="GREEN">MDT</Color>는 증류탑 <ItemImage id="gregtech:gt.blockmachines:1126"/>의 직접적인 업그레이드입니다. 탑 모드에서 최대 256 병렬, 증류기 모드에서 1024 병렬을 제공하고, 본격적인 오버클럭을 위한 <Color id="GREEN">멀티 앰프 및 레이저 에너지 해치</Color>를 지원하며, 무제한 티어 건너뛰기를 갖기 때문입니다. 
<br clear="all"/>

> [!NOTE]
> 구조를 제외하고 멀티블록에 다음 변경 사항이 적용되었습니다:
> 증류기 및 증류탑 모드를 모두 지원합니다
> 증류탑 모드: 동일 병렬(256), 120% 속도, 90% EU 사용량
> 증류기 모드: $$256 \times (1 + \text{Tower Height} \div 2)$$ 병렬, 150% 속도, 50% EU 사용량
> 나콰다 처리로 LuV 티어에 제한됩니다
> 구조의 일부로 추가할 수 있는 "조각"이 있어 크기가 가변적입니다

## 건설
<Color id="GREEN">MDT</Color>에는 티어별 구성 요소가 없습니다. 높이는 추가된 출력 조각 수에 따라 30-54블록 높이입니다. 구조는 자연스럽게 5개 구역으로 나뉘며, 모두 필수입니다. 구조의 바닥에는 컨트롤러가 배치되며, 입력 버스, 유지보수 해치, 에너지 해치를 배치해야 합니다. 구조의 왼쪽에는 작은 청동 "출력 파이프"가 있으며, 여기에 입력 해치를 배치해야 합니다. 구조의 반대쪽에는 유사한 강철 파이프가 있으며, 여기에 출력 버스를 배치합니다. 강철 입력 파이프 위에는 응축기 탑이 있으며, 출력 해치용 슬롯이 있습니다(추가된 조각 수에 따라 3-11개). 마지막으로, 구조의 주요 비용은 탑 자체에 있으며, 이곳에는 어떤 종류의 해치나 버스도 놓을 공간이 없습니다.

## 기본 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15516"/><ItemImage id="gregtech:gt.blockmachines:15516"/>
- 361 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 215 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 179 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 100-166 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 99 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 80-81 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 43-44 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 41 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 1+ 에너지 해치(모든 나콰다 중앙 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(모든 중앙 나콰다 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ 입력 버스(모든 중앙 나콰다 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0-1 입력 해치(왼쪽의 청동 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0-1 출력 버스(오른쪽의 강철 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:80" />
- 3 출력 해치(오른쪽의 청동 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:60" />

## 조각당 요구 사항:
- 57 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 48 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 32 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 27 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 16 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 16 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1 출력 해치(오른쪽의 청동 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:60" />

## 최대 크기 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15516"/><ItemImage id="gregtech:gt.blockmachines:15516"/>
- 553 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 443 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 307 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 164-230 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 207 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 135-136 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 66-67 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 41 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 1+ 에너지 해치(모든 나콰다 중앙 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(모든 중앙 나콰다 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ 입력 버스(모든 중앙 나콰다 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0-1 입력 해치(왼쪽의 청동 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0-1 출력 버스(오른쪽의 강철 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:80" />
- 11 출력 해치(오른쪽의 청동 파이프 케이싱을 대체합니다) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">MDT</Color>들은 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 이 구조는 공유하기 다소 어색하며, 수직으로 벽 공유하지 않는 한 절약 효과는 미미합니다. 수직으로 공유하면 전체 구조가 105블록 높이가 됩니다.

## 사용법
<Color id="GREEN">MDT</Color>는 이제 아래에 설명된 두 가지 모드를 제공합니다:

### 증류탑 모드:
이 모드에서 <Color id="GREEN">MDT</Color>는 일반 증류탑과 유사하게 유체를 모든 구성 분획으로 동시에 증류합니다. 각 분획은 레시피의 NEI 미리보기에 따라 구조의 서로 다른 층에서 출력됩니다. 순서는 왼쪽에서 오른쪽, 아래에서 위입니다. 예를 들어 석유를 증류할 때 출력 순서는 황산 중질 연료, 황산 경질 연료, 황산 나프타, 황산 가스입니다. 이 모드에서 기계는 256 병렬, 일반 증류탑 대비 120% 속도, EU 사용량의 90%를 얻습니다.

### 증류기 모드:
이 모드에서 <Color id="GREEN">MDT</Color>는 하나의 입력과 하나의 출력으로 일반 증류 레시피를 실행합니다. 입력에 대한 출력은 컨트롤러 또는 입력 버스에 필요한 출력에 해당하는 프로그래밍된 회로를 제공하여 지정됩니다. 이 모드를 사용하면 150% 속도, EU 사용량의 50%를 얻습니다. 맨 아래 출력 해치만 사용되더라도 구조가 형성되려면 모든 해치가 반드시 있어야 한다는 점에 유의하십시오. 이 기계로 얻는 병렬 수는 다음과 같습니다.
<Latex formula="256 \times \Biggl( 1+\frac{\text{Tower Height}}{2} \Biggr)"/>
여기서 "Tower Height"는 구조에 있는 조각의 수입니다(맨 위 조각은 포함하지 않습니다). 구조 높이에 따라 512-1024 병렬 범위를 제공합니다.