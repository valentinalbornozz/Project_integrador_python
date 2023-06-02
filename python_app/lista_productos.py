html_template = """
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lista de Productos</title>
    <style>
                body {{
                    background: #00366c55;
                }}

                .container {{
                    max-width: 400px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }}

                h1 {{
                    color: black;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}

                h2 {{
                    margin-top: 30px;
                    color: black;
                }}

                form {{
                    margin-top: 20px;
                    text-align: left;
                }}

                label {{
                    display: block;
                    margin-bottom: 10px;
                    color: black;
                }}

                input[type="text"],
                input[type="number"] {{
                    width: 100%;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                    margin-bottom: 20px;
                    border-radius: 20px;
                }}

                input[type="submit"] {{
                    background-color: #0759fdb8;
                    color: black;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    border-radius: 20px;
                }}

                input[type="submit"]:hover {{
                    color: white;
                }}

                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}

                th,
                td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    background-color: white;
                }}

                th {{
                    background-color: #f2f2f2;
                }}

                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}

                a {{
                    background: #0759fdb8;
                    text-decoration: none;
                    color: black;
                    padding: 10px;
                    border-radius: 20px;
                    display: inline-grid;
                    justify-content: center;
                    align-content: center;
                    margin-top: 10px;
                }}

                a:hover {{
                    color: white;
                }}
            </style>
  </head>
  <body>
    <h1>Lista de Productos</h1>
    {% if products %}
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Cantidad</th>
          </tr>
        </thead>
        <tbody>
          {% for product in products %}
            <tr>
              <td>{{ product.id }}</td>
              <td>{{ product.nombre }}</td>
              <td>{{ product.precio }}</td>
              <td>{{ product.cantidad_stock }}</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p>No se encontraron productos registrados.</p>
    {% endif %}
    <a href="/">Volver al inicio</a>
  </body>
</html>
"""

