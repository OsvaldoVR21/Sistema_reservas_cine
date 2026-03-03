from datetime import datetime, date
from enum import Enum
#                                            Enums
class TipoSala(Enum):
    DOS_D = "2D"
    TRES_D = "3D"
    IMAX = "IMAX"

class RolEmpleado(Enum):
    TAQUILLERO = "TAQUILLERO"
    ADMIN = "ADMIN" 
    LIMPIEZA = "LIMPIEZA"

class EstadoReserva(Enum):
    PENDIENTE = "PENDIENTE"
    PAGADO = "PAGADA"
    CANCELADA = "CANCELADA"

#                                            Personas

class Persona:
    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        print(f"{self.nombre} ha iniciado sesión\n")

    def logout(self):
        print(f"{self.nombre} ha cerrado sesión\n")

class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntos_fidelidad = 0
        self.historial_reservas = []

    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        print(f"Reserva {reserva.id_reserva} añadida al historial de {self.nombre}.")

class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, telefono, id_empleado: str, rol: RolEmpleado, horario: str):
        super().__init__(id_persona, nombre, email, telefono)
        self.id_empleado = id_empleado
        self.rol = rol
        self.horario = horario

    def gestionar_funciones(self):
        if self.rol == RolEmpleado.ADMIN:
            print(f"Acceso concedido: El Administrador {self.nombre} está gestionando funciones.")
            return True
        else:
            print(f"Acceso denegado: El rol {self.rol.value} no tiene permisos.")
            return False

#                                              Cine

class Espacio:
    def __init__(self, id_espacio: int, nombre: str, ubicacion: str):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificar_disponibilidad(self): pass

class Sala(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion, tipo: TipoSala, capacidad_total: int, es_vip: bool):
        super().__init__(id_espacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidad_total = capacidad_total
        self.es_vip = es_vip
        self.asientos_ocupados = set()

    def calcular_asientos_libres(self):
        return self.capacidad_total - len(self.asientos_ocupados)

class ZonaComida(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion):
        super().__init__(id_espacio, nombre, ubicacion)
        self.inventario = {} # Map<String, int>

    def actualizar_inventario(self, producto, cantidad):
        self.inventario[producto] = cantidad

#                                              Pelicula

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

class Funcion:
    def __init__(self, id_funcion: int, pelicula: Pelicula, sala: Sala, horario_inicio: datetime, precio_base: float):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.sala = sala
        self.horario_inicio = horario_inicio
        self.precio_base = precio_base

    def obtener_detalles_funcion(self):
        return f"Película: {self.pelicula.titulo} | Sala: {self.sala.nombre} | Hora: {self.horario_inicio}"

#                                               Gestión

class Promocion:
    def __init__(self, codigo, descripcion, porcentaje_descuento: float, fecha_expiracion: datetime):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentaje_descuento = porcentaje_descuento
        self.fecha_expiracion = fecha_expiracion

    def es_valida(self):
        fecha_exp_solo_dia = self.fecha_expiracion
        if hasattr(self.fecha_expiracion, 'date'):
            fecha_exp_solo_dia = self.fecha_expiracion.date()
        return datetime.now().date() <= fecha_exp_solo_dia
    
class Reserva:
    def __init__(self, id_reserva: int, usuario: Usuario, funcion: Funcion, asientos: list):
        for asiento in asientos:
            if asiento in funcion.sala.asientos_ocupados:
                raise ValueError(f"Error: El asiento {asiento} ya está ocupado.")
        
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos 
        self.estado = EstadoReserva.PENDIENTE
        self.monto_total = len(asientos) * funcion.precio_base

    def aplicar_promocion(self, promo: Promocion):
        if promo.es_valida():
            descuento = self.monto_total * (promo.porcentaje_descuento / 100)
            self.monto_total -= descuento
            print(f"Promoción '{promo.codigo}' aplicada. Nuevo total: ${self.monto_total}")
        else:
            print("La promoción ha expirado.")

    def confirmar_pago(self):
        for asiento in self.asientos:
            self.funcion.sala.asientos_ocupados.add(asiento)
        self.estado = EstadoReserva.PAGADO
        print(f"Pago confirmado para la reserva {self.id_reserva}.")

    def generar_ticket(self):
        print("\n" + "="*30)
        print("CINEMAS PROGRAVANZADA")
        print("\n" + "="*30)
        print(f"TICKET - RESERVA #{self.id_reserva}")
        print("\n" + "-"*30)
        print(f"CINE: {self.funcion.sala.ubicacion}")
        print(f"PELÍCULA: {self.funcion.pelicula.titulo}")
        print(f"ASIENTOS: {', '.join(self.asientos)}")
        print(f"TOTAL: ${self.monto_total}")
        print(f"ESTADO: {self.estado.value}")
        print("="*30 + "\n")