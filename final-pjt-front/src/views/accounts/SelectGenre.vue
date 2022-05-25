<template>
  <div>
    <div class="gerneBackground">
      <br>
      <h1 class="header">선호하는 장르를 골라주세요!</h1>
      <h4 class="header">회원님을 위한 추천영화 데이터로 사용됩니다.</h4>
      <br>
      <div class="container">

        <div class="row">

          <div v-for="genre in genres" :key="genre.pk" class="col-3 d-flex justify-content-center align-items-center my-3">
            <button
            class="btn btn-secondary  btn-lg rounded-pill text-black"
            style="background-color: white; border-style:none; font-weight:600; width: 150px; height: 60px; box-shadow: 2px 2px 2px green;"
              @click="select(genre.pk)"
            >{{ genre.name }}</button><br>
          </div>
        </div>
      </div>

      <!-- submit button -->
      <div>
        <div v-if="selectedGenre.length >= 3">
          <router-link :to="{name: 'Main'}">
            <button class="btn btn-light btn-lg rounded-pill my-3" style="font-weight:600; width: 150px; height: 60px; box-shadow: 2px 2px 2px gray;">
              제출
            </button>
          </router-link>
        </div>
        <div v-else>
          <button class="btn btn-light btn-lg rounded-pill my-3" style="font-weight:600; width: 150px; height: 60px; box-shadow: 2px 2px 2px gray;"
            @click="goalert()"
            disabled="disabled"
          >제출</button>
        </div>
      </div>
      <br>

      <!-- 선택한 장르 ui -->
      <div class="d-flex justify-content-center">

        <div
          v-for="genre, idx in selectedGenres"
          :key="idx"
          :genre="genre"
          
        >
          <button 
            class=" btn btn-secondary rounded-pill mx-2" 
            @click="select(genre.pk)" 
            style="width:100px; height:40px" >{{ genre.name }}</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'SelectGenre',
  data(){
    return{
      selectedGenre : [],
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
.gerneBackground{
  filter: brightness(110%);
  height: 100vh;
  margin:0;
  background-image: url("@/assets/genreselect_bg.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  opacity: 90%;
  /* position: sticky; */
}

.header{
  color: aliceblue;
  font-weight: 500;
  text-shadow: 2px 2px 2px gray;

}
</style>