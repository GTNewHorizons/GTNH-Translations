---
item_ids:
  - gregtech:gt.blockmachines:15543
navigation:
  title: 산업용 코크스 오븐
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15543
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 산업용 코크스 오븐

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15543"/>
</GameScene>
<Color id="GREEN" >산업용 코크스 오븐 (ICO)</Color>은 통나무를 대량으로 숯과 하나의 유체 부산물(석탄 가스, 목재 가스, 목초액, 목타르 또는 숯 부산물)로 태우기 위한 EV 티어 다중블록입니다. 유체 부산물은 에틸렌, 벤젠, 톨루엔과 같은 유기 화합물을 생산하는 데 유용합니다. <Color id="GREEN">ICO</Color>는 가열 코일 티어당 <Color id="RED">2%</Color>의 에너지 절감(곱연산)을 얻고 구조에 추가된 슬라이스마다 <Color id="BLUE">16</Color>개를 더한 <Color id="BLUE">32</Color>개의 병렬 처리를 제공하므로 열분해 오븐 <ItemImage id="gregtech:gt.blockmachines:15546"/> 및 고급 코크스 오븐 <ItemImage id="Railcraft:machine.alpha:12"/>의 직접적인 업그레이드입니다. 추가 슬라이스는 무제한인 이터널을 제외한 모든 가열 코일 티어에서 15개로 제한됩니다(기본 구조 포함 총 16개). <Color id="GREEN">ICO</Color>는 또한 인피니티 가열 코일 이상을 사용할 때 하나의 <Color id="GREEN">다중 앰프 에너지 해치</Color>를 사용할 수 있는 능력을 해금합니다. 

<br clear="all"/>

> [!NOTE]
> 다중블록에는 (구조를 제외하고) 다음과 같은 변경 사항이 적용되었습니다:
> - "슬라이스 구조": ICO는 이제 추가 "슬라이스"를 가질 수 있으며, 각 슬라이스는 구조 티어에 따라 +8/16 병렬 처리를 제공합니다 (최대 15슬라이스, 이터널 코일은 무제한 슬라이스를 해금합니다)
> - 다중 앰프 지원: 인피니티 코일 이상을 사용하면 단일 다중 앰프 해치를 사용할 수 있습니다!
> - EU 절약: 전압 티어당 -4% EU/t 대신 이제 가열 코일당 -2% EU/t를 사용합니다 (곱연산)

## 건설
<Color id="GREEN">ICO</Color>에는 두 가지 티어 구성 요소가 있습니다. 코크스 오븐 케이싱은 기본 병렬 처리 수와 슬라이스당 추가 병렬 처리 수를 모두 결정합니다. 가열 코일은 기계의 에너지 절감량을 결정합니다. 버스/해치는 기본 구조의 모든 구조용 코크스 오븐 케이싱을 대체할 수 있습니다--추가 슬라이스는 아닙니다. 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위한 여러 개의 일반 에너지 해치 또는 가열 코일이 인피니티 이상일 경우 하나의 다중 앰프 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "coke_oven_casing" 및 "coil"로 해당 구성 요소의 티어를 지정하고, 하위 채널 "length"로 총 슬라이스 수를 지정하여 구조를 시각화/건설하십시오. 

### 기본 구조 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15543"/><ItemImage id="gregtech:gt.blockmachines:15543"/>
- 35-48 <ItemLink id="miscutils:miscutils.blockcasings:1"/><ItemImage id="miscutils:miscutils.blockcasings:1"/>
- 10 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8 가열 코일 (티어별) <ItemImage id="gregtech:gt.blockcasings5:3"/>
- 8 내열/내화 코크스 오븐 케이싱 <ItemImage id="miscutils:miscutils.blockcasings:2"/> / <ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 1개 이상 에너지 해치 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 머플러 해치 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0개 이상 출력 해치 (모든 구조용 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 각 추가 슬라이스 요구 사항:
- 19 <ItemLink id="miscutils:miscutils.blockcasings:1"/><ItemImage id="miscutils:miscutils.blockcasings:1"/>
- 10 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8 가열 코일 (티어별) <ItemImage id="gregtech:gt.blockcasings5:3"/>
- 5 내열/내화 코크스 오븐 케이싱 <ItemImage id="miscutils:miscutils.blockcasings:2"/> / <ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>

### 벽 공유
<Color id="GREEN">ICO</Color>는 반대쪽 끝에서 수평으로 뒤집힌 다른 ICO와 구조 대부분을 벽 공유할 수 있습니다. 이 방식은 케이싱, 프레임 박스, 가열 코일을 엄청나게 절약해 주므로 강력히 권장됩니다--두 번째 기계는 사실상 무료입니다. 그러나 버스/해치는 기본 구조로 제한되므로 해당 구성에서는 공유할 수 없습니다. 에너지 절감량과 관계없이 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로, <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계가 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">ICO</Color>는 가열 코일 티어당 2%의 에너지 절감(곱연산)을 얻고 구조에 추가된 슬라이스마다 16개를 더한 32개의 병렬 처리를 제공하므로, 다음 표에서 볼 수 있듯이 열분해 오븐 및 고급 코크스 오븐의 직접적인 업그레이드입니다. 추가 슬라이스는 무제한인 이터널을 제외한 모든 가열 코일 티어에서 15개로 제한됩니다(기본 구조 포함 총 16개). 

<Color id="GREEN">ICO</Color>는 주로 통나무를 숯으로 태우는 데 사용되며, 입력 버스 또는 컨트롤러의 프로그래밍된 회로에 따라 결정되는 하나의 유체 부산물을 선택할 수 있습니다. 가장 흔한 선택은 숯 부산물이며, 이는 증류탑 <ItemImage id="gregtech:gt.blockmachines:1126"/>에서 디메틸벤젠, 목재 가스, 목초액, 목타르로 분해되기 때문입니다. 또 다른 흔한 선택은 니트로벤젠을 더 직접적/효율적으로 만들기 위한 목타르입니다. 또한 통나무 4개당 250L의 질소 가스를 사용하여 기계의 처리 속도를 두 배로 높이는 옵션이 있으며, 이 역시 입력 버스 또는 컨트롤러의 프로그래밍된 회로에 따라 결정됩니다.