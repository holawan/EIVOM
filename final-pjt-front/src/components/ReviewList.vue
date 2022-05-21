<template>
  <div>
    <h1>ReviewList</h1>
    
    <review-list-item
      v-for="review in reviews"
      :review="review"
      :key="review.pk"  
    ></review-list-item>

    <review-form></review-form>
  </div>
</template>

<script>
import ReviewForm from './ReviewForm.vue'
import ReviewListItem from './ReviewListItem.vue'

export default {
  name:'ReviewList',
  components: {
    ReviewForm,
    ReviewListItem,
  },
  props:{ reviews:Array }
}
</script>

<style>

</style>