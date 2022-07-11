<template>
  <head>
    <title>Error 404</title>
  </head>
  <body>
    <div class="container-404">
      <h1>Error 404</h1>
      <p>Esta página no se encuentra disponible.</p>
      <a href="/pizza" class="boton"> Volver a la Página Principal </a>
    </div>
  </body>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}
body {
  background: rgb(252, 108, 44);
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container-404 {
  text-align: center;
  width: 100%;
  max-width: 400px;
  background: #fff;
  padding: 20px;
  box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.3);
  border-radius: 5px;
  line-height: 1.7;
  color: #434343;
}
.boton {
  display: inline-block;
  margin-top: 15px;
  text-decoration: none;
  background: #64c564;
  color: #fff;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 15px;
}
</style>
