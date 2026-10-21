Для работы нужна {color_name:Турбина} в контроллере
Очищает загрязнение в окрестных чанках {color_range:{var:chunk_size}x{var:chunk_size}}
Во время работы потребляет фиксированные {color_eu_usage:{var:eu_usage} {EU/t}}
{hr}
Каждая {color_name:выхлопная система} убирает из одного чанка в секунду следующее количество загрязнения
{color_amount:{var:global_multiplier} * B * turbineEff * FLOOR({var:scaling_factor}^mufflerTier)}
- Бонус тира этого механизма (B) = {color_amount:{var:tier_bonus}}
- turbineEff = эффективность {color_name:турбины}
- Эффективный тир {color_name:выхлопной системы} ограничен тиром {color_name:энерговвода}
{hr}
Подавайте {color_key:абсорбирующие фильтры} через {color_name:входной люк}, чтобы удвоить очистку ({color_time:{var:filter_lifespan} с} на фильтр)
Каждая проблема с техобслуживанием снижает очистку на {color_amount:{var:maint_penalty}%}