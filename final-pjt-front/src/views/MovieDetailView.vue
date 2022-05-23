<template>
  <div>
    <h2>{{ movie.title }} </h2>

    <!-- movie like ui -->
    <div>
      LikeIt: 
      <button
        @click="likeMovie(movieId)"
      >좋아요</button>
    </div>
    <div>
      AddCrew:
      <button
        @click="addMovie(this.movieId)"
      >크루에 추가하기</button>
    </div>

    <!-- movie cast -->
    <div 
      v-for="actor,idx in this.movie.actors"
      :key="idx"
      :idx="idx"
    >
      <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="">
        <h5>{{ movie.actors[idx] }}</h5>
      </router-link>
      


    </div>


    <movie-review-list :reviews="this.reviews"></movie-review-list>
    <movie-rec-similar></movie-rec-similar>
  </div>
</template>

<script>
import MovieReviewList from '@/components/MovieReviewList.vue'
import MovieRecSimilar from '@/components/MovieRecSimilar.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'MovieDetailView',
  components:{
    MovieReviewList,
    MovieRecSimilar,
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
    }
  },
  methods: {
    ...mapActions([
      'likeMovie',
      'fetchMovie',
      'addMovie',
      'readReviews'
    ])
  },
  created(){
    
    this.fetchMovie(this.movieId)
    this.readReviews(this.movieId)
    
  },

}
</script>

<style>

</style>