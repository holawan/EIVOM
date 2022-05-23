import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

Vue.config.productionTip = false
//src/main.js
// import Vue from 'vue'

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
