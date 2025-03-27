class Libro:
    def __init__(self, titulo, autor, genero, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} | Género: {self.genero} | Disponibles: {self.cantidad}"

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.cargar_libros_iniciales()

    def cargar_libros_iniciales(self):
        libros_iniciales = [
            ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 3),
            ("Crónica de una muerte anunciada", "Gabriel García Márquez", "Realismo mágico", 2),
            ("El amor en los tiempos del cólera", "Gabriel García Márquez", "Romance", 1),
            ("1984", "George Orwell", "Ciencia ficción", 3),
            ("Rebelión en la granja", "George Orwell", "Fábula política", 2),
            ("Fahrenheit 451", "Ray Bradbury", "Ciencia ficción", 1),
            ("El resplandor", "Stephen King", "Terror", 2),
            ("It", "Stephen King", "Terror", 0),
            ("Cementerio de animales", "Stephen King", "Terror", 1),
            ("Drácula", "Bram Stoker", "Terror", 1),
            ("Frankenstein", "Mary Shelley", "Ciencia ficción", 2),
            ("El principito", "Antoine de Saint-Exupéry", "Fábula", 4),
            ("El psicoanalista", "John Katzenbach", "Thriller psicológico", 2),
            ("La historia interminable", "Michael Ende", "Fantasía", 3),
            ("Los juegos del hambre", "Suzanne Collins", "Distopía", 2),
            ("Sinsajo", "Suzanne Collins", "Distopía", 1),
            ("En llamas", "Suzanne Collins", "Distopía", 2),
            ("Rayuela", "Julio Cortázar", "Experimental", 2),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", "Aventura", 1),
            ("La sombra del viento", "Carlos Ruiz Zafón", "Novela histórica", 3),
        ]
        for titulo, autor, genero, cantidad in libros_iniciales:
            self.catalogo[titulo] = Libro(titulo, autor, genero, cantidad)

    def mostrar_libros_disponibles(self):
        print("\n📚 Libros DISPONIBLES:")
        disponibles = False
        for libro in self.catalogo.values():
            if libro.cantidad > 0:
                print(libro)
                disponibles = True
        if not disponibles:
            print("No hay libros disponibles actualmente.")

    def mostrar_libros_no_disponibles(self):
        print("\n📕 Libros NO DISPONIBLES:")
        no_disponibles = False
        for libro in self.catalogo.values():
            if libro.cantidad == 0:
                print(libro)
                no_disponibles = True
        if not no_disponibles:
            print("Todos los libros tienen al menos una unidad disponible.")

    def consultar_por(self, criterio, valor):
        encontrados = []
        for libro in self.catalogo.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                encontrados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                encontrados.append(libro)
            elif criterio == "genero" and valor.lower() in libro.genero.lower():
                encontrados.append(libro)

        if encontrados:
            print("\n🔍 Resultados de la búsqueda:")
            for libro in encontrados:
                print(libro)
        else:
            print("❌ No se encontraron libros que coincidan con ese criterio.")

    def coger_libro(self, titulo):
        libro = self.catalogo.get(titulo)
        if libro and libro.cantidad > 0:
            libro.cantidad -= 1
            print(f"📖 Has coger: {titulo}")
        elif libro:
            print("⚠️ No hay unidades disponibles para este libro.")
        else:
            print("❌ El libro no existe en el sistema.")

    def devolver_libro(self, titulo):
        libro = self.catalogo.get(titulo)
        if libro:
            libro.cantidad += 1
            print(f"✅ Gracias por devolver: {titulo}")
        else:
            print("❌ Este libro no pertenece a nuestra biblioteca.")

    def donar_libro(self, titulo, autor, genero, cantidad):
        if titulo in self.catalogo:
            self.catalogo[titulo].cantidad += cantidad
            print(f"🎁 Gracias por donar más copias de: {titulo}")
        else:
            self.catalogo[titulo] = Libro(titulo, autor, genero, cantidad)
            print(f"🎉 ¡Gracias por tu donación! Nuevo libro añadido: {titulo}")

def mostrar_menu():
    print("\n=== MENÚ DE LA BIBLIOTECA ===")
    print("1. Consultar disponibilidad")
    print("2. Coger un libro")
    print("3. Devolver un libro")
    print("4. Donar un libro")
    print("5. Salir")

def mostrar_submenu_consulta():
    print("\n📖 ¿Cómo deseas consultar?")
    print("1. Ver libros disponibles / no disponibles")
    print("2. Buscar por título")
    print("3. Buscar por autor")
    print("4. Buscar por género literario")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            mostrar_submenu_consulta()
            subopcion = input("Selecciona una opción de consulta (1-4): ")

            if subopcion == "1":
                biblioteca.mostrar_libros_disponibles()
                biblioteca.mostrar_libros_no_disponibles()
            elif subopcion == "2":
                titulo = input("🔍 Ingresa el título a buscar: ")
                biblioteca.consultar_por("titulo", titulo)
            elif subopcion == "3":
                autor = input("🔍 Ingresa el autor a buscar: ")
                biblioteca.consultar_por("autor", autor)
            elif subopcion == "4":
                genero = input("🔍 Ingresa el género a buscar: ")
                biblioteca.consultar_por("genero", genero)
            else:
                print("❌ Opción de consulta no válida.")

        elif opcion == "2":
            titulo = input("📖 Ingresa el título del libro a coger: ")
            biblioteca.coger_libro(titulo)

        elif opcion == "3":
            titulo = input("📥 Ingresa el título del libro a devolver: ")
            biblioteca.devolver_libro(titulo)

        elif opcion == "4":
            titulo = input("🎁 Título del libro a donar: ")
            autor = input("Autor del libro: ")
            genero = input("Género literario: ")
            try:
                cantidad = int(input("Cantidad a donar: "))
                biblioteca.donar_libro(titulo, autor, genero, cantidad)
            except ValueError:
                print("⚠️ Cantidad inválida.")

        elif opcion == "5":
            print("👋 ¡Gracias por usar el sistema de biblioteca!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
