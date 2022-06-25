import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import pizza from "../views/pizza.vue";
import entradas from "../views/entradas.vue";
import gaseosas from "../views/gaseosas.vue";
import carrito from "../views/carrito.vue";
import logout from "../views/logout";

const routes = [
  {
    path: "/logout",
    name: "Logout",
    component: logout,
  },
  {
    path: "/carrito",
    name: "Carrito",
    component: carrito,
  },
  {
    path: "/gaseosas",
    name: "Gaseosas",
    component: gaseosas,
  },
  {
    path: "/entradas",
    name: "Entradas",
    component: entradas,
  },
  {
    path: "/pizza",
    name: "Pizza",
    component: pizza,
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
