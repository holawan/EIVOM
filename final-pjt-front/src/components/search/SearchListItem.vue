<template class="row">
<router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
    <div @click="onClickItem" class="searchitem col-3 my-1" style="border: solid 3px;">
      <img  style="width: 16rem; height: 19rem; "
        v-if="poster_path"
        :src="poster_path"
        alt="movie_poster"
      >
      <p class="my-2">  {{ movie.title }}</p>
    </div>
    </router-link>
</template>

<script>
export default {
  name: 'SearchListItem',
  props: {
    movie: {}
  },
  methods: {
    onClickItem () {
      this.$emit('on-click-item', this.movie)
    }
  },
  computed: {
    poster_path () {
      if (this.movie.poster_path) {
        return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      } else {
        return ''
      }
    }
  }
}
</script>

<style>
  .searchitem {
    display:inline-block; padding: 0px 0px;  margin-right:10px;
    cursor: pointer;
  }

  .searchitem:hover {
    background: #eee;
  }
</style>