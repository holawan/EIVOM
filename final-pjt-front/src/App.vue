<template>
  <div id="app">
    <!-- <nav-bar></nav-bar> -->
    <router-view></router-view>
  </div>
</template>


<script>
// import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  // components: { NavBar },
  methods: {

  },
  created(){

  }, 
}

</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height:100vh;
  width:100vw;
}

nav {
  padding: 30px;
}

/* nav a {
  font-weight: bold;
  color: #2c3e50;
} */

/* nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
