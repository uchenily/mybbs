// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store' // vuex
import router from './router'

// 导入样式
import './assets/style/reset.css'
import './assets/style/style.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store, // main.js中创建的store将会被派发到每一个子组件中
  router: router,
  components: { App: App },
  template: '<App/>'
})
