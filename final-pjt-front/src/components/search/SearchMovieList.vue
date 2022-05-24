<template>
  <div>
    <SearchListItemPreview
      v-for="(movie, idx) in movieList"
      :movie=movie
      :key=idx></SearchListItemPreview>
    <SearchListItem
      v-for="(movie2) in movieListMain"
      :movie=movie2
      :key=movie2.pk
      @on-click-item="onClickItem"
    ></SearchListItem>
  </div>
</template>

<script>
import SearchListItem from '@/components/search/SearchListItem'
import SearchListItemPreview from '@/components/search/SearchListItemPreview'
export default {
  name: 'SearchList',
  components: {
    SearchListItem,
    SearchListItemPreview
  },
  props: {
    movieList: {},
    movieListMain:{},
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