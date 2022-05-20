<template>
  <div>
    <h1>Profile</h1>
    <hr>
    <h1>UserInfo</h1>
    <my-crew-list></my-crew-list>
    <my-movie-list></my-movie-list>
  </div>
</template>

<script>
import MyCrewList from '@/components/MyCrewList.vue'
import MyMovieList from '@/components/MyMovieList.vue'

export default {
  name: 'UserView',
  components:{
    MyCrewList,
    MyMovieList,
  }
}
</script>

<style>

</style>