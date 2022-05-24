<template>
  <div>
    <SearchListItem
      v-for="(movie, idx) in movieList"
      :movie=movie
      :key=idx
      @on-click-item="onClickItem"
    />
  </div>
</template>

<script>
import SearchListItem from '@/components/search/SearchListItem'
export default {
  name: 'SearchList',
  components: {
    SearchListItem
  },
  props: {
    movieList: {}
  },
  methods: {
    onClickItem (movie) {
      this.$emit('on-click-item', movie)
    }
  }
}
</script>

<style>

</style>