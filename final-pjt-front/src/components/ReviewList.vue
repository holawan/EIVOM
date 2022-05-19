<template>
  <div>
    <h1>ReviewList</h1>
    <review-form></review-form>
    <review-list-item></review-list-item>
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
  }
}
</script>

<style>

</style>