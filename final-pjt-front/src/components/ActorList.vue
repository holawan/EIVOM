<template>
  <div>

    <!-- <div
      v-for="actor,idx in this.movie.actors"
      :key="idx"
      :idx="idx"
    >
      <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }" style="text-decoration: none; color: black; font-weight: bold; ">
        <div class="col-4 actor_card mx-auto" style="width: 16rem;  border:3px solid black; border-radius: 1em;">
          <img class="card-img-top mb-2 " :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="Card image cap" style="width:100%; border-top-left-radius: 0.7rem;border-top-right-radius: 0.7rem; height:20rem; box-sizing:content-box;">
          <br>
            <h5 class="mt-1" style="text-align: center; ">{{ movie.actors[idx] }}</h5>
        </div>
      </router-link>

    </div> -->
    
      <div class="col-2"
        v-for="actor,idx in this.movie.actors"
        :key="idx"
        :idx="idx"
      >
        <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }" style="text-decoration: none; color: black; font-weight: bold; ">
          <div v-if="idx<6" class=" actor_card mx-auto" style="width: 13rem;  height:20rem; border:0 0 2px 0; border-top-left-radius: 1rem;border-top-right-radius: 1rem;">
            <img v-if="movie.actors_path[idx]" class="card-img-top mb-2 mx-0 " :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="Card image cap" style="width:100%; height: 100%; border-top-left-radius: 0.7rem;border-top-right-radius: 0.7rem;box-sizing:content-box;">
            <img v-else src="@/assets/none_profile_image.png" style="width:13rem; height:15rem;" alt="">
            <br>
              <h5 class="mt-1" style="text-align: center;">{{ movie.actors[idx] }}</h5>
          </div>
        </router-link>

    </div>
          <!-- <div class="swiper-pagination" slot="pagination"></div> -->
  </div>
</template>


<script>
import { mapActions, mapGetters } from 'vuex'

export default {

  name : 'ActorList',
    props:{ 
    movieId:null ,
  },
  components: {
    
  },
   computed : {
    ...mapGetters(['movie']),
  },
  methods : {

        ...mapActions(['fetchMovie' ])
  },


    created(){
    if(this.movie.length) {
      console.log('있어!')
      console.log(this.movie)
      }else{
        console.log('없어!받아올게')
         this.fetchMovie(this.movieId)
         console.log('받았어!')
      }

  },

}
</script>

<style>

</style>