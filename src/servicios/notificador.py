# Clase Notificador: simula el envío de notificaciones sobre incidentes.
class Notificador:

    # Método que envía una notificación sobre el incidente.
    def enviar(self, incidente):
        print(f"Notificación: {incidente.id} => {incidente.estado}")