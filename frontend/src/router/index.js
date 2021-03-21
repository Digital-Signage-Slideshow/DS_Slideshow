import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import store from '../store' // your vuex store 

const ifNotAuthenticated = (to, from, next) => {
  console.log('authenticated: ' + store.getters.isAuthenticated);
  console.log('token: ' + localStorage.getItem('user-token'));

  if (!store.getters.isAuthenticated) {
    next()
    return
  }

  next('/')
}

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next()
    return
  }

  next('/login');
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter: ifAuthenticated,
  },

  {
    path: '/login',
    name: 'Login',

    component: () => import('../views/Login.vue'),
    beforeEnter: ifNotAuthenticated,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router