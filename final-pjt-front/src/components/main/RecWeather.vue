// 날씨기반 영화추천
// 날씨에 따른 추천할 영화 데이터 만들고
// 날씨 (비, 눈, 맑음, 구름 정도?) api로 가져오기 => 가능할까요? 네!!!!

<template>
  <div>
    <h1>RecWeather</h1>
    <h2>{{ weather }}</h2>
    <h2>{{ weatherMovies }}</h2>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default { 
  name: 'RecWeather',
  computed:{
    ...mapGetters(['weather', 'weatherMovies']),
  },
  methods:{
    ...mapActions(['getWeather']),
  },
  created(){
    this.getWeather('seoul')
  }

}
</script>

<style>

</style>