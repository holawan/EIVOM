<template>
  <div>
    <h1>Select Genre</h1>
    <div v-for="genre in genres" :key="genre.pk">
      {{ genre.name }}
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'SelectGenre',
  // data(){

  // },
  computed:{
    ...mapGetters(['genres']),
  },
  methods:{
    ...mapActions(['loadGenre']),
    
  },
  created(){
    this.loadGenre()

  }

}
</script>

<style>

</style>