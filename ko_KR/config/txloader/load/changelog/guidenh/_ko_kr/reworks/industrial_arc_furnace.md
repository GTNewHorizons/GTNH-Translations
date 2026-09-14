---
item_ids:
  - gregtech:gt.blockmachines:15548
navigation:
  title: 산업용 아크 용광로
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15548
categories:
    - 구조 개편
author: Skorched
date: 2026-05-31
---

# 산업용 아크 용광로

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15548"/>
</GameScene>
<Color id="GREEN">산업용 아크 용광로 (IAF)</Color>는 전기 아크로 재료를 극한까지 가열하고 분해하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">IAF</Color>는 다양한 목적을 위한 여러 모드를 실행할 수 있고 최대 <Color id="RED">10배</Color>의 속도, 이중 완벽(8/4) 오버클럭, <Color id="BLUE">1024</Color> 병렬 처리를 제공하므로 단일블록 아크 용광로의 직접적인 업그레이드입니다. 본격적인 오버클럭을 위해 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>를 지원합니다. <Color id="GREEN">IAF</Color>는 대부분의 레시피에 플라즈마를 사용할 수도 있으며, 이는 단일블록 아크 용광로에서는 더 이상 사용할 수 없습니다.
<br clear="all"/>

> [!NOTE]
> 멀티블록에 다음과 같은 변경 사항이 적용되었습니다(구조물 제외):
> - 다양한 모드: "일반", EBF 모드(EBF 레시피 전력 16배), 광석 모드(화로 제련이 가능한 원광을 처리하여 용융 금속 생성)
> - 새로운 전극 메커니즘: IAF는 이제 기계의 능력치를 결정하는 전극 아이템을 요구합니다. 변경 사항이 포괄적이므로 자세한 내용은 아래를 참조하십시오.

## 건설
<Color id="GREEN">IAF</Color>에는 티어 구성 요소가 없습니다. 본격적인 오버클럭을 위해 다중 앰프 에너지 해치를 지원합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오.

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15548"/><ItemImage id="gregtech:gt.blockmachines:15548"/>
- 175 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 10-173 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 101 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 72 <ItemLink id="bartworks:bw.werkstoffblockscasing.01:32090"/><ItemImage id="bartworks:bw.werkstoffblockscasing.01:32090"/>
- 30 가열 코일 (아무거나) <ItemImage id="gregtech:gt.blockcasings5:13"/>
- 17 <ItemLink id="miscutils:miscutils.blockcasings:14"/><ItemImage id="miscutils:miscutils.blockcasings:14"/>
- 15 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 12 <ItemLink id="gregtech:gt.blockcasings13:2"/><ItemImage id="gregtech:gt.blockcasings13:2"/>
- 12 <ItemLink id="miscutils:miscutils.blockcasings:3"/><ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 1+ 에너지 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1 전극 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:14203" />
- 0+ 입력 버스 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:60" />
- 0+ 전극 감지 해치 (케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:14204" />


### 벽 공유
<Color id="GREEN">IAF</Color>는 각 면을 벽 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 전극마다 요구 암페어가 다를 수 있으므로 에너지 해치를 공유할 때는 주의해야 합니다.

## 사용법
<Color id="GREEN">IAF</Color>에는 아래에 설명된 3가지 작동 모드가 있습니다. 선택한 모드와 관계없이 <Color id="BLUE">시동 시간</Color>(일반 모드는 6초, 광석 모드는 10초)이 있으며, 아크 작업이 끝난 후 종료 단계가 있습니다. 속도, 병렬 처리, 오버클럭 및 전력 사용량은 전극 해치에 반드시 배치해야 하는 전극에 의해 결정됩니다. 사용 가능한 전극 중 일부는 특별 보너스를 가지고 있으므로, 선택에 도움이 되도록 NEI의 툴팁을 반드시 확인하십시오!

가동 시 아크 용광로는 처리를 시작하기 전에 아크를 점화해야 하며, 레시피가 완료된 후에는 6초의 종료 단계가 진행됩니다.

### 일반 모드:
<Color id="GREEN">IAF</Color>는 이 모드에서 재활용 레시피를 포함한 표준 아크 용광로 레시피를 처리합니다. 대부분의 일반 레시피는 선택적으로 플라즈마를 사용할 수도 있으며, 이는 단일블록 아크 용광로에서는 더 이상 불가능합니다.

### 제련 모드:
<Color id="GREEN">IAF</Color>는 이제 모든 EBF 레시피를 처리할 수 있지만, 전력 비용이 16배 듭니다. 전력에 여유가 있다면 EBF의 부담을 일부 덜어줄 수 있습니다.

### 광석 모드:
<Color id="GREEN">IAF</Color>는 이 모드를 사용하여 광석과 원광을 직접 용융 금속으로 처리할 수 있습니다. 이는 입력 광석이 화로에서 직접 제련될 수 있는 경우에만 작동합니다(예를 들어 처리 라인이나 EBF가 필요하지 않음).

이 모드에서 시동 시간은 10초입니다. 모든 입력 버스에서 모든 광석과 원광을 소비합니다. 대기 중인 광석 양이 용량을 초과하면 시동 단계가 즉시 종료됩니다. 5틱 동안 광석이 입력되지 않으면 시동도 즉시 종료됩니다.

## 전극 유지보수
공정이 발생할 때마다 전극 해치의 전극이 손상됩니다. 전극은 전극 해치에 삽입되며, 전극을 꺼내거나 교체하면 기계의 전원이 차단됩니다. 여기에는 0틱 교체도 포함되므로, 전극을 교체하려면 기계의 전원을 내려야 합니다.

- 내구도가 30% 미만이면 5% 확률로 무작위 아크 서지가 발생합니다(아크를 다시 시작함)
- 내구도가 10% 미만이면 2% 확률로 아크 안의 아이템이 소멸합니다

따라서 받은 손상에 따라 전극 교체를 자동화하는 것이 필수적입니다. 이 자동화는 전극 감지 해치를 사용하여 도움을 받을 수 있으며, 이 해치는 내구도를 감지하고 GUI에서 설정 가능한 임계값에서 레드스톤 신호를 출력합니다.

<Color id="GREEN">IAF</Color>는 티어 건너뛰기를 __할 수 없습니다__. 가동 시 기계는 $$\text{MaxParallels} \times \text{AmpsPerParallel} \times (1+\text{SurgePenalty})$$ 암페어를 소비하며, 이는 전극에 따라 상당히 높을 수 있습니다!