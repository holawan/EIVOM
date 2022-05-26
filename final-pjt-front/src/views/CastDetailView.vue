<template>
  <div class="container">
    <nav-bar :now="CastDetail"></nav-bar>

    <!-- info -->
    <div class="col-4 align-self-center px-0">
      <img v-if="actorInfo.profile_path" :src="'https://image.tmdb.org/t/p/w400/'+ actorInfo.profile_path" style="width: 60%; " alt="">
      <h1 v-else>이미지 준비중인 배우입니다.</h1>
      <h3 v-if="actorInfo.also_known_as">
      {{ actorInfo.also_known_as[0] }}
      </h3>
      <h5>{{ actorInfo.name }} </h5>
      <p></p>
    </div>
    
    <!-- filmography -->
    <!-- filmo movid list item으로 변경 가능? -->
    <div class="row">
      <div class="col-2" style="width: 13rem; height:22rem; " v-for="filmo in filmos.cast" :key="filmo.id">
        <router-link style="text-decoration: none; color: black;" :to="{name: 'MovieDetail', params: { movie_pk:filmo.id } }">
          <div class="col-4 card mx-4 mb-5" style="width: 13rem; height:15rem;padding-left:0px;">
            <img  v-if="filmo.poster_path"  class="card-img-top " :src="'https://image.tmdb.org/t/p/w400/'+ filmo.poster_path" alt="Card image cap" style="width:13rem; height:15rem; box-sizing:content-box;">
            <img v-else src="@/assets/none_movie_image.png" style="width:13rem; height:19rem;" alt="">
            <div class="card-body">
              <p class="mb-0 mt-2" >{{filmo.title}}</p>
              <p class="card-text mt-0">{{filmo.character}}</p>
            </div>
          </div>
        </router-link>
      </div>

    </div>
    
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CastDetailView',
  components: {
    NavBar
  },
  data(){
    return {
      castId: this.$route.params.castId,
      
    }
  },
  computed:{
    ...mapGetters(['filmos', 'actorInfo']),
  },
  methods:{
    ...mapActions(['getActorInfo' ,'getCastDetail'])
  },
  created(){
    this.getActorInfo(this.castId)
    this.getCastDetail(this.castId)
  }
}
</script>

<style>

</style>