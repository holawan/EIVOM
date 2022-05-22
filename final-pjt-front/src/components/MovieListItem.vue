<template>
  <div>
    <h1>MovielistItem</h1>
    <div @click="clickMovie()">
      {{ movie.title }}
    </div>

  </div>
</template>

<script>

import router from '@/router'


export default {
  name: 'MovieListItem',
  props:{
    movie:{
      type:Object
    }
  },
  methods:{
    clickMovie(){
      const movie = this.movie
      router.push({ name: 'MovieDetail', params:{ movie_pk:movie.id }})
    },
  },

}
</script>

<style>

</style>