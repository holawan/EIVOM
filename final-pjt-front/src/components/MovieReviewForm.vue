<template  v-for="index in 5">
  <div>
    <h1>MovieReviewForm</h1>
    <!-- <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input type="text" id="review"  v-model="content" required>
      <label for="rate">rate: </label>
      <input type="text" id="rate"  v-model="rate" required>
      <button>review</button>
    </form> -->
    <form @submit.prevent="onSubmit" class="d-flex justify-content-center">
      <div class="form-group">
        <label for="review">한 줄 리뷰</label>
        <small id="reviewHelp" class="form-text text-muted"></small>
        <input type="text" class="form-control" v-model="content" id="review" aria-describedby="reviewHelp" placeholder="다양한 생각을 남겨주세요">
      </div>
      <div class="form-group">
        <label for="rate">별점</label>
        <input type="text" class="form-control" v-model="rate" id="rate" placeholder="별점을 입력하세요 ! ">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div>
         <mark class="star" :class="index < score ? 'active' : ''" @click="getActiveStar(index)"></mark>
    </div>
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
      score :0
      }
  },
  methods:{
    ...mapActions(['createReview', 'fetchMovie']),
    onSubmit(){
      console.log(this.movieId)
      this.createReview({ movieId: this.movieId, content: this.content, rate:this.rate})
      this.content = ''
    },
    getActiveStar(index) {
      this.score = index + 1;
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

<!-- <style lang="scss"> -->
<style>
mark {
  background-color: transparent;
}
button {
  background: none;
  border: solid 1px;
  border-radius: 2em;
  font: inherit;
  padding: 0.75em 2em;
}
  
  .star {
    display: inline-block;
    position: relative;
    width: 0px;
    height: 0px;
    margin: 50px 0;
    border-right: 100px solid transparent!important;
    border-bottom: 70px solid lightgray;
    border-left: 100px solid transparent!important;
    color: lightgray;
    transform: rotate(35deg);
    cursor: pointer;
    
    &.active {
      border-color: yellow;
      
      &:after,
      &:before {
        border-color: yellow;
      }
    }
    
    &:before {
      display: block;
      position: absolute;
      top: -45px;
      left: -65px;
      width: 0;
      height: 0;
      border-bottom: 80px solid lightgray;
      border-left: 30px solid transparent!important;
      border-right: 30px solid transparent!important;
      transform: rotate(-35deg);
      content: '';
    }
    
    &:after {
      display: block;
      position: absolute;
      top: 3px;
      left: -105px;
      width: 0px;
      height: 0px;
      border-right: 100px solid transparent!important;
      border-bottom: 70px solid lightgray;
      border-left: 100px solid transparent!important;
      color: lightgray;
      transform: rotate(-70deg);
      content: '';
    }
  }
</style>