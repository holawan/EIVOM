<template>
  <div>
    <h1>MovieReview</h1>
    <movie-review-form></movie-review-form>
    <movie-review-item></movie-review-item>
  </div>
</template>

<script>
import MovieReviewForm from './MovieReviewForm.vue'
import MovieReviewItem from './MovieReviewItem.vue'

export default {
  name:'MovieReview',
  components:{
    MovieReviewForm,
    MovieReviewItem,
  }

}
</script>

<style>

</style>