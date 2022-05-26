<template>
  <div>
    <nav-bar :now="'Crew'"></nav-bar>

    <div class="row">
      <div class="col-8 offset-2">
        <div>
          <img src="@/assets/crew_back.png" alt="crewback" class="crewback">
        </div>

        <!-- 내가 가입한 크루 -->
        <div>
          <div class="col-12">
            <div class="col-3 offset-1">
              <br>
              <h4 align="start">내가 가입한 크루</h4>
              <h1 style="font-family: 'East Sea Dokdo', cursive;" align="start">같이:봄</h1>
            </div>
            <router-link :to="{ name: 'CrewCreate' }" class="col-3">
              <button class="btn btn-lg rounded-pill text-black " style="background-color:antiquewhite;">크루 만들기</button>
            </router-link> 
          </div>

          <my-crew-list></my-crew-list>

        </div>
      </div>
      
      <near-crew-list></near-crew-list>
    </div>
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
.crewback{

}

</style>