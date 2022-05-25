<template>
  <div>
    <h1>Select Genre</h1>
    <div v-for="genre in genres" :key="genre.pk">
      <button
        @click="select(genre.pk)"
      >{{ genre.name }}</button>
    </div>
    <div v-if="selectedGenre.length >= 3">
      <router-link :to="{name: 'Main'}">
        <button>
          제출
        </button>
      </router-link>
    </div>
    <div v-else>
      <button
        @click="goalert()"
        disabled="disabled"
      >제출</button>
    </div>

    <!-- 선택한 장르 ui -->
    <div
      v-for="genre, idx in selectedGenres"
      :key="idx"
      :genre="genre"
    >
      <button @click="select(genre.pk)">{{ genre.name }}</button>
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
    ...mapGetters(['genres', 'selectedGenres', 'nowSelectGenrePk']),
  },
  methods:{
    ...mapActions(['loadGenre', 'selectGenre']),
    select(genrePk){
      if (genrePk in this.selectedGenre) {
        console.log('여기')
        console.log(genrePk)
        this.selectGenre(genrePk)
        for(let i = 0; i < this.selectedGenre.length; i++) {
          if(this.selectedGenre[i] === 'genrePk')  {
            this.selectedGenre.splice(i, 1);
            i--;
          }
        }
      } else {
        this.selectedGenre.push(genrePk)
        this.selectGenre(genrePk)
      }     
    },
    goalert(){
      alert('장르를 3개 이상 선택해주세요')
    }
    
  },
  created(){
    this.loadGenre()

  }

}
</script>

<style>

</style>