class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def calcular_total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items)


class Pago:
    def procesar_pago(self, pedido, metodo_pago):
        if metodo_pago == "tarjeta":
            print("Procesando pago con tarjeta...")
        elif metodo_pago == "efectivo":
            print("Pago en efectivo recibido.")
        else:
            print("Método de pago no válido.")
        print(f"Total pagado: ${pedido.calcular_total()}")


class Factura:
    def generar_factura(self, pedido):
        print(f"Factura para {pedido.cliente}:")
        for item in pedido.items:
            print(f"- {item['nombre']} x {item['cantidad']} = ${item['precio'] * item['cantidad']}")
        print(f"Total: ${pedido.calcular_total()}")


class Cocina:
    def enviar_pedido(self, pedido):
        print(f"Enviando pedido a cocina: {pedido.items}")


class Stock:
    def actualizar_stock(self, pedido):
        print("Actualizando stock en la base de datos...")



# Crear un pedido con datos ficticios
pedido_cliente = Pedido(
    cliente="Juan Pérez",
    items=[
        {"nombre": "Hamburguesa", "precio": 5.0, "cantidad": 2},
        {"nombre": "Refresco", "precio": 2.0, "cantidad": 1},
    ]
)

# Instanciar las otras clases que gestionan diferentes aspectos del pedido
pago = Pago()
factura = Factura()
cocina = Cocina()
stock = Stock()

# Procesar pago del cliente
pago.procesar_pago(pedido_cliente, "tarjeta")

# Generar factura
factura.generar_factura(pedido_cliente)

# Enviar pedido a cocina
cocina.enviar_pedido(pedido_cliente)

# Actualizar el stock
stock.actualizar_stock(pedido_cliente)