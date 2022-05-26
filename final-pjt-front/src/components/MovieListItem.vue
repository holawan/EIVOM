<template>
<div class="item">
  <div >
    <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
      <div class="card card-block pr-3 embed-responsive embed-responsive-1by1" >
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top embed-responsive-item" alt="...">
        <div class="card-body">
          <p class="card-text">{{ movie.title }}</p>
        </div>
      </div>  
    </router-link>
  </div>
  {{movie}}
  <div>
</div>
</div>
</template>


<script>
import { mapGetters } from 'vuex'
// import router from '@/router'

export default {
  name: 'MovieListItem',
  props:{
    movieId:{
      movie:Object
    },
  data() {
    return {
    }
  }
  },
 
  computed:{
    ...mapGetters(['authHeader',])
  },


  
}

</script>

<style>
.item{display:inline-block; padding: 10px 20px; background: #ccc; margin-right:10px;}

</style>