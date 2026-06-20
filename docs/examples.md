# Ejemplos de solicitudes

La API puede utilizarse desde distintos lenguajes de programación y herramientas.

## Obtener todos los bocadillos

=== "Python"

    ```python
    import requests

    response = requests.get(
        "http://127.0.0.1:8000/snacks/",
        timeout=10,
    )

    response.raise_for_status()

    snacks = response.json()

    for snack in snacks:
        print(snack["name"])
    ```

=== "JavaScript"

    ```javascript
    fetch("http://127.0.0.1:8000/snacks/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("La solicitud falló");
        }

        return response.json();
      })
      .then((snacks) => {
        snacks.forEach((snack) => {
          console.log(snack.name);
        });
      })
      .catch((error) => {
        console.error(error);
      });
    ```

=== "cURL"

    ```bash
    curl http://127.0.0.1:8000/snacks/
    ```

## Obtener un bocadillo por ID

=== "Python"

    ```python
    import requests

    snack_id = 2

    response = requests.get(
        f"http://127.0.0.1:8000/snacks/{snack_id}",
        timeout=10,
    )

    response.raise_for_status()

    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const snackId = 2;

    fetch(`http://127.0.0.1:8000/snacks/${snackId}`)
      .then((response) => response.json())
      .then((snack) => console.log(snack))
      .catch((error) => console.error(error));
    ```

=== "cURL"

    ```bash
    curl http://127.0.0.1:8000/snacks/2
    ```

## Crear un bocadillo

=== "Python"

    ```python
    import requests

    new_snack = {
        "name": "Plutonian Ice Cream",
        "price": 8.75,
        "planet_of_origin": "Pluto",
        "is_radioactive": False,
    }

    response = requests.post(
        "http://127.0.0.1:8000/snacks/",
        json=new_snack,
        timeout=10,
    )

    response.raise_for_status()

    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const newSnack = {
      name: "Plutonian Ice Cream",
      price: 8.75,
      planet_of_origin: "Pluto",
      is_radioactive: false
    };

    fetch("http://127.0.0.1:8000/snacks/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newSnack)
    })
      .then((response) => response.json())
      .then((snack) => console.log(snack))
      .catch((error) => console.error(error));
    ```

=== "cURL"

    ```bash
    curl -X POST http://127.0.0.1:8000/snacks/ \
      -H "Content-Type: application/json" \
      -d "{\"name\":\"Plutonian Ice Cream\",\"price\":8.75,\"planet_of_origin\":\"Pluto\",\"is_radioactive\":false}"
    ```

!!! tip "Documentación interactiva"

    FastAPI genera automáticamente una interfaz interactiva de Swagger en `http://127.0.0.1:8000/docs`. Desde esa página puedes probar todos los endpoints sin escribir código adicional.

Regresa a la [página de inicio](index.md).