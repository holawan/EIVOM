<template>
  <div id="app">
    <nav-bar></nav-bar>
    <hr />
    <router-view></router-view>
    <div class="jb-image"><img src="@/assets/main_bg.jpg" alt=""></div>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: { NavBar },
  methods: {

  },
  created(){

  }, 
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
