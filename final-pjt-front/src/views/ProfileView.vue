<template>
  <div>
    <nav-bar :now="'Profile'"></nav-bar>
    <h1>Profile</h1>
    <hr>
    <h1>UserInfo</h1>
    <my-crew-list></my-crew-list>
    <my-movie-list :movies="profile.like_movies"></my-movie-list>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyCrewList from '@/components/MyCrewList.vue'
import MyMovieList from '@/components/MyMovieList.vue'

export default {
  name: 'UserView',
  components:{
    NavBar,
    
    MyCrewList,
    MyMovieList,
  }
}
</script>

<style>

</style>