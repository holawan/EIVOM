<template>
  <div>
    <h1>Select Genre</h1>
    <div v-for="genre in genres" :key="genre.pk">
      <button
        @click="select(genre.pk)"
      >{{ genre.name }}</button>
    </div>
    <div
      v-if="selectedGenre.length === 3"
    ><button
        @click="selectGenre({genre1: selectedGenre[0], genre2: selectedGenre[1], genre3: selectedGenre[2]})">제출
      </button></div>
    <div v-else>
      <button
        @click="goalert()"
        disabled="disabled"
      ></button>
    </div>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'SelectGenre',
  data(){
    return{
      selectedGenre : []
    }
  },
  computed:{
    ...mapGetters(['genres']),
  },
  methods:{
    ...mapActions(['loadGenre', 'selectGenre']),
    select(genrePk){

      this.selectedGenre.push(genrePk)
      console.log(this.selectedGenre)
    },
    goalert(){
      alert('장르를 3개 선택해주세요')
    }
    
  },
  created(){
    this.loadGenre()

  }

}
</script>

<style>

</style>