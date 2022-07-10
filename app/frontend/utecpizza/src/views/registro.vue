<template>
  <body>
    <form @submit.prevent="singup" class="registro-form">
      <div v-if="error" class="mensaje_error" role="alert">
        <p>{{ error }}</p>
      </div>
      <input
        v-model="username"
        class="controls"
        type="text"
        placeholder="Ingrese un nombre de usuario"
      />
      <input
        v-model="password"
        class="controls"
        type="password"
        placeholder="Ingrese una contrasena"
      />
      <input
        v-model="name"
        class="controls"
        type="text"
        placeholder="Ingrese su nombre"
      />
      <input
        v-model="lastname"
        class="controls"
        type="text"
        placeholder="Ingrese su apellido"
      />
      <input
        v-model="email"
        class="controls"
        type="email"
        placeholder="Ingrese su correo"
      />
      <input
        v-model="adress"
        class="controls"
        type="text"
        placeholder="Ingrese su direccion"
      />
      <input
        v-model="phone"
        class="controls"
        type="number"
        placeholder="Ingrese su numero de telefono"
      />
      <button class="botons" type="submit">Registrar</button>
      <p>
        <router-link class="irIngresar" to="/">
          ¿Ya tienes una cuenta? Inicia Sesión
        </router-link>
      </p>
    </form>
  </body>
</template>

<script>
export default {
  name: "Registrar",
  data() {
    return {
      username: "",
      password: "",
      name: "",
      lastname: "",
      email: "",
      adress: "",
      phone: "",
      error: "",
    };
  },
  methods: {
    async singup() {
      const path = "http://127.0.0.1:5000/users";
      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
          name: this.name,
          lastname: this.lastname,
          email: this.email,
          adress: this.adress,
          phone: this.phone,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("response: ", response);
      console.log("data: ", data);
      if (data["success"]) {
        this.$router.push({
          name: "Ingresar",
        });
      } else {
        this.error = "Usuario y/o email ya está en uso.";
      }
    },
  },
};
</script>

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
.a {
  width: 100%;
  border-radius: 20px;
  border: none;
  padding: 12px;
  color: white;
  margin: 10px 0;
  font-weight: bold;
  font-size: 16px;
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

.mensaje_error {
  width: 200px;
  height: 30px;
  margin-left: 58px;
  margin-bottom: 20px;
  border-radius: 3px;
}

.mensaje_error p {
  text-align: center;
  background: #ffd5d5;
  color: rgb(233, 26, 26);
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 15px;
  border-radius: 3px;
}
</style>
