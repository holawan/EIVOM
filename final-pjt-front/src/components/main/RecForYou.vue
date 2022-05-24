// 당신을 위한 추천
// 클러스터링 / ML

<template>
  <div class="home container">
    <div>
      <h1 class="d-flex justify-content-center">RecForYou</h1>
    </div>
    <div class="d-flex justify-content-center">
      <h2>{{ cmTitle }}</h2>
    </div>
    
    <div class="row justify-content-center">

    
      <div
      v-for="movie in this.clusterMovies"
      :key="movie.pk"
      >
        <div>
          <router-link :to="{name: 'MovieDetail', params: {movie_pk:movie.pk} }">
              <div class="col-3 card mx-4 mb-5" style="width: 18rem;padding-left:0px;">
                <img class="card-img-top " :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" alt="Card image cap" style="width:18rem; height:25rem; box-sizing:content-box;">
                <br>
                <div class="card-body">
                  <h4 class="card-text">{{movie.title}}</h4>
                </div>
              </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RecForYou',
  methods:{
    ...mapActions(['getClusterMovies'])
  },
  computed:{
    ...mapGetters(['clusterMovies', 'cmTitle'])
  },
  created(){
    this.getClusterMovies()
  }
}
</script>

<style>

.home{
  display: flex;

}

</style>