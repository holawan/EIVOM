<template>
  <div class="item">
    <div v-if="movie.pk">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.pk} }">
        <div class="card  pr-3 embed-responsive embed-responsive-1by1" style="width: 18rem;padding-left:0px;" >
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top embed-responsive-item" alt="..." style="width:18rem; height:25rem;">
          <h3 class="MLIh3">{{ movie.title }}</h3>
        </div>
      </router-link>
    </div>

    <div v-if="movie.id">
      <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
        <div class="card pr-3" style="width: 18rem;padding-left:0px;">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" style="width:18rem; height:25rem;" class="card-img-top" alt="...">
          <h3 class="MLIh3">{{ movie.title }}</h3>
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
.item{display:inline-block; padding: 5px 0px; background: rgb(255, 255, 255); margin-right:10px;}
.card:hover {
     transform: scale(1.1);
     filter:brightness(0.5);

     z-index: 2000;
  box-shadow: 0 10px 20px rgba(255, 238, 0, 0.698), 0 4px 8px rgba(184, 237, 115, 0.06);
}
.card:hover.MLIh3 {
  position: absolute;
  top: 10rem;
  left: 1rem;
  opacity: 100;
}
.card{
  max-width: 100%;
  max-height: 100%;
}
.MLIh3{
  position: absolute;
  top: 10rem;
  left: 1rem;
  opacity: 0;
}
/* h3:hover{
  position: absolute;
  top: 10rem;
  left: 1rem;
  opacity: 100;
} */
</style>