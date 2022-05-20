<template>
  <div>
    <h1>MovieDetailView</h1>
    <h2>{{ movie.title }} </h2>

    <!-- movie like ui -->
    <div>
      LikeIt: 
      <button
        @click="likeMovie(movieId)"
      >{{ likeCount }} </button>
    </div>


    <movie-cast></movie-cast>
    <movie-review-list :reviews="movie.reviews"></movie-review-list>
    <movie-rec-similar></movie-rec-similar>
  </div>
</template>

<script>
import MovieCast from '@/components/MovieCast.vue'
import MovieReviewList from '@/components/MovieReviewList.vue'
import MovieRecSimilar from '@/components/MovieRecSimilar.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'MovieDetailView',
  components:{
    MovieCast,
    MovieReviewList,
    MovieRecSimilar,
  },
  data(){
    return {
      movieId: this.$route.params.movieId
    }
  },
  computed: {
    ...mapGetters(['movie']),
    likeCount(){
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'likeMovie',
      'fetchMovie',

    ])
  },
  created(){
    this.fetchMovie(this.movieId)
  }
}
</script>

<style>

</style>