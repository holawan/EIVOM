<template>
  <div>
    <h1>MovieDetailView</h1>
    <h2>{{ movie.title }} </h2>

    <!-- movie like ui -->
    <div>
      LikeIt: 
      <button
        @click="likeMovie(movieId)"
      >좋아요 하트 색깔 바뀌기</button>
    </div>
    <div>
      AddCrew:
      <button
        @click="addMovie(movieId)"
      > </button>
    </div>

    <movie-review-list :reviews="movie.reviews"></movie-review-list>
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
    ...mapGetters(['movie']),
    likeCount(){
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'likeMovie',
      'fetchMovie',
      'addMovie',

    ])
  },
  created(){
    this.fetchMovie(this.movieId)
  }
}
</script>

<style>

</style>