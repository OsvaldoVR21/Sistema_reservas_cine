from ReservasCine import *
from datetime import datetime, date

def ejecutar_pruebas():
    print("REGISTRO DE INVENTARIO")

    #10 peliculas
    peliculas = [
        Pelicula("Matrix", "1999", "B", "Terror"),
        Pelicula("Avengers: Endgame", "2019", "A", "Acción"),
        Pelicula("Spider-Man: Into the Spider-Verse", "2018", "A", "Acción"),
        Pelicula("Joker", "2019", "A", "Acción"),
        Pelicula("Cars", "2006", "A", "Acción"),
        Pelicula("Kung Fu Panda", "2008", "A", "Animación"),
        Pelicula("El rey León", "2016", "A", "Acción"),
        Pelicula("It", "2017", "A", "Drama"),
        Pelicula("Toy Story", "1995", "A", "Animación"),
        Pelicula("Guardianes de la galaxia", "2014", "A", "Acción")
    ]

    for i, p in enumerate(peliculas):
        print(f"Pelicula {i+1}: {p.titulo}")

    #10 usuarios
    usuarios = [
        Usuario(1, "Juan", "juan@gmail.com", "555-0001"),
        Usuario(2, "Pedro", "pedro@gmail.com", "555-0002"),
        Usuario(3, "Carlos", "carlos@gmail.com", "555-0003"),
        Usuario(4, "Luis", "luis@gmail.com", "555-0004"),
        Usuario(5, "Maria", "maria@gmail.com", "555-0005"),
        Usuario(6, "Jose", "jose@gmail.com", "555-0006"),
        Usuario(7, "Ana", "ana@gmail.com", "555-0007"),
        Usuario(8, "Luz", "luz@gmail.com", "555-0008"),
        Usuario(9, "Juana", "juana@gmail.com", "555-0009"),
        Usuario(10, "Maria", "maria@gmail.com", "555-0010")
    ]

    print("\nUSUARIOS REGISTRADOS")
    for i, u in enumerate(usuarios):
        print(f"Usuario {i+1}: {u.nombre}")

    print("\nPRUEBA DE MÉTODOS INDIVIDUALES")
    usuarios[0].login()
    usuarios[1].login()
    usuarios[2].login()
    usuarios[3].login()
    usuarios[4].login()
    usuarios[5].login()
    usuarios[6].login()
    usuarios[7].login()
    usuarios[8].login()
    usuarios[9].login()

    usuarios[0].logout()
    usuarios[1].logout()
    usuarios[2].logout()
    usuarios[3].logout()
    usuarios[4].logout()
    usuarios[5].logout()
    usuarios[6].logout()
    usuarios[7].logout()
    usuarios[8].logout()
    usuarios[9].logout()

    usuarios[0].login()

    #Reto
    print("\n>>>INICIANDO PROCESO DE RESERVA...")
    sala_imax = Sala(101, "Sala 04 (IMAX)", "Plaza Diamante", TipoSala.IMAX, 100, True)
    funcion_avengers = Funcion(1, peliculas[1], sala_imax, datetime(2026, 1, 20, 20, 0), 150.00)

    #Asiento ocupado para prueba error
    sala_imax.asientos_ocupados.add("A2")

    usuario_actual = usuarios[0]
    print(f"Usuario: {usuario_actual.nombre}\n Puntos Fidelidad: {usuario_actual.puntos_fidelidad}")
    print(f"Pelicula: {funcion_avengers.pelicula.titulo}\nSala: {sala_imax.nombre}\nHorario: {funcion_avengers.horario_inicio}")

    #Seleccion de asientos
    asientos_pedidos = ["A1", "A2", "B5"]
    print(f"Seleccione sus asientos:{asientos_pedidos}")

    try:
        reserva = Reserva(995, usuario_actual, funcion_avengers, asientos_pedidos)
    except ValueError as e:
        print(f"[SISTEMA]: Verificando disponibilidad de asientos...")
        print(f"[ERROR]: {e}")
        print(f"[SISTEMA]: Seleccione asientos disponibles")

    #Intento corregido
    nuevos_asientos = ["A1","A3","B5"]
    print(f"Seleccione sus asientos:{nuevos_asientos}")
    reserva = Reserva(995, usuario_actual, funcion_avengers, nuevos_asientos)
    print(f"[OK]: Asientos {nuevos_asientos} seleccionados")

    print(f"Monto base: ${reserva.monto_total}")

    #Gestión comercial
    print("\n>>>APLICANDO GESTION COMERCIAL...")
    promo_est = Promocion("PROMO_ESTUDIANTE", "Desc. de estudiantes", 10.0, datetime(2026, 1, 20, 20, 0))

    print(f"?Cuenta con codigo de promocion? SI")
    print(f"Código: {promo_est.codigo}")
    print(f"[SISTEMA]: Validando cóidigo... Descuento del 20% aplicado")

    reserva.aplicar_promocion(promo_est)
    reserva.confirmar_pago()

    #Resumen final
    print("\n>>>RESUMEN FINAL...")
    print(f"Usuario: {reserva.usuario.nombre}")
    print(f"Función: {reserva.funcion.pelicula.titulo}")
    print(f"Asientos: {reserva.asientos}")
    print(f"Monto total: ${reserva.monto_total}")
    print(f"Estado: {reserva.estado.value}")

    print("\n>>>VALIDACION DE DATOS FINALIZADA")

    
    print("\n>>>TICKET...")
    reserva.generar_ticket()

if __name__ == "__main__":
    ejecutar_pruebas()