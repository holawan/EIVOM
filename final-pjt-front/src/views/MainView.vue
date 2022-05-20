<template>
  <div>
    <h1>MainView</h1>
    <box-office></box-office>
    <rec-for-you></rec-for-you>
    <rec-weather></rec-weather>
    <rec-weekly></rec-weekly>
    <rec-actor></rec-actor>
    <rec-similar></rec-similar>
    <rec-highly-view></rec-highly-view>
    <rec-master-piece></rec-master-piece>
    <rec-genre></rec-genre>

  </div>
</template>

<script>
import BoxOffice from '@/components/main/BoxOffice.vue'
import RecActor from '@/components/main/RecActor.vue'
import RecForYou from '@/components/main/RecForYou.vue'
import RecGenre from '@/components/main/RecGenre.vue'
import RecHighlyView from '@/components/main/RecHighlyView.vue'
import RecMasterPiece from '@/components/main/RecMasterPiece.vue'
import RecSimilar from '@/components/main/RecSimilar.vue'
import RecWeather from '@/components/main/RecWeather.vue'
import RecWeekly from '@/components/main/RecWeekly.vue'


export default {
  name: 'MainView',
  components:{
    BoxOffice,
    RecActor,
    RecForYou,
    RecGenre,
    RecHighlyView,
    RecMasterPiece,
    RecSimilar,
    RecWeather,
    RecWeekly,
  }

}
</script>

<style>

</style>