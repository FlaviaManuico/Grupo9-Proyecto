<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <div class="app">
      <Navegacion />
      <router-view />
    </div>
    <div class="menu">
      <div class="pizzas">
        <img alt="Hawaiana" src="../assets/pizzas/Hawaiana.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pizza Hawaiana</h5>
            <h5 class="price">Desde S/ 10.00</h5>
          </div>
          <select class="opt" name="seleccion1">
            <option value="5" selected>Familiar (+ S/ 22.90)</option>
            <option value="6">Grande (+ S/ 12.90)</option>
            <option value="7">Mediana (+ S/ 6.90)</option>
            <option value="8">Personal</option>
          </select>
          <div class="boton">
            <button class="selec">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="pizzas">
        <img alt="Americana" src="../assets/pizzas/Americana.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pizza Americana</h5>
            <h5 class="price">Desde S/ 7.00</h5>
          </div>
          <select class="opt" name="seleccion2">
            <option value="9" selected>Familiar (+ 22.90)</option>
            <option value="10">Grande (+ 12.90)</option>
            <option value="11">Mediana (+ S/ 6.90)</option>
            <option value="12">Personal</option>
          </select>
          <div class="boton">
            <button class="selec">Añadir al Carrito</button>
          </div>
        </div>
      </div>
      <div class="pizzas">
        <img alt="Pepperoni" src="../assets/pizzas/Pepperoni.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pizza de Pepperoni</h5>
            <h5 class="price">Desde S/ 8.00</h5>
          </div>
          <select class="opt" name="seleccion3">
            <option value="13" selected>Familiar (+ S/ 22.90)</option>
            <option value="14">Grande (+ S/ 12.90)</option>
            <option value="15">Mediana (+ S/6.90)</option>
            <option value="16">Personal</option>
          </select>
          <div class="boton">
            <button class="selec">Añadir al Carrito</button>
          </div>
        </div>
      </div>
      <div class="pizzas">
        <img alt="Mozzarella" src="../assets/pizzas/Queso.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pizza Mozzarella</h5>
            <h5 class="price">Desde S/ 9.00</h5>
          </div>
          <select class="opt" name="seleccion4">
            <option value="17" selected>Familiar (+ S/ 22.90)</option>
            <option value="18">Grande (+ S/ 12.90)</option>
            <option value="19">Mediana (+ S/ 6.90)</option>
            <option value="20">Personal</option>
          </select>
          <div class="boton">
            <button class="selec">Añadir al Carrito</button>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Navegacion from "../components/Navegacion.vue";
export default {
  name: "App",
  components: {
    Navegacion,
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

.pizzas {
  display: grid;
  position: relative;
  grid-template-columns: align;
  grid-template-rows: auto 1fr;
  border-radius: 15px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  margin: 0 20px;
}

.details > select {
  background-color: rgb(252, 108, 44);
  border: none;
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  text-align: center;
  border-radius: 5px;
  width: 100%;
  height: 50px;
}
.pizzas img {
  position: relative;
  width: 100%;
  border-radius: 15px 15px 0 0;
  max-width: 100%;
  height: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  -o-object-fit: contain;
  object-fit: contain;
}

.details {
  padding: 20px 10px;
  display: grid;
  grid-template-rows: auto 1fr;
  grid-row-gap: 15px;
}
.details-sub {
  display: grid;
  grid-template-columns: auto auto;
}
.details-sub > h5 {
  font-weight: 600;
  font-size: 18px;
}
.price {
  text-align: right;
}
.details > p {
  color: #6f6f6f;
  font-size: 15px;
  line-height: 28px;
  font-weight: 400;
  align-self: stretch;
}

.details > button {
  background-color: #64c564;
  border: none;
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  border-radius: 5px;
  width: 100%;
  height: 40px;
}

.boton > button {
  background-color: #64c564;
  border: none;
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  border-radius: 5px;
  width: 100%;
  height: 40px;
}
</style>
