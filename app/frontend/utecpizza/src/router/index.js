import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/ingresar",
    name: "Ingresar",
    component: () =>
      import(/* webpackChunkName: "ingresar" */ "../views/ingresar.vue"),
  },
  {
    path: "/carrito",
    name: "Carrito",
    component: () =>
      import(/* webpackChunkName: "carrito" */ "../views/carrito.vue"),
  },
  {
    path: "/gaseosas",
    name: "Gaseosas",
    component: () =>
      import(/* webpackChunkName: "gaseosas" */ "../views/gaseosas.vue"),
  },
  {
    path: "/entradas",
    name: "Entradas",
    component: () =>
      import(/* webpackChunkName: "entradas" */ "../views/entradas.vue"),
  },
  {
    path: "/pizza",
    name: "Pizza",
    component: () =>
      import(/* webpackChunkName: "pizza" */ "../views/pizza.vue"),
  },
  {
    path: "/",
    name: "Pizza",
    component: () =>
      import(/* webpackChunkName: "pizza" */ "../views/pizza.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
