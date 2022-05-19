<template>
  <div>
    <h1>SearchView</h1>
    <search-var></search-var>
    <search-genre></search-genre>
    <search-list></search-list>
  </div>
</template>

<script>
import SearchVar from '@/components/SearchVar.vue'
import SearchList from '@/components/SearchList.vue'
import SearchGenre from '@/components/SearchGenre.vue'

export default {
  name: 'SearchView',
  components: {
    SearchVar,
    SearchList,
    SearchGenre,
  }
  

}
</script>

<style>

</style>