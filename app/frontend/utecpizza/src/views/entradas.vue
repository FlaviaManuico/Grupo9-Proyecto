<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <div class="menu">
      <div class="entradas">
        <img alt="PanAjo" src="../assets/entradas/PanAlAjo.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pan al Ajo (x2)</h5>
            <h5 class="price">S/ 4.00</h5>
          </div>
          <div class="boton">
            <button class="selec" value="1">Añadir al Carrito</button>
          </div>
        </div>
      </div>
      <div class="entradas">
        <img alt="PanAjo" src="../assets/entradas/PanAlAjo.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Pan al Ajo (x4)</h5>
            <h5 class="price">S/ 8.00</h5>
          </div>
          <div class="boton">
            <button class="selec" value="2">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="entradas">
        <img alt="PalitosQueso" src="../assets/entradas/PalitosDeQueso.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Palitos de Queso (x2)</h5>
            <h5 class="price">S/ 5.50</h5>
          </div>
          <div class="boton">
            <button class="selec" value="3">Añadir al Carrito</button>
          </div>
        </div>
      </div>

      <div class="entradas">
        <img alt="PalitosQueso" src="../assets/entradas/PalitosDeQueso.jpeg" />
        <div class="details">
          <div class="details-sub">
            <h5>Palitos de Queso (x4)</h5>
            <h5 class="price">S/ 11.00</h5>
          </div>
          <div class="boton">
            <button class="selec" value="4">Añadir al Carrito</button>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<style>
.entradas {
  display: grid;
  position: relative;
  grid-template-columns: align;
  grid-template-rows: auto 1fr;
  border-radius: 15px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  margin: 0 20px;
}
.entradas img {
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
