<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
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

<style>
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
</style>
