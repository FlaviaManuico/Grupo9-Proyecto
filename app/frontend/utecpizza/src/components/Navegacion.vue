<template>
  <header class="barranav">
    <nav>
      <div class="logo">
        <router-link to="/pizza"
          ><img src="@/assets/logo.png" alt=""
        /></router-link>
      </div>
      <ul class="navigation">
        <li><router-link class="link" to="/">Pizza 🍕 </router-link></li>
        <li>
          <router-link class="link" to="/entradas">Entradas 🥟 </router-link>
        </li>
        <li>
          <router-link class="link" to="/gaseosas">Bebidas 🥤</router-link>
        </li>
        <li>
          <router-link class="link" to="/carrito">Carrito 🛒 </router-link>
        </li>
        <li><router-link class="link" to="/ingresar">Log-out</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
header {
  background-color: rgba(254, 111, 47, 255);
  z-index: 99;
  width: 100%;
  position: fixed;
  transition: 0.5s ease all;
  color: black;

  nav {
    display: flex;
    flex-direction: row;
    padding: 12px 0;
    width: 90%;
    margin: auto;
    @media (min-width: 1140px) {
      max-width: 1140px;
    }
  }

  ul,
  .link {
    color: rgba(239, 239, 239, 255);
    list-style: none;
    text-decoration: none;
  }

  li {
    text-transform: uppercase;
    padding: 16px;
    margin-left: 16px;
    display: inline-block;
  }

  .link {
    font-size: 16px;
    padding-bottom: 4px;
    border-bottom: 1px solid transparent;

    &:hover {
      color: rgba(239, 239, 239, 255);
      border-color: rgba(239, 239, 239, 255);
    }
  }

  .logo {
    display: flex;
    align-items: center;

    img {
      height: 60px;
    }
  }
}
</style>
