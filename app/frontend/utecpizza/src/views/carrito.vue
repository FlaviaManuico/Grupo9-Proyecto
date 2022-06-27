<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <div class="carrito-container">
      <h1>Carrito de Compras</h1>
      <div class="pedidos">
        <table id="miTabla" class="producto">
          <thead>
            <tr>
              <th>Producto</th>
              <th>Precio</th>
              <th>Eliminar</th>
            </tr>
          </thead>

          <tfoot>
            <tr>
              <td><h3>Total (en soles):</h3></td>
              <td colspan="3"><h3>-----</h3></td>
              <td></td>
            </tr>
          </tfoot>
          <tbody>
            <tr>
              <td id="pedidos"></td>
              <td></td>
              <td>
                <button class="delete-button">&cross;</button>
              </td>
              <td></td>
            </tr>
          </tbody>
        </table>

        <p><button class="calculo">Calcular</button></p>
        <p>
          <button id="chk" class="checkout" action="/checkout">Checkout</button>
        </p>
      </div>
    </div>
  </body>
</template>

<style>
.pedidos {
  display: grid;
  position: relative;
  grid-template-columns: align;
  grid-template-rows: auto 1fr;
  border-radius: 15px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  margin: 0 20px;
}

.carrito-container {
  max-width: 1000px;
  margin: 0 auto;
}
.carrito-container h1 {
  padding: 120px 10px;
  text-align: center;
  text-transform: uppercase;
  text-decoration: underline;
}

.producto {
  padding: 20px;
  width: 100%;
}
.producto thead th {
  font-size: 20px;
}

table tr {
  font-size: 18px;
  padding: 20px;
  width: 100%;
}

tbody {
  font-size: 16px;
}

.pedidos {
  text-align: left;
  max-width: 100%;
}

.btn-area:hover {
  background-color: #76bfb6;
  color: #fff;
  font-weight: 600;
}

.btn-area i {
  margin-right: 5px;
}

tbody button {
  bottom: 20px;
  right: 20px;
  padding: 10px 10px;
  background-color: #f94343;
  color: white;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  font-family: "Poppins", sans-serif;
}
.calculo {
  position: relative;
  bottom: 15px;
  right: -305px;
  padding: 15px 40px;
  background-color: rgb(252, 108, 44);
  color: white;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  font-family: "Poppins", sans-serif;
}

.checkout {
  position: absolute;
  bottom: 15px;
  right: 305px;
  padding: 15px 40px;
  background-color: #64c564;
  color: white;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  font-family: "Poppins", sans-serif;
}
</style>