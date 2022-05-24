<template>
  <div>
    <SearchVar
      @text-input="onTextInput"
      @search-text="onSearchText"
    />
    <SearchMovieList
      :movieList="movieList"
      :movieListMain="movieListMain"
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
      this.searchPreview(params)
        .then(res => {
          this.movieList = res.data
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