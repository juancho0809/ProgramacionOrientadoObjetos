

class Computadora:
    numero_serie = ''
    marca = ''
    procesador = ''
    sistema_operativo = ''
    memoria = ''
    aula = ''

    def __init__(self,numero_serie,marca,procesador,sistema_operativo,memoria,aula)->None:
        self.numero_serie = numero_serie
        self.marca = marca
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo
        self.memoria = memoria
        self.aula = aula

    def encender():
        print("Encienda")

    def ejecutar_programa():
        print("Se ejecuta")

    def almacenar_archivos():
        print("guardado")

    def cerrar_programa():
        print("cerrado")


mi_computadora = Computadora(23444,'MAC','intel','Windows','4GB','502')

print(mi_computadora.procesador)



