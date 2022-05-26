<template>
  <div>
    <nav-bar :now="'ArticleEdit'"></nav-bar>

    <h1>Article Edit</h1>

    <!-- edit form -->
    <article-form
      v-if="isArticle" :article="article" :crew_pk="crew_pk" action="update"
    >

    </article-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ArticleForm from '@/components/ArticleForm.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'ArticleEditView',
  data(){
    return{
      crew_pk: this.$route.params.crew_pk,
      article_pk: this.$route.params.article_pk
    }
  },
  components:{NavBar, ArticleForm},
  computed:{
    ...mapGetters(['article', 'isArticle'])
  },
  methods:{
    ...mapActions(['fetchArticle'])
  },
  created(){
    this.fetchArticle({crew_pk: this.crew_pk, article_pk: this.article_pk})
  }

}
</script>

<style>

</style>