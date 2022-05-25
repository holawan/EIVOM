<template>

    <div>
      <router-link :to="{name: 'CastDetail', params: { castId:movie.actor_id[idx] } }" style="text-decoration: none; color: black; font-weight: bold; ">
        <div class="col-4 actor_card mx-auto" style="width: 16rem;  border:3px solid black; border-radius: 1em;">
          <img class="card-img-top mb-2 " :src="'https://image.tmdb.org/t/p/w400/'+ movie.actors_path[idx]" alt="Card image cap" style="width:100%; border-top-left-radius: 0.7rem;border-top-right-radius: 0.7rem; height:20rem; box-sizing:content-box;">
          <br>
            <h5 class="mt-1" style="text-align: center; ">{{ movie.actors[idx] }}</h5>
        </div>
      </router-link>

    </div>
</template>

<script>
export default {
  name:'ActorListItem',
  props : {
    actor : Object
  },
}
</script>

<style>

</style>