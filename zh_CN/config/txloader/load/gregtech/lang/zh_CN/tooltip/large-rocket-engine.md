燃烧{gold:火箭燃料}发电（每秒至少 {var:min_fuel} {var:unit}）
输出功率没有上限，仅受{white:动力仓}大小限制
但在 {aqua:{var:cap1} EU/t} 和 {aqua:{var:cap2} EU/t} 处存在会降低燃料效率的软上限（未增压）
{dark_red:未启用时请勿放入火箭燃料——启动时燃料将被销毁！}
{gray:{hr}}
燃烧过程还需要以下额外输入：
每小时消耗 {aqua:{var:lubricant_amount}{var:unit}} 的{white:{var:lubricant}}（增压时 ×{var:boost}）
每刻消耗相当于当前 EU/t {aqua:{var:air_percent}%} 的{white:空气}（仅通过进气仓输入）
每刻消耗相当于当前 EU/t {aqua:{var:coolant_percent}%} 的{white:{var:coolant}}进行增压（可选）
{gray:{hr}}
若空气耗尽，机器将停机，且必须手动重启
增压会将软上限分别提升至 {aqua:{var:cap1_boosted} EU/t} 和 {aqua:{var:cap2_boosted} EU/t}
预热时间取决于当前输出功率，为 {var:warmup_min}-{var:warmup_max} 秒
{gray:{hr}}
每 {aqua:{var:pollution_unit} EU/t} 产生 {dark_purple:{var:pollution}} 污染
