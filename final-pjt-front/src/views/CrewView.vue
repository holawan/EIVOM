<template>
  <div>
    <nav-bar :now="Crew"></nav-bar>

    <h1>CrewView</h1>
    <router-link :to="{ name: 'CrewCreate' }">CrewCreate</router-link>
    <my-crew-list></my-crew-list>
    <near-crew-list></near-crew-list>
    
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import NearCrewList from '@/components/NearCrewList.vue'
import MyCrewList from '@/components/MyCrewList.vue'


export default {
  name: 'CrewView',
  components:{
    NavBar,
    
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