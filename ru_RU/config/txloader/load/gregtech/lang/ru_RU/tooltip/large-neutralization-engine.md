Растворяет все ваши проблемы!
{gray:{hr}}
Можно подавать {aqua:щёлочь} для повышения {light_purple:эффективности}:
{aqua:{var:sodium_hydroxide_rate}/мин} {aqua:гидроксида натрия} : {light_purple:{var:sodium_hydroxide_eff}%}
{aqua:{var:potassium_hydroxide_rate}/мин} {aqua:гидроксида калия} : {light_purple:{var:potassium_hydroxide_eff}%}
{aqua:{var:caesium_hydroxide_rate}/мин} {aqua:гидроксида цезия} : {light_purple:{var:caesium_hydroxide_eff}%}
{aqua:{var:francium_hydroxide_rate}/мин} {aqua:гидроксида франция} : {light_purple:{var:francium_hydroxide_eff}%}
{gray:{hr}}
Производит {dark_green:токсичные отходы} при сжигании кислот
Если {dark_green:токсичные отходы} превысят {dark_aqua:вместимость}, мультиблок {red:взорвётся}
Каждый тик {dark_green:токсичные отходы} растут на {green:0.05 * плотность топлива (EU/Л)^0.8 * расход топлива ({var:fluid_unit}) * rand({var:residue_rand_min}, {var:residue_rand_max})}
Каждый тик {dark_green:токсичные отходы} уменьшаются на {green:базовый распад * бонус распада * токсичные отходы^0.08}
{yellow:Отходы распадаются в 10 раз медленнее, когда мультиблок выключен}
{gray:{hr}}
Вставьте до {blue:16 роборук} для увеличения {blue:бонуса распада}:
{white:Бонус распада =} {green:sqrt(роборуки) * N^(тир роборуки - 1)}, где {green:N=1.2} ({var:tier_iv}§7-) или {green:N=1.4} ({var:tier_luv}§7+)
Каждую минуту с шансом {green:роборуки / (45 * (тир роборуки + 1))} исчезает ровно одна {blue:роборука}
{gray:{hr}}
Структура имеет {gold:3 тира}, которые определяют {blue:базовый распад} и {dark_aqua:вместимость}:
{gold:T1} : {gold:Укреплённый неодушевлённый корпус} : {blue:{var:tier1_decay}} : {dark_aqua:{var:tier1_capacity}}
{gold:T2} : {gold:Прецизионный стационарный корпус} : {blue:{var:tier2_decay}} : {dark_aqua:{var:tier2_capacity}}
{gold:T3} : {gold:Ультимативный статичный корпус} : {blue:{var:tier3_decay}} : {dark_aqua:{var:tier3_capacity}}