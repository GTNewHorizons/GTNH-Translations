---
item_ids:
  - gregtech:gt.blockmachines:15555
navigation:
  title: 산업용 대형 망치
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15555
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---
# 산업용 대형 망치

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15555"/>
</GameScene>
<Color id="GREEN">산업용 대형 망치</Color>는 모루에서 금속을 단조하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">산업용 대형 망치</Color>는 단일블록 단조 망치와 증기 압착기 <ItemImage id="gregtech:gt.blockmachines:31083"/>의 직접적인 상위 버전입니다. 200% 속도로 작동하고 $$\text{전압 티어} \times \text{솔레노이드 티어} \times 6$$ 병렬 처리를 제공하기 때문입니다(최대 1,080). 

<br clear="all"/>

> [!NOTE]
> 다음 변경 사항은 (구조를 제외하고) 멀티블록에 적용되었습니다:

## 건설
<Color id="GREEN">산업용 대형 망치</Color>에는 티어가 있는 구성 요소가 하나 있습니다. 솔레노이드 코일이 총 병렬 처리 수를 결정합니다. 버스/해치는 구조물 어디에서든 모든 단조 케이싱을 대체할 수 있습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "solenoid"로 구조물을 시각화/건설해 솔레노이드 코일의 티어를 지정하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15555"/><ItemImage id="gregtech:gt.blockmachines:15555"/>
- 10-29 <ItemLink id="miscutils:gtplusplus.blockcasings.5:6"/><ItemImage id="miscutils:gtplusplus.blockcasings.5:6"/>
- 20 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:32100"/><ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:32100"/>
- 3 솔레노이드 초전도 코일 (티어별) <ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:10"/>
- 2 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 1개 이상 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0개 이상 출력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">산업용 대형 망치</Color>는 각 면을 벽 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 사이에서 공유할 수 있습니다. 

## 사용법
산업용 대형 망치는 단일블록 단조 망치와 증기 압착기의 직접적인 상위 버전입니다. 200% 속도로 작동하고 $$\text{전압 티어} \times \text{솔레노이드 티어} \times 6$$ 병렬 처리를 제공하기 때문입니다