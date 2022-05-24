<template>
  <div>
    <SearchVar
      @text-input="onTextInput"
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
      
      this.search(params)
        .then( res => {
          this.movieList = res.data
          console.log(res.data)
        })
        .catch( err => {
          console.log(err)
        })
    },
    async search (params) {
      // url 확인
      let url = `${URL}/${params}`

      return await axios({
        method: 'get',
        url,
        headers : this.authHeader
      })
    }
  }
}
</script>

<style>

</style>