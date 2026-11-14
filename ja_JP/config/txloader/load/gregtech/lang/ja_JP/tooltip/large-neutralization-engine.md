全部の問題を解(溶)きましょう！
{gray:{hr}}
必要に応じて {aqua:塩基} を追加して、{light_purple:効率} を高めることができます
{aqua:{var:sodium_hydroxide_rate}/min}の{aqua:水酸化ナトリウム} : {light_purple:{var:sodium_hydroxide_eff}%}
{aqua:{var:potassium_hydroxide_rate}/min}の{aqua:水酸化カリウム} : {light_purple:{var:potassium_hydroxide_eff}%}
{aqua:{var:caesium_hydroxide_rate}/min}の{aqua:水酸化セシウム} : {light_purple:{var:caesium_hydroxide_eff}%}
{aqua:{var:francium_hydroxide_rate}/min}の{aqua:水酸化フランシウム} : {light_purple:{var:francium_hydroxide_eff}%}
{gray:{hr}}
酸を消費することで{dark_green:有毒な残留物}が発生します
{dark_green:有毒な残留物}が{dark_aqua:容量}を超過すると機械が{red:爆発}します
毎Tick、{dark_green:有毒な残留物}が{green:0.05 * 燃料密度 (EU/L)^0.8 * 燃料消費 ({var:fluid_unit}) * {var:residue_rand_min}～{var:residue_rand_max}の乱数 }増加
毎Tick、{dark_green:有毒な残留物}が{green:崩壊係数 * 崩壊強化 * 有毒な残留物^0.08}減少
{yellow:有毒な残留物はマルチブロックが無効な場合、10分の1の速度で減少します}
{gray:{hr}}
{blue:崩壊強化}は{blue:ロボットアーム}を挿入すると、{blue:16個を}上限に増加します
{white:崩壊強化 =} {green:(ロボットアームの個数)の平方根 * N^(ロボットアームのTier - 1)} :Nの値は{var:tier_iv}§7以下の場合{green:1.2}、{var:tier_luv}§7以上の場合{green:1.4}
毎分{green:ロボットアームの個数 / (45 * (ロボットアームのTier + 1))}の確率で、1つ{blue:ロボットアーム}が減少
{gray:{hr}}
この構造物は{gold:3段階のTier}を持ち、{blue:崩壊係数}と{dark_aqua:容量}を決定します
{gold:T1} : {gold:強化無機質マシン外装} : {blue:{var:tier1_decay}} : {dark_aqua:{var:tier1_capacity}}
{gold:T2} : {gold:精密静止マシン外装} : {blue:{var:tier2_decay}} : {dark_aqua:{var:tier2_capacity}}
{gold:T3} : {gold:究極静的マシン外装} : {blue:{var:tier3_decay}} : {dark_aqua:{var:tier3_capacity}}