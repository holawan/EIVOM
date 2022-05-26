<template>
  <div>
    <nav-bar :now="CastDetail"></nav-bar>

    <!-- info -->
    <div>
      <img :src="'https://image.tmdb.org/t/p/w400/'+ actorInfo.profile_path" alt="">
      <h3 v-if="actorInfo.also_known_as">
      {{ actorInfo.also_known_as[0] }}
      </h3>
      <h5>{{ actorInfo.name }} </h5>
      <p></p>
    </div>
    
    <!-- filmography -->
    <!-- filmo movid list item으로 변경 가능? -->
    <div v-for="filmo in filmos.cast" :key="filmo.id">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk:filmo.id } }">
        <div class="col-4 card mx-4 mb-5" style="width: 18rem;padding-left:0px;">
          <img class="card-img-top " :src="'https://image.tmdb.org/t/p/w400/'+ filmo.poster_path" alt="Card image cap" style="width:10rem; height:15rem; box-sizing:content-box;">
          <br>
            <h5>{{filmo.title}}</h5>
          <div class="card-body">
            <p class="card-text">{{filmo.character}}</p>
          </div>
        </div>
      </router-link>
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