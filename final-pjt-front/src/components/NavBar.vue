<template>
<div id="nav">
  <nav class="navbar navbar-expand-lg navbar-light py-0" style="background-color:gray; opacity:70%; height:80px;">
      <div class="row" style="width:100vw; ">
        <div class="col-8 offset-2 d-flex flex-row">

        <div class="col-2 d-flex justify-content-center align-items-center">
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

        <!-- center -->
        <div class="col-8">
          <!-- logo -->
          <div class="col-12">
            <router-link :to="{ name: 'Main' }" style="text-decoration:none; color:black;">
              <img src="@/assets/eivom_logo.png" alt="" style="height:60px; width:100px;">
            </router-link>
          </div>
          <div class="col-12 d-flex justify-content-around">
            <div class="">
              <router-link :to="{ name: 'Main' }" style="text-decoration:none; color:black;">
                <h6>
                  MAIN
                </h6> 
              </router-link>
            </div>

            <div class>
              <router-link :to="{ name: 'Crew' }" style="text-decoration:none; color:black;">
                <h6>
                  CREW
                </h6> 
              </router-link>
            </div>

          </div>
        </div>

        <!-- profile or logout -->
        <div class="col-2 d-flex justify-content-center align-items-center">
          <div v-if="isLoggedIn && now==='profile'">
            <router-link :to="{ name: 'Logout'}" style="text-decoration:none; color:black;">
              <h4>
                Logout
              </h4> 
            </router-link>
          </div>


          <div v-if="isLoggedIn">
            <router-link :to="{ name: 'Profile', params:{user_pk: currentUser} }" style="text-decoration:none; color:black;">
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
      </div>

  </nav>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:'NavBar',
  data(){
    return {
      user_pk: this.currentUser
    }
  },
  props:{
    now: String,
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'logintf'])
  },

  mounted(){
    console.log('1',this.isLoggedIn)
    console.log('2',this.currentUser)
    console.log('3',this.logintf)
    console.log('4',this.user_pk)
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