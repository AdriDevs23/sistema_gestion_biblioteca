# Creamos una clase llamada 'Libro' que debe contener los atributos: titulo (string), autor (string), isbn (string) y disponible (booleano que inicia como True)

class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True

    # Getters y setters para los atributos
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible

    # Métodos requeridos por la práctica
    def agregar(self):
        titulo = str(input("Introduce el título del libro: "))
        autor = str(input("Introduce el autor del libro: "))
        isbn = str(input("Introduce el ISBN del libro: "))
        nuevo_libro = Libro(titulo, autor, isbn)
        biblioteca.append(nuevo_libro)
        print("Libro agregado con éxito.")

    def prestar(self):
        isbn = str(input("Introduce el ISBN del libro que quieres prestar: "))
        for libro in biblioteca:
            if isbn == libro.isbn:
                if libro.disponible:
                    libro.disponible = False
                    print("¡Libro prestado correctamente!")
                    return
                else:
                    print("El libro ya está prestado.")
                    return
        print("No se ha encontrado ningún libro con ese ISBN.")

    def devolver(self):
        isbn = str(input("Introduce el ISBN del libro que quieres devolver: "))
        for libro in biblioteca:
            if isbn == libro.isbn:
                if not libro.disponible:
                    libro.disponible = True
                    print("¡Libro devuelto correctamente!")
                    return
                else:
                    print("El libro no estaba prestado.")
                    return
        print("No se ha encontrado ningún libro con ese ISBN.")

    def mostrar(self):
        if not biblioteca:
            print("No hay libros en la biblioteca.")
            return
        print("Lista de libros en la biblioteca:")
        for libro in biblioteca:
            disponibilidad = "Sí" if libro.disponible else "No"
            print(f"Título: {libro.titulo}\n"
                f"Autor: {libro.autor}\n"
                f"ISBN: {libro.isbn}\n"
                f"Disponible: {disponibilidad}\n")

    def buscar(self):
        isbn = str(input("Introduce el ISBN del libro que quieres buscar: "))
        if not biblioteca:
            print("No hay libros en la biblioteca.")
            return
        for libro in biblioteca:
            if isbn == libro.isbn:
                disponibilidad = "Sí" if libro.disponible else "No"
                print(f"Título: {libro.titulo}\n"
                    f"Autor: {libro.autor}\n"
                    f"ISBN: {libro.isbn}\n"
                    f"Disponible: {disponibilidad}")
                return
        print("No se ha encontrado ningún libro con ese ISBN.")


# Lista global de libros
biblioteca = []

# Menú interactivo
def menu():
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            libro = Libro("", "", "")
            libro.agregar()
        elif opcion == "2":
            libro = Libro("", "", "")
            libro.prestar()
        elif opcion == "3":
            libro = Libro("", "", "")
            libro.devolver()
        elif opcion == "4":
            libro = Libro("", "", "")
            libro.mostrar()
        elif opcion == "5":
            libro = Libro("", "", "")
            libro.buscar()
        elif opcion == "6":
            print("¡Gracias por usar el sistema de gestión de biblioteca!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Ejecución del menú
if __name__ == "__main__":
    menu()