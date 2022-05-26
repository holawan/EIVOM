<template>
<div id="nav">
  <nav class="navbar navbar-expand-lg navbar-light py-0" style="background-color: white; opacity:70%; height:80px;">
      <div class="row" style="width:100vw; ">
        <div class="col-2 d-flex justify-content-center">
          <!-- search magnifier -->
          <router-link :to="{ name: 'Search' }" style="text-decoration:none; color:black" >
            <div class="d-flex flex-row align-items-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              <h4>Search</h4>
            </div>
          </router-link>
        </div>

        <div class="col-4">
          <router-link :to="{ name: 'Main' }" style="text-decoration:none; color:black;">
            <h4>
              MAIN
            </h4> 
          </router-link>
        </div>

        <div class="col-4">
          <router-link :to="{ name: 'Crew' }" style="text-decoration:none; color:black;">
            <h4>
              CREW
            </h4> 
          </router-link>
        </div>

        <!-- profile or logout -->
        <div class="col-2">
          <div v-if="isLoggedin && now==='profile'">
            <router-link :to="{ name: 'Logout'}" style="text-decoration:none; color:black;">
              <h4>
                Logout
              </h4> 
            </router-link>
          </div>

          <div v-if="isLoggedIn">
            <router-link :to="{ name: 'Profile', parmas:{user_pk: currentUser} }" style="text-decoration:none; color:black;">
              <h4>
                Profile
              </h4> 
            </router-link>
          </div>

          <div v-else>
            <router-link :to="{ name: 'Login'}" style="text-decoration:none; color:black;">
              <h4>
                Login
              </h4> 
            </router-link>
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