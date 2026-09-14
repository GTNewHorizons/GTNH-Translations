---
item_ids:
  - gregtech:gt.blockmachines:28055
navigation:
  title: 산업 농장
  parent: crops.md
  icon: gregtech:gt.blockmachines:28055
categories:
    - 작물
    - 신규 멀티블록
author: Skorched
date: 2026-05-24
---

# 산업 농장
게임을 어느 정도 진행하다 보면, 기존의 작은 작물 관리기들을 한계까지 밀어붙이려 할 때 버거워지기 시작합니다. CropsNH는 자체적인 해결책인 <Color id="GREEN">산업 농장</Color>을 제공합니다.

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:28055" />
</GameScene>
<Color id="GREEN">산업 농장</Color>은 작물의 대량 재배 및 수확을 위한 MV 티어 멀티블록입니다. <Color id="GREEN">산업 농장</Color>은 한 번에 한 종류의 작물만 재배할 수 있지만, 수용량은 씨앗 재배대의 티어와 기계 길이에 따라 크게 증가합니다. <Color id="GREEN">산업 농장</Color>은 기계 내부의 작물 성장을 마치 세계에 실제로 설치된 것처럼 시뮬레이션합니다. 유일한 입력은 물, 전력이며, 비료 유닛이 설치되어 있다면 비료가 추가될 수 있습니다. 출력은 작물의 평균 능력치, 환경 보너스, 업그레이드 유닛 보너스에 따라 조정됩니다. 선택할 수 있는 5가지 고유 업그레이드 유닛이 있고 기계 길이에 따라 1-12개의 업그레이드 슬롯이 있지만, 유닛의 티어는 씨앗 재배대의 티어와 정확히 일치해야 합니다. 
<br clear="all"/>
## 건설:
<Color id="GREEN">산업 농장</Color>의 길이는 씨앗 재배대의 티어에 따라 3-14블록입니다. 업그레이드 유닛은 구조물 최상층의 목재 프레임 박스에만 설치할 수 있으며, 씨앗 재배대의 티어와 정확히 일치해야 합니다. 버스/해치는 구조물 양 끝 중앙의 벽돌 농업용 케이싱에만 설치할 수 있습니다. 유리는 에너지 해치의 최대 티어를 결정합니다. 레이저 에너지 해치는 지원되지 않지만, 오버클럭된 성장 가속 유닛이 있다면 여러 개의 다중 앰프 에너지 해치를 사용할 수 있습니다. 그렇지 않으면 필요에 따라 여러 개의 일반 에너지 해치를 사용할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 하위 채널 "if_tier"와 "glass"로 구조물을 시각화/건설하십시오. 이들은 각각 기계의 티어와 유리의 티어를 지정합니다. 하위 채널 "if_upgrade"가 1로 설정되지 않으면 업그레이드 유닛은 자동 배치되지 않습니다.

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:28055" /> <ItemImage id="gregtech:gt.blockmachines:28055" />
- 26-48 <ItemLink id="cropsnh:cropsnh.casings1" /> <ItemImage id="cropsnh:cropsnh.casings1" />
- 4-48 티어별 유리 <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 3-36 씨앗 재배대(티어별) <ItemImage id="cropsnh:cropsnh.seedBed:2" />
- 1-12 <ItemLink id="gregtech:gt.blockframes:809" /> <ItemImage id="gregtech:gt.blockframes:809" />
- 0-12 업그레이드 유닛(목재 프레임 박스 아무거나) <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" />
- 1+ 에너지 해치(케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1+ 입력 버스(케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ 입력 해치(케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ 출력 버스(케이싱 아무거나) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유:
<Color id="GREEN">산업 농장</Color>은 케이싱, 유리, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 최상층을 바로 위에 거꾸로 놓인 다른 산업 농장과 겹치게 하는 것이 가장 효과적이며 강력히 권장됩니다. 이는 업그레이드 유닛 세트 전체를 공유하기 때문입니다. 

## 사용법:
> [!WARNING]
> 이 섹션은 수학 비중이 비교적 높지만, 직접 계산할 필요가 없다면 각 항목이 어떻게 측정되는지 대략적으로 이해하는 데 본문을 사용할 수 있습니다

<Color id="GREEN">산업 농장</Color>은 티어나 길이에 관계없이 고정된 5초 주기로 작동합니다. 각 주기 시작 시 <Color id="GREEN">산업 농장</Color>은 입력 해치에서 물을 소비하며, 비료 유닛이 있다면 입력 버스에서 비료를 소비할 수 있습니다. 소비량은 아래 방정식에서 볼 수 있듯 기계의 총 씨앗 수용량에 따라 달라집니다. 기계 안에 실제로 몇 개의 씨앗이 들어 있는지는 중요하지 않습니다. 
<Latex formula="\text{Water/Cycle (L) = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil" />
<Latex formula="\text{Fertilizer/Cycle (L)} = \lceil \text{Seed Capacity} \times 2^{\text{OC}} \times \frac{100}{256} \rceil "/>

<Color id="GREEN">산업 농장</Color>은 내부 작물의 성장을 시뮬레이션하고 평균 결과를 조정합니다. 실제 세계의 작물과 동일한 모든 방정식을 사용하지만, 수분 보너스와 하늘 보너스는 둘 다 자동으로 최대치가 됩니다. 직접적인 하늘 노출이 필요하지 않으며 날씨도 고려하지 않습니다. 먼저 모든 환경 보너스를 합산하여 작물의 영양 값을 구하십시오. 
<Latex scale="0.8" formula="\text{Humidity Bonus} = \text{Max} \Bigg( 0,\text{ Min} \Bigg( 1,\frac{\text{Biome Humidity\%} - 0.5}{0.3 }\Bigg)\Bigg) \times 14"/>

<Latex scale="0.8" formula="\text{Biome Bonus} = \text{Min}(2\text{, Biome Preferences Met}) \times 14"/>
<Latex scale="0.8" formula="\text{Nutrients} = 17.9 + \text{Fertilization Bonus} + \text{Max}(\text{Humidity Bonus, Biome Bonus})" />

> [!NOTE]
> <Color id="GREEN">비료 보너스 </Color>는 비료를 주지 않으면 1이고, 비료를 주면 1.5입니다

다음으로 성장 속도와 성장 배율로부터 작물의 전체 성장률을 계산합니다. 이는 주로 영양 값과 작물의 평균 능력치에 따라 달라지며, 아래 방정식과 같습니다. 비료 유닛은 위의 비료 보너스에 더해 성장 배율을 50% 증가시킨다는 점에 유의하십시오. 이론상 작물이 5초 이내에 더 성장할 수 있더라도 주기당 최대 성장률은 100%입니다. 
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients} \geq \text{Crop Tier} \times 2) = \frac{(6 + \text{Crop Growth}) \times (100 + \text{Nutrients} - 10 \times \text{Crop Tier})}{100}" />
<Latex scale="0.65" formula="\text{Growth Speed} (\text{Nutrients}< \text{Crop Tier} \times 2) = \text{Max}\Biggl(0,\frac{(6 + \text{Crop Growth}) \times (100 + 4 \times (\text{Nutrients} - 10 \times \text{Crop Tier}))}{100}\Biggr)" />
<Latex scale="0.65" formula="\text{Growth Mult} = (1 + \text{Growth Acceleration Units}) \times {\text{Fertilization Bonus}} \times 2^{\text{OC}}" />

> [!NOTE]
> $$\text{OC}$$ here refers to the amount of overclocks

<Latex scale="0.65" formula="\text{Growth\%} = \text{Min} \Bigg( 1, \frac{1}{\lceil \text{Crop Growth Points} \div (\text{Growth Speed} \times \text{Growth Mult} \times (100 \div 256)) \rceil} \Bigg)" />

마지막으로 가산 보너스와 배율 보너스로부터 전체 출력을 계산합니다. 이는 주로 작물의 평균 능력치에 따라 달라지며, 비료 유닛에 의해 다시 한 번 증가합니다. 여기에서 씨앗 재배대 보너스와 고급 수확 유닛 보너스도 적용됩니다.

<Latex scale="0.60" formula="\text{Additive Bonus} = 0.01 \times (\text{Crop Gain} + 1)" />
<Latex scale="0.60" formula="\text{Mult Bonus} = (\text{Crop Drop Rate})^{\text{Crop Tier}} \times 1.03^{\text{Crop Gain}} \times (1 + \text{Seed Bed Bonus} + 0.5_{\text{fertilizer}}) \times (1 + 0.2 \times \text{Harvesting Units})"/>
<Latex scale="0.60" formula="\text{Output} = (\text{Output Stack Size} + \text{Additive Bonus})\times \text{Output Base Chance} \times \text{Mult Bonus} \times \text{Growth}\%" />

## 업그레이드 유닛:
<Color id="GREEN">산업 농장</Color>에는 작물 성장 속도와 기계 전반의 성능을 향상시키기 위한 다양한 업그레이드 유닛을 장착할 수 있습니다. 선택할 수 있는 5가지 고유 업그레이드 유닛이 있으며, 구조물 최상층의 목재 프레임 박스에만 설치할 수 있으므로 기계 길이에 따라 1-12개의 업그레이드 슬롯이 있습니다. 업그레이드 유닛의 티어는 씨앗 재배대의 티어와 정확히 일치해야 합니다. 
- <ItemImage id="cropsnh:cropsnh.advancedHarvestingUnit:2" /> __고급 수확 유닛(MV+)__: 이 유닛은 유닛당 드롭량을 +20%, 전력 소비를 +50% 증가시킵니다. 더 높은 티어의 유닛도 정확히 같은 이점을 제공합니다. 구조물당 고급 수확 유닛은 2개만 설치할 수 있습니다
- <ItemImage id="cropsnh:cropsnh.fertilizerUnit:2" /> __비료 유닛(MV+)__: 이 유닛은 <Color id="GREEN">산업 농장</Color>이 출력 생산을 높이기 위해 각 주기 시작 시 항상 <Color id="GREEN">농축 비료</Color>를 소비하도록 합니다. 또한 기계에서 아이템 비료를 사용할 수 없게 만듭니다. 이는 성장 속도를 x1.5, 드롭 수를 +50%, 전력 소비를 +50% 증가시키지만, 농축 비료가 떨어지면 처리를 중단합니다. 더 높은 티어의 유닛도 정확히 같은 이점을 제공하지만 주기당 더 많은 농축 비료를 요구합니다. 구조물당 비료 유닛은 1개만 설치할 수 있습니다
- <ItemImage id="cropsnh:cropsnh.environmentalEnhancementUnit:2" /> __환경 강화 유닛(MV+)__: 이 유닛은 컨트롤러 GUI에 환경 모듈 슬롯을 해금하고 유닛당 전력 소비를 +50% 증가시킵니다. 환경 모듈은 기계 내부의 시뮬레이션된 온도 및/또는 바이옴을 변경하여 작물에 이상적인 재배 조건을 제공합니다. 더 높은 티어의 유닛도 정확히 같은 이점을 제공합니다. 구조물당 환경 강화 유닛은 2개만 설치할 수 있습니다
- <ItemImage id="cropsnh:cropsnh.growthAccelerationUnit:2" /> __성장 가속 유닛(MV+)__: 이 유닛은 유닛당 작물 성장 속도를 +100%, 전력 소비를 +125% 증가시킵니다. 이 유닛은 오버클럭된 성장 가속 유닛과 호환되지 않으며, 더 높은 티어의 유닛도 정확히 같은 이점을 제공합니다. 구조물당 성장 가속 유닛의 수에는 제한이 없습니다
- <ItemImage id="cropsnh:cropsnh.overclockedGrowthAccelerationUnit:7" /> __오버클럭된 성장 가속 유닛(ZPM+)__: 이 유닛은 <Color id="RED">다중 앰프 에너지 해치</Color>를 사용할 수 있는 능력을 해금하고, <Color id="GREEN">산업 농장</Color>이 다른 멀티블록처럼 충분한 전력으로 오버클럭될 수 있게 합니다. 기본 전압은 씨앗 재배대의 티어에 따라 달라집니다. 각 오버클럭은 기본 주기 시간에 영향을 주지 않고 출력 생산량, 물 소비량, 비료 소비량을 두 배로 만듭니다. 이 유닛은 성장 가속 유닛과 호환되지 않으며, 더 높은 티어의 유닛도 정확히 같은 이점을 제공합니다. 구조물당 오버클럭된 성장 가속 유닛은 1개만 설치할 수 있습니다.