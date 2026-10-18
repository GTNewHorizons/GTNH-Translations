---
item_ids:
    gregtech:gt.blockmachines:1000
navigation:
    title: 工业高炉
    parent: ./tier-lv-index.md
    icon: gregtech:gt.blockmachines:1000
quest_ids:
    - AAAAAAAAAAAAAAAAAAAATQ
---

# 工业高炉

<GameScene interactive={true} wrap="square" align="right" width="380" height="300" >
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_ponder.json" />
</GameScene>

## <ItemImage id="gregtech:gt.blockmachines:1000"/> 工业高炉

```filetree
|-- **来源**:         [GregTech5u](https://github.com/GTNewHorizons/GT5-Unofficial/blob/master/src/main/java/gregtech/common/tileentities/machines/multi/MTEElectricBlastFurnace.java)
|-- **机器类型**:   工业高炉
|-- **等级**:           [LV](./tier-lv-index.md)
|-- **详情**
|   |-- **尺寸**:                   3x3x4
|   |-- **能源仓**:         标准
|   |-- **[超频](../../tierskipping-overcloking-parallels/overclocking.md)**: 有损
|   \-- **污染**:              400 gibbl/s
|-- [Wiki 页面](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)
\-- 任务: <QuestLink id="AAAAAAAAAAAAAAAAAAAATQ==" />
```

<ItemImage id="gregtech:gt.blockmachines:1000" /> **工业高炉**（**EBF**）是一种 [LV](./tier-lv-index.md)等级的[多方块结构](/gtnh-basics/multiblocks.md)，用于以比普通熔炉更高的热量把粉熔炼成锭。

工业高炉是 <ItemImage id="gregtech:gt.blockmachines:140" /> 砖高炉的直接升级版：它以电力而非可燃燃料驱动，并能处理更高级别的材料。

结构中的加热线圈决定了机器的热容量，而能源仓则决定了电压。将两者都升级，即可解锁新配方并让机器[超频](../../tierskipping-overcloking-parallels/overclocking.md)。

工业高炉遵循多方块的标准行为，例如会从消声仓排放污染、偶尔需要维护，以及断电时销毁原料。物品与流体分别通过总线和仓进行输入/输出。

<RecipesFor id="gregtech:gt.blockmachines:1000" input="gregtech:gt.blockcasings:11" />

# 建造
工业高炉的顶层和底层由 <ItemImage id="gregtech:gt.blockcasings:11" /> **隔热机械方块**构成，中间两层则是加热线圈。

加热线圈决定了机器的热容量，且所有线圈必须处于同一等级，结构才能成型。

总线/仓只能替换底层的机械方块，但消声仓除外——它只能放在顶层中央的机械方块上。另一个例外是输出仓：放在底层时收集流体，放在顶层时收集气体。回收气体的数量取决于消声仓的等级。

工业高炉以能源仓的[电压等级](../../power/voltage-tiers.md)运行，但放入两个能源仓即可超频到下一个电压等级。

使用 <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> 来预览/搭建结构，并用子通道 "coil" 指定加热线圈的等级。

| 所需方块 |
|:--------------------------------------------------------------------------------------------|
| 1 <ItemImage id="gregtech:gt.blockmachines:1000" /> **工业高炉**（控制器） |
| 16 <ItemImage id="gregtech:gt.blockcasings5" /> **加热线圈**[^one] |
| 0-15 <ItemImage id="gregtech:gt.blockcasings:11" /> **隔热机械方块** |
| 1+ <ItemImage id="gregtech:gt.blockmachines:41" /> **能源仓**（任意底层机械方块） |
| 1 <ItemImage id="gregtech:gt.blockmachines:90" /> **维护仓**（任意底层机械方块） |
| 1 <ItemImage id="gregtech:gt.blockmachines:91" /> **消声仓**（顶层中央机械方块） |
| 0+ <ItemImage id="gregtech:gt.blockmachines:71" /> **输入总线**（任意底层机械方块） |
| 0+ <ItemImage id="gregtech:gt.blockmachines:51" /> **输入仓**（任意底层机械方块） |
| 0+ <ItemImage id="gregtech:gt.blockmachines:81" /> **输出总线**（任意底层机械方块） |
| 0+ <ItemImage id="gregtech:gt.blockmachines:61" /> **输出仓**（任意顶层/底层机械方块） |
[^one]: 这是一个**分等级**的组件。

> [!WARNING]
> 不支持多安培能源仓和激光能源仓。

## 共享墙体

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right" >
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

工业高炉的每一面都可以与其他结构共享墙体，以节省机械方块、加热线圈和总线/仓。将多台工业高炉并排紧贴是最有效且强烈推荐的做法，因为这样可以省下大量加热线圈，并降低增建工业高炉的成本。

例如，四联共享的工业高炉只需 42 个加热线圈即可建成，而不用完整的 64 个。唯一的缺点是升级加热线圈比较麻烦，因为所有线圈必须处于同一等级，各个结构才能成型。

共享维护仓、输出总线和输入仓也非常有用，但**不要**共享能源仓，因为工业高炉经常需要超频到更高的电压等级，而这会用掉两个能源仓所能提供的最大 4A 电力。把这部分电力分给两台机器根本行不通，会导致其中一台断电。

为了不必把物流管道铺到机器底下就能方便地操作各总线和仓，你可以选择用扳手将控制器方块旋转 90 度，侧向建造四联工业高炉。

> [!CAUTION]
> 格雷科技多方块结构存在一些潜在危险，可能导致其断电甚至 ++**爆炸**++。
> * 不要让工业高炉暴露在雨中。
> * 不要用任何方块、线缆或管道堵住消声仓。
> * 不要超过能源仓的电压等级。
> * 在整个配方运行期间提供稳定的电力。
> * 若启用了防销毁保护，请确保留有空间容纳所有输出。

# 使用
结构成型且所有维护问题都修复完毕后，工业高炉就终于可以投入使用了。不过，尽管玩家此时只能用上 LV 能源仓，却没有 LV 配方；处理 <ItemImage id="gregtech:gt.metaitem.01:11305" /> 钢和 <ItemImage id="gregtech:gt.metaitem.01:11019" /> 铝至少需要 MV 电力。

解决方法是在结构中放入两个能源仓，让机器[超频](../../tierskipping-overcloking-parallels/overclocking.md)到下一个电压等级。能源仓通常只抽取 1A 电力，但在这种情况下最多可抽取 2A。这意味着两个能源仓可以抽取 4A 电力，相当于下一个电压等级的 1A。

要持续供应 4A 电力，附近至少需要四台[单方块](../../singleblock/singleblock-index.md) <ItemImage id="gregtech:gt.blockmachines:1115" /> 蒸汽轮机。钢和铝的配方只消耗 120 EU/t，因此可以容忍一些线损，但不能太多。

以下是满足这些供电需求并运行工业高炉的两种方法。两种方法都假设玩家**没有**使用超导导线——无论电流大小或距离远近，超导导线的线损都为零。

## 方法一：将线损降至最低
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

在能源仓附近放置<u>四</u>台蒸汽轮机，把损耗降到最低。
* 只需要四台蒸汽轮机。
* 无法为其他机器供电。
* 线损较低。

## 方法二：缓冲线损
<GameScene interactive={true} width="240" height="240" zoom="1.5">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

在能源仓附近放置一个带 4 个以上槽位的 <ItemImage id="gregtech:gt.blockmachines:171" /> 电池箱，用额外的蒸汽轮机来弥补线损。
* 需要五台或更多蒸汽轮机。
* 需要电池与高安培线缆。
* 可以为其他机器供电。
* 线损较高。

## 热容量
结构中内置的加热线圈决定了工业高炉的热容量，进而决定了它能运行哪些配方。对控制器使用 <ItemImage id="gregtech:gt.metaitem.01:32762" /> 便携式扫描仪可查看其当前热容量；使用 [NEI](/introduction/introduction-index.md) 可查看配方的最低热容量。

例如，一台白铜线圈的工业高炉热容量为 1,801K，足以熔炼钢（1,000K）和铝（1,300K），但**不足以**处理 <ItemImage id="gregtech:gt.metaitem.01:11856" /> 太阳能级硅（2,273K）。此外，MV 以上每高一个电压等级，热容量还会获得 +100K 加成，如下图所示：

<LineChart title="温度加成" categories="LV,MV,HV,EV,IV,LuV,ZPM,UV,UHV,UEV,UIV,UMV,UXV,MAX,MAX+" yAxisUnit="K" width="600">
  <Series name="Heat" data="0,0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300" color="#E15759"/>
</LineChart>

超出配方的最低热容量可获得两种相互独立的加成。第一种是每超出 900K 获得 5% 的能耗折扣（**乘算**）。第二种是每超出 1,800K 获得[无损超频](../../tierskipping-overcloking-parallels/overclocking.md#perfect-overclocking-44)。后者尤为强力，因为工业高炉通常执行的是有损超频，在相同耗电之下效果只有一半。

> [!NOTE]
> *有损超频* - 消耗 4 倍电力换取 2 倍速度（4/2）。
> *无损超频* - 消耗 4 倍电力换取 4 倍速度（4/4）。

例如，假设使用 HV 电力和 <ItemImage id="gregtech:gt.blockcasings5:2" /> **镍铬合金线圈方块**熔炼 <ItemImage id="TConstruct:materials:12" /> **生铝**（1,300K）。含氮气的基础配方在 60 秒内消耗 144,000 EU，速率为 120 EU/t。该工业高炉的热容量为 3,701K，恰好比配方的最低热容量高出 2,401K。这意味着可获得两次 5% 能耗折扣和一次无损超频。最终配方只需在 15 秒内消耗 130,200 EU，速率为 120 EU/t x 0.95 x 0.95 x 4 = 434 EU/t。

> [!TIP]
> * 可以放置不止一个输入总线/输入仓，这对存放各种流体输入（例如氢气、氧气、氮气、氦气）很有用。到 EV 解锁四重输入仓后，它也非常好用。
> * 强烈建议随着需求增长而增建更多工业高炉。GTNH 有意把配方时间设得很长，以迫使玩家扩建自己的基础设施。
> * 同一种材料往往有不止一个配方，因此请定期翻阅 [NEI](/introduction/introduction-index.md)，找出最适合你的那一个。例如，大多数锭都有与各种稀有气体搭配的配方来缩短熔炼时间；钢可以用熟铁粉代替铁粉来制作，从而获得显著的时间和能耗折扣。
> * 一台熔炼熟铁粉的 MV 工业高炉制钢速度相当于 48 座砖高炉，而且它还能进一步超频。

# 故障排除
## 结构不完整
检查结构是否满足所有最低要求（机械方块数量、一个维护仓、一个消声仓，以及一个或更多能源仓）。如果一切齐备，请尝试在控制器 GUI 中强制进行一次结构检查。另外检查工业高炉内部没有多余的东西，例如不可见的照明方块。

## 无法启动
检查配方是否正确（物品、流体和编程电路）。同时检查消声仓没有被方块、线缆或管道堵住。工业高炉完全没有收到电力时也可能出现这一问题。检查线缆是否连接妥当，以及所有蒸汽轮机的朝向是否正确。

## 运行一秒后停机并销毁原料
检查 EU 供应是否充足。线损可能过大，或者蒸汽轮机数量不足。另外检查各高级消声仓中是否装有空气滤网。

## 输出空间不足。
检查输出总线/输出仓是否已满。配方也可能正尝试输出气体，这需要在结构顶层放置输出仓；而流体输出则需要输出仓放在结构底层。如果某个输出并不特别重要，可以尝试为物品、流体或两者启用销毁模式。