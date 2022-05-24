<template>
  <div>
    <h1>ReviewListItem</h1>
    <div>
      <router-link :to="{name: 'profile', params: { nickname: review.user.nickname } }">
        {{ review.user.nickname }}
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name:'ReviewListItem',
  props:{ review:Object },

}
</script>

<style>

</style>