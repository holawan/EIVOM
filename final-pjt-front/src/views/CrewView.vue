<template>
  <div>
    <h1>CrewView</h1>
    <router-link :to="{ name: 'CrewCreate' }">CrewCreate</router-link>
    <my-crew-list></my-crew-list>
    <near-crew-list></near-crew-list>
    
  </div>
</template>

<script>
import NearCrewList from '@/components/NearCrewList.vue'
import MyCrewList from '@/components/MyCrewList.vue'


export default {
  name: 'CrewView',
  components:{
    NearCrewList,
    MyCrewList,
  },
  methods:{
    crewcreate(){

    }
  }
}
</script>

<style>

</style>