<template>

    <div class="d-flex ">
      <div>
        
        </div>
      <router-link :to="{name: 'Profile', params: { user_pk: this.review.user.pk } }">
      <div class="col-3">
        <img :src="'http://127.0.0.1:8000'+ profile.image" alt="" style="width:120px;height:120px; border-radius:100px">
      </div>
        <!-- {{ payload.nickname }} -->
      </router-link>
        <div class="offset-1 mb-0">
          <h5 class="mb-0"> {{profile.nickname}}</h5>
          <p class="mb-0 mt-0">{{date}}</p>
            <div class="star-ratings mb-0 d-flex">
              <div 
                class="star-ratings-fill space-x-2 text-lg"
                :style="{ width: ratingToPercent + '%' }"
              >
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
              <div class="star-ratings-base space-x-2 text-lg">
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
                <p class="mb-0">{{payload.rate}}점 </p>
            </div>
          <h3 class="mb-1">{{ payload.content }} </h3>
        </div>
    </div>
      <!-- {{payload}} -->

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MovieReviewItem',
  props: { review:Object },
  data(){
    return {
      // 수정 삭제할거면 필요
      payload: {
        // nickname: this.profile.nickname,
        movieId: this.review,
        reviewId: this.review.id,
        content: this.review.content,
        rate: this.review.rate,
        created_at : this.review.created_at
      
      }
    }
  },
  computed:{
    
    ...mapGetters(['profile']),
      ratingToPercent() {
      const score = this.payload.rate *20;
      return score ;
  },
    date() {
      const date = this.payload.created_at.slice(0,10)
      return date
    }
  },
  methods:{
    ...mapActions(['fetchProfile'])
  },
  created(){
    this.fetchProfile(this.review.user.pk)
  },

}
</script>

<style>

</style>