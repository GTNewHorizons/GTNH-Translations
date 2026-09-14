---
item_ids:
  - gregtech:gt.blockmachines:1033
navigation:
  title: 스핀마트론-2737
  parent: multis.md
  icon: gregtech:gt.blockmachines:1033
categories:
    - 새 멀티블록
author: Skorched
date: 2026-05-25
---

# 스핀마트론-2737
&lt;GameScene wrap="square" align="right"&gt;
  &lt;ImportStructureLib controller="gregtech:gt.blockmachines:1033" /&gt;
&lt;/GameScene&gt;
&lt;Color id="GREEN"&gt;스핀마트론-2737&lt;/Color&gt;은(는) 먼지, 액체 및 기타 아이템을 대량으로 원심분리하여 하위 구성 요소나 구성 원소로 분리하는 ZPM 티어 멀티블록입니다. 표준 모드에서 &lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) &lt;Color id="RED"&gt;300%&lt;/Color&gt; 속도로 작동하고, 일반적으로 필요한 EU/t의 &lt;Color id="BLUE"&gt;70%&lt;/Color&gt;만 사용하며, 터빈 티어 합계당 &lt;Color id="GREEN"&gt;4&lt;/Color&gt;개의 병렬을 제공하므로 산업용 원심분리기 &lt;ItemImage id="gregtech:gt.blockmachines:15512"/&gt;에서 직접 업그레이드한 것입니다. 거대하지 않은 터빈은 더 적은 병렬을 제공하므로 피해야 합니다. 또한 무제한 티어 건너뛰기를 지원하므로 전압에 관계없이 모든 레시피를 실행할 수 있습니다. &lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 작동하려면 $$\text{레시피 티어} \times 10 L/s$$의 등유가 필요하며, 또는 같은 양의 생물촉매 추진 유체를 사용하면 병렬 수를 추가로 1.25배로 늘릴 수 있습니다.

&lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 성능과 기능에 영향을 주는 세 가지 모드(경량, 표준, 중량)를 가지고 있습니다. 경량 모드는 +100% 속도 보너스를 제공하지만 최대 레시피 티어는 $$\text{전압 티어} - 3$$로 제한됩니다. 표준 모드는 위에서 설명한 것과 같습니다. 중량 모드는 병렬 수를 32로 나누고, T3 구조가 필요하며, 생물촉매 추진 유체가 필요합니다. 중량 모드는 특별히 필요한 경우에만 사용해야 합니다. 
<br clear="all"/>

## 건설:
&lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 프레임 박스와 중앙 로터 블록의 재질에 대응하는 네 가지 구조 티어를 가지고 있습니다. 각 구조 티어는 컨트롤러 내부에 터빈 슬롯 2개를 추가로 제공하여 최대 병렬 수를 늘립니다. 버스/해치는 구조물 어디에서나 진동 안전 케이싱&lt;ItemImage id="gregtech:gt.blockcasings12:9"/&gt;을(를) 대체할 수 있습니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. &lt;Color id="GREEN"&gt;멀티앰프 및 레이저 에너지 해치&lt;/Color&gt;를 지원하지만, 오버클럭은 해치 티어 + 1로 제한됩니다. 컨트롤러에 드라이버를 사용하여 애니메이션을 비활성화할 수 있습니다. &lt;ItemLink id="structurelib:item.structurelib.constructableTrigger"/&gt;&lt;ItemImage id="structurelib:item.structurelib.constructableTrigger"/&gt;를 사용하여 하위 채널 "glass"로 구조물을 시각화/건설하십시오. 유리 티어를 지정하고 한 스택에 보유한 프로젝터 수로 전체 구조 티어를 결정합니다.

터빈 자체는 로터 어셈블리에 들어가지 않습니다. 대신 챔버 컨트롤러 설정에서 컨트롤러에 배치하십시오. 실제로 거기에 배치되지 않아도 로터 어셈블리에 시각적으로 나타납니다. 드라이버로 컨트롤러를 우클릭하여 정적 및 애니메이션 터빈 텍스처를 전환할 수 있습니다. 챔버 컨트롤러 설정에는 T2 생물촉매 추진 유체를 활성화하는 옵션도 있습니다. &lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 등유 대신 해당 유체가 기계 내부에 있을 때 자동으로 감지하지 않습니다. 

### 필요:
- 1 &lt;ItemLink id="gregtech:gt.blockmachines:1033"/&gt;&lt;ItemImage id="gregtech:gt.blockmachines:1033"/&gt;
- 550-711 &lt;ItemLink id="gregtech:gt.blockcasings12:9"/&gt;&lt;ItemImage id="gregtech:gt.blockcasings12:9"/&gt;
- 264 &lt;ItemLink id="GoodGenerator:supercriticalFluidTurbineCasing"/&gt;&lt;ItemImage id="GoodGenerator:supercriticalFluidTurbineCasing"/&gt;
- 160 &lt;ItemLink id="gregtech:gt.blockcasings9"/&gt;&lt;ItemImage id="gregtech:gt.blockcasings9"/&gt;
- 144 &lt;ItemLink id="gregtech:gt.blockglass1:6"/&gt;&lt;ItemImage id="gregtech:gt.blockglass1:6"/&gt;
- 81 티어 유리 (아무거나) &lt;ItemImage id="bartworks:BW_GlasBlocks"/&gt;
- 56 중앙 로터 블록 (멀티 티어에 따라 티어 지정) &lt;ItemImage id="gregtech:gt.blockmetal4:13"/&gt;
- 54 &lt;ItemLink id="miscutils:gtplusplus.blockcasings.5:2"/&gt;&lt;ItemImage id="miscutils:gtplusplus.blockcasings.5:2"/&gt;
- 24 &lt;ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/&gt;&lt;ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/&gt;
- 9 프레임 박스 (멀티 티어에 따라 티어 지정) &lt;ItemImage id="miscutils:blockFrameGtPikyonium64B"/&gt;
- 8 &lt;ItemLink id="gregtech:gt.blockmachines:30010"/&gt; &lt;ItemImage id="gregtech:gt.blockmachines:30010"/&gt;
- 1+ 에너지 해치 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:40"/&gt;
- 1 유지보수 해치 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:90"/&gt;
- 0+ 입력 버스 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:70"/&gt;
- 0+ 입력 해치 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:50"/&gt;
- 0+ 출력 버스 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:80"/&gt;
- 0+ 출력 해치 (아무 진동 안전 케이싱) &lt;ItemImage id="gregtech:gt.blockmachines:60"/&gt;
### 벽 공유:
&lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 케이싱, 로터 어셈블리, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 터빈 자체는 컨트롤러 내부에 저장되므로 포함되지 않습니다. 

## 사용법:
표준 모드에서 &lt;Color id="GREEN"&gt;스핀마트론&lt;/Color&gt;은(는) 300% 속도로 작동하고, 일반적으로 필요한 EU/t의 70%만 사용하며, 터빈 티어 합계당 4개의 병렬을 제공하므로 산업용 원심분리기에서 직접 업그레이드한 것입니다. 거대 터빈이 가장 효과적입니다. 대형/일반/소형 터빈은 전체 합계에 각각 티어 값의 75%/50%/25%만 기여하기 때문입니다. 예를 들어, 두 개의 거대 아다만티움 터빈(티어 10)을 장착한 스핀마트론은 총 4 x (10+10) = 80개의 병렬을 가집니다.

스핀마트론에는 아래에 나열된 세 가지 작동 모드가 있습니다. 컨트롤러 GUI의 "기계 정보 표시"에서 모드를 변경하십시오. 경량 모드는 벌집과 불순한 먼지 같은 낮은 티어 레시피에 탁월합니다. 표준 모드는 $$\text{전압 티어} - 3$$ 제한보다 높은 티어의 레시피에 이상적입니다. 그리고 중량 모드는 특별히 필요한 경우에만 사용해야 합니다.

- 경량 모드 - +100% 속도 보너스를 제공하지만, 최대 레시피 티어는 $$\\
text{전압 티어} - 3$$로 제한됩니다.
- 표준 모드 - 원래 설명에서 변경 없음.
- 중량 모드 - 병렬을 32로 나누고, 최소 T3 구조가 필요하며, 등유 대신 생물촉매 추진 유체가 필요합니다.