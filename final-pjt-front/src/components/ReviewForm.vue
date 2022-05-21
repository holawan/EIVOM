<template>
  <div>
    <h1>ReviewForm</h1>
    <input type="text" @keyup.enter="inputReview" v-model="review">
  </div>
</template>

<script>
export default {
  name:'ReviewForm',
  data(){
    return {review:''}
  },
  methods:{
    inputReview(){
      const newReview = this.review
      if (newReview){
        console.log('새 리뷰!!!')
        this.review = ''
      }
    }
  }

}
</script>

<style>

</style>