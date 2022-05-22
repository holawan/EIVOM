<template>
  <div>
    <h1>MovieReviewForm</h1>
    <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input type="text" id="review"  v-model="content" required>
      <label for="rate">rate: </label>
      <input type="text" id="rate"  v-model="rate" required>
      <button>review</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'
export default {
  name:'MovieReviewForm',
  data(){
    return {
      content:'',
      rate:'',
      movieId: this.$route.params.movie_pk,
      }
  },
  methods:{
    ...mapActions(['createReview', 'fetchMovie']),
    onSubmit(){
      console.log(this.movieId)
      this.createReview({ movieId: this.movieId, content: this.content, rate:this.rate})
      this.content = ''
    }
  },
  computed:{
    ...mapGetters(['reviews'])
  },
  created(){
    this.fetchMovie(this.movieId)
  }

}
</script>

<style>

</style>