每24小时损失总储量1%的能量。
被动损耗上限为每个{var:tierColorName}电容{red:{var:maxPassiveDrain}} EU/t
此后电容每提高1级，被动损耗增加{dark_red:100}倍
被动损耗还需乘以当前维护问题数方为实际损耗。
{gray:{hr}}
外围玻璃等级为最高电容等级-3
添加更多或更换更好的电容可提升电容库容量
{gray:{hr}}
使用螺丝刀右击启用无线模式
仅在多方块结构中有{var:tierColorName}+电容时方可启用无线模式。
启用后每{blue:{var:rebalanceTicks}}刻，电容库会尝试与
无线EU网络进行再平衡。
当电容库中能量低于{red:{var:wirelessEuCap}}（{var:tierColorName}）EU时
将会从网络中抽取能量输入电容库中。
超出此阈值时，则会从电容库中抽取{dark_red:{bold:{underline:全部多余}}}EU并输入到无线网络
这可能会搞坏你的基地，小心点
电容等级每提高1级，此阈值增加{dark_red:100}倍
