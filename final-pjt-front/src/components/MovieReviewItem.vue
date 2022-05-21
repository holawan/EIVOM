<template>
  <div>
    <h1>MovieReviewItem</h1>
    <div>
      <router-link :to="{name: 'profile', params: { nickname: review.user.nickname } }">
        {{ review.user.nickname }}
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name:'MovieReviewItem',
  props: { review:Object },
  data(){
    return {
      // 수정 삭제할거면 필요
      payload: {
        movieId: this.review,
        reviewId: this.review.id,
        content: this.review.content
      }
    }
  }
}
</script>

<style>

</style>