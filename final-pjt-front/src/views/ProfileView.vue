<template>
  <div>
    <nav-bar :now="'Profile'"></nav-bar>
    <h1>Profile</h1>
    <hr>
    <h1>UserInfo</h1>
    <my-crew-list></my-crew-list>
    <!-- <my-movie-list :movies="profile.user.like_movies"></my-movie-list> -->
    <div>

    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyCrewList from '@/components/MyCrewList.vue'
// import MyMovieList from '@/components/MyMovieList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'UserView',
  data (){
    return {
    }
  },
  components:{
    NavBar,
    
    MyCrewList,
    // MyMovieList,
  },
  computed :{
    ...mapGetters(['profile'])
  },
  methods : {
    ...mapActions(['fetchProfile'])
  },
  mounted(){
    this.fetchProfile(1)
    console.log(this.profile,'profile!')
  }
}
</script>

<style>

</style>