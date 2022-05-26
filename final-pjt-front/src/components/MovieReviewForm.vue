<template  v-for="index in 5"  class="d-flex justify-content-center continer">
  <div>
    <!-- <h1>MovieReviewForm</h1> -->
    <!-- <form @submit.prevent="onSubmit">
      <label for="review">review: </label>
      <input type="text" id="review"  v-model="content" required>
      <label for="rate">rate: </label>
      <input type="text" id="rate"  v-model="rate" required>
      <button>review</button>
    </form> -->
    <div >

      <form @submit.prevent="onSubmit" >
        <div class="form-group row">
          <div class="col-12" >
            <label for="review" style="font-size: 30px;">한 줄 리뷰</label>
            <small id="reviewHelp" class="form-text text-muted"></small>
            <input type="text" class="form-control" v-model="content" id="review" aria-describedby="reviewHelp" placeholder="다양한 생각을 남겨주세요">
      <div class="d-flex justify-content-center">
        <h3 class="mt-3">당신의 평점</h3>
        
        <StarRating v-model="rate" id="rate" :rate="parseFloat(10) / 2" :read-only="false" :increment="1" @click="print('클릭')"></StarRating>
  
      </div>
      <br>
      <br>
            <button type="submit" class="btn btn-warning rounded-pill">Submit</button>
          </div>
          </div>
        <div class="form-group">
          <label for="rate"></label>
          <!-- <input type="text" class="form-control" v-model="rate" id="rate" placeholder="별점을 입력하세요 ! " style="display: hidden;"> -->
        </div>
        <div>
          
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import { mapActions, mapGetters} from 'vuex'
export default {
  name:'MovieReviewForm',
  components :{
    StarRating
  },
  data(){
    return {
      content:'',
      rate:'',
      movieId: this.$route.params.movie_pk,
      score :0,
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
    },
    click(event){
      console.log(event)
      console.log(this.rate)
    },

  },
  computed:{
    ...mapGetters(['reviews','movie']),
  },
  created(){
    this.fetchMovie(this.movieId)
  }

}
</script>

<!-- <style lang="scss"> -->
<style>
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>