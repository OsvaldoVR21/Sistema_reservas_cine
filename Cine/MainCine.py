from SistemaReservasCine import *
from datetime import datetime, date

pelicula1 = Pelicula("Avengers: Endgame", 180, "B", "Acción")

sala1 = Sala(101, "Sala 1", "Plaza Central", TipoSala.DOS_D, 10, False)

horario = datetime(2026, 5, 16, 10, 0)
funcion1 = Funcion("F1", pelicula1, sala1, horario, 100.0)

usuario1 = Usuario(1, "Osvaldo", "osvalvaz21@gmail.com", "1234567890")

try:
    reserva1 = Reserva("R-001", usuario1, funcion1, ["A1", "A2"])
    usuario1.crear_reserva(reserva1)

    promo1 = Promocion("P1", "Descuento de 10%", 10.0, datetime(2026, 12, 16))
    reserva1.aplicar_promocion(promo1)

    reserva1.confirmar_pago()
    
    ticket1 = reserva1.generar_ticket()
    print(ticket1)

except ValueError as e:
    print(f"Error en la reserva: {e}")