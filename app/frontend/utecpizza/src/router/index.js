import { createRouter, createWebHashHistory } from "vue-router";
import pizza from "../views/pizza.vue";
import entradas from "../views/entradas.vue";
import gaseosas from "../views/gaseosas.vue";
import carrito from "../views/carrito.vue";

const routes = [
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
    name: "Pizza",
    component: pizza,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
