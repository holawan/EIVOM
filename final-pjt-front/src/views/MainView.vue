<template>
  <div>
    <h1>MainView</h1>
    <box-office></box-office>
    <rec-for-you ></rec-for-you>
    <rec-weather></rec-weather>
    <rec-highly-view></rec-highly-view>
    <rec-master-piece></rec-master-piece>
    <rec-genre></rec-genre>

  </div>
</template>

<script>
import BoxOffice from '@/components/main/BoxOffice.vue'
import RecForYou from '@/components/main/RecForYou.vue'
import RecGenre from '@/components/main/RecGenre.vue'
import RecHighlyView from '@/components/main/RecHighlyView.vue'
import RecMasterPiece from '@/components/main/RecMasterPiece.vue'
import RecWeather from '@/components/main/RecWeather.vue'


export default {
  name: 'MainView',
  components:{
    BoxOffice,
    RecForYou,
    RecGenre,
    RecHighlyView,
    RecMasterPiece,
    RecWeather,
  },
}
</script>

<style>

</style>