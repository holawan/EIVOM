<template>
  <section class="container">
    <nav-bar :now="'MovieDetail'"></nav-bar>
    <!-- <div class="backdrop row m-0 my-5" :style="{ backgroundImage:  `url(${backdropUrl})` }" > -->
      <br>
      <br>
      <br>
    <div class="row my-5">
      <div class="col-4 align-self-center px-0" style="height: 80% ">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" id="poster-img"  style="width: 60%;  filter: brightness(100%); opacity: 1;" alt="...">
        <div class="col-12 d-flex justify-content-center">
          <div class="col-6">
            <button @click="likeMovie(movieId)">Like It</button>
          </div>
          <div class="col-6"> 
            <button @click="addMovie(this.movieId)">Add Crew</button>
          </div>
        </div>
      </div>
      <div class="col-7  text-dark">
        <div>
          <div class="d-flex ">
            <h2 class="mt-3 custom-break-word">{{ movie.title }}</h2>
            <div class="mt-4 offset-1"> {{ movie.release_date }}</div>
          </div>
          <h4  v-if="movie.title!==movie.original_title" class="custom-break-word offset-1 " align="left">{{ movie.original_title }}</h4>
          <div class="d-flex " v-for="genre,idx in movie.genres" :key="idx" :genre="genre">
              {{genre.name}}
          </div>
          <h5> {{movie.runtime}} 분</h5>
          <hr>
          <p>{{movie.tagline}}</p>
          <hr>
          <p class="custom-break-word color-dark">{{ movie.overview }}</p>
        </div>
        <div>
              <div class="star-ratings">
              <div 
                class="star-ratings-fill space-x-2 text-lg"
                :style="{ width: ratingToPercent + '%' }"
              >
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
              <div class="star-ratings-base space-x-2 text-lg">
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
                <p>{{this.movie.vote_average}}점 </p>
            </div>
        </div>
        </div>
      </div>
      <h1 class="mb-5 mx-2 " style="text" align="left">주요 출연진</h1>
      <actor-list :movieId ="movieId" class="row d-flex justify-content-center" ></actor-list>
      <br>
      <br>
      <movie-review-list :reviews="this.reviews"></movie-review-list>
      <movie-rec-similar></movie-rec-similar>
    <!-- movie like ui -->
  </section>

    <!-- movie cast -->
    
    

    <!-- <div 
      v-for="actor,idx in this.movie.actors"
      :key="idx"
      :idx="idx"
    >
      <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }">
        <div class="col-4 card mx-4 mb-5" style="width: 18rem;padding-left:0px;">
          <img class="card-img-top " :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="Card image cap" style="width:10rem; height:15rem; box-sizing:content-box;">
          <br>
            <h5>{{ movie.actors[idx] }}</h5>
        </div>
      </router-link>
    </div> -->
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MovieReviewList from '@/components/MovieReviewList.vue'
import MovieRecSimilar from '@/components/MovieRecSimilar.vue'
import ActorList from '@/components/ActorList.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'MovieDetailView',
  components:{
    NavBar,

    MovieReviewList,
    MovieRecSimilar,
    ActorList,
  },
  data(){
    return {
      movieId: this.$route.params.movie_pk
    }
  },
  computed: {
    ...mapGetters(['movie', 'reviews']),
    likeCount(){
      return this.movie.like_users?.length
    }, 
    backdropUrl(){
      return `https://image.tmdb.org/t/p/w400/${this.movie.backdrop_path}`
    },
    ratingToPercent() {
      const score = this.movie.vote_average *10;
      return score ;
  },
  },
  methods: {
    ...mapActions([
      'likeMovie',
      'fetchMovie',
      'addMovie',
      'readReviews'
    ])
  },
  mounted(){
    
    this.fetchMovie(this.movieId)
    this.readReviews(this.movieId)
    
  },

}
</script>

<style>
.backdrop{
  /* opacity: 0.5; */
  /* height: 100vh; */
  margin:0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
</style>