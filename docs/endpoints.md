# Endpoints de la API

La API de Cafetería Intergaláctica proporciona diferentes endpoints para administrar los bocadillos disponibles.

## Endpoints generales

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Devuelve un mensaje de bienvenida |
| `GET` | `/health` | Comprueba si la API está funcionando |

## Endpoints de bocadillos

| Método | Endpoint | Descripción | Código |
|---|---|---|---|
| `GET` | `/snacks/` | Devuelve todos los bocadillos | `200` |
| `GET` | `/snacks/{snack_id}` | Devuelve un bocadillo específico | `200` |
| `POST` | `/snacks/` | Crea un nuevo bocadillo | `201` |
| `PUT` | `/snacks/{snack_id}` | Actualiza un bocadillo | `200` |
| `DELETE` | `/snacks/{snack_id}` | Elimina un bocadillo | `200` |

## Obtener todos los bocadillos

```http
GET /snacks/
```

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "name": "Moon Cheese",
    "price": 4.99,
    "planet_of_origin": "The Moon",
    "is_radioactive": false
  },
  {
    "id": 2,
    "name": "Martian Hot Chips",
    "price": 7.5,
    "planet_of_origin": "Mars",
    "is_radioactive": true
  }
]
```

## Filtrar bocadillos radioactivos

El parámetro de consulta `radioactive` permite filtrar los resultados según su estado radioactivo.

Para obtener solamente bocadillos radioactivos:

```http
GET /snacks/?radioactive=true
```

Para obtener solamente bocadillos no radioactivos:

```http
GET /snacks/?radioactive=false
```

## Obtener un bocadillo por ID

```http
GET /snacks/2
```

Ejemplo de respuesta:

```json
{
  "id": 2,
  "name": "Martian Hot Chips",
  "price": 7.5,
  "planet_of_origin": "Mars",
  "is_radioactive": true
}
```

Si el bocadillo no existe, la API devolverá:

```json
{
  "detail": "Snack not found. An alien may have eaten it."
}
```

## Crear un bocadillo

```http
POST /snacks/
Content-Type: application/json
```

Cuerpo de la solicitud:

```json
{
  "name": "Plutonian Ice Cream",
  "price": 8.75,
  "planet_of_origin": "Pluto",
  "is_radioactive": false
}
```

Ejemplo de respuesta:

```json
{
  "id": 4,
  "name": "Plutonian Ice Cream",
  "price": 8.75,
  "planet_of_origin": "Pluto",
  "is_radioactive": false
}
```

## Actualizar un bocadillo

```http
PUT /snacks/1
Content-Type: application/json
```

Cuerpo de la solicitud:

```json
{
  "name": "Premium Moon Cheese",
  "price": 6.99,
  "planet_of_origin": "The Moon",
  "is_radioactive": false
}
```

## Eliminar un bocadillo

```http
DELETE /snacks/1
```

Ejemplo de respuesta:

```json
{
  "message": "Moon Cheese was launched into space."
}
```

!!! tip "Probar los endpoints"

    Puedes probar todos los endpoints desde la interfaz de Swagger disponible en `http://127.0.0.1:8000/docs`.

Consulta los [ejemplos de solicitudes](examples.md) para aprender a consumir la API desde distintas herramientas.