<template>
  <div>
    
    <!-- <div>
      <router-link :to="{name: 'profile', params: { nickname: comments.user.nickname } }">
        {{ comments.user.nickname }}
      </router-link>
    </div> -->
  {{comment.content}}
  </div>
</template>

<script>
export default {
  name:'ReviewListItem',
  props:{ comment:Object },

}
</script>

<style>

</style>