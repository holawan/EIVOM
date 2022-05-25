<template>
  <div class="item">
    <div v-if="movie.pk">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.pk} }">
        <div class="card card-block pr-3" style="width: 18rem;">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text">{{ movie.title }}</p>
          </div>
        </div>
      </router-link>
    </div>

    <div v-if="movie.id">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
        <div class="card card-block pr-3" style="width: 18rem;">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text">{{ movie.title }}</p>
          </div>
        </div>
      </router-link>
    </div>

  </div>
</template>

<script>


export default {
  name: 'MovieListItem',
  props:{
    movie:{
      type:Object
    }
  },
}

</script>

<style>
.item{display:inline-block; padding: 10px 20px; background: #ccc; margin-right:10px;}
.card:hover {
     transform: scale(1.1);
     z-index: 2000;
  box-shadow: 0 10px 20px rgba(238, 234, 236, 0.698), 0 4px 8px rgba(0,0,0,.06);
}
</style>