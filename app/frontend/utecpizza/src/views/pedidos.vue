<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <div class="app">
      <Navegacion />
      <router-view />
    </div>
    <div class="carrito-container">
      <h1>Carrito de Compras</h1>
      <div class="pedidos">
        <table id="miTabla" class="producto">
          <thead>
            <tr>
              <th>Producto</th>
              <th>Precio</th>
              <th>Cantidad</th>
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
            <tr v-for="(detail, index) in details" :key="detail">
              <td id="pedidos">{{ products[index].comida }}</td>
              <td id="pedidos">{{ products[index].precio }}</td>
              <td id="pedidos">{{ detail.cantidad }}</td>
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

<script>
import Navegacion from "../components/Navegacion.vue";
export default {
  name: "pedidos",
  data() {
    return {
      pedido_id: JSON.parse(localStorage.getItem("user-info"))["pedido_id"],
      details: [],
      products: [],
      detail: {
        pedido_id: "",
        producto_id: "",
        cantidad: "",
      },
    };
  },
  components: {
    Navegacion,
  },
  mounted() {
    let u = localStorage.getItem("user-info");
    if (!u) {
      this.$router.push({
        name: "Ingresar",
      });
    }
  },
  created() {
    this.postDetail();
  },
  methods: {
    async postDetail() {
      const path = "http://127.0.0.1:5000/cart";
      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          pedidoID: this.pedido_id,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      this.details = data.detalles;
      this.products = data.productos;
      console.log("response: ", response);
      console.log("data: ", this.details);
      console.log("data: ", this.products);
    },
    async deleteDetail(detailID) {
      const path = "http://127.0.0.1:5000/details/" + detailID;
      const response = await fetch(path, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("response: ", response);
      console.log("data: ", data);
    },
  },
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
body {
  background-color: #f3f3f3;
  font-family: "Poppins", sans-serif;
}

.menu {
  padding: 100px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  grid-gap: 40px 40px;
}

.enlace {
  background-color: #cb202d;
  color: #ffffff;
  /* margin-bottom: 30px; */
  /* padding: 10px 0 10px 0; */
  position: left;
  text-align: left;
}

.heading li a {
  text-decoration: none;
  font-size: 20px;
  color: white;
  padding: 15px;
  display: block;
  box-sizing: border-box;
  border-right: 1px #e9ebee;
}

.heading li {
  display: inline-block;
  text-align: start;
}

.heading li a:hover {
  background: #ef8354;
}

.heading {
  background-color: #cb202d;
  color: #ffffff;
  margin-bottom: 30px;
  padding: 10px 0 10px 0;
  grid-column: 1/-1;
  text-align: left;
}
.heading > h1 {
  font-weight: 400;
  font-size: 30px;
  letter-spacing: 10px;
  margin-bottom: 10px;
}
.heading > h3 {
  font-weight: 600;
  font-size: 22px;
  letter-spacing: 5px;
}
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
