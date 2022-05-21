<template>
  <div>
    <h1>MovielistItem</h1>
    <section @click="clickMovie">
      {{ movieItem.title }}
    </section>

  </div>
</template>

<script>

import router from '@/router'

import { mapGetters } from 'vuex'
export default {
  name: 'MovieListItem',
  props:{
    movieItem:{
      type:Object
    }
  },
  methods:{
    clickMovie(){
      const movie = this.movieItem
      router.push({ name: 'MovieDetail', parmas:{ movieId:movie.id }})
    },
  },
  computed: {
    ...mapGetters(['selectedMovie']),

  }

}
</script>

<style>

</style>