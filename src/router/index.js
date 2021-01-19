import Vue from "vue";
import VueRouter from "vue-router";
import products from "../views/products.vue";
import Home from "../views/Home.vue";
import locations from "../views/locations.vue";
import prod_movs from "../views/prod_movs.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    meta: { title: "Home" },
  },
  {
    path: "/products",
    name: "products",
    component: products,
    meta: { title: "Products" },
  },
  {
    path: "/locations",
    name: "locations",
    component: locations,
    meta: { title: "Locations" },
  },
  {
    path: "/prod_movs",
    name: "prod_movs",
    component: prod_movs,
    meta: { title: "Product Movements" },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
