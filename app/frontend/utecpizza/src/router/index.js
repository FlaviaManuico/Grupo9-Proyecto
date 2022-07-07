import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/registro",
    name: "Registrar",
    component: () =>
      import(/* webpackChunkName: "ingresar" */ "../views/registro.vue"),
  },
  {
    path: "/ingresar",
    name: "Ingresar",
    component: () =>
      import(/* webpackChunkName: "ingresar" */ "../views/ingresar.vue"),
  },
  {
    path: "/pedidos",
    name: "Pedidos",
    component: () =>
      import(/* webpackChunkName: "pedidos" */ "../views/pedidos.vue"),
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
    name: "Ingresar",
    component: () =>
      import(/* webpackChunkName: "ingresar" */ "../views/ingresar.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
