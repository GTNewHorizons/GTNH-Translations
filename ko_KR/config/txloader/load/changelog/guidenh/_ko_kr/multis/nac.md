---
item_ids:
  - gregtech:gt.blockmachines:9500
navigation:
  title: 나노칩 조립 단지
  parent: multis.md
  icon: gregtech:gt.blockmachines:9500
categories:
    - 새 멀티블록
author: Skorched
date: 2026-05-26
---

# 나노칩 조립 단지
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9500" />
</GameScene>
<Color id="GREEN">나노칩 조립 단지 (NAC)</Color>는 대량 회로 조립을 위한 UEV 티어 멀티블록입니다. <Color id="GREEN">NAC</Color>는 크리스탈, 웻웨어, 바이오웨어, 광학, 피코, 양자 회로용 <ItemLink id="gregtech:gt.blockmachines:12735"/> <ItemImage id="gregtech:gt.blockmachines:12735"/>의 직접적인 업그레이드입니다. 왜냐하면 <Color id="RED">무제한 병렬 처리</Color>를 제공하고, <Color id="BLUE">2/2 완벽 오버클럭</Color>을 실행하며, 레시피 전체 지속 시간 동안 사용할 수 있는 에너지가 충분하지 않으면 처리를 시작하지 않기 때문입니다. <Color id="GREEN">NAC</Color>는 또한 엄청나게 높은 처리량을 위해 <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>멀티앰프 및 레이저 에너지 해치를 지원합니다.

모든 처리와 회로 조립은 구조물 중앙의 제어실을 둘러싼 모듈에 의해 수행됩니다. 선택할 수 있는 11개의 고유 모듈과 12개의 모듈 슬롯이 있습니다. 일부 모듈은 고유한 난이도나 비용을 가지지만, 대부분은 비교적 단순합니다. 아이템과 회로 부품(CC)은 진공 컨베이어 해치와 진공 컨베이어 파이프를 통해 모듈 간에 라우팅되며, 이들은 무제한 저장 용량과 처리량을 가집니다. 동일한 회로 유형을 충분히 제작하면 <Color id="GREEN">NAC</Color>가 해당 회로 계열에 교정되고 추가 보너스를 부여합니다. 
<br clear="all"/>

## 건설:
<Color id="GREEN">NAC</Color>는 12개의 모듈 슬롯으로 둘러싸인 대형 제어실로 구성됩니다. 제어실은 기계의 입력과 출력 모두를 담당하고, 모듈은 회로 부품(CC)을 처리합니다. 멀티앰프 및 레이저 에너지 해치가 지원되지만, 하나만 있을 수 있으며 제어실 내부나 아래에 있어야 합니다. 전력은 <ItemLink id="gregtech:gt.blockmachines:14003"/><ItemImage id="gregtech:gt.blockmachines:14003"/>와 유사하게 요청되는 순서대로 제어실에서 모든 모듈로 자동 분배됩니다. 유일한 예외는 <ItemLink id="gregtech:gt.blockmachines:9504"/><ItemImage id="gregtech:gt.blockmachines:9504"/>로, 에너지 버퍼를 채우는 우선순위가 다른 모든 모듈보다 낮습니다. 정비 해치는 없습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오.

모듈은 자체 컨트롤러와 건설 요구 사항을 가진 독립적인 멀티블록입니다. 모듈 슬롯의 상단 가장자리에 있는 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 중 하나를 교체하고 멀티블록 구조 홀로그램 프로젝터를 사용하여 시각화/건설하십시오. 어떤 방향으로도 향할 수 있지만, 거꾸로 건설할 수는 없습니다. 올바르게 완료하면 <Color id="GREEN">NAC</Color>가 활성화되었을 때 모듈의 컨트롤러에 "메인 컴플렉스에 연결됨"이 표시되어야 합니다. 
### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9500"/><ItemImage id="gregtech:gt.blockmachines:9500"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 3,956개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 2,226개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 1,708-1,720개
- <ItemLink id="gregtech:gt.blockcasings12:3"/><ItemImage id="gregtech:gt.blockcasings12:3"/> 721개
- <ItemLink id="gregtech:gt.blockframes:324"/><ItemImage id="gregtech:gt.blockframes:324"/> 53개
- <ItemLink id="gregtech:gt.blockcasings12:4"/><ItemImage id="gregtech:gt.blockcasings12:4"/> 32개
- 에너지 해치 1개 (제어실 내 아무 측면 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:15065"/>
- 입력 버스 0개 이상 (제어실 내 아무 측면 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 출력 버스 0개 이상 (제어실 내 아무 측면 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:80"/>

## 진공 컨베이어 시스템
<Color id="GREEN">NAC</Color>만의 고유한 <ItemLink id="gregtech:gt.blockmachines:9501"/> (VCI) <ItemImage id="gregtech:gt.blockmachines:9501"/> 및 <ItemLink id="gregtech:gt.blockmachines:9502"/> (VCO) <ItemImage id="gregtech:gt.blockmachines:9502"/> 해치는 모듈 간에 아이템이나 CC를 이동시킵니다. 이들은 작동하려면 색상을 지정해야 하고 연결이 1대1이어야 한다는 점에서 광학 전송 및 수신 해치와 유사합니다. 해치는 기계별이므로 <Color id="GREEN">NAC</Color> 간에 CC를 전송할 수 없습니다. 해치를 연결하는 진공 컨베이어 파이프도 색상을 지정해야 하며 자유롭게 구부릴 수 있습니다. 모든 것에 색상을 지정하려면 <ItemLink id="gregtech:gt.metaitem.01:32468"/><ItemImage id="gregtech:gt.metaitem.01:32468"/>를 사용하는 것을 강력히 권장합니다.

두 해치 모두 한 번에 최대 16개의 고유 아이템 스택을 보관할 수 있으며, 용량 상한과 연결 간 전송 제한이 없습니다. 이를 통해 엔드 게임까지 쉽게 확장할 수 있는 엄청나게 높은 처리량을 얻을 수 있습니다. 해치 내부에 저장된 아이템과는 직접 상호작용할 수 없지만, 저장된 아이템을 AE2 저장 셀로 비우기/포장 해제하거나 모든 저장 아이템을 단순히 삭제하는 옵션이 있습니다. 유체는 진공 컨베이어 시스템으로 들어가지 않으며, 이를 사용하는 모듈로 직접 라우팅해야 합니다.

아이템이 올바른 모듈로 라우팅되도록 적절히 필터링하거나 분할하는 방법은 두 가지입니다. 첫 번째는 NAC에 들어가기 전에 모든 것을 필터링하는 것이고, 두 번째는 <ItemLink id="gregtech:gt.blockmachines:9510"/><ItemImage id="gregtech:gt.blockmachines:9510"/> 모듈을 사용하는 것입니다. 후자는 모듈 슬롯을 사용하지만, 입력 색상, 출력 색상, 아이템 유형 및/또는 공급된 레드스톤 레벨에 따라 사용자 지정 라우팅을 허용합니다. 

----------

## 모듈:
<Color id="GREEN">NAC</Color>는 고정된 5초 주기로 회로 부품(CC)을 포장 및 포장 해제할 뿐입니다. 실제로 회로를 처리하고 조립하는 것은 모듈입니다. 제어실 주위에 12개의 모듈 슬롯과 선택할 수 있는 11개의 고유 모듈이 있지만, 모든 모듈이 필요한 것은 아니며 각 모듈의 개수에는 제한이 없습니다. 추가 공정에도 불구하고, 모듈은 회로 조립 라인에서 직접 업그레이드한 것입니다. 왜냐하면 무제한 병렬 처리, 레시피 티어보다 높은 각 전압 티어마다 5초까지 내려가는 2/2 완벽 오버클럭을 실행하며, 제작에 충분한 에너지 버퍼가 없으면 처리를 시작하지 않기 때문입니다. 즉, 엄청나게 높은 처리량을 가지며 전력 부족이나 아이템 소실이 발생할 수 없습니다. 오버클럭은 더 긴 레시피의 속도를 높이기 위해 병렬 처리보다 먼저 계산됩니다.

<Color id="GREEN">NAC</Color>의 일반적인 작업 흐름은 아래에 나열되어 있습니다. 참고용 이미지도 제공되지만, 모든 것(예: 스플라이스된 프레임 박스)이 나노칩 조립 매트릭스로 라우팅되는 것은 아니므로 약간 단순화된 것입니다. 더 자세한 설정 안내는 아래 교정 섹션을 참고하십시오. 
1. 제어실의 <u>색상이 지정된</u> 입력 버스(일반 또는 스톡킹)를 통해 아이템을 삽입합니다.
2. <Color id="GREEN">NAC</Color>는 아이템을 CC로 포장하고 같은 색상의 VCO 해치로 전송합니다.
3. 미리 처리하지 않았다면 나노입자 분배기 모듈로 포장된 CC를 필터링하여 올바른 모듈로 라우팅합니다.
4. 모듈은 포장된 CC를 가공된 부품(PC)으로 바꾸며, 이는 포장 해제되거나 <Color id="GREEN">NAC</Color>를 떠날 수 없습니다.
5. 나노칩 조립 매트릭스에서 PC를 결합하여 회로 CC를 만들고 제어실로 다시 라우팅합니다.
6. <Color id="GREEN">NAC</Color>는 회로 CC를 포장 해제하고 회수할 수 있도록 출력 버스로 전송합니다.
<FloatingImage src="../assets/multis/nac_overview.png" displayWidth="384">
  <ImageAnnotation>
    Fox의 나노칩 조립 단지 개요
  </ImageAnnotation>
</FloatingImage>
<br clear="all"/>

## 나노칩 조립 매트릭스 <ItemImage id="gregtech:gt.blockmachines:9504"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9504" />
</GameScene>
<Color id="GREEN">나노칩 조립 매트릭스</Color>는 가공된 부품(PC)으로부터 회로 CC를 조립합니다. 이 모듈은 회로 CC를 제어실로 보내 실제 회로로 포장 해제하기 전의 항상 마지막 단계입니다. <Color id="GREEN">나노칩 조립 매트릭스</Color>는 에너지 버퍼를 채우는 우선순위가 모든 모듈 중 가장 낮으며, 5초까지 내려가는 2/2 완벽 오버클럭은 레시피 전압 티어가 아니라 레시피 케이싱 티어를 기준으로 합니다. 둘 다 NEI에 표시되며 서로 다른 경우가 많습니다.
<br clear="all"/>
<Latex formula="\text{Max Overclocks} = \text{Energy Hatch Tier} - \text{Recipe Casing Tier}"/>

<Color id="GREEN">나노칩 조립 매트릭스</Color>로의 입력은 별도의 VCI에 있을 수 있으며 모두 같은 색상일 필요가 없습니다. 또한 레시피가 조립 라인 레시피와 동일하게 보임에도 불구하고 부품 순서에 제한이 없습니다. 출력 색상은 종종 회로 기판 또는 인케이스먼트 PC인 첫 번째 재료를 기준으로 합니다. 

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9504"/><ItemImage id="gregtech:gt.blockmachines:9504"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 25개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 24개
- 부품 조립 라인 케이싱 (티어별) 20개 <ItemImage id="GoodGenerator:componentAssemblylineCasing"/>
- <ItemLink id="gregtech:gt.blockframes:325"/><ItemImage id="gregtech:gt.blockframes:325"/> 12개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 8개
- <ItemLink id="gregtech:gt.sheetmetal:325"/><ItemImage id="gregtech:gt.sheetmetal:325"/> 3개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>


| 회로 계열   | 케이싱 티어    |
|--------------- | --------------- |
| 크리스탈 | LuV |
| 웻웨어 | ZPM |
| 바이오웨어 | UV  |
| 광학 | UHV |
| 피코 | UEV   |
| 양자 | UIV |
| 플랑크  | UMV |


## 나노입자 분배기 <ItemImage id="gregtech:gt.blockmachines:9510"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9510" />
</GameScene>
<Color id="GREEN">나노입자 분배기</Color>는 모든 CC를 필터링하고 정리합니다. 컨트롤러 GUI를 통해 규칙 관리자를 열어 입력 색상, 출력 색상, 아이템 유형 및/또는 공급된 레드스톤 레벨에 따라 사용자 지정 라우팅 규칙을 설정하십시오. 최소한 하나 이상의 입력 색상과 하나 이상의 출력 색상이 선택되어 있어야 합니다. <Color id="GREEN">나노입자 분배기</Color>는 아이템 유형만으로, 또는 CC의 미포장 버전만으로 필터링할 수 없습니다. 단일 아이템 유형에 대해 유효한 필터가 여러 개 있으면, 해당 아이템은 필터들 사이에 균등하게 분배됩니다.

분배기 레드스톤 입력은 구조물 상단의 나노칩 메시 인터페이스 케이싱을 대체하는 선택적 해치이며 외부 레드스톤 수신기 역할을 합니다. 들어오는 레드스톤 신호의 세기는 규칙 관리를 위해 해치 GUI에서 구성된 채널과 연결됩니다. 
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9510"/><ItemImage id="gregtech:gt.blockmachines:9510"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 37개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 18개
- <ItemLink id="gregtech:gt.blockframes:765"/><ItemImage id="gregtech:gt.blockframes:765"/> 10개
- <ItemLink id="gregtech:gt.blockmachines:9515"/> 0개 이상 (아무 상단 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9515"/>
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## 부품 준비 장치 <ItemImage id="gregtech:gt.blockmachines:9505"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9505" />
</GameScene>
<Color id="GREEN">부품 준비 장치</Color>는 SMD CC를 처리합니다. 이 모듈은 모든 회로 계열에 필요합니다.
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9505"/><ItemImage id="gregtech:gt.blockmachines:9505"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 44개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 20개
- <ItemLink id="gregtech:gt.blockframes:979"/><ItemImage id="gregtech:gt.blockframes:979"/> 17개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 8개
- <ItemLink id="gregtech:gt.blockcasingsNH:10"/><ItemImage id="gregtech:gt.blockcasingsNH:10"/> 4개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## 나노정밀 전선 추적기 <ItemImage id="gregtech:gt.blockmachines:9509"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9509" />
</GameScene>
<Color id="GREEN">나노정밀 전선 추적기</Color>는 전선 CC를 처리합니다. 이 모듈은 모든 회로 계열에 필요합니다.
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9509"/><ItemImage id="gregtech:gt.blockmachines:9509"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 46개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 28개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 25개
- <ItemLink id="gregtech:gt.blockframes:985"/><ItemImage id="gregtech:gt.blockframes:985"/> 20개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## 나노정밀 절단 챔버 <ItemImage id="gregtech:gt.blockmachines:9508"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9508" />
</GameScene>
<Color id="GREEN">나노정밀 절단 챔버</Color>는 볼트, 프레임 박스, 메모리 칩 및 웨이퍼 CC를 처리합니다. 이 모듈은 모든 회로 계열에 필요합니다.
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9508"/><ItemImage id="gregtech:gt.blockmachines:9508"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 31개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 28개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 24개
- <ItemLink id="gregtech:gt.blockframes:129"/><ItemImage id="gregtech:gt.blockframes:129"/> 21개
- <ItemLink id="gregtech:gt.blockcasings9:12"/><ItemImage id="gregtech:gt.blockcasings9:12"/> 16개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 입력 해치 1개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>

## 전체 기판 침지 장치 <ItemImage id="gregtech:gt.blockmachines:9506"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9506" />
</GameScene>
<Color id="GREEN">전체 기판 침지 장치</Color>는 회로 기판 CC를 해당 침지액으로 세정하여 처리합니다. 레시피는 침지액을 전혀 소비하지 않지만, 불순물을 최대 100%까지 증가시킵니다. 불순물이 높을수록 모듈의 전력 소비가 최대 300%까지 증가하며, 컨트롤러 GUI를 통해 수동으로 또는 구성된 백분율 수준에서 자동 배출을 작동시켜 배출할 때까지 이어집니다. 자동 배출은 1-100% 사이여야 하므로 탱크는 결국 다시 채워야 합니다.

사용 가능한 침지액은 네 가지지만, 내부 탱크는 한 번에 하나만 보관할 수 있습니다. 시작하려면 일반 입력 해치를 통해 500,000L에서 1,000,000L 사이의 침지액을 공급하십시오. 초과 침지액은 소비되지 않으며, 최대치보다 적게 보유하면 다음 방정식에서 볼 수 있듯이 불순물이 증가하는 속도가 빨라집니다. 총 아이템 수는 반복 간에 이월되므로 레시피나 배치 크기에 관계없이 1,000개 아이템마다 한 번씩 불순물이 추가됩니다. 
<br clear="all"/>

<Latex formula="+\text{Impurity}\% = \frac{10,000,000,000,000 \times \lfloor \text{Items} \div 1,000 \rfloor}{\text{Immersion Fluid}^{2.5}}"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9506"/><ItemImage id="gregtech:gt.blockmachines:9506"/> 1개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 52개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 27개
- <ItemLink id="miscutils:blockFrameGtOctiron"/><ItemImage id="miscutils:blockFrameGtOctiron"/> 19개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 10개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 입력 해치 1개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>

| 회로 기판   | 침지액    |
|--------------- | --------------- |
| 엘리트(크리스탈)   | 염화철(III)   |
| 웻웨어   | 성장 촉매 배지   |
| 바이오웨어   | 멸균 생물 촉매 배지   |
| 광학   | 프리즘 산   |

----------

| 침지액 | 불순물 증가% | 최대 수명 |
| --------------- | --------------- | --------------- |
| 500,000L | 1,000개당 0.056% | 1,786,000개 아이템 |
| 750,000L | 1,000개당 0.021% | 4,872,000개 아이템 |
| 1,000,000L | 1,000개당 0.010% | 10,000,000개 아이템 |

----------


| 불순물 | EU/t |
| -------------- | --------------- |
| 0-15% | 70% + (2 x 불순물%) |
| 15-65% | 100% |
| 65-100% | 100% + (2 x 불순물%) |

## 나노미터 인케이스먼트 래퍼 <ItemImage id="gregtech:gt.blockmachines:9513"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9513" />
</GameScene>

<Color id="GREEN">나노미터 인케이스먼트 래퍼</Color>는 시트 및 프레임 박스 CC를 처리합니다. 이 모듈은 대부분의 레시피에 여러 입력이 있고 출력이 여러 다른 위치에서 필요한 경우가 많기 때문에 필터링하기 가장 어렵습니다. 이 모듈은 모든 회로 계열에 필요합니다. 
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9513"/><ItemImage id="gregtech:gt.blockmachines:9513"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 47개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 40개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 32개
- <ItemLink id="gregtech:gt.blockframes:391"/><ItemImage id="gregtech:gt.blockframes:391"/> 32개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## 초전도성 스트랜드 분배기 <ItemImage id="gregtech:gt.blockmachines:9511"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9511" />
</GameScene>
<Color id="GREEN">초전도성 스트랜드 분배기</Color>는 활성 상태일 때 슈퍼 쿨런트 1,000 L/s를 소비하여 초전도체 CC를 처리합니다. 이 모듈은 피코/양자 회로 계열에는 필요하지 않습니다. 
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9511"/><ItemImage id="gregtech:gt.blockmachines:9511"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 40개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 29개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 24개
- <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils:8"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:8"/> 16개
- <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils:7"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:7"/> 6개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 입력 해치 1개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>

## 초고에너지 에칭 어레이 <ItemImage id="gregtech:gt.blockmachines:9507"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9507" />
</GameScene>
<Color id="GREEN">초고에너지 에칭 어레이</Color>는 자체 레이저 소스 해치로 크리스탈 CC를 처리합니다. 완전히 교정된 크리스탈 NAC에서 모듈의 전력 소비는 레이저 소스 해치의 $$\log_4(\text{Amps})$$로 나뉘고, 레시피 지속 시간은 $$\text{Voltage Tier} - 9$$로 나뉩니다. 이 모듈은 광학 또는 피코/양자 회로 계열에는 필요하지 않습니다. 
<br clear="all"/>

| 암페어   | EU/t    |
|--------------- | --------------- |
| 256   | 100%   |
| 1,024   | 50.0%   |
| 4,096   | 33.3%   |
| 16,384   | 25.0%   |
| 65,536   | 20.0%   |
| 262,144   | 16.7%   |
| 1,048,576   | 14.3%   |
| 4,194,304   | 12.5%   |
| 16,777,216   | 11.1%   |

| 전압   | 지속 시간    |
|--------------- | --------------- |
| UEV   | 100%   |
| UIV   | 50%   |
| UMV   | 33%   |
| UXV   | 25%   |


### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9507"/><ItemImage id="gregtech:gt.blockmachines:9507"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 28개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 24개
- <ItemLink id="gregtech:gt.blockframes:582"/><ItemImage id="gregtech:gt.blockframes:582"/> 17개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 13개
- <ItemLink id="gtnhlanth:casing.shielded_accelerator"/><ItemImage id="gtnhlanth:casing.shielded_accelerator"/> 9개
- <ItemLink id="gregtech:gt.blockglass1:3"/><ItemImage id="gregtech:gt.blockglass1:3"/> 4개
- 레이저 소스 해치 1개 <ItemImage id="gregtech:gt.blockmachines:15230"/>
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## 가속 생물학 조정기 <ItemImage id="gregtech:gt.blockmachines:9514"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9514" />
</GameScene>
<Color id="GREEN">가속 생물학 조정기</Color>는 생체 CC를 처리합니다. 완전히 교정된 웻웨어 NAC에서는 성장 촉매 배지를 전혀 소비하지 않으며, 완전히 교정된 바이오웨어 NAC에서는 멸균 생물 촉매 배지를 전혀 소비하지 않습니다. 이 모듈은 크리스탈, 광학 또는 피코/양자 회로 계열에는 필요하지 않습니다. 
<br clear="all"/>

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9514"/><ItemImage id="gregtech:gt.blockmachines:9514"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 37개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 36개
- <ItemLink id="gregtech:gt.blockframes:329"/><ItemImage id="gregtech:gt.blockframes:329"/> 36개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 20개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 입력 해치 1개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>

## 광학 최적화 정리기 <ItemImage id="gregtech:gt.blockmachines:9512"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9512" />
</GameScene>
<Color id="GREEN">광학 최적화 정리기</Color>는 3등급에서 8등급 사이(포함)의 두 종류 정제수로 세정하여 광학 CC를 처리합니다. 각 정제수는 다음 표에서 볼 수 있듯이 모듈에 보너스를 부여합니다. 유사한 효과는 서로 곱연산으로 중첩되며, 완전히 교정된 광학 NAC에서는 모든 효과가 두 번 적용됩니다. 이 모듈은 크리스탈, 웻웨어, 바이오웨어 또는 피코/양자 회로 계열에는 필요하지 않습니다. 

| 정제수 | 비용 | 보너스 |
| --------------- | --------------- | --------------- |
| 3등급 | 1,000 L/s | 물 비용 x0.8 |
| 4등급 | 800 L/s | 물 비용 x0.6 |
| 5등급 | 800 L/s | 지속 시간 x0.9 |
| 6등급 | 600 L/s | 지속 시간 x0.7 |
| 7등급 | 600 L/s | EU/t x0.9 |
| 8등급 | 400 L/s | EU/t x0.7 |

### 필요:
- <ItemLink id="gregtech:gt.blockmachines:9512"/><ItemImage id="gregtech:gt.blockmachines:9512"/> 1개
- <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/> 55개
- <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> 49개
- <ItemLink id="gregtech:gt.blockframes:976"/><ItemImage id="gregtech:gt.blockframes:976"/> 48개
- <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/> 40개
- <ItemLink id="gregtech:gt.blockmachines:9501"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- <ItemLink id="gregtech:gt.blockmachines:9502"/> 0개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 입력 해치 1개 이상 (아무 베이스 인터페이스 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>
----------
## 교정:
<Color id="GREEN">NAC</Color>는 나노칩 조립 매트릭스(NAM)에서 제작된 모든 회로를 기록하여 지난 100,000개 회로 중 각 회로 유형의 빈도를 추적합니다. 회로 기록은 1,000개 회로마다 한 번만 갱신되며 가장 오래된 정보부터 대체합니다. 컨트롤러 GUI를 통해 현재 회로 기록과 다음 1,000개 회로까지의 진행 상황을 확인하십시오.

동일한 회로 유형이 충분히 제작되면 <Color id="GREEN">NAC</Color>가 해당 회로 계열에 교정되고, 다음 표에서 볼 수 있듯이 최대 세 가지 중첩 보너스를 얻습니다. 한 번에 하나의 교정만 활성화할 수 있으며, 더 높은 티어가 더 낮은 티어보다 우선순위가 높습니다. 각 교정 티어에는 현재 활성화된 것을 식별하는 데 도움이 되도록 컨트롤러 GUI 내 기계 이름에 추가되는 고유한 접두사가 있습니다. 교정 보너스를 최대화하려면 회로 계열마다 <Color id="GREEN">NAC</Color>를 하나씩 건설하는 것이 좋습니다. 

교정에 관한 세부 사항은 각 회로 유형에 따라 매우 다르고 여기에서 설명하기에는 너무 자세하므로, 더 많은 정보를 원하시면 [NAC 위키 페이지](https://wiki.gtnewhorizons.com/wiki/Nanochip_Assembly_Complex)를 참고하십시오!