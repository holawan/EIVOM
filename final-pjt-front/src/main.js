import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

Vue.config.productionTip = false
//src/main.js
// import Vue from 'vue'
import GAuth from 'vue-google-oauth2'
import installElement from './plugins/element/installElement.js'
Vue.use(GAuth, {clientId: '12467946330-34q6at20mlbfvoh2makedvrbfiq7rpuh.apps.googleusercontent.com', scope: 'profile email https://www.googleapis.com/auth/plus.login'})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
