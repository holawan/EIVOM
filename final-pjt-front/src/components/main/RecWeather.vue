// 날씨기반 영화추천
// 날씨에 따른 추천할 영화 데이터 만들고
// 날씨 (비, 눈, 맑음, 구름 정도?) api로 가져오기 => 가능할까요? 네!!!!

<template>
  <div>
    <div style="background-color:white; height:50px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">오늘같은 날씨엔! </h1>
      <h1 align="start">오늘의 날씨는 ? {{ weather }}</h1>
    </div>

    <div>
      <movie-list
        :movies="weatherMovies"
      ></movie-list>
    </div>
    <hr>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default { 
  name: 'RecWeather',
  components:{
    MovieList,
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
  mounted(){
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