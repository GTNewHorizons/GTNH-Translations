---
item_ids:
  - gregtech:gt.blockmachines:368
navigation:
  title: 대량 고형화기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:368
categories:
    - 새 멀티블록
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대량 고형화기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:368"/>
</GameScene>
<Color id="GREEN">대량 고형화기</Color>는 액체 금속을 주형에 주조하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">대량 고형화기</Color>는 단일블록 유체 고형화기의 직접적인 업그레이드로, 최대 <Color id="RED">300%</Color> 속도로 작동하고 일반적으로 필요한 EU/t의 <Color id="BLUE">80%</Color>만 사용하며 전압 티어당 <Color id="GREEN">10</Color>개의 병렬 처리를 제공합니다. 속도는 기계가 작동하는 동안 초당 5% 증가하고 비활성 상태에서는 초당 10% 감소합니다. 고형화기 해치 <ItemImage id="gregtech:gt.blockmachines:31781"/>에는 자체 해치의 유체에만 적용되는 주형을 위한 설정 가능한 고스트 슬롯이 있어 하나의 기계로 필요한 만큼 많은 레시피를 처리할 수 있습니다. <Color id="GREEN">대량 고형화기</Color>는 UEV에서 [엑소 주조소](../multis/exo_foundry.md)로 대체됩니다.

<br clear="all"/>

> [!NOTE]
> 다음 변경 사항이 멀티블록에 적용되었습니다(구조 제외):
> - 지원 중단: 기존 유체 성형기를 대체합니다.
> - 고형화기 해치: 유체를 받고 고스트 주형 슬롯이 있는 새로운 해치입니다.
> - 병렬 처리: "슬라이스"당 2 + 3개 대신 전압 티어당 10개의 병렬 처리를 제공합니다.

## 건설
<Color id="GREEN">대량 고형화기</Color>에는 하나의 티어 구성 요소가 있습니다. 유리는 에너지 해치의 최대 티어를 결정합니다. UEV 티어 유리는 모든 티어를 허용하여 사실상 제한을 제거합니다. 버스/해치는 구조상 어디서든 고형화기 케이싱을 대체할 수 있습니다. <Color id="RED">다중 앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 사용할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "glass"로 구조를 시각화/건설하여 유리의 티어를 지정하십시오.

<Color id="GREEN">대량 고형화기</Color>의 고유 기능은 <Color id="BLUE">고형화기 해치</Color> <ItemImage id="gregtech:gt.blockmachines:31781"/>로, 이는 주형을 위한 설정 가능한 고스트 슬롯이 있는 입력 해치입니다. 주형 슬롯을 Shift-클릭하면 사용 가능한 모든 옵션이 있는 메뉴가 열립니다. 주형은 입력 분리 설정과 관계없이 자체 해치에 있는 유체에만 적용됩니다. 고형화기 해치는 내부 용량을 늘리기 위해 네 가지 티어가 있으며 결국 제작 입력 버퍼로 대체됩니다.

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:368"/><ItemImage id="gregtech:gt.blockmachines:368"/>
- 24-73 <ItemLink id="gregtech:gt.blockcasings10:13"/><ItemImage id="gregtech:gt.blockcasings10:13"/>
- 42 티어 유리 <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 34 <ItemLink id="gregtech:gt.blockcasings10:14"/><ItemImage id="gregtech:gt.blockcasings10:14"/>
- 13 <ItemLink id="gregtech:gt.blockcasings:11"/><ItemImage id="gregtech:gt.blockcasings:11"/>
- 7 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1개 이상 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1개 정비 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">대량 고형화기</Color>는 각 면을 벽 공유하여 케이싱, 유리, 버스/해치를 절약할 수 있습니다. 어떤 레시피도 1A 이상의 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계가 공유할 수 있습니다.

## 사용법
<Color id="GREEN">대량 고형화기</Color>는 단일블록 유체 고형화기의 직접적인 업그레이드로, 최대 300% 속도로 작동하고 일반적으로 필요한 EU/t의 80%만 사용하며 다음 표에서 볼 수 있듯이 전압 티어당 10개의 병렬 처리를 제공합니다.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 |

<Color id="GREEN">대량 고형화기</Color>의 속도는 작동 중 초당 5% 증가하고 비활성 상태에서는 초당 10% 감소합니다. 즉, 최대 속도에 도달하는 데 40초의 실행 시간이 걸리지만, 잃는 데는 20초밖에 걸리지 않습니다. 부스트를 최대한 활용하려면 패턴을 복제하고 기계를 가능한 한 오래 작동시키는 것을 적극 권장합니다.