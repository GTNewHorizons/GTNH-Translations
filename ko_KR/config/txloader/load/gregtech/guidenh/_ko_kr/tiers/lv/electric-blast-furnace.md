---
item_ids:
    gregtech:gt.blockmachines:1000
navigation:
    title: 전기 용광로
    parent: ./tier-lv-index.md
    icon: gregtech:gt.blockmachines:1000
quest_ids:
    - AAAAAAAAAAAAAAAAAAAATQ
---

# 전기 용광로

<GameScene interactive={true} wrap="square" align="right" width="380" height="300" >
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_ponder.json" />
</GameScene>

## <ItemImage id="gregtech:gt.blockmachines:1000"/> 전기 용광로

```filetree
|-- **출처**:         [GregTech5u](https://github.com/GTNewHorizons/GT5-Unofficial/blob/master/src/main/java/gregtech/common/tileentities/machines/multi/MTEElectricBlastFurnace.java)
|-- **기계 유형**:   용광로
|-- **티어**:           [LV](./tier-lv-index.md)
|-- **세부 정보**
|   |-- **크기**:                   3x3x4
|   |-- **에너지 해치**:         일반
|   |-- **[오버클록](../../tierskipping-overcloking-parallels/overclocking.md)**: 불완전
|   \-- **오염**:              400 gibbl/s
|-- [위키 페이지](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)
\-- 퀘스트: <QuestLink id="AAAAAAAAAAAAAAAAAAAATQ==" />
```

<ItemImage id="gregtech:gt.blockmachines:1000" /> **전기 용광로**(**EBF**)는 일반 화로보다 높은 열로 가루를 주괴로 제련하는 [LV](./tier-lv-index.md) 티어의 [다중 블록](/gtnh-basics/multiblocks.md) 기계입니다.

EBF는 <ItemImage id="gregtech:gt.blockmachines:140" /> 벽돌 용광로의 직접적인 상위 기계입니다. 가연성 연료 대신 전기를 사용하며 더 높은 티어의 재료를 처리할 수 있습니다.

구조물의 가열 코일은 기계의 열 용량을 결정하고, 에너지 해치는 전압을 결정합니다. 두 부품을 모두 업그레이드하면 새로운 제조법을 해금하고 기계를 [오버클록](../../tierskipping-overcloking-parallels/overclocking.md)할 수 있습니다.

EBF는 머플러 해치로 오염을 배출하고, 가끔 유지보수가 필요하며, 전력 공급이 끊기면 재료를 소멸시키는 등 일반적인 다중 블록 기계의 작동 방식을 따릅니다. 아이템과 유체는 각각 버스와 해치를 통해 삽입하고 추출합니다.

<RecipesFor id="gregtech:gt.blockmachines:1000" input="gregtech:gt.blockcasings:11" />

# 건설

EBF는 위쪽과 아래쪽 층에 <ItemImage id="gregtech:gt.blockcasings:11" /> **내열 기계 케이싱**을 설치하고, 가운데 두 층에 가열 코일을 설치하여 건설합니다.

가열 코일이 기계의 열 용량을 결정하며, 구조물이 형성되려면 모든 가열 코일이 같은 티어여야 합니다.

버스와 해치는 아래쪽 층의 케이싱만 교체할 수 있습니다. 단, 머플러 해치는 위쪽 중앙 케이싱으로 위치가 제한됩니다. 또 다른 예외로 출력 해치는 아래쪽 층에서는 유체를, 위쪽 층에서는 기체를 수집합니다. 회수되는 기체의 양은 머플러 해치의 티어에 따라 달라집니다.

EBF는 에너지 해치의 [전압 티어](../../power/voltage-tiers.md)로 작동하지만, 에너지 해치 두 개를 설치하면 다음 전압 티어로 오버클록할 수 있습니다.

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" />를 사용하고 하위 채널 "coil"을 지정하면 가열 코일의 티어에 맞춰 구조물을 확인하거나 건설할 수 있습니다.

| 필요 구성                                                                                    |
|:--------------------------------------------------------------------------------------------|
| 1 <ItemImage id="gregtech:gt.blockmachines:1000" /> **전기 용광로**(컨트롤러) |
| 16 <ItemImage id="gregtech:gt.blockcasings5" /> **가열 코일**[^one]                      |
| 0-15 <ItemImage id="gregtech:gt.blockcasings:11" /> **내열 기계 케이싱**           |
| 1+ <ItemImage id="gregtech:gt.blockmachines:41" /> **에너지 해치**(아래쪽 케이싱 아무 곳)     |
| 1 <ItemImage id="gregtech:gt.blockmachines:90" /> **유지보수 해치**(아래쪽 케이싱 아무 곳) |
| 1 <ItemImage id="gregtech:gt.blockmachines:91" /> **머플러 해치**(위쪽 중앙 케이싱)     |
| 0+ <ItemImage id="gregtech:gt.blockmachines:71" /> **입력 버스**(아래쪽 케이싱 아무 곳)        |
| 0+ <ItemImage id="gregtech:gt.blockmachines:51" /> **입력 해치**(아래쪽 케이싱 아무 곳)      |
| 0+ <ItemImage id="gregtech:gt.blockmachines:81" /> **출력 버스**(아래쪽 케이싱 아무 곳)       |
| 0+ <ItemImage id="gregtech:gt.blockmachines:61" /> **출력 해치**(위쪽 또는 아래쪽 케이싱 아무 곳) |
[^one]: **티어가 있는** 부품입니다.

> [!WARNING]
> 다중 암페어 및 레이저 에너지 해치는 지원되지 않습니다.

## 벽 공유

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right" >
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

EBF는 케이싱, 가열 코일, 버스와 해치를 절약하기 위해 각 측면을 벽 공유할 수 있습니다. EBF를 나란히 겹쳐 배치하는 방식이 가장 효과적이며 강력히 권장됩니다. 가열 코일을 상당히 절약하고 추가 EBF의 비용을 줄일 수 있기 때문입니다.

예를 들어 4중 공유 EBF는 완전한 구조에 필요한 64개 대신 가열 코일 42개만으로 건설할 수 있습니다. 유일한 단점은 가열 코일을 업그레이드하기 어렵다는 점입니다. 구조물이 형성되려면 모든 가열 코일이 같은 티어여야 하기 때문입니다.

유지보수 해치, 출력 버스, 입력 해치를 공유하는 것도 유용하지만, 에너지 해치는 공유하지 마십시오. EBF는 더 높은 전압 티어로 오버클록해야 하는 경우가 많으며, 이때 에너지 해치 두 개에서 최대 4A를 사용하기 때문입니다. 이를 두 기계에 나누어 공급하는 것은 불가능하며, 한쪽의 전력 공급이 끊기게 됩니다.

기계 아래로 물류를 연결하지 않고도 버스와 해치에 쉽게 접근하려면, 렌치로 컨트롤러 블록을 90도 회전한 뒤 4중 EBF를 옆으로 건설할 수 있습니다.

> [!CAUTION]
> GregTech 다중 블록에는 전력 공급이 끊기거나 심지어 ++**폭발**++을 일으킬 수 있는 위험 요소가 있습니다.
> * EBF를 비에 노출하지 마십시오.
> * 머플러 해치를 어떤 블록, 케이블 또는 파이프로도 막지 마십시오.
> * 에너지 해치의 전압 티어를 초과하지 마십시오.
> * 제조법이 진행되는 동안 지속적으로 전력을 공급하십시오.
> * 소멸 방지 기능이 활성화되어 있다면 출력물을 위한 공간이 있는지 확인하십시오.

# 사용법

구조물이 형성되고 모든 유지보수 문제가 해결되면 EBF를 사용할 준비가 완료됩니다. 하지만 플레이어가 LV 에너지 해치만 사용할 수 있음에도 LV 제조법은 없습니다. <ItemImage id="gregtech:gt.metaitem.01:11305" /> 강철과 <ItemImage id="gregtech:gt.metaitem.01:11019" /> 알루미늄을 처리하려면 최소 MV 전력이 필요합니다.

해결 방법은 에너지 해치 두 개를 구조물에 설치하여 기계를 다음 전압 티어로 [오버클록](../../tierskipping-overcloking-parallels/overclocking.md)하는 것입니다. 에너지 해치는 일반적으로 전력을 1A만 끌어오지만, 이와 같은 상황에서는 최대 2A까지 끌어올 수 있습니다. 따라서 에너지 해치 두 개는 4A의 전력을 끌어오며, 이는 다음 전압 티어의 1A에 해당합니다.

지속적으로 4A의 전력을 공급하려면 근처에 최소 네 대의 [단일 블록](../../singleblock/singleblock-index.md) <ItemImage id="gregtech:gt.blockmachines:1115" /> 증기 터빈이 필요합니다. 강철과 알루미늄 제조법은 120 EU/t만 소비하므로 케이블 손실이 약간 발생해도 괜찮지만, 손실이 너무 커서는 안 됩니다.

다음은 이러한 전력 요구 사항을 충족하여 EBF를 작동시키는 두 가지 방법입니다. 두 방법 모두 암페어 또는 거리에 관계없이 케이블 손실이 0인 초전도체 전선을 **사용하지 않는다는** 전제하에 설명합니다.

## 방법 1: 케이블 손실 최소화
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

손실을 최소화하려면 에너지 해치 가까이에 증기 터빈 <u>네 대</u>를 배치하십시오.
* 증기 터빈 네 대만 필요합니다.
* 다른 기계에는 전력을 공급할 수 없습니다.
* 케이블 손실이 더 적습니다.

## 방법 2: 케이블 손실 완충
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

에너지 해치 근처에 슬롯이 4개 이상인 <ItemImage id="gregtech:gt.blockmachines:171" /> 배터리 버퍼를 설치하고, 추가 터빈으로 손실을 보충하십시오.
* 증기 터빈이 다섯 대 이상 필요합니다.
* 배터리와 고암페어 케이블이 필요합니다.
* 다른 기계에도 전력을 공급할 수 있습니다.
* 케이블 손실이 더 큽니다.

## 열 용량

구조물에 설치된 가열 코일이 EBF의 열 용량을 결정하며, 이에 따라 작동할 수 있는 제조법도 결정됩니다. 컨트롤러에 <ItemImage id="gregtech:gt.metaitem.01:32762" /> 휴대용 스캐너를 사용하면 현재 열 용량을 확인할 수 있으며, 제조법의 최소 열 용량은 [NEI](/introduction/introduction-index.md)에서 확인할 수 있습니다.

예를 들어 백동 EBF의 열 용량은 1,801K로, 강철(1,000K)과 알루미늄(1,300K)을 제련하기에는 충분하지만 <ItemImage id="gregtech:gt.metaitem.01:11856" /> 태양광급 실리콘(2,273K)에는 **충분하지 않습니다**. 또한 다음 표와 같이 MV 이후의 각 전압 티어마다 +100K의 열 보너스가 있습니다.

<LineChart title="Heat Bonus" categories="LV,MV,HV,EV,IV,LuV,ZPM,UV,UHV,UEV,UIV,UMV,UXV,MAX,MAX+" yAxisUnit="K" width="600">
  <Series name="Heat" data="0,0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300" color="#E15759"/>
</LineChart>

제조법의 최소 열 용량을 초과하면 두 가지 별도 보너스를 얻습니다. 첫 번째는 900K를 초과할 때마다 에너지 소비량이 5% 감소하는 보너스이며, **곱연산**으로 적용됩니다. 두 번째는 1,800K를 초과할 때마다 [완벽한 오버클록](../../tierskipping-overcloking-parallels/overclocking.md#perfect-overclocking-44)이 적용되는 것입니다. EBF는 일반적으로 같은 전력으로 불완전한 오버클록을 수행하며 효율이 절반이므로, 후자의 효과가 특히 강력합니다.

> [!NOTE]
> *불완전한 오버클록* - 2배의 속도로 4배의 전력을 소비합니다(4/2).
> *완벽한 오버클록* - 4배의 속도로 4배의 전력을 소비합니다(4/4).

예를 들어 HV 전력과 <ItemImage id="gregtech:gt.blockcasings5:2" /> **니크롬 코일**을 사용하여 <ItemImage id="TConstruct:materials:12" /> **알루미늄 원석**(1,300K)을 제련한다고 가정해 보겠습니다. 질소를 사용하는 기본 제조법은 60초 동안 144,000 EU를 소비하며, 소비율은 120 EU/t입니다. EBF의 열 용량은 3,701K이며, 이는 제조법의 최소 열 용량보다 정확히 2,401K 높습니다. 따라서 에너지 소비량 5% 감소가 두 번 적용되고 완벽한 오버클록이 한 번 적용됩니다. 그 결과 제조법은 15초 동안 130,200 EU만 소비하며, 소비율은 120 EU/t x 0.95 x 0.95 x 4 = 434 EU/t가 됩니다.

> [!TIP]
> * 입력 버스와 입력 해치는 여러 개 설치할 수 있으며, 다양한 유체 입력물(예: 수소, 산소, 질소, 헬륨)을 보관할 때 유용합니다. EV에서 해금되는 4중 입력 해치도 매우 효과적입니다.
> * 재료 수요가 증가하면 EBF를 추가로 건설하는 것이 강력히 권장됩니다. GTNH의 제조법 시간은 플레이어가 기반 시설을 확장하도록 의도적으로 길게 설정되어 있습니다.
> * 같은 재료에도 제조법이 여러 개 있는 경우가 많으므로, 주기적으로 [NEI](/introduction/introduction-index.md)를 확인하여 자신에게 가장 적합한 제조법을 찾으십시오. 예를 들어 대부분의 주괴는 각 희가스마다 제련 시간이 짧아지는 제조법이 있으며, 강철은 철 가루 대신 연철 가루로 제작하면 시간과 에너지를 크게 절약할 수 있습니다.
> * 연철 가루를 제련하는 MV EBF는 강철을 만드는 데 벽돌 용광로 48대와 같은 속도를 내며, 그 이상으로 오버클록할 수도 있습니다.

# 문제 해결
## 불완전한 구조

최소 요구 사항을 모두 충족하는지 확인하십시오. 케이싱 수, 유지보수 해치 하나, 머플러 해치 하나, 에너지 해치 하나 이상이 필요합니다. EBF에 모든 부품이 있다면 컨트롤러의 GUI에서 구조물 검사를 강제로 실행해 보십시오. 또한 보이지 않는 조명 블록 등 EBF 내부에 아무것도 없는지 확인하십시오.

## 작동하지 않음

제조법이 올바른지 확인하십시오. 아이템, 유체, 프로그래밍된 회로를 확인해야 합니다. 또한 머플러 해치가 블록, 케이블 또는 파이프로 막혀 있지 않은지 확인하십시오. EBF에 전력이 전혀 공급되지 않아도 이 문제가 발생할 수 있습니다. 케이블이 연결되어 있는지, 증기 터빈이 올바른 방향을 향하고 있는지 확인하십시오.

## 1초 동안 작동한 후 꺼지고 재료가 소멸됨

충분한 EU가 공급되고 있는지 확인하십시오. 케이블 손실이 너무 크거나 증기 터빈이 부족할 가능성이 있습니다. 또한 고급 머플러에 공기 필터가 설치되어 있는지 확인하십시오.

## 출력 공간 부족

출력 버스 또는 출력 해치가 가득 차 있지 않은지 확인하십시오. 유체 출력에는 구조물 아래쪽 층의 출력 해치가 필요하지만, 제조법에서 구조물 위쪽 층의 출력 해치가 필요한 기체를 출력하려는 것일 수도 있습니다. 출력물 중 하나가 특별히 중요하지 않다면 아이템, 유체 또는 둘 다에 대해 소멸 모드를 활성화해 보십시오.