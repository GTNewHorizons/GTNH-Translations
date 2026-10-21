Ускоряет пучки частиц до тех пор, пока они не начнут производить пучок фотонов в результате релятивистского эффекта Лармора
Поэтому электрически нейтральные {dark_purple:частицы} и пучки с {dark_green:Фокусом} менее 25 остаются неизменными
{lang:gtnhlanth.tt.beaminfo}
{hr}
Для работы требуется {color_amount:32.000 {var:fluidUnit}/с} {color_cold:хладагента}, возвращается в виде {color_hot:горячего хладагента}
{lang:gtnhlanth.tt.coolant.oxygen}
{lang:gtnhlanth.tt.coolant.nitrogen}
{lang:gtnhlanth.tt.coolant.coolant}
{lang:gtnhlanth.tt.coolant.Scoolant}
{hr}
Повышение мощности увеличивает §6Скорость выходного пучка
Чем ниже температура §bхладагента§7, тем лучше сохраняется {dark_green:Фокус пучка}
Повышение тира {light_purple:корпусов антенны} увеличивает эффективность механизма
Все {blue:энергии} в формулах ниже должны быть в keV
{hr}
{blue:Энергия выходного пучка}{color_formula: = {color_note:IR} * {color_note:коэффициент масштабирования мощности}}
где {color_note:IR}{color_formula: = ({blue:Энергия входного пучка})^(1.13 * ({light_purple:тир антенны})^(4/9)) / 40.000.000}
и {color_note:коэффициент масштабирования мощности}{color_formula: = 1 - 0.15^({color_eu_usage:общая подаваемая {EU/t}} / (30.384 * ({light_purple:тир антенны})^2.5))}
{hr}
{dark_green:Фокус выходного пучка}{color_formula: = ({dark_green:Фокус входного пучка} + {color_note:Фокус механизма})/2.5}, если {dark_green:Фокус входного пучка} > {color_note:Фокус механизма}
{dark_green:Фокус выходного пучка}{color_formula: = {dark_green:Фокус входного пучка} * {color_note:Фокус механизма}/100}, если {dark_green:Фокус входного пучка} <= {color_note:Фокус механизма}
где {color_note:Фокус механизма}{color_formula: = макс.(10, мин.(90, 1.5^(12 - {color_cold:Температура хладагента}/40)))}
{hr}
{gold:Скорость выходного пучка}{color_formula: = округление вниз(2.5^({light_purple:тир антенны}) * sqrt({color_eu_usage:общая подаваемая {EU/t}}) * {gold:Скорость входного пучка}/15.000)}