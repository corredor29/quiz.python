🍔 Sistema de Gestión de Inventario - Cafetería Campuslands
Este proyecto es una solución automatizada para la gestión de ingredientes, hamburguesas, chefs y categorías en la cafetería de Campuslands. Busca optimizar el control de stock y reducir el desperdicio, asegurando una operación más eficiente y una experiencia satisfactoria para los clientes.

🧾 Descripción del Problema
La cafetería enfrenta problemas por la mala gestión de ingredientes, como:

Falta de ingredientes esenciales.

Desperdicio de insumos.

Dificultad para planificar pedidos.

Experiencias de cliente inconsistentes.

Este sistema se plantea como solución para permitir un control en tiempo real del inventario, mejorar la planificación de compras y facilitar la gestión de hamburguesas y chefs.

📂 Estructura de Archivos JSON
🥬 Ingredientes (ingredientes.json)
json
Copiar
Editar
[
  {
    "nombre": "Pan",
    "descripcion": "Pan de hamburguesa clásico",
    "precio": 2.5,
    "stock": 500
  }
]
🍔 Hamburguesas (hamburguesas.json)
json
Copiar
Editar
[
  {
    "nombre": "Clásica",
    "categoria": "Clásica",
    "ingredientes": ["Pan", "Carne de res", "Queso cheddar"],
    "precio": 10,
    "chef": "ChefA"
  }
]
📋 Categorías (categorias.json)
json
Copiar
Editar
[
  {
    "nombre": "Clásica",
    "descripcion": "Hamburguesas clásicas y sabrosas"
  }
]
👨‍🍳 Chefs (chefs.json)
json
Copiar
Editar
[
  {
    "nombre": "ChefA",
    "especialidad": "Carnes"
  }
]
⚙️ Funcionalidades
Ingredientes
Registrar, leer, actualizar y eliminar ingredientes.

Registrar historial de ingredientes utilizados.

Aumentar precios, eliminar ingredientes sin stock, incrementar unidades.

Categorías
CRUD de categorías con nombre y descripción.

Chefs
CRUD de chefs con nombre y especialidad.

Cambiar especialidades.

Agregar nuevos chefs.

Hamburguesas
CRUD de hamburguesas con nombre, categoría, ingredientes, precio y chef.

Agregar o eliminar ingredientes de hamburguesas.

Eliminar hamburguesas con menos de 5 ingredientes.

📊 Módulo de Reportes
Consultas disponibles:

Ingredientes con stock menor a 400.

Hamburguesas de la categoría “Vegetariana”.

Chefs especializados en “Carnes”.

Aumentar el precio de ingredientes en 1.5.

Hamburguesas preparadas por “ChefB”.

Nombre y descripción de todas las categorías.

Eliminar ingredientes con stock de 0.

Agregar ingrediente a la hamburguesa “Clásica”.

Hamburguesas con “Pan integral”.

Cambiar especialidad de “ChefC” a “Cocina Internacional”.

Ingrediente más caro.

Hamburguesas sin “Queso cheddar”.

Incrementar el stock de “Pan” en 100 unidades.

Eliminar hamburguesas con menos de 5 ingredientes.

Agregar nuevo chef especializado en “Cocina Asiática”.

Listar hamburguesas por precio ascendente.

Ingredientes cuyo precio esté entre $2 y $5.

Actualizar la descripción del “Pan”.

Hamburguesa más cara preparada por chef “Gourmet”.

Listar ingredientes con número de hamburguesas que los contienen.

💻 Requisitos Técnicos
Python 3.8+

Uso de archivos JSON como almacenamiento local.

Aplicación en consola.

🧪 Cómo Ejecutar
Clona este repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/sistema-cafeteria-campuslands.git
cd sistema-cafeteria-campuslands
Ejecuta el programa principal:

bash
Copiar
Editar
python main.py
Sigue las instrucciones en consola para interactuar con el sistema.
Felipe corredor silva

🤝 Contribuciones
