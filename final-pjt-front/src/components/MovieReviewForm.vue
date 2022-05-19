<template>
  <div>
    <h1>MovieReviewForm</h1>
    <input type="text" @keyup.enter="inputMovieReview" v-model="movieReview">
  </div>
</template>

<script>
export default {
  name:'MovieReviewForm',
  data(){
    return {movieReview:''}
  },
  methods:{
    inputMovieReview(){
      const newReview = this.movieReview
      if (newReview){
        console.log('새 리뷰!!!')
        this.movieReview = ''
      }
    }
  }

}
</script>

<style>

</style>