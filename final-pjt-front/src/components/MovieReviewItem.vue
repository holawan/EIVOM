<template>
  <div>
    <div>
      <router-link :to="{name: 'Profile', params: { user_pk: this.review.user.pk } }">
        <!-- {{ payload.nickname }} -->
      </router-link>
    </div>
    <div>
      <p>{{ payload.content }} {{ payload.rate }} </p>
      
    </div>
  </div>
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
      
      }
    }
  },
  computed:{
    ...mapGetters(['profile'])
    
  },
  methods:{
    ...mapActions(['fetchProfile'])
  },
  created(){
    this.fetchProfile(this.review.user.pk)
    // console.log(this.profile)
  }
}
</script>

<style>

</style>