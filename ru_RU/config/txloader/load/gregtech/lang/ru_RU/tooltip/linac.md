Ускоряет пучки частиц до более высоких энергий, пропуская их через электрическое поле
Поэтому электрически нейтральные {color_mechanic:частицы} остаются неизменными
{lang:gtnhlanth.tt.beaminfo}
{hr}
Для работы требуется {aqua:Длина * 1.000 {var:fluidUnit}/с} {aqua:хладагента}, возвращается в виде {red:горячего хладагента}
{lang:gtnhlanth.tt.coolant.oxygen}
{lang:gtnhlanth.tt.coolant.nitrogen}
{lang:gtnhlanth.tt.coolant.coolant}
{lang:gtnhlanth.tt.coolant.Scoolant}
{hr}
Увеличение длины/мощности повышает {blue:Энергию выходного пучка}, но снижает {dark_green:Фокус выходного пучка}
Чем ниже температура {aqua:хладагента}, тем лучше сохраняется {dark_green:Фокус пучка}
{hr}
{blue:Энергия выходного пучка}{color_formula: = макс.(}{color_note:V}{white:, 50) * 10^}{color_note:IE}
где {color_note:V}{color_formula: = 0.25 * (Длина - 1) * cbrt({color_eu_usage:подаваемый {EU/t}})}
и {color_note:IE}{color_formula: = 1 + мин.({blue:Энергия входного пучка}, 7500) / }{blue:Макс. энергия частиц}
{hr}
{dark_green:Фокус выходного пучка}{color_formula: = (Фокус входного пучка + {color_note:Фокус механизма})/2}, если {dark_green:Фокус входного пучка}{color_formula: > {color_note:Фокус механизма}}
{dark_green:Фокус выходного пучка}{color_formula: = {dark_green:Фокус входного пучка} * {color_note:Фокус механизма}/100}, если {dark_green:Фокус входного пучка}{color_formula: <= {color_note:Фокус механизма}}
где {color_note:Фокус механизма}{color_formula: = мин.(90, макс.(5, (-0.9 * (Длина-1) * 1.1^(0.2 * {aqua:Температура хладагента}) + 110)))}