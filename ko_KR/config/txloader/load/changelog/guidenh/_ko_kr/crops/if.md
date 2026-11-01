---
item_ids:
  - gregtech:gt.blockmachines:28055
navigation:
  title: 산업용 농장
  parent: crops.md
  icon: gregtech:gt.blockmachines:28055
categories:
    - 작물
    - 새로운 다중블록
author: Skorched
date: 2026-05-24
---

# 산업용 농장
게임을 진행하다 보면, 작물 관리 장치들을 한계까지 몰아붙일 경우 성능이 버거워지기 시작합니다. CropsNH에서는 이에 대한 해결책으로 <Color id="GREEN">산업용 농장</Color>을 제공합니다.

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:28055" />
</GameScene>
<Color id="GREEN">산업용 농장</Color>은 작물을 대량으로 재배하고 수확하기 위한 MV 티어 다중블록입니다. <Color id="GREEN">산업용 농장</Color>은 한 번에 한 종류의 작물만 재배할 수 있지만, 모판의 티어와 기계의 길이에 따라 용량이 크게 증가합니다. <Color id="GREEN">산업용 농장</Color>은 실제 세계에 작물을 심은 것처럼 내부에서 작물의 성장을 시뮬레이션합니다. 물과 전력만 입력하면 되며, 시비 유닛이 설치되어 있다면 비료도 필요할 수 있습니다. 출력량은 작물의 평균 능력치와 환경 보너스, 업그레이드 유닛 보너스에 따라 달라집니다. 선택할 수 있는 업그레이드 유닛은 5종이며, 기계 길이에 따라 업그레이드 슬롯이 1~12개 제공됩니다. 단, 유닛의 티어는 모판의 티어와 정확히 일치해야 합니다.
<br clear="all"/>
## 건설:
<Color id="GREEN">산업용 농장</Color>의 길이는 모판의 티어에 따라 3~14블록입니다. 업그레이드 유닛은 구조물 최상층의 목재 프레임 상자에만 설치할 수 있으며, 유닛의 티어는 모판의 티어와 정확히 일치해야 합니다. 버스와 해치는 구조물 양 끝 중앙에 있는 벽돌 농업용 케이싱에만 설치할 수 있습니다. 유리의 티어에 따라 에너지 해치의 최대 티어가 결정됩니다. 레이저 에너지 해치는 지원되지 않지만, 오버클럭 성장 가속 유닛이 있으면 멀티 앰프 에너지 해치를 여러 개 설치할 수 있습니다. 그 외의 경우에는 필요에 따라 일반 에너지 해치를 여러 개 설치할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" />를 사용하면 구조물을 미리 보거나 건설할 수 있습니다. 하위 채널 "if_tier"와 "glass"를 사용해 각각 기계의 티어와 유리의 티어를 지정하십시오. 하위 채널 "if_upgrade"를 1로 설정하지 않으면 업그레이드 유닛은 자동으로 배치되지 않습니다.

### 필요 재료:
- 1 <ItemLink id="gregtech:gt.blockmachines:28055" /> <ItemImage id="gregtech:gt.blockmachines:28055" />
- 26-48 <ItemLink id="cropsnh:cropsnh.casings1" /> <ItemImage id="cropsnh:cropsnh.casings1" />
- 4-48 티어별 유리 <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 3-36 모판 (티어별) <ItemImage id="cropsnh:cropsnh.seedBed:2" />
- 1-12 <ItemLink id="gregtech:gt.blockframes:809" /> <ItemImage id="gregtech:gt.blockframes:809" />
- 0-12 업그레이드 유닛 (목재 프레임 상자 아무거나) <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" />
- 1개 이상 에너지 해치 (케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1개 이상 입력 버스 (케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1개 이상 입력 해치 (케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1개 이상 출력 버스 (케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유:
<Color id="GREEN">산업용 농장</Color>은 케이싱과 유리, 버스 및 해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 가장 효율적이고 적극 권장하는 방법은 다른 구조물을 바로 위에 거꾸로 겹쳐 최상층을 공유하는 것입니다. 이렇게 하면 업그레이드 유닛 한 세트를 통째로 공유할 수 있습니다.

## 사용법:
> [!WARNING]
> 이 항목에는 계산이 다소 많이 포함되어 있지만, 직접 계산할 필요가 없다면 각 요소를 어떻게 측정하는지 대략적으로 파악하는 데 활용할 수 있습니다.

<Color id="GREEN">산업용 농장</Color>은 티어나 길이에 관계없이 고정된 5초 주기로 작동합니다. 각 주기가 시작될 때 <Color id="GREEN">산업용 농장</Color>은 입력 해치에서 물을 소모하며, 시비 유닛이 설치되어 있다면 입력 버스에서 비료도 소모할 수 있습니다. 소모량은 다음 식에 나와 있듯이 기계의 총 씨앗 수용량에 따라 달라집니다. 기계 내부에 실제로 씨앗이 몇 개 들어 있는지는 관계없습니다.
<Latex formula="\text{Water/Cycle (L) = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil" />
<Latex formula="\text{Fertilizer/Cycle (L)} = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil "/>

<Color id="GREEN">산업용 농장</Color>은 내부 작물의 성장을 시뮬레이션하고 평균 결과를 반영합니다. 물리적인 세계에서 작물을 재배할 때와 같은 식을 사용하지만, 수분 보너스와 하늘 보너스는 모두 자동으로 최댓값이 적용됩니다. 하늘에 직접 노출될 필요가 없으며 날씨도 영향을 주지 않습니다. 먼저 여러 환경 보너스를 모두 더해 작물의 영양분 값을 구합니다.
<Latex scale="0.8" formula="\text{Humidity Bonus} = \text{Max} \Bigg( 0,\text{ Min} \Bigg( 1,\frac{\text{Biome Humidity\%} - 0.5}{0.3 }\Bigg)\Bigg) \times 14"/>

<Latex scale="0.8" formula="\text{Biome Bonus} = \text{Min}(2\text{, Biome Preferences Met}) \times 14"/>
<Latex scale="0.8" formula="\text{Nutrients} = 17.9 + \text{Fertilization Bonus} + \text{Max}(\text{Humidity Bonus, Biome Bonus})" />

> [!NOTE]
> <Color id="GREEN">시비 보너스</Color>는 비료를 사용하지 않을 때 1, 사용하면 1.5입니다.

다음으로 성장 속도와 성장 배율을 사용해 작물의 전체 성장률을 계산합니다. 다음 식에서 볼 수 있듯이, 이 값은 주로 영양분 값과 작물의 평균 능력치에 따라 달라집니다. 시비 유닛은 위의 시비 보너스에 더해 성장 배율을 50% 높입니다. 작물이 이론상 5초 이내에 더 자랄 수 있더라도, 주기당 최대 성장률은 100%입니다.
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients} \geq \text{Crop Tier} \times 2) = \frac{(6 + \text{Crop Growth}) \times (100 + \text{Nutrients} - 10 \times \text{Crop Tier})}{100}" />
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients}< \text{Crop Tier} \times 2) = \text{Max}\Biggl(0,\frac{(6 + \text{Crop Growth}) \times (100 + 4 \times (\text{Nutrients} - 10 \times \text{Crop Tier}))}{100}\Biggr)" />
<Latex scale="0.65" formula="\text{Growth Mult} = (1 + \text{Growth Acceleration Units}) \times {\text{Fertilization Bonus}} \times 2^{\text{OC}}" />

> [!NOTE]
> 여기서 $$\text{OC}$$는 오버클럭 횟수를 뜻합니다.

<Latex scale="0.65" formula="\text{Growth\%} = \text{Min} \Bigg( 1, \frac{1}{\lceil \text{Crop Growth Points} \div (\text{Growth Speed} \times \text{Growth Mult} \times (100 \div 256)) \rceil} \Bigg)" />

마지막으로 가산 보너스와 배율 보너스를 사용해 전체 출력량을 계산합니다. 이 값은 주로 작물의 평균 능력치에 따라 달라지며, 시비 유닛으로 더욱 증가합니다. 이 단계에서 모판 보너스와 고급 수확 유닛 보너스도 적용됩니다.

<Latex scale="0.60" formula="\text{Additive Bonus} = 0.01 \times (\text{Crop Gain} + 1)" />
<Latex scale="0.60" formula="\text{Mult Bonus} = (\text{Crop Drop Rate})^{\text{Crop Tier}} \times 1.03^{\text{Crop Gain}} \times (1 + \text{Seed Bed Bonus} + 0.5_{\text{fertilizer}}) \times (1 + 0.2 \times \text{Harvesting Units})"/>
<Latex scale="0.60" formula="\text{Output} = (\text{Output Stack Size} + \text{Additive Bonus})\times \text{Output Base Chance} \times \text{Mult Bonus} \times \text{Growth}\%" />

## 업그레이드 유닛:
<Color id="GREEN">산업용 농장</Color>에는 작물의 성장률과 기계의 전체 성능을 높이는 다양한 업그레이드 유닛을 장착할 수 있습니다. 선택할 수 있는 유닛은 5종이며, 구조물 최상층의 목재 프레임 상자에만 설치할 수 있으므로 기계 길이에 따라 업그레이드 슬롯이 1~12개 제공됩니다. 업그레이드 유닛의 티어는 모판의 티어와 정확히 일치해야 합니다.
- <ItemImage id="cropsnh:cropsnh.advancedHarvestingUnit:2" /> __고급 수확 유닛 (MV+)__: 유닛 하나당 드롭량이 +20%, 전력 소비량이 +50% 증가합니다. 더 높은 티어의 유닛도 효과는 동일합니다. 구조물 하나에 고급 수확 유닛을 최대 2개까지 설치할 수 있습니다.
- <ItemImage id="cropsnh:cropsnh.fertilizerUnit:2" /> __시비 유닛 (MV+)__: 이 유닛을 사용하면 <Color id="GREEN">산업용 농장</Color>은 출력 생산량을 높이기 위해 매 주기가 시작될 때마다 <Color id="GREEN">농축 비료</Color>를 소모해야 합니다. 또한 기계에서 아이템 형태의 비료를 사용할 수 없게 됩니다. 성장 속도가 1.5배, 드롭량이 +50%, 전력 소비량이 +50% 증가하지만, 농축 비료가 떨어지면 작동이 중단됩니다. 더 높은 티어의 유닛도 효과는 동일하지만 주기마다 더 많은 농축 비료를 소모합니다. 구조물 하나에 시비 유닛을 1개만 설치할 수 있습니다.
- <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" /> __환경 개선 유닛 (MV+)__: 이 유닛은 컨트롤러 GUI에 환경 모듈 슬롯을 추가하고, 유닛 하나당 전력 소비량을 +50% 증가시킵니다. 환경 모듈은 기계 내부에서 시뮬레이션되는 온도 및/또는 생물 군계를 바꾸어 작물이 최적의 조건에서 자라도록 합니다. 더 높은 티어의 유닛도 효과는 동일합니다. 구조물 하나에 환경 개선 유닛을 최대 2개까지 설치할 수 있습니다.
- <ItemImage id="cropsnh:cropsnh.growthAccelerationUnit:2" /> __성장 가속 유닛 (MV+)__: 이 유닛은 작물의 성장 속도를 +100%, 전력 소비량을 유닛 하나당 +125% 증가시킵니다. 오버클럭 성장 가속 유닛과 함께 사용할 수 없습니다. 더 높은 티어의 유닛도 효과는 동일합니다. 구조물 하나에 설치할 수 있는 성장 가속 유닛의 수에는 제한이 없습니다.
- <ItemImage id="cropsnh:cropsnh.overclockedGrowthAccelerationUnit:7" /> __오버클럭 성장 가속 유닛 (ZPM+)__: 이 유닛을 설치하면 <Color id="RED">멀티 앰프 에너지 해치</Color>를 사용할 수 있으며, 다른 다중블록과 마찬가지로 충분한 전력이 있을 때 <Color id="GREEN">산업용 농장</Color>을 오버클럭할 수 있습니다. 기본 전압은 모판의 티어에 따라 달라집니다. 오버클럭할 때마다 기본 주기 시간은 그대로 유지하면서 출력 생산량, 물 소모량, 비료 소모량이 두 배로 증가합니다. 성장 가속 유닛과 함께 사용할 수 없습니다. 더 높은 티어의 유닛도 효과는 동일합니다. 구조물 하나에 오버클럭 성장 가속 유닛을 1개만 설치할 수 있습니다.