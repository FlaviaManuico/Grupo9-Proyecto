<template>
  <body>
    <section class="registro-form">
      <input
        class="controls"
        type="text"
        name="usuario"
        id="usuario"
        placeholder="Ingrese un nombre de usuario"
      />
      <input
        class="controls"
        type="password"
        name="contrasena"
        id="contrasena"
        placeholder="Ingrese una contrasena"
      />
      <input
        class="controls"
        type="text"
        name="nombre"
        id="nombre"
        placeholder="Ingrese su nombre"
      />
      <input
        class="controls"
        type="text"
        name="apellido"
        id="apellido"
        placeholder="Ingrese su apellido"
      />
      <input
        class="controls"
        type="email"
        name="email"
        id="email"
        placeholder="Ingrese su correo"
      />
      <input
        class="controls"
        type="text"
        name="direccion"
        id="direccion"
        placeholder="Ingrese su direccion"
      />
      <input
        class="controls"
        type="number"
        name="telefono"
        id="telefono"
        placeholder="Ingrese su numero de telefono"
      />
      <botons class="botons" type="submit">"Registrar"</botons>
      <form id="irIngreso">
        <p>
          <a href="/ingresar" id="Ingresar"
            >¿Ya tienes una cuenta? Inicia Sesión</a
          >
        </p>
      </form>
    </section>
  </body>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #f3f3f3;
  font-family: "Poppins", sans-serif;
}

.registro-form {
  width: 380px;
  background: white;
  padding: 30px;
  margin: auto;
  margin-top: 100px;
  border-radius: 20px;
  border: 1px solid #dedede;
  font-family: "Poppins", sans-serif;
  color: #5a5b5d;
}

.registro-form h4 {
  font-size: 20px;
  margin-bottom: 18px;
}

.controls {
  width: 100%;
  background: white;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 16px;
  border: 1px solid #a4a7aa;
  font-family: "calibri";
  font-size: 18px;
  color: rgb(4, 3, 3);
}

.registro-form p {
  height: 40px;
  text-align: center;
  font-size: 18px;
  line-height: 40px;
}

.registro-form a {
  color: rgb(72, 69, 69);
  text-decoration: none;
  font-size: 14px;
}

.registro-form a:hover {
  color: #ff7f00;
  text-decoration: underline;
}

.registro-form .botons {
  width: 100%;
  background: #ff7f00;
  border-radius: 20px;
  border: none;
  padding: 12px;
  color: white;
  margin: 10px 0;
  font-weight: bold;
  font-size: 16px;
}
</style>
