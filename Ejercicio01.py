class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def calcular_total(self):
        total = sum(item['precio'] * item['cantidad'] for item in self.items)
        return total

    def procesar_pago(self, metodo_pago):
        if metodo_pago == "tarjeta":
            print("Procesando pago con tarjeta...")
        elif metodo_pago == "efectivo":
            print("Pago en efectivo recibido.")
        else:
            print("Método de pago no válido.")

    def generar_factura(self):
        print(f"Factura para {self.cliente}:")
        for item in self.items:
            print(f"- {item['nombre']} x {item['cantidad']} = ${item['precio'] * item['cantidad']}")
        print(f"Total: ${self.calcular_total()}")

    def enviar_pedido_cocina(self):
        print(f"Enviando pedido a cocina: {self.items}")

    def actualizar_stock(self):
        print("Actualizando stock en la base de datos...")



# Crear un pedido con datos ficticios
pedido_cliente = Pedido(
    cliente="Juan Pérez",
    items=[
        {"nombre": "Hamburguesa", "precio": 5.0, "cantidad": 2},
        {"nombre": "Refresco", "precio": 2.0, "cantidad": 1},
    ]
)



pedido_cliente.calcular_total()
pedido_cliente.generar_factura()