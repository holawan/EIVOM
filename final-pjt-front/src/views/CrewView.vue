<template>
  <div class="container">
    <nav-bar :now="'Crew'"></nav-bar>

    <div class="row">
      <div class="col-12">
          <img src="@/assets/crew_back.png" alt="crewback" class="crewback"  style="width: 100%;">


        <!-- 전체 크루^^! -->
        <div>
          <div class="col-12">
            <div class="col-3 offset-1">
              <br>
              <h4>    </h4>
              <h1 style="font-family: 'East Sea Dokdo', cursive;" align="start">같이:봄</h1>
            </div>
            <router-link :to="{ name: 'CrewCreate' }" class="col-3">
              <button class="btn btn-lg rounded-pill text-black " style="background-color:antiquewhite;">크루 만들기</button>
            </router-link> 
          </div>
        </div>

        <div>
          <crew-list
          v-for="crew in crews"
          :key="crew.pk"
          :crew="crew"
          >
            {{crew.name}}
          </crew-list>
        </div>

      </div>
      
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
<<<<<<< HEAD

import { mapActions, mapGetters } from 'vuex'
=======
import NearCrewList from '@/components/NearCrewList.vue'
>>>>>>> 724bb67df53fbe6b9d03ff57fe893056d211ece4


export default {
  name: 'CrewView',
  components:{
    NavBar,
<<<<<<< HEAD
  },
  data(){
    return{
    }
=======
    
    NearCrewList,
>>>>>>> 724bb67df53fbe6b9d03ff57fe893056d211ece4
  },
  methods:{
    ...mapActions(['fetchCrews'])
  },
  computed:{
    ...mapGetters(['crews'])
  },
  created(){
    this.fetchCrews()
  }
}
</script>

<style>
</style>