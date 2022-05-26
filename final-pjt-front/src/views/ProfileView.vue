<template class="container">
  <div class="row">
    <div class="col-10 offset-1">
      <nav-bar :now="'Profile'"></nav-bar>
       <img :src="'http://127.0.0.1:8000' + profile.backdrop" id="poster-img"  style="width: 60%;  filter: brightness(100%); opacity: 1;" alt="...">
    </div>
    <div class="col-10 d-flex my-5 " >
      <img class="offset-3" :src="'http://127.0.0.1:8000' + profile.image" id="poster-img"  style="width: 7rem; height: 7rem;  filter: brightness(100%); border: solid 3px; border-radius: 100% ; opacity: 1;" alt="...">
      <div class="mx-5">
        
        <div style="font-size: 30px;">{{profile.nickname}}</div>
        <div style="font-size : 20px;">{{profile.introduce}}</div>
        
      </div>
    </div>
    <hr>
    <div v-if="profile">

      <movie-list-item v-for="movieId,idx in likeMovies"
          :key="idx"
          :movieId="movieId">

        </movie-list-item>
    </div>
    <my-crew-list></my-crew-list>
    <!-- {{this.likeMovies}} -->
    <!-- <my-movie-list :movies="profile.user.like_movies"></my-movie-list> -->
    <div>
      {{profile}}
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyCrewList from '@/components/MyCrewList.vue'
// import MyMovieList from '@/components/MyMovieList.vue'
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../components/MovieListItem.vue'

export default {
  name: 'UserView',
  data (){
    return {
      current_pk : this.$route.params.user_pk,
      
    }
  },
  components:{
    NavBar,
    MovieListItem,
    
    MyCrewList
    // MyMovieList,
  },
  computed :{
    ...mapGetters(['profile']),
    likeMovies() {
      return this.profile.user.like_movies
    }
  },
  methods : {
    ...mapActions(['fetchProfile'])
  },
  mounted(){
    this.fetchProfile(this.current_pk)
    console.log(this.profile,'profile!')
  }
}
</script>

<style>

</style>