<template>
  <div>
    <h1>MovieReviewForm</h1>
    <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input type="text" id="review"  v-model="content" required>
      <button>review</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MovieReviewForm',
  data(){
    return {content:''}
  },
  computed:{
    ...mapGetters(['movie']),
  },
  methods:{
    ...mapActions(['createReview']),
    onSubmit(){
      this.createReview({ movieId: this.movie.id, content: this.content, })
      this.content = ''
    }
  }

}
</script>

<style>

</style>