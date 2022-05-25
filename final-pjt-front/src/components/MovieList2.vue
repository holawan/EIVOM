<template>
  <div>
    <movie-list-item
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
        <vue-glide v-if="movies.length"
      class="glide__track m-4"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1100: {perView: 4}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for = "(movie, idx) in movies"
        :key="idx">
        
        <movie-list-carousel
          :movie="movie"
        />
        
      </vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
import MovieListCarousel from './MovieListCarousel.vue'
// import MovieListItem from './MovieListItem.vue'

export default {
  name:'MovieList',
  components:{MovieListItem, MovieListCarousel},
  props:{
    movies:Array,
  }
}
</script>

<style>

</style>