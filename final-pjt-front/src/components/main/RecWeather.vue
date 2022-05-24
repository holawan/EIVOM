// 날씨기반 영화추천
// 날씨에 따른 추천할 영화 데이터 만들고
// 날씨 (비, 눈, 맑음, 구름 정도?) api로 가져오기 => 가능할까요? 네!!!!

<template>
  <div>
    <h1>RecWeather</h1>
    <h2>{{ weather }}</h2>
    <movie-list-item
      v-for="movie in weatherMovies"
      :key="movie.pk"
      :movie="movie"
    >
    </movie-list-item>
    

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'
export default { 
  name: 'RecWeather',
  components:{
    MovieListItem,
  },

  computed:{
    ...mapGetters(['weather', 'weatherMovies','authHeader']),
    
  },
  methods:{
    ...mapActions(['getWeather', 'fetchWeatherMovie']),
    // authHeader : function(){
    //   this.$store.state.accounts.authHeader
    // }
  },
  created(){
    this.getWeather({
      location : 'daejeon',
      header : this.authHeader
  })
  }
  // watch :{
  //   authHeader(value){
  //     console.log(value)
  //     this.getWeather('seoul')
  //   }
  // }
}

</script>

<style>

</style>