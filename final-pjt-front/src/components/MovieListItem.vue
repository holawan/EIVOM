<template>
  <div class="item">
    <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.pk} }">
      <div class="card card-block pr-3" style="width: 18rem;">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{ movie.title }}</p>
        </div>
      </div>
    </router-link>

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

</style>