def calcular_iva(valor_compra:int):
    IVA=0.19
    valor_iva_producto=valor_compra*IVA
    return valor_iva_producto

def descuento_producto(valor_sin_descuento:int,porcentaje_descuento:int):
    descuento=valor_sin_descuento*(porcentaje_descuento/100)
    valor_final = valor_sin_descuento-descuento
    return valor_sin_descuento