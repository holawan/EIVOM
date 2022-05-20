<template>
  <div>
    <h1>MovieReview</h1>
    
    <movie-review-item
      v-for="review in reviews"
      :review="review"
      :key="review.pk"
    ></movie-review-item>
    
    <movie-review-form></movie-review-form>
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
  },
  props: { reviews:Array }

}
</script>

<style>

</style>