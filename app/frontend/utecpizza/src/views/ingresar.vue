<template>
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <div class="form-login">
      <h5>Ingresar</h5>
      <form @submit.prevent="login">
        <div v-if="error" class="mensaje_error" role="alert">
          <p>{{ error }}</p>
        </div>
        <input
          v-model="username"
          class="controls"
          type="text"
          placeholder="Ingrese su usuario"
        />
        <input
          v-model="password"
          class="controls"
          type="password"
          placeholder="Ingrese su contraseña"
        />
        <button class="button" type="submit">Ingresar</button>
      </form>
      <form id="irRegistro" class="link">
        <p>
          <a href="/registro" id="Registrarse"
            >¿Aún no tienes una cuenta? Regístrate</a
          >
        </p>
      </form>
    </div>
  </body>
</template>

<script>
export default {
  name: "Ingresar",
  data() {
    return {
      username: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      const path = "http://127.0.0.1:5000/login";
      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("response: ", response);
      console.log("data: ", data);
      if (data["success"]) {
        localStorage.setItem("user-info", JSON.stringify(data));
        this.$router.push({
          name: "Pizza",
        });
      } else {
        this.error = "Usuario o contraseña incorrecta";
      }
    },
  },
  mounted() {
    let u = localStorage.getItem("user-info");
    if (u) {
      this.$router.push({
        name: "Pizza",
      });
    }
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
  background-color: #f6f7f8;
}

.form-login {
  width: 400px;
  /* height: 310px; */
  background: white;
  margin: auto;
  font-family: "Poppins", sans-serif;
  margin-top: 220px;
  border: 1px solid #dedede;
  border-radius: 20px;
  padding: 20px 30px;
  color: #5a5b5d;
}

.form-login h5 {
  margin: 0;
  text-align: center;
  height: 40px;
  margin-bottom: 10px;
  border-bottom: 1px solid;
  font-size: 25px;
  color: #0c0c0c;
}

.controls {
  width: 100%;
  border: 1px solid #b5c4d2;
  margin-bottom: 15px;
  padding: 11px 10px;
  background: white;
  font-size: 14px;
  font-weight: bold;
}

.button {
  width: 100%;
  height: 40px;
  background: #ff7f00;
  border: none;
  color: white;
  font-size: 16px;
  border-radius: 20px;
}

.form-login p {
  height: 40px;
  text-align: center;
  font-size: 18px;
  line-height: 40px;
}

.form-login a {
  color: rgb(72, 69, 69);
  text-decoration: none;
  font-size: 14px;
  margin-bottom: 10px;
}

.form-login a:hover {
  color: #ff7f00;
  text-decoration: underline;
}
.mensaje_error {
  width: 200px;
  height: 30px;
  margin-left: 65px;
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
