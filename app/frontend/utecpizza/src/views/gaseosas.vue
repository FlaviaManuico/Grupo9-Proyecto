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
      <div class="bebidas">
        <img alt="Fanta" src="../assets/bebidas/FantaPersonal.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Fanta personal</h5>
            <h5 class="price">S/ 3.20</h5>
          </div>
          <div class="boton">
            <button class="selec" value="39">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="bebidas">
        <img alt="Sprite" src="../assets/bebidas/SpritePersonal.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Sprite personal</h5>
            <h5 class="price">S/ 3.20</h5>
          </div>
          <div class="boton">
            <button class="selec" value="45">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="bebidas">
        <img alt="Coca" src="../assets/bebidas/CocaColaPersonal.png" />
        <div class="details">
          <div class="details-sub">
            <h5>Coca Cola personal</h5>
            <h5 class="price">S/ 2.50</h5>
          </div>
          <div class="boton">
            <button class="selec" value="40">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="bebidas">
        <img alt="Inca" src="../assets/bebidas/IncaKolaPersonal.png" />
        <div class="details">
          <div class="details-sub">
            <h5>Inca Kola personal</h5>
            <h5 class="price">S/2.50</h5>
          </div>
          <div class="boton">
            <button class="selec" value="46">Añadir al Carrito</button>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import Navegacion from "./views/Navegacion.vue";
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
.bebidas {
  display: grid;
  position: relative;
  grid-template-columns: repeat(1, 1fr);
  grid-template-rows: repeat(1, 1fr);
  border-radius: 15px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  margin: 0 20px;
}
.bebidas img {
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
