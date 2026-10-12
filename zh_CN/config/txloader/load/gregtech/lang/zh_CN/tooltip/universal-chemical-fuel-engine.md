燃烧！燃烧！燃烧！
使{yellow:助燃剂}与{gold:燃气}，{gold:柴油}或{gold:火箭燃料}反应，以高达 {aqua:150%} 的效率产生电力
除{white:动力仓}的容量外，输出功率没有软限制或上限
没有助燃剂时不会产生电力
如果{white:动力仓}已满，或输出功率超过其承载能力，多余的电力将被销毁
{gray:{hr}}
效率取决于{yellow:助燃剂}与{gold:燃料}的比例（R）
助燃剂越多，效率越高
效率遵循指数曲线 {aqua:exp(-C/R) * {var:efficiency_ceiling}}，其中{white:C}是由燃料类型决定的常数
{gold:燃气/柴油}：{white:C={var:gas_coefficient}} | {gold:火箭燃料}：{white:C={var:rocket_coefficient}}
{gray:{hr}}
每秒产生 {dark_purple:sqrt(EU/t)} 点污染
