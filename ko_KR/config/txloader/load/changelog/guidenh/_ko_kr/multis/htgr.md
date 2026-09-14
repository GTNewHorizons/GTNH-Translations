---
item_ids:
  - gregtech:gt.blockmachines:12791
navigation:
  title: 고온 가스 냉각 원자로
  parent: multis.md
  icon: gregtech:gt.blockmachines:12791
categories:
    - 새 멀티블록
author: Skorched
date: 2026-05-31
---

# 고온 가스 냉각 원자로
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12791" />
</GameScene>
<Color id="GREEN">고온 가스 냉각 원자로(HTGR)</Color>는 TRISO <ItemImage id="kubatech:htgr_item_triso_fuel:1"/> 구슬을 핵분열로 붕괴시켜 값진 부산물을 얻는 IV 티어 멀티블록입니다. <Color id="GREEN">HTGR</Color>은 가공을 시작하려면 최소 100개의 TRISO 구슬과 51,200L의 헬륨으로 초기화해야 하지만, 최대치인 10,000개의 TRISO 구슬과 512,000L의 헬륨보다 적게 보유하면 효율이 감소하고 전력 소비가 증가합니다. 선택적으로 IC2 냉각수 및/또는 증류수를 공급하면 붕괴 과정을 극적으로 가속하고 최대 소요 시간을 1,000초에서 단 10초로 줄일 수 있습니다. <Color id="GREEN">TRISO</Color>는 각 작업이 시작될 때 최대 TRISO 구슬의 0.14%와 헬륨의 0.05%를 소비하지만, 이후 10초 동안 최소 1,536 EU/t를 사용하여 최대 5,000 L/t의 고온 냉각수와 160,000 L/t의 증기를 생산합니다. 연소된 TRISO 구슬은 산업용 원심분리기에서 재활용하여 원래 투입물 대부분을 되돌려받고, sunnarium, 인듐, 루테튬 분진, 란타넘 같은 몇 가지 추가 산출물을 얻을 수 있습니다. 최대 연료 처리량은 시간당 5,094개의 TRISO 구슬입니다.

고온 냉각수는 열 보일러 <ItemImage id="gregtech:gt.blockmachines:15557"/>, 대형 열교환기 <ItemImage id="gregtech:gt.blockmachines:1154"/>, 또는 Whakawhiti Wera XL <ItemImage id="gregtech:gt.blockmachines:31079"/>에서 과열 증기를 생산하거나, 극한 열교환기에서 초임계 증기를 생산하는 데 사용됩니다. 그런 다음 증기는 대형 증기 터빈에서 전력을 생산하는 데 사용됩니다. 최대 효율에서 111A 이상의 LuV 전력을 기대할 수 있습니다.

<Color id="GREEN">HTGR</Color>은 <Color id="RED">토륨 고온 원자로(THTR)</Color>와 매우 유사합니다. 차이점은 <Color id="RED">THTR</Color>이 훨씬 오래 작동하고 부산물을 거의 생산하지 않는다는 점입니다. 즉, 자원에는 <Color id="GREEN">HTGR</Color>을, 전력에는 <Color id="RED">THTR</Color>을 사용하십시오.
<br clear="all"/>

## 건설:
<Color id="GREEN">HTGR</Color>은 네 개의 개별 구조물로 구성됩니다. 이 구조물들의 정확한 위치는 컨트롤러를 기준으로 고정되어 있으며, 구조물이 형성되려면 네 개 모두 필요합니다. 커다란 보라색 구체는 원자로이며, 상단에는 TRISO 구슬용 입력 버스가, 하단에는 연소된 TRISO 구슬 <ItemImage id="kubatech:htgr_item_burned_triso_fuel:3"/>용 출력 버스가 있습니다. 중앙의 높은 수직 구조물은 1차 냉각재 타워로, 측면에는 IC2 냉각수용 입력 해치가, 상단에는 고온 냉각수용 출력 해치가 있습니다. 가장자리의 더 작은 수직 구조물은 2차 냉각재 타워로, 상단 근처에는 증류수용 입력 해치가, 하단 근처에는 증기용 출력 해치가 있습니다. 헬륨 입력 해치, 에너지 해치, 유지보수 해치는 모두 구조물 중앙의 펌프 위쪽 상단 세 개의 케이싱에만 제한됩니다. <Color id="RED">멀티 앰프 및 레이저 에너지 해치</Color>는 지원되지 않으며, 일반 에너지 해치는 하나만 있을 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오.

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:12791"/><ItemImage id="gregtech:gt.blockmachines:12791"/>
- 273 <ItemLink id="gregtech:gt.blockcasings13:3"/><ItemImage id="gregtech:gt.blockcasings13:3"/>
- 272 <ItemLink id="gregtech:gt.blockcasings10:3"/><ItemImage id="gregtech:gt.blockcasings10:3"/>
- 164 <ItemLink id="gregtech:gt.blockframes:81"/><ItemImage id="gregtech:gt.blockframes:81"/>
- 162 <ItemLink id="gregtech:gt.blockcasings13:1"/><ItemImage id="gregtech:gt.blockcasings13:1"/>
- 45 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 41 <ItemLink id="gregtech:gt.blockcasings13:2"/><ItemImage id="gregtech:gt.blockcasings13:2"/>
- 30 <ItemLink id="gregtech:gt.blockcasings2:14"/><ItemImage id="gregtech:gt.blockcasings2:14"/>
- 24 <ItemLink id="gregtech:gt.blockcasings13"/><ItemImage id="gregtech:gt.blockcasings13"/>
- 23 <ItemLink id="gregtech:gt.blockcasings:5"/><ItemImage id="gregtech:gt.blockcasings:5"/>
- 20 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 17 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:10"/><ItemImage id="gregtech:gt.blockcasings2:10"/>
- 2 <ItemLink id="gregtech:gt.blockcasings2:11"/><ItemImage id="gregtech:gt.blockcasings2:11"/>
- 1 <ItemLink id="gregtech:gt.blockcasings2:6"/><ItemImage id="gregtech:gt.blockcasings2:6"/>
- 1 에너지 해치 (펌프 위 상단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (펌프 위 상단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 입력 버스 (TRISO 구슬용 하나) <ItemImage id="gregtech:gt.blockmachines:70" />
- 3 입력 해치 (IC2 냉각수용 하나, 증류수용 하나, 헬륨용 하나) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1 출력 버스 (연소된 TRISO 구슬용 하나) <ItemImage id="gregtech:gt.blockmachines:80" />
- 2 출력 해치 (고온 냉각수용 하나, 증기용 하나) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유:
<Color id="GREEN">HTGR</Color>은 버스/해치 위치 제한과 컨트롤러를 회전하거나 뒤집을 수 없다는 점 때문에 구조물의 중요한 부분을 벽 공유할 수 없습니다. 원자로 부분조차 완벽하게 대칭이 아니므로 공유할 수 없습니다.

## 사용법:
<Color id="GREEN">HTGR</Color>에는 아래에 나열된 두 가지 작동 모드가 있습니다. 기계가 유휴 상태일 때 스크루드라이버로 컨트롤러를 우클릭하여 모드를 전환하십시오.

- 일반 - TRISO 구슬과 헬륨을 내부에 저장하고, 최소 조건이 충족되면 가공을 시작합니다.
- 비우기 - 내부에 저장된 모든 TRISO 구슬을 출력 버스로 반환합니다.

<Color id="GREEN">HTGR</Color>은 헬륨 가스를 사용하여 원자로 내부 TRISO 구슬의 핵분열 붕괴를 안정화합니다. IC2 냉각수와 증류수는 선택 사항이지만, 붕괴 과정을 극적으로 가속하여 연료를 더 빠르게 연소시킬 수 있으므로 적극 권장됩니다. 최종 산출물은 연소된 TRISO 구슬이며, 이는 산업용 원심분리기에서 재활용하여 원래 자원 일부를 되돌려받고 다른 곳에 사용할 몇 가지 추가 산출물을 얻습니다. 있는 경우 IC2 냉각수는 고온 냉각수로 변환되고, 증류수는 TRISO 구슬과 헬륨의 양에 비례하는 속도로 증기로 변환됩니다.

## 연료:
<Color id="GREEN">HTGR</Color>은 연료로 TRISO 구슬(펠릿이 아님)을 사용합니다. 총 9가지 유형이 있지만, 필요하다면 모두 같은 기계에서 동시에 사용할 수 있습니다. 가공을 시작하기 위한 최소 연료량은 100개의 TRISO 구슬이지만, 최대치인 10,000개의 TRISO 구슬보다 적게 보유하면 다음 방정식과 그래프에서 볼 수 있듯 기계의 효율이 감소합니다.

TRISO 구슬은 재료에 따라 고유한 재료 능력치를 가집니다. NEI 툴팁에서는 "Properties: [x], [y], [z]"로 표시되며, 여기에 마우스를 올리면 볼 수 있습니다: <ItemImage id="kubatech:htgr_item_burnerd_triso_fuel:3"/>. 이 속성은 각각 기본값($$b$$), 배수($$m$$), 지수($$e$$)이며, 이 장에서 더 자세히 설명하듯 발전량 및 가공 시간과 직접 관련됩니다:

효율은 기계가 작동 중일 때 증가시킬 수 없으며 100%를 초과할 수 없습니다. 유지보수 문제는 각각 최대 효율을 20% 감소시킵니다.

<Latex formula="\text{Efficiency\%} = 0.1 + 0.9 \Biggl( 1 - \Biggl( 1 - \frac{\text{TRISO Balls}}{10,000} \Biggr)^3 \Biggr"/>


<FunctionGraph title="Efficiency of HTGR base on stored TRISO Balls" xRange="0..10000" domain="0..100" xLabel="TRISO Balls" yLabel="Efficiency (%)"> 
<Plot expr="0.1 + 0.9 * (1 - (1 - (x)/(10000))^3) * 100" color="#ff55ff"/>
</FunctionGraph>


<Color id="GREEN">HGTR</Color>의 효율은 다음 방정식에서 볼 수 있듯 각 작업의 지속 시간 및 사용된 재료의 능력치에 정비례합니다.

<Latex formula="\text{Duration (s) } = (100 + (900 \times \text{Efficiency})) \times \eta">
  여기서:
  $$\eta$$: 가공 시간 계수
</Latex>
<Latex formula="\eta = \frac{1}{e^2}">
  여기서:
  $$\eta$$: 가공 시간 계수
  $$e$$: 사용된 TRISO 구슬의 지수 능력치
</Latex>

<Color id="GREEN">HGTR</Color>의 효율은 다음 방정식에서 볼 수 있듯 작업당 소비/연소되는 TRISO 구슬의 양에도 정비례합니다. 이는 작업당 최대 14.15개의 TRISO 구슬입니다. 하지만 냉각수가 없을 때의 속도는 두 변수 모두 효율에 선형으로 비례하므로 지속 시간과 관계없이 시간당 51개로 고정됩니다.

<Latex formula="-\text{Balls/Operation} = \text{TRISO Balls} \times \frac{\pi - 3}{100} \times \text{Efficiency}"/>

<Color id="GREEN">HGTR</Color>은 동일한 수의 연소된 TRISO 구슬을 출력합니다. 다음 표에서 볼 수 있듯 다양한 유용한 부산물을 얻기 위해 TRISO 구슬을 원심분리하십시오. 대부분의 투입물은 더 많은 연료를 만들기 위해 반환되며, 다른 곳에 사용할 몇 가지 추가 산출물이 있습니다. 특히, 발광석 TRISO 구슬은 sunnarium을, 은 TRISO 구슬은 인듐을, 토륨 TRISO 구슬은 루테튬을, 세슘 TRISO 구슬은 란타넘을 생산합니다.

## 냉각재:
<Color id="GREEN">HGTR</Color>에서 유일하게 필수적인 냉각재는 헬륨입니다. 가공을 시작하기 위한 최소 헬륨량은 51,200L이지만, 최대치인 512,000L보다 적게 보유하면 다음 방정식에서 볼 수 있듯 기계의 전력 소비가 증가합니다. 최대 전력 소비는 61,440 EU/t이고 최소 전력 소비는 1,536 EU/t입니다. <Color id="GREEN">HGTR</Color>은 각 작업 시작 시 현재 헬륨의 정확히 0.05%를 소비하므로 원자로는 시간이 지나면서 천천히 다시 채워야 합니다.

<Latex formula="-\text{EU/t} = 1,536 \times \Biggl( 1 + 39 \times \Biggl( 1 - \frac{\text{Helium} - 51,200}{460,800} \Biggr) \Biggr)"/>

선택적으로 IC2 냉각수 및/또는 증류수를 공급하면 TRISO 구슬의 붕괴 과정을 극적으로 가속할 수 있습니다. IC2 냉각수는 초당 총 지속 시간의 7%를 건너뛰고, 증류수는 초당 총 지속 시간의 3%를 건너뛰며, 함께 사용하면 초당 총 지속 시간의 10%를 건너뜁니다. 즉, 전체 1,000초 작업이 10초 이내에 끝날 수 있으면서도 동일한 양의 TRISO 구슬을 소비합니다. 발전에는 매우 비효율적이지만, 증식 및 부산물 수확에는 매우 유용합니다. 기본 시간당 51개의 TRISO 구슬은 시간당 최대 5,094개까지 증가합니다.

<Color id="GREEN">HGTR</Color>이 사용하는 IC2 냉각수와 증류수의 양은 다음 표에서 볼 수 있듯 현재 TRISO 구슬의 양과 현재 헬륨의 양에 따라 달라집니다. IC2 냉각수는 완벽한 1:1 비율로 고온 냉각수로 변환되고, 증류수는 1:160 비율로 증기로 변환됩니다.

## 전력:
높은 유지 비용에도 불구하고, <Color id="GREEN">HGTR</Color>은 작업당 최대 10초 동안 인상적인 5,000 L/t의 고온 냉각수와 160,000 L/t의 증기를 출력합니다. 냉각수만의 처리량은 토륨 고온 원자로 <ItemImage id="gregtech:gt.blockmachines:12733"/>보다 약간 더 많고, 유체 원자로 출력의 72배, 심부 지열 가열 펌프 <ItemImage id="gregtech:gt.blockmachines:12729"/> 출력의 26배입니다. 또한 극한 열교환기에서 초임계(SC) 증기를, 열 보일러, 대형 열교환기, 또는 Whakawhiti Wera XL에서 과열(SH) 증기를 생성하기에 충분하고도 남습니다. 유일한 문제는 그렇게 많은 고온 냉각수를 처리하려면 많은 열교환기와 막대한 증류수 공급이 필요하다는 점이며, 이는 다음 표에서 볼 수 있습니다. EHE는 더 많은 기계를 건설해야 하더라도 초임계 증기가 전체적으로 더 많은 전력을 제공하므로 WWXL보다 권장됩니다.

변환 비율

- 1 L/t 고온 냉각수 = 200 L/t SC 증기 (EHE) 또는 200 L/t SH 증기 (열 보일러, LHE, WWXL)
- 200 L/t SC 증기 = 200 L/t SH 증기 = 200 L/t 증기
- 160 L/t 증기 = 1 L/t 증류수

고온 냉각수와 증기의 출력은 각각 최대 5,000 L/t 및 160,000 L/t이지만, 출력 속도는 다음 방정식을 통해 사용되는 TRISO 구슬의 능력치와 직접 관련됩니다:

<Latex formula="\text{Outputs /t} = \text{Base Outputs} \times b\times(m^e)">
  여기서:
    $$b$$: 재료 기본 능력치
    $$m$$: 재료 배수 능력치
    $$e$$: 재료 지수 능력치
</Latex>