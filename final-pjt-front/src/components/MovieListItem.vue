<template>
  <div>
    <h1>MovielistItem</h1>
    <section @click="clickMovie">
      {{ movieTitle }}
    </section>

  </div>
</template>

<script>
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
      router.push({ name: 'MovieDetail'})
    },
  },
  computed: {
    ...mapGetters(['selectedMovie']),
    movieTitle(){
      const title = _.unescape(this.movieItem.snippet.title)
      return title
    },
  }

}
</script>

<style>

</style>