<template>

    <div class="d-flex "  >
      <router-link :to="{name: 'Profile', params: { user_pk: this.review.user.pk } }">
          <div class="col-3">
            <img :src="'http://127.0.0.1:8000'+ payload.image" alt="" style="width:120px;height:120px; border-radius:100px">
          </div>
      </router-link>
        <div class="offset-1 mb-0">
          <h5 class="mb-0 d-flex"> {{payload.nickname}}</h5>
          <p class="mb-0 mt-0  d-flex">{{date}}</p>
          <div v-if="!isEditing">
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
                <h3 class="mb-1  d-flex">{{ payload.content }} </h3>

          </div>
        <StarRating v-if="isEditing" v-model="payload.rate" id="rate" :rate="parseFloat(10) / 2" :read-only="false" :increment="1" @click="print('클릭')"></StarRating>

          <!--  -->
           <div v-if="isEditing">
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
              <label for="rate"></label>
              <!-- <input class="mb-0" type="text" v-model="payload.rate"> -->
              <input class="mb-0" type="text" v-model="payload.content">
              <button @click="onUpdate" class="btn btn-secondary rounded-pill"> Update</button>
              <button @click="switchIsEditing" class="btn btn-danger rounded-pill"> Cancle</button>
            </div>

           </div>
            <span v-if="currentUsernow == payload.commentUser" class="d-flex" >
            <!-- <span  > -->
            <button @click="switchIsEditing" :rate="parseFloat(10) / 2" class="btn btn-secondary rounded-pill">Edit</button> 
            <button @click="onDelete" class="btn btn-danger rounded-pill">Delete</button>
            </span>
        </div>
    
    </div>

</template>

<script>
import StarRating from 'vue-star-rating'
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MovieReviewItem',
  props: { review:Object },
  components:{
    StarRating,
  },
  data(){
    return {
      // 수정 삭제할거면 필요
      isEditing : false,
      payload: {
        nickname: this.review.user.profile.nickname,
        pk : this.review.pk,
        movieId: this.review.movie,
        content: this.review.content,
        rate: this.review.rate,
        created_at : this.review.created_at,
        commentUser : this.review.user.pk,
        image : this.review.user.profile.image,

      
      },
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
    },
    currentUsernow() {
      const currentUsernow = localStorage.getItem('user_pk')
      return currentUsernow
    }
    // currentUsernow() {
    //   const currentUsernow = this.currentUser
    //   return currentUsernow
    // },
    // commentUsernow() {
    //   const commentUsernow = this.commentUser
    //   return commentUsernow
    // }
  },
  methods:{
    ...mapActions(['fetchProfile','updateReview','deleteReview']),
    switchIsEditing() {
      this.isEditing =! this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
     

    },
    onDelete() {
      this.deleteReview(this.payload)
      this.$router.go()
    }

  },
  created(){
    this.fetchProfile(this.review.user.pk)
  },

}
</script>

<style>

</style>