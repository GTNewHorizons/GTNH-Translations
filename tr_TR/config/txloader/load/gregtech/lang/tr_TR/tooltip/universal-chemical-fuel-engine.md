YANIYOR YANIYOR YANIYOR
{yellow:Combustion Promoter} maddesini {color_key:Gaz}, {color_key:Dizel} veya {color_key:Roket Yakıtı} ile reaksiyona sokarak {color_efficiency:150%} verime kadar güç üretir
{color_name:Dinamo Kapağı} boyutu dışında güç çıktısında yumuşak sınır veya üst limit yoktur
Combustion Promoter olmadan hiç güç üretilmez
{color_name:Dinamo Kapağı} doluysa veya çıktı dinamo verimini aşarsa fazla güç yok edilir
{hr}
Verim, {yellow:Combustion Promoter} miktarının {gold:Yakıt} miktarına oranı ({color_formula:R}) ile belirlenir
Combustion Promoter ne kadar fazlaysa verim o kadar yüksek olur
Üstel bir eğri izler: {color_formula:exp(-C / R) * {var:efficiency_ceiling}}; burada {color_formula:C}, yakıt tipine bağlı bir sabittir
{color_key:Gaz/Dizel Yakıt}: {color_formula:C = {var:gas_coefficient}} | {color_key:Roket Yakıtı}: {color_formula:C = {var:rocket_coefficient}}
{hr}
Saniyede {color_pollution:sqrt({EU/t})} kirlilik üretir