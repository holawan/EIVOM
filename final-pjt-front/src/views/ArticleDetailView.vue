<template>
  <div>
    <h1>ArticleDetailView</h1>
    {{ article.title }}
    {{ article.user }}
    {{ article.content }}
    {{ }}
    <comment-list
    ></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleDetailView',
  components:{
    CommentList,
  },
  data(){
    return {
      crewId: this.$route.params.crewId,
      articleId: this.$route.params.articleId
    }
  },
  computed:{
    ...mapGetters(['article', 'comments', ])
  },
  methods:{
    ...mapActions(['fetchArticle', 'fetchComments', 'fetchProfile'])
  },
  created(){
    this.fetchArticle({crew_pk: this.crewId, article_pk: this.articleId})
    this.fetchComments(this.articleId)

  }

}
</script>

<style>

</style>