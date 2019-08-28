/* eslint-disable */
import Vue from 'vue'
import { store } from '../store/store'
import Router from 'vue-router'
import Mainpage from '@/components/mainpage'
import Dashboard from '@/components/Dashboard/dashboard'
import Signin from '@/components/User/signin'
import Home from '@/components/User/home'
import CostPrediction from '@/components/CostPrediction/costprediction.vue'
import CostToConfiguration from '@/components/CostToConfiguration/costtoconfig.vue'
import DesktopCost from "@/components/CostPrediction/desktopcost";
import LaptopCost from "@/components/CostPrediction/laptopcost";
import Order from '@/components/Order/ordersummary'
Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: "*",
      redirect: "/"
    },
    {
      path: "/",
      name: "Mainpage",
      component: Mainpage
    },
    {
      path: "/home",
      name: "Home",
      component: Home,
      children: [
        {
          path: "/signin",
          name: "Signin",
          component: Signin,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/dashboard",
          name: "Dashboard",
          component: Dashboard,
          meta: {
            authRequired: true
          }
        },
        {
          path: "/costpred",
          name: "CostPrediction",
          component: CostPrediction,
          meta: {
            authRequired: true
          }
        },
        {
          path: "/getconfig",
          name: "CostToConfiguration",
          component: CostToConfiguration,
          meta: {
            authRequired: true
          }
        },
        {
          path: "/desktopcost",
          name: "DesktopCost",
          component: DesktopCost,
          meta: {
            authRequired: true
          }
        },
        {
          path: "/laptopcost",
          name: "LaptopCost",
          component: LaptopCost,
          meta: {
            authRequired: true
          }
        },
        {
          path: "/orders",
          name: "Order",
          component: Order,
          meta: {
            authRequired: true
          }
        }
      ]
    }
  ],
  mode: "history"
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
    if (!store.getters.getUserId) {
      next({
        path: '/signin',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
