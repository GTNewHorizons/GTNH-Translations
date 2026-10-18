将电极插入 {green:电极仓}
速度、并行数、超频及能耗均取决于电极
部分电极具有特殊效果，请查看其提示信息
耐久度低于 {red:{var:surge_threshold}%} 时：有 {red:{var:surge_chance}%} 几率触发一次 {dark_red:电弧浪涌}
每次执行配方前起弧，起弧功率随电极惩罚和并行数缩放
工作结束后灭弧
{gray:{hr}}
{gold:高炉模式}：
以 {green:{var:blast_power_multiplier}倍}的能耗处理{white:工业高炉}配方
{gray:{hr}}
{gold:矿石模式}：
将金属矿石加工为熔融金属
启动时间：{green:{var:ore_startup_seconds}} 秒
消耗{green:输入总线}中的所有矿石和粗矿
若所有并行均被占用，启动立即结束
若在 {green:{var:ore_idle_ticks}} 刻内没有矿石输入，启动立即结束
产出{gold:熔融金属}
{yellow:仅限可用熔炉熔炼的矿石，无需高炉处理}
{gray:{hr}}
手持{white:螺丝刀}右键以切换模式
