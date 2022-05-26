<template>
  <div class="item">
    <div v-if="movie">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.pk} }">
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
import axios from 'axios'
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
// import router from '@/router'

export default {
  name: 'MovieListItem',
  props:{
    movieId:{
      type:Number
    },
  data() {
    return {
      movie : ''
    }
  }
  },
  methods:{
    fetchMovie2(movieId){
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: this.authHeader,
      })
      .then(res => {
        this.movie = res.data
        console.log(res.data)
        
      })
      .catch(err => {
        if (err.response.status === 404){
          console.error(err)
          console.log(movieId)
          // router.push({name: 'Sorry'})
        }
      })
    },
  },
  computed:{
    ...mapGetters(['authHeader',])
  },
  created() {
    console.log(this.movieId)
    this.fetchMovie2(this.movieId)
    console.log('나 무비',this.movie)
  }
  
}

</script>

<style>
.item{display:inline-block; padding: 10px 20px; background: #ccc; margin-right:10px;}

</style>