# Asigna a la variable de bucle `i` un valor inicial de 5000

i = 5000

# Bucle while que genera ID de empleados únicos para el departamento de ventas iterando a través de los números
# y muestra cada ID creado
# Este bucle muestra “Solo quedan 10 ID de empleado válidos” una vez que `i` alcanza 5100

while i <= 5150: 
    print(i)
    if i == 5100:
        print("Solo quedan 10 ID de empleado válidos")
    i = i + 5