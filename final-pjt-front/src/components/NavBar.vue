<template>
<div>
  <search-view></search-view>
  <router-link :to="{ name: 'Main' }">Main</router-link> |
  <router-link :to="{ name: 'Crew' }">Crew</router-link> |
  <router-link :to="{ name: 'User' }">User</router-link>

</div>
</template>

<script>
import SearchView from '@/views/SearchView.vue'

export default {
  name:'NavBar',
  components:{
    SearchView,
  }


}
</script>

<style>

</style>