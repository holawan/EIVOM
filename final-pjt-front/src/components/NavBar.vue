<template>
<div id="nav">
  <nav class="navbar navbar-expand-lg navbar-light py-0" style="background-color: rgb(253, 243, 192);;">
    <div lass="container-fluid py-0">

      <div class="text">
        <div>
          <router-link :to="{ name: 'Search' }">Search</router-link>
        </div>

        <div>
          <router-link :to="{ name: 'Main' }">Main</router-link>
        </div>

        <div>
          <router-link :to="{ name: 'Crew' }">Crew</router-link>
        </div>

        <!-- profile or logout -->
        <div>
          <div v-if="isLoggedin && now==='profile'">
            <router-link :to="{ name: 'Logout'}">Logout</router-link>
          </div>

          <div v-if="isLoggedIn">
            <router-link :to="{ name: 'Profile', parmas:{user_pk: currentUser} }">Profile</router-link>
          </div>

          <div v-else>
            <router-link :to="{ name: 'Login'}">Profile</router-link>
          </div>
        </div>
      </div>

    </div>
  </nav>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:'NavBar',
  props:{
    now: String,
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  }

}
</script>

<style>
#nav {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a.router-link-exact-active {
  color: #7eb6ff;
}

b-navbar-nav{
  /* display: flex;
  flex-direction: row-reverse; */
  position: absolute;
  right: 0px;
}

.text{
  text-decoration: none;
}


</style>