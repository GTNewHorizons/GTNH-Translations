输入为{red:岩浆}、{red:热冷却液}、{red:热太阳能盐}或{red:等离子体}
输出为{blue:熔岩岩浆}、{blue:IC2冷却液}、{blue:冷太阳能盐}或{blue:熔融金属}
过程中将蒸馏水转化为{white:过热蒸汽}或{white:超临界蒸汽}
若高温流体输入速率超过特定{light_purple:阈值}，则输出{white:超临界蒸汽}
蒸馏水耗尽时会立即爆炸
{gray:{hr}}
{red:熔岩} | 超临界阈值 {light_purple:80,000 {var:unit}/s} | 最大输入 {red:160,000 {var:unit}/s} | 最大输出 {white:640,000 {var:unit}/t 超临界蒸汽}
{red:热冷却液} | 超临界阈值 {light_purple:8,000 {var:unit}/s} | 最大输入 {red:128,000 {var:unit}/s} | 最大输出 {white:1,280,000 {var:unit}/t 超临界蒸汽}
{red:热太阳能盐} | 超临界阈值 {light_purple:1,600 {var:unit}/s} | 最大输入 {red:3,200 {var:unit}/s} | 最大输出 {white:160,000 {var:unit}/t 超临界蒸汽}
{gray:{hr}}
{red:等离子体}无论输入速率如何，始终输出{white:致密超临界蒸汽}
最大输入与输出速率取决于等离子体的密度（EU/L）
{gray:{hr}}
控制器中的电路能以降低蒸汽产量为代价来降低超临界阈值
每超过1个电路，{light_purple:-150 {var:unit}/s} 超临界阈值和{white:-1.5%}蒸汽输出
