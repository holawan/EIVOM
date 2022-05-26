<template>
  <div>
    <nav-bar :now="'ArticleDetail'"></nav-bar>

    <h1>ArticleDetailView</h1>
    <!-- {{ article.title }}
    {{ article.user }}
    {{ article.content }} -->
    <h1>ReviewListItem</h1>
      <comment-list-item 
        v-for="comment in article.comments"
        :comment="comment"
        :key="comment.pk"  
      ></comment-list-item>

    <comment-form
      :crew_pk="crewId"
      :article_pk="articleId"
    ></comment-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import CommentForm from '@/components/CommentForm.vue'
import CommentListItem from '@/components/CommentListItem.vue'

import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleDetailView',
  components:{
    NavBar,
    CommentForm,
    CommentListItem,
  },
  data(){
    return {
      articleId: this.$route.params.article_pk,
      crewId: this.$route.params.crew_pk,
    }
  },
  computed:{
    ...mapGetters(['article',])
  },
  methods:{
    ...mapActions(['fetchArticle', 'fetchProfile'])
  },
  created(){
    this.fetchArticle({crew_pk: this.crewId, article_pk: this.articleId})
    console.log(this.crewId,'크루')
  },
  mounted(){
    this.fetchArticle({crew_pk: this.crewId, article_pk: this.articleId})
    console.log(this.crewId,'크루')
  },


}
</script>

<style>

</style>