<template>
  <div>
    <h1>Select Genre</h1>
    {{genres}}
    <p v-for="genre in genres" :key="genre.id">
      {{genre.name}}
    </p>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'
export default {
  name: 'SelectGenre',
  // data(){

  // },
  computed:{
    ...mapGetters(['genres']),
    ...mapState(['genres'])
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