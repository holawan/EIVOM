<template>
  <div>
    <nav-bar :now="'ArticleCreate'"></nav-bar>
    <br>
    <br>
    <br>
    <br>
    
    <article-form
      :article="article"
      :crew_pk="crew_pk"
      action="create"
    ></article-form>
 
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ArticleForm from '@/components/ArticleForm.vue'

export default {
  name: 'ArticleCreateView',
  components:{
    NavBar,
    ArticleForm,
  },
  data(){
    return {
      crew_pk: this.$route.params.crew_pk,
      article:{
        pk: null,
        title: '',
        content: '',

      }
    }
  },

}
</script>

<style>

</style>