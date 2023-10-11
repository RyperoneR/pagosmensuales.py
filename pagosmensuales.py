prestamo = float(input("¿Cuánto dinero te han prestado?:"))
pagos_anuales = float(input("¿En cuántos años tienes que pagar el prestamo?: "))
interes = float(input("¿Cuále es el porcentage del interes del prestamo?:"))

pagos_mensuales = (pagos_anuales*12)
intereses = ((prestamo/100)*interes)
total_a_pagar = (intereses+prestamo)
mensualidad = (total_a_pagar/pagos_mensuales)

print("Tienes que pagar al mes: ", mensualidad)