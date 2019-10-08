import Vue      from 'vue'
import Router   from 'vue-router'
// user
import Index        from '@/components/Index'
import Login        from '@/components/Login'
import Logout       from '@/components/Logout'
import Register     from '@/components/Register'
import Topic        from '@/components/Topic'
import TopicNew     from '@/components/TopicNew'
import Category     from '@/components/Category'
import Categories   from '@/components/Categories'

// admin
import AdminIndex   from '@/components/admin/Index'
import AdminLogin   from '@/components/admin/Login'
import AdminLogout  from '@/components/admin/Logout'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/admin',
      name: 'AdminIndex',
      component: AdminIndex
    },{
      path: '/admin/login',
      name: 'AdminLogin',
      component: AdminLogin
    },{
      path: '/admin/logout',
      name: 'AdminLogout',
      component: AdminLogout
    },{
      path: '/',
      name: 'Index',
      component: Index
    },{
      path: '/login',
      name: 'Login',
      component: Login
    },{
      path: '/logout',
      name: 'Logout',
      component: Logout
    },{
      path: '/register',
      name: 'Register',
      component: Register
    },{
      path: '/topics/:id',
      name: 'Detail',
      component: Topic
    },{
      path: '/topic/new',
      name: 'TopicNew',
      component: TopicNew
    },{
      path: '/categories',
      name: 'Categories',
      component: Categories
    },{
      path: '/categories/:id',
      name: 'Category',
      component: Category
    },]
})
