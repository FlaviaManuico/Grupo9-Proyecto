<template>
  <div class="app">
    <Navegacion />
    <router-view />
  </div>
</template>

<script>
import Navegacion from "./components/Navegacion.vue";
export default {
  name: "App",
  components: {
    Navegacion,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
