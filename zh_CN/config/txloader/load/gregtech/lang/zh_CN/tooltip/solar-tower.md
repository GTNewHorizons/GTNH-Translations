为未来贡献绿色能源
在周围建造 1-5 环{white:太阳能反射器}以产生热量
太阳能反射器越多，热量越高，整体冷却液吞吐量也越大
最大热量为 100,000，但达到该上限没有任何风险或危险
{gray:{hr}}
每 {var:cycle} 秒按 1:1 的比例将{blue:冷太阳能盐}转化为{red:热太阳能盐}
每转化 1{var:unit}，热量降低 1，直到热量降至零
多余的冷太阳能盐不会被消耗
{gray:{hr}}
仅当{white:热量 >=} {red:{var:threshold}}且{white:效率 =} {aqua:100%}时才会发生转化
效率初始为 {aqua:0%}，每 10 秒提高 {aqua:+1%}
{gray:{hr}}
{white:热量效率 =} {red:1 - (热量 - {var:center})^{var:exp} / {var:coefficient}}，峰值位于 {red:{var:center}}
{white:每循环热量 =} {red:反射器数量 * 热量效率 * ({var:loss} + 2^(环数 - 1)) - {var:loss}}
{yellow:下雨时热量获取减半，夜晚时停止}
