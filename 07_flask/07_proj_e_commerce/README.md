# E-commerce API

Este es un proyecto de práctica de desarrollo backend: una API REST para administrar usuarios, productos, carritos de compras, compras y devoluciones. Lo desarrollé con Python y Flask, usando PostgreSQL para guardar los datos y Redis para almacenar temporalmente algunas consultas.

El objetivo es practicar operaciones CRUD, relaciones entre tablas, autenticación, manejo de transacciones, caché y pruebas unitarias. **No es una tienda lista para producción ni procesa pagos reales**: registra los métodos de pago que el usuario selecciona para una compra.

## Tecnologías

- **Python y Flask:** servidor y endpoints de la API.
- **PostgreSQL:** base de datos relacional.
- **SQLAlchemy ORM:** modelos, relaciones y consultas a la base de datos.
- **Redis:** caché de algunas respuestas de consultas.
- **PyJWT (RS256):** generación y validación de tokens de acceso y actualización.
- **Argon2:** hash y verificación de contraseñas.
- **pytest y unittest.mock:** pruebas unitarias, principalmente de carritos y transacciones.

## Funcionalidades principales

- Registro e inicio de sesión de usuarios.
- Roles `User` y `Administrator`, con validaciones de acceso en distintos endpoints.
- Administración de productos, direcciones de facturación y métodos de pago.
- Creación y actualización de carritos de compras.
- Compras que crean facturas y descuentan existencias de productos.
- Devoluciones que marcan la factura como devuelta y reponen existencias.
- Caché en Redis para algunas consultas GET.

## Estructura del proyecto

Los archivos de la aplicación están directamente dentro de `07_proj_e_commerce/`. Los tests están en `tests/`.

```text
07_proj_e_commerce/
├── main.py                 # Endpoints y servidor Flask
├── db.py                   # Modelos y métodos de SQLAlchemy
├── db_engine.py            # Conexión a PostgreSQL
├── create_tables.py        # Creación de tablas
├── seed_admin.py           # Creación del primer administrador
├── services.py             # Lógica de compras y devoluciones
├── validations.py          # Validaciones de acceso
├── jwt_manager.py          # Generación y validación de JWT
├── ioc_container.py        # Inicialización de servicios compartidos
├── cache.py                # Cliente y operaciones de Redis
├── cache_functions.py      # Consulta e invalidación de caché
├── credentials/
│   └── redis_creds.py      # Configuración local de Redis (crear si falta)
├── keys/
│   ├── private.pem         # Llave privada (generar localmente)
│   └── public.pem          # Llave pública (generar localmente)
├── docs/
│   └── tables_diagram.jpg  # Diagrama de la base de datos
└── tests/
    ├── test_services.py
    └── test_carts.py
```

> Las carpetas `credentials/`, `keys/` y `docs/` deben existir según corresponda. No se deben subir contraseñas ni llaves privadas al repositorio. La imagen de `docs/` sí se debe subir en el mismo PR que el README.

## Requisitos previos

Antes de ejecutar el proyecto, se necesita:

1. Python 3 y `pip`.
2. PostgreSQL instalado y en ejecución (el código actual se conecta al puerto `5432`).
3. Redis instalado y en ejecución localmente.
4. OpenSSL, para generar las llaves de JWT.
5. Git, si se va a clonar el repositorio.

Para instalar las librerías de Python, desde la raíz de `07_proj_e_commerce/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask SQLAlchemy psycopg2-binary redis PyJWT cryptography argon2-cffi pytest
```

## Configuración inicial

Los comandos siguientes se ejecutan desde `07_proj_e_commerce/` y suponen que PostgreSQL y Redis están instalados en el equipo.

### 1. Configurar PostgreSQL

El archivo `db_engine.py` contiene actualmente una cadena de conexión fija, con esta estructura:

```python
DB_URI = "postgresql://USUARIO:CONTRASEÑA@localhost:5432/postgres"
```

Antes de iniciar la aplicación, hay que editar **la conexión real de `db_engine.py`** y poner el usuario, contraseña, puerto y nombre de base de datos que correspondan a la instalación local. La aplicación utiliza la base de datos `postgres` por defecto en el código entregado.

Los modelos están configurados para usar el esquema PostgreSQL `e_commerce`. Hay que crearlo antes de ejecutar `create_tables.py`:

```bash
psql -U postgres -d postgres -c "CREATE SCHEMA IF NOT EXISTS e_commerce;"
```

Si se utiliza otro usuario o base de datos, hay que ajustar esos parámetros en el comando. También se puede crear el esquema desde pgAdmin, ejecutando:

```sql
CREATE SCHEMA IF NOT EXISTS e_commerce;
```

Después, crear las tablas mediante SQLAlchemy:

```bash
python create_tables.py
```

El script utiliza `Base.metadata.create_all(engine)`. Crea las tablas que faltan, pero **no es un sistema de migraciones**: si se modifica una tabla existente, `create_all()` no aplica automáticamente todos los cambios.

### 2. Configurar Redis local

Iniciar el servidor Redis en el equipo. Por ejemplo, si se instaló con Homebrew en macOS:

```bash
brew services start redis
redis-cli ping
```

El segundo comando debería responder `PONG`. En otros sistemas, Redis puede iniciarse con el administrador de servicios correspondiente.

La aplicación importa `host`, `port` y `password` desde `credentials/redis_creds.py`. Si ese archivo no existe, crear la carpeta y el archivo con los datos de la instalación local. Para una instalación local de Redis **sin contraseña**, su contenido puede ser:

```python
host = "localhost"
port = 6379
password = None
```

Si Redis tiene contraseña, cambiar `password` por la correspondiente. `ioc_container.py` crea la conexión al iniciarse la aplicación, por lo que Redis debe estar disponible desde el principio.

### 3. Generar las llaves de JWT

`jwt_manager.py` lee dos archivos desde la carpeta `keys/`: `private.pem` y `public.pem`. Para generarlos, ejecutar:

```bash
mkdir -p keys
openssl genrsa -out keys/private.pem 2048
openssl rsa -in keys/private.pem -pubout -out keys/public.pem
```

La llave privada sirve para firmar tokens y la pública para verificarlos. Se usa el algoritmo **RS256**. No compartir ni subir `private.pem` a Git.

Los *access tokens* duran **15 minutos** y los *refresh tokens* **7 días**, según la configuración de `jwt_manager.py`.

### 4. Crear el primer administrador

El archivo `seed_admin.py` crea un usuario con rol `Administrator` y guarda su contraseña usando Argon2.

**Antes de ejecutarlo**, abrir `seed_admin.py` y cambiar los valores de `username`, `password`, `email` y `full_name` por datos propios de la instalación local. Este archivo utiliza valores fijos en su implementación actual, así que no conviene conservar las credenciales de ejemplo ni subir credenciales reales al repositorio.

Luego ejecutar:

```bash
python seed_admin.py
```

Este paso se realiza solo para crear el administrador inicial; no es necesario repetirlo cada vez que se inicia el servidor. Conviene revisar el resultado y comprobar el registro en PostgreSQL si aparece algún error.

## Iniciar el servidor

Con PostgreSQL y Redis activos, las dependencias instaladas y las llaves generadas:

```bash
python main.py
```

La aplicación está configurada para ejecutarse en:

```text
http://localhost:7000
```

Actualmente `main.py` utiliza `debug=True`, que es útil para desarrollar y depurar, pero **no debe utilizarse en producción**.

Para probar la API se puede utilizar Postman o una herramienta similar. Por ejemplo, el registro de usuarios se hace con `POST /register` enviando un JSON con `username`, `password`, `email` y `full_name`. El inicio de sesión utiliza `POST /login` con `username` y `password`.

Los endpoints protegidos utilizan el encabezado:

```text
Authorization: Bearer <access_token>
```

## Endpoints principales

| Método | Ruta | Función |
| --- | --- | --- |
| POST | `/register` | Registrar usuario |
| POST | `/login` | Iniciar sesión |
| POST | `/refresh-token` | Obtener otro access token con un refresh token |
| GET | `/users` | Consultar usuarios (administrador) |
| GET | `/me/<identifier>` | Consultar perfil |
| POST / GET | `/products` | Crear / consultar productos |
| GET / PATCH / DELETE | `/products/<product_id>` | Consultar / actualizar / eliminar producto |
| POST / GET | `/me/<identifier>/billing` | Crear / consultar direcciones de facturación |
| POST / GET | `/me/<identifier>/payment_methods` | Crear / consultar métodos de pago del usuario |
| POST / GET | `/me/<identifier>/carts` | Crear o recuperar carrito activo / consultar carritos |
| GET / PUT / DELETE | `/me/<identifier>/carts/<cart_id>` | Consultar / actualizar / eliminar carrito |
| GET | `/me/<identifier>/invoices` | Consultar facturas del usuario |
| POST | `/checkout/<cart_id>` | Comprar el contenido de un carrito |
| POST | `/return/<invoice_id>` | Devolver una compra |

Esta tabla es un resumen, no una especificación completa de todos los endpoints. En `main.py` están definidas las rutas y los campos esperados de cada petición.

Para realizar una compra mediante `POST /checkout/<cart_id>`, el cuerpo JSON incluye `billing_address_id` y `user_payment_method_id`. El usuario se identifica desde el token, y la fecha de compra se asigna en el servidor.

## Base de datos

El proyecto utiliza el esquema `e_commerce` con nueve tablas relacionadas:

- **users:** cuentas y roles de usuario.
- **products:** catálogo, precios y existencias.
- **carts** y **cart_products:** carritos y productos incluidos en cada carrito.
- **invoices** y **invoice_products:** compras realizadas y sus productos.
- **billing_addresses:** direcciones de facturación del usuario.
- **payment_methods:** tipos de método de pago disponibles.
- **user_payment_methods:** métodos asociados a cada usuario.

![Diagrama de la base de datos](docs/tables_diagram.jpg)

[Ver el diagrama de la base de datos](docs/tables_diagram.jpg)

Usé tablas intermedias como `cart_products` e `invoice_products` para guardar la cantidad y el precio total de cada producto dentro de una compra o carrito. También utilicé claves foráneas para relacionar los registros y restricciones en PostgreSQL para ciertos estados y roles. Por ejemplo, hay un índice único parcial para permitir **como máximo un carrito `Active` por usuario**.

## Decisiones técnicas

### SQLAlchemy y transacciones

Utilicé SQLAlchemy ORM para representar las tablas como clases de Python y trabajar con sus relaciones. En `services.py`, las compras y las devoluciones modifican varios registros: facturas, productos, stock y estado del carrito. Por eso se usa una sesión con `commit()` al completar la operación y `rollback()` cuando ocurre una excepción. La intención es evitar guardar cambios incompletos si algo falla.

### Redis, TTL e invalidación

Agregué caché en algunos endpoints GET para evitar repetir consultas a PostgreSQL cuando se solicita la misma información varias veces. Por ejemplo, las consultas de productos, carritos y facturas pueden devolver datos desde Redis mientras exista una entrada válida.

El caché tiene un **TTL (*time to live*)**, para que los datos expiren automáticamente y no permanezcan guardados para siempre. Los tiempos varían según el endpoint: por ejemplo, la lista de carritos usa 180 segundos, la lista de productos 900 segundos y las facturas 1200 segundos. `CacheManager.store_data()` también agrega un pequeño valor aleatorio (*jitter*) de hasta 30 segundos al TTL recibido, para que varias claves no expiren en el mismo instante.

Además, implementé funciones de invalidación para intentar eliminar entradas relacionadas cuando se crean, actualizan o eliminan datos. Esto reduce el riesgo de devolver información desactualizada.

### Autenticación y contraseñas

Utilicé JWT para identificar al usuario en las peticiones protegidas. Elegí RS256 para separar la llave que firma los tokens de la que los verifica. También separé los access tokens (duración corta) de los refresh tokens (duración mayor).

Para las contraseñas utilicé Argon2, de modo que no se guarden en texto plano en la base de datos. Las validaciones de permisos comprueban, según el endpoint, que la persona tenga acceso a su propio recurso o tenga rol de administrador.

## Pruebas unitarias

Las pruebas están en `tests/test_services.py` y `tests/test_carts.py`. Utilicé **pytest** y **unittest.mock** para simular operaciones de SQLAlchemy y otras dependencias, sin depender de los datos que existan en PostgreSQL.

Entre los escenarios probados se encuentran:

- Compras válidas y fallidas (carrito inexistente o inactivo, falta de stock, permisos, etc.).
- Devoluciones de compras y recuperación de existencias.
- Creación, consulta, actualización y eliminación de carritos.
- Manejo de excepciones, `commit()` y `rollback()`.

Para ejecutar los tests desde la raíz del proyecto:

```bash
python -m pytest tests/ -v
```

Los tests compartidos se ejecutan con mocks y está confirmado que pasan.