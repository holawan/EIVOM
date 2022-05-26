<template>
<div id="nav" class="fixed-top">
  <nav class="navbar navbar-expand-lg navbar-light py-0" style="background-color:rgba(128,128,128,0.5); height:100px;">
      <div class="row" style="width:100vw; ">
        <div class="col-8 offset-2 d-flex flex-row">

        <div class="col-2 d-flex justify-content-center align-items-center">
          <!-- search magnifier -->
          <router-link :to="{ name: 'Search' }" style="text-decoration:none; color:black">
            <div class="d-flex flex-row align-items-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
              </svg>
              <h4 style="font-weight:bold">Search</h4>
            </div>
          </router-link>
        </div>

        <!-- center -->
        <div class="col-8">
          <!-- logo -->
          <div class="col-12">
            <router-link :to="{ name: 'Main' }" style="text-decoration:none; color:black;">
              <img src="@/assets/eivom_logo.png" alt="" style="height:120px; width:200px;">
            </router-link>
          </div>
        </div>

        <!-- profile or logout -->
        <div class="col-2 d-flex justify-content-center align-items-center">

            <router-link :to="{ name: 'Crew'}" style="text-decoration:none; color:black;" >
              <h4 style="font-weight:bold">
                Crew
              </h4> 
            </router-link>

            <router-link :to="{ name: 'Profile', params:{user_pk: currentUser.pk} }"  class="mx-3" style="text-decoration:none; color:black;">
              <h4 style="font-weight:bold">
                Profile
              </h4> 
            </router-link>

            <router-link :to="{ name: 'Logout'}" style="text-decoration:none; color:black;">
              <h4>
                Logout
              </h4> 
            </router-link>
        </div>
      </div>
      </div>

  </nav>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'NavBar',
  data () {
    return{
    }
  },
  props:{
    now: String,
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  },
  methods :{
    ...mapActions(['fetchCurrentUser'])
  },

  mounted(){

    if (!this.currentUser.pk) {
      this.fetchCurrentUser()}
    this.user_pk = localStorage.getItem('pk')
  },
  updated(){
    console.log(this.currentUser.pk)
  }


}
</script>

<style>
#nav {

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