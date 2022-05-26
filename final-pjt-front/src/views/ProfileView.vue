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
    <!-- {{profile.user.like_movies}} -->

      <div class="row">
        <div class="col-2" v-for="movie,idx in profile.user.like_movies"
            :key="idx"
            :movie="movie">
              <div >
            <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
              <div class="card card-block pr-3 embed-responsive embed-responsive-1by1" >
                <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top embed-responsive-item" alt="...">
                <div class="card-body">
                  <p class="card-text">{{ movie.title }}</p>
                </div>
              </div>  
            </router-link>
          </div>
          </div>

      </div>
    
    </div>
    <!-- {{this.likeMovies}} -->
    <!-- <my-movie-list :movies="profile.user.like_movies"></my-movie-list> -->
      <!-- {{profile}} -->

</template>

<script>
import NavBar from '@/components/NavBar.vue'
// import MyMovieList from '@/components/MyMovieList.vue'
import { mapActions, mapGetters } from 'vuex'
// import MovieListItem from '../components/MovieListItem.vue'

export default {
  name: 'UserView',
  data (){
    return {
      current_pk : this.$route.params.user_pk,
    }
  },
  components:{
    NavBar,
    // MovieListItem,
    
    // MyCrewList
    // MyMovieList,
  },
  computed :{
    ...mapGetters(['profile']),

  },
  methods : {
    ...mapActions(['fetchProfile'])
  },
  created(){
    this.fetchProfile(this.current_pk)
    console.log(this.profile,'profile!')
  },
  
}
</script>

<style>

</style>