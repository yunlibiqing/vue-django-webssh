import Vue from 'vue'
import Router from 'vue-router'
import Term from '@/components/Term'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WebSSH',
      component: Term
    }
  ]
})
