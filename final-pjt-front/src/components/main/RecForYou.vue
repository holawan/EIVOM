// 당신을 위한 추천
// 클러스터링 / ML

<template>
  <div>
    <h1>RecForYou</h1>
    <h2>{{ cmTitle }}</h2>
    
    <div
     v-for="movie in this.clusterMovies"
     :key="movie.pk"
    >
      <div>
        <router-link :to="{name: 'MovieDetail', params: {movie_pk:movie.pk} }">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" alt="">
          <h3>{{ movie.title }}</h3>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RecForYou',
  methods:{
    ...mapActions(['getClusterMovies'])
  },
  computed:{
    ...mapGetters(['clusterMovies', 'cmTitle'])
  },
  created(){
    this.getClusterMovies()
  }
}
</script>

<style>

</style>