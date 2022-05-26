<template>
  <div>
    <h1 style="font-weight:bold">이 영화에 리뷰 남기기 </h1>
    
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
  name:'MovieReviewList',
  components:{
    MovieReviewForm,
    MovieReviewItem,
  },
  props: { 
    reviews:Array, }
  
}
</script>

<style>

</style>