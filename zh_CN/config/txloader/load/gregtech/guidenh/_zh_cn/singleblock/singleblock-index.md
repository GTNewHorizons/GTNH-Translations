---
navigation:
  title: "单方块机器"
  icon: gregtech:gt.blockmachines:106
  parent: /index.md
  position: 10
---

# 单方块机器

单方块机器仅由一个方块构成。它们的用途有限，而且只要存在对应的[多方块机器](../multiblocks/multiblocks_index.md)，它们就总是更慢或效率更低。它们无法升级（高压蒸汽机器除外），因此替换它们总是意味着重新合成一台新机器。尽管如此，它们对前期进度不可或缺，其中一些在整个游戏中始终有用。到了 EV 至 IV 阶段，当大多数[多方块机器](../multiblocks/multiblocks_index.md)解锁后，玩家便会逐渐弃用单方块机器。

# 机器朝向

每台单方块机器，无论是蒸汽还是电力，都有两个特殊面和四个普通面。可以使用 <ItemLink id="gregtech:gt.metatool.01:16" showIcon="left" /> 更改其朝向，遵循格雷科技 3x3 扳手规则。

- **正面**：外观上最具辨识度的面，且只能朝向水平方向。它完全不能输入或输出物品、流体、蒸汽或电力。
  - 手持扳手，对任意侧面 <kbd>Shift</kbd> + <kbd>右键</kbd> 可改变正面方向。
- **输出面**：黑色背景上带小白框端口的那个面。
  - 对蒸汽机器而言，这是排放废蒸汽压力的排气口。
  - 对电力机器而言，这是用于弹出产物的物品输出面。
  - 手持扳手，对任意侧面 <kbd>右键</kbd> 可改变输出面。
- **其余各面**：剩下的四个面彼此等效，可以输入或输出物品、流体、蒸汽或电力。

# 蒸汽机器

单方块蒸汽机器以蒸汽为动力，在蒸汽时代被大量使用。蒸汽由锅炉产生。每个标准版本都有对应的钢制高压版本。

蒸汽机器不会爆炸，不受雨雪影响，可以安全地放置在室外。

## 类别

单方块蒸汽机器只有六种，每种都有标准版和高压版：

| 功能 | 标准版 | 高压版 |
|----------|----------|---------------|
| 熔炉 | <ItemLink id="gregtech:gt.blockmachines:103" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:104" showIcon="left" /> |
| 合金炉 | <ItemLink id="gregtech:gt.blockmachines:118" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:119" showIcon="left" /> |
| 压缩机 | <ItemLink id="gregtech:gt.blockmachines:115" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:116" showIcon="left" /> |
| 研磨机 | <ItemLink id="gregtech:gt.blockmachines:106" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:107" showIcon="left" /> |
| 提取机 | <ItemLink id="gregtech:gt.blockmachines:109" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:110" showIcon="left" /> |
| 锻造锤 | <ItemLink id="gregtech:gt.blockmachines:112" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmachines:113" showIcon="left" /> |

## 图形界面

- **蒸汽表**：位于左上角，显示内部蒸汽缓冲。所有蒸汽机器都有 16,000 L 的内部缓冲。
- **存储槽位**：底部的两个槽位，没有特殊行为。
- **静音按钮**：位于右上角。也可以手持 <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> <kbd>右键</kbd>机器来切换。

蒸汽机器不支持自动输出。

## 能量

机器从既非正面也非排气口的四个面接受蒸汽，填入内部缓冲。它以 4 L 蒸汽 = 1 EU 的比例运行 LV 级配方，即 50% 效率。青铜机器的运行时长是 LV 配方正常时长的两倍。

| 机器类型 | 蒸汽消耗 (L/t) | 时长 |
|--------------|------------|----------|
| 蒸汽机器 | 2x | 2x |
| 高压蒸汽机器 | 4x | 1x |

高压版本以两倍速率消耗蒸汽并将配方时长减半，相当于执行一次 2/2 无损[超频](../tierskipping-overcloking-parallels/overclocking.md)。

手持 <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> <kbd>右键</kbd>机器即可暂停或恢复运行。

## 物品运输与排气

除正面和排气口之外的四个面都可以输入或输出。蒸汽机器无法自行弹出物品，因此需要漏斗或其他运输系统来取出产物。

排气口是蒸汽机器的输出面。每次配方完成后，机器必须通过该面排出废气。如果排气口被堵住，机器就无法完成配方。配方完成时站在排气口旁边会对玩家造成 3.5 颗心的伤害。

## 故障

- 排气口被堵塞 -> 会出现故障图标，在废气排出之前机器不会继续运行。
- 蒸汽缓冲耗尽 -> 会出现故障图标。如果蒸汽缓冲随后很快得到补充，机器会重试该配方。如果蒸汽供应根本不足，机器可能反复失败、丢失全部进度并浪费蒸汽。

# 电力机器

> [!WARNING]
> 单方块电力机器可能会爆炸。请仔细阅读[爆炸](#explosions)一节。

单方块电力机器是 LV 阶段第一批必须合成的机器。它们有特定用途、固定的电压等级，升级时必须整体更换。

## 图形界面

电力机器的图形界面比蒸汽机器更复杂：

- **物品输入/输出槽位**：进度条两侧的浅色槽位。
- **流体输入/输出槽位**：物品槽位下方的深色槽位。手持容器时可直接与其交互：<kbd>左键</kbd>会装满或清空所有匹配的流体容器，而 <kbd>右键</kbd>只处理一个容器。
- **电力槽位**：接受同电压的工具或电池。当内部缓冲足够满时会为其充电；当缓冲不足时可以从中取电。它也可以当作普通存储槽位使用。
- **数据槽位**：只出现在扫描仪、打印机、复印机等特殊机器上。
- **集成电路槽位**：位于右下角。滚动<kbd>鼠标滚轮</kbd>或点击可调高或调低电路编号；<kbd>Shift</kbd> + <kbd>左键</kbd>打开选择器界面；<kbd>Shift</kbd> + <kbd>右键</kbd>可清除。
- **自动输出开关**：左下角的两个按钮。启用后，机器可以弹出物品或流体。蒸汽机器没有此功能。
- **静音按钮**：位于右上角。也可以手持 <ItemLink id="gregtech:gt.metatool.01:12" showIcon="left" /> <kbd>右键</kbd>机器来切换。

## 能量

电力机器以 EU 运行。它们有一个小型内部 EU 缓冲，大小等于机器电压（EU）的 64 倍，即 1A 标准电压在 3.2 秒内消耗的电量。例如，LV 机器存储 2,048 EU，而 HV 机器存储 32,768 EU。

机器持续从本地电力网络请求能量包来填满缓冲。它们的最大输入电流为：

$$\text{Maximum Input Current} = \left\lfloor\frac{\text{Recipe Rated Power} \times 2}{\text{Machine Operating Voltage}}\right\rfloor + 1 \text{ A}$$

- 大多数单方块机器：最大 2A。
- 热力离心机：最大 4A。
- 电弧炉：最大 6A。

手持 <ItemLink id="gregtech:gt.metatool.01:14" showIcon="left" /> <kbd>右键</kbd>机器即可暂停或恢复运行。

## 超频

单方块电力机器使用 4/2 非完美超频：每次超频使耗电量乘以 4、配方时间减半，因此总能耗翻倍。单方块质量发生器是唯一例外，使用 2/2 无损超频。

完整系统请参阅**[超频](../tierskipping-overcloking-parallels/overclocking.md)**。

## 物流

除正面之外的五个面都可以输出。既非正面也非输出面的四个面可以输入。

- **自动输出**：在图形界面中启用自动输出开关后，输出面即可弹出物品或流体。
- **允许从输出面输入**：手持 <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> 并对正面或输出面 <kbd>右键</kbd>来切换。
- **输入过滤**：手持螺丝刀并对正面或输出面 <kbd>Shift</kbd> + <kbd>右键</kbd>来启用。启用后，输入物品会按配方映射进行过滤。
- **输入堆叠**：手持 <ItemLink id="Forestry:solderingIron" showIcon="left" /> 并对正面 <kbd>Shift</kbd> + <kbd>右键</kbd>来启用，允许同一槽位容纳多种物品。

## 故障

当内部 EU 缓冲耗尽时，机器会失败。配方进度会丢失，但输入状态会保留。如果缓冲随后很快得到补充，机器会重试该配方。如果供电本身不足，机器可能反复失败、丢失进度并浪费 EU。

## 爆炸

单方块电力机器在以下情况下会爆炸：

- **过压**：如果接收到高于自身电压的能量包，会立即爆炸。例如，向 LV 机器输入 MV 能量包。
- **火焰**：如果机器存储的 EU 超过容量的 20%，则每个游戏刻以 1/1000 的概率检查一次。若任一面处于着火状态，机器会爆炸。
- **雨雪**：如果机器存储了 EU，同样每个游戏刻以 1/1000 的概率检查一次。下雨时，有 1/10 的概率立即爆炸、9/10 的概率起火；雷暴时，有 1/3 的概率立即爆炸。
- 爆炸会将所有存储的 EU 以 IV 级电力释放到每根相连的线缆或相邻机器上，可能引发连锁爆炸或使附近线缆过载。
- [多方块机器](../multiblocks/multiblocks_index.md)上的通电仓也可能因相同原因起火或爆炸。
