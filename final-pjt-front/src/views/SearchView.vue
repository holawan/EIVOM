<template>
  <div>
    <SearchVar
      @text-input="onTextInput"
      @search-text="onSearchText"
    />
    <SearchMovieList
      :movieList="movieList"
    />
  </div>
</template>

<script>
import axios from 'axios'

import SearchVar from '@/components/search/SearchVar.vue'
import SearchMovieList from '@/components/search/SearchMovieList.vue'
import { mapGetters } from 'vuex'

const URL = "http://localhost:8000/movies/search"


export default {
  name: 'SearchView',
  data () {
    return {
      selectedMovie: '',
      movieList: '',
      movieListMain : '',
    }
  },
  components: {
    SearchVar,
    SearchMovieList
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods: {
    onTextInput (textInput) {
      const params = textInput
      console.log(params)
      this.searchPreview(params)
        .then(res => {
          this.movieList = res.data
          console.log(res.data,'프리뷰')
        })
    },
      async searchPreview(params) {
        // url 확인
        let url = `${URL}/${params}`
  
        return await axios({
          method: 'get',
          url,
          headers : this.authHeader
        })
      },


      //경계
    onSearchText(search) {
      const params = search
      this.searchMain(params)
        .then( res => {
          this.movieListMain = res.data
          console.log(res.data,'사진까지')
        })
        .catch( err => {
          console.log(err)
        })
    },
    async searchMain(params) {
      // url 확인
      let url = `${URL}/${params}`

      return await axios({
        method: 'get',
        url,
        headers : this.authHeader
      })
    },
  }
}
</script>

<style>

</style>