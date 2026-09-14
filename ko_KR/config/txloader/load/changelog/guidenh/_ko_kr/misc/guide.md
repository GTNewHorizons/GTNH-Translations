---
navigation:
  title: GuideNH
  parent: misc.md
  icon: minecraft:book
categories:
    - 기타 변경 사항
author: Skorched
date: 2026-05-27
---

# GuideNH
GuideNH는 2.9를 위한 완전히 새로운 모드로, 이전에는 퀘스트 북이나 위키 같은 외부 사이트에 묻혀 있던 게임 내 정보를 더 쉽게 접근할 수 있도록 제공하기 위해 설계되었습니다.

> [!IMPORTANT]
> 이는 위키를 __대체__하기 위한 것이 아니라, 시작하는 데 필요한 중요한 게임 내 정보를 제공하기 위한 것입니다.

## 사용법
마우스를 왼쪽에 올리면 "내비게이션" 바가 나타납니다. 이는 가이드에서 정의한 "최상위" 분류를 표시합니다. 가이드는 일반적으로 관련 모드별로 구분됩니다(예: AE2 가이드는 AppliedEnergistics2 아래에 있습니다). 하지만 지금 읽고 계신 변경 로그처럼 일부 예외도 있습니다!

여기에서 해당 분류를 펼치면 그 분류에 속한 가이드가 표시됩니다. 분류 색인 페이지를 클릭하면 해당 분류의 기본 개요와 모든 하위 페이지로 가는 링크를 볼 수 있습니다.

페이지는 내비게이션 바 오른쪽에서 북마크할 수 있으며, 헤더 바에서 접근하는 홈 페이지에서는 기록과 함께 추천 가이드를 표시합니다!

검색 기능도 내장되어 있어, 별도로 검색하지 않고도 필요한 것을 찾을 수 있습니다.

가이드 작성자는 페이지의 "item_id"로 아이템이나 블록을 설정할 수도 있으며, 그러면 인벤토리나 NEI 자체에서 "가이드를 열려면 [G]를 길게 누르십시오" 문구를 통해 가이드를 열 수 있습니다.

## 기능
기능 목록은 솔직히 여기에 제대로 나열하기에는 너무 길기 때문에, 이 모드에서 표현할 수 있는 아이디어의 범위를 보여주기 위해 다소 무작위로 모은 것들을 봐 주십시오:

<Color id="GREEN">이것은 ~~같은~~ <u>다른</u> ___형식___의 __예시__입니다</Color>

<GameScene width="420" height="280" zoom={3} interactive={true}>
  <ImportStructure src="../assets/reworks/coke_oven.snbt" />
  <ImportPonder src="../assets/reworks/coke_oven.json"/>
</GameScene>

<br clear="all"/>

<Latex tooltip="Look mom! A tooltip!" color="FF55FF" formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: 현재 <Color id="GREEN">흐름</Color> 속도
  - $$\dot{m}^*$$: 최적 흐름 속도
  - $$\eta$$: 효율
</Latex>

<br clear="all"/>

<FunctionGraph title="Efficiency of Fuels Based on Promoter Ratio" xRange="0..2" domain="0..2" xLabel="Combustion Promotor to Fuel Ratio ($$R$$)" yLabel="Efficiency (%)"> <Plot expr="1.5*e^((-0.04)/x)*100" color="#ff55ff" label="Gas/Diesel Fuels (C=0.04)"/>
<Plot expr="1.5*e^((-0.005)/x)*100" color="#ffff55" label="Rocket Fuels (C=0.005)"/>
</FunctionGraph>

<br clear="all"/>

<RecipeFor id="gregtech:gt.blockmachines:15529" input="gregtech:gt.blockmachines:1246"/>

<br clear="all"/>

<GameScene>
  <ImportStructureLib controller="gregtech:gt.blockmachines:9500" />
</GameScene>

## 기술 세부 사항
GuideNH는 <Color id="GREEN">Markdown</Color> 페이지를 사용하며, YAML 프런트매터와 MDX 스타일 런타임 태그를 사용합니다. 페이지는 `_en_us` 같은 언어 폴더 아래에 두어 특정 언어에 속하도록 지정합니다.

태그의 전체 목록과 내비게이션 등의 세부 처리 방식은 [Wiki!](https://github.com/ABKQPO/GuideNH)를 확인하십시오.