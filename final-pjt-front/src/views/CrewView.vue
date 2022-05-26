<template>
  <div class="container">
    <nav-bar :now="'Crew'"></nav-bar>

    <div class="row">
      <div class="col-12">
          <img src="@/assets/crew_back.png" alt="crewback" class="crewback"  style="width: 100%;">


        <!-- 전체 크루^^! -->
        <div>
          <div class="col-12">
              <br>
                <h1  class="d-flex justify-content-center" style="font-family: 'East Sea Dokdo', cursive;" align="start">같이:봄</h1>
                  <div class="row d-flex justify-content-center">
                    <div class="col-2"
                    v-for="crew,idx in crews"
                    :key="idx"
                    :crew="crew"
                    >
                    <router-link style="text-decoration: none; color: black;" :to="{name: 'CrewDetail',params : {crew_pk : crew.pk}}">
                    <h3>
                      <img :src="'http://127.0.0.1:8000'+ crew.crew_image" class="card-img-top embed-responsive-item" style="width:10rem; " alt="...">
                      {{crew.crewname}}
                    </h3>
                    </router-link>

                    </div>
                  </div>
              <!-- </router-link> -->
            </div>
            <router-link :to="{ name: 'CrewCreate' }" class="col-3">
              <button class="btn btn-lg rounded-pill text-black " style="background-color:antiquewhite;">크루 만들기</button>
            </router-link> 
          </div>
        </div>

      </div>
      
    </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

import { mapActions, mapGetters } from 'vuex'



export default {
  name: 'CrewView',
  components:{
    NavBar},
  data(){
    return{
    }

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