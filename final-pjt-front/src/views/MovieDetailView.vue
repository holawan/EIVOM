<template>
  <div>
    <div class="backdrop row m-0 my-5">
      <div class="col-12 col-md-3 align-self-center" style="height: 100%;">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" id="poster-img"  style="width: 100%;" alt="...">
      </div>
      
      <div class="col-12 col-md-9 text-dark">
        <h3 class="mt-3 custom-break-word">{{ movie.title }}</h3>
        <div class="custom-break-word">장르: {{ movie.genres }}</div>
        <hr>
        <p class="custom-break-word">{{ movie.overview }}</p>
        <hr>
        <div>{{ movie.release_date }} 개봉</div>
        <div class="custom-break-word">원제목: {{ movie.original_title }}</div>
        <!-- <div>언어: {{ movie.original_language }}</div> -->
        <hr>
        <hr>
        <!-- {{movie}} -->
      </div>
    </div>
    <!-- movie like ui -->
    <div>
      LikeIt: 
      <button
        @click="likeMovie(movieId)"
      >좋아요</button>
    </div>
    <div>
      AddCrew:
      <button
        @click="addMovie(this.movieId)"
      >크루에 추가하기</button>
    </div>      

    <!-- <div 
      v-for="actor,idx in this.movie.actors"
      :key="idx"
      :idx="idx"
    >
      <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }">
        <div class="col-4 card mx-4 mb-5" style="width: 18rem;padding-left:0px;">
          <img class="card-img-top " :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="Card image cap" style="width:10rem; height:15rem; box-sizing:content-box;">
          <br>
            <h5>{{ movie.actors[idx] }}</h5>
        </div>
      </router-link>
    </div> -->

    <actor-list :actors="this.movie.actorInfo"></actor-list>


    <movie-review-list :reviews="this.reviews"></movie-review-list>
    <movie-rec-similar></movie-rec-similar>
  </div>
</template>

<script>
import MovieReviewList from '@/components/MovieReviewList.vue'
import MovieRecSimilar from '@/components/MovieRecSimilar.vue'
import { mapActions, mapGetters } from 'vuex'
import ActorList from '../components/ActorList.vue'


export default {
  name: 'MovieDetailView',
  components:{
    MovieReviewList,
    MovieRecSimilar,
    ActorList,
  },
  data(){
    return {
      movieId: this.$route.params.movie_pk,
      actorInfo : {
        actors : this.movie.actors,
        actorId : this.movie.actorId,
        actorPath : this.movie.actors_path,
      }
    }
  },
  computed: {
    ...mapGetters(['movie', 'reviews']),
    likeCount(){
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'likeMovie',
      'fetchMovie',
      'addMovie',
      'readReviews'
    ])
  },
  created(){
    
    this.fetchMovie(this.movieId)
    this.readReviews(this.movieId)
    
  },

}
</script>

<style>

</style>