每次运行消耗最多 {green:{var:fuel_percent}%} 的{white:燃料}
为开始运行，其中至少 {green:{var:min_helium}%} 为{gold:氦}
{gold:氦}可使热交换器效率线性提升，最大容量时可达{green:100%}
反应堆每次运行损失{green:{var:helium_lost}%}的{gold:氦}
消耗 {aqua:{var:power} EU/t}，缺少{gold:氦}时消耗量将增加最多 {green:{var:power_penalty}倍} 
{gray:{hr}}
单次运行时长取决于反应堆填充水平（x%）
介于 {green:{var:min_time}} 秒与 {green:{var:max_time}} 秒之间
其 {green:10%} 为固定值，{green:90%} 取决于公式 y=1-(1-x)^3(x为填充百分比)
每个维护问题会使冷却效率降低 {green:20%} 
{gray:{hr}}
提供{gold:冷却液}/ {gold:水}/两者均可加速配方进程，
加速值为每秒{green:{var:coolant_speedup}%} / {green:{var:water_speedup}%} / {green:{var:total_speedup}%}
达到最大加速效果所需的流体量随{gold:TRISO燃料丸数量}而变化
每燃料丸每秒消耗{green:{var:coolant_per_ball}}{gold:冷却液}和{green:{var:water_per_ball}} {gold:蒸馏水}
