import Vue from 'vue'
import VueRouter from 'vue-router'
import products from '../views/products.vue'
import locations from '../views/locations.vue'
import prod_movs from '../views/prod_movs.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Products',
    component: products
  },
  {
    path: '/products',
    name: 'products',
    component: products
  },
  {
    path: '/locations',
    name: 'locations',
    component: locations
  },
  {
    path: '/prod_movs',
    name: 'prod_movs',
    component: prod_movs
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
