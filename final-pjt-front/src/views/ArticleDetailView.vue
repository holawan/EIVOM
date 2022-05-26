<template>
  <div>
    <nav-bar :now="'ArticleDetail'"></nav-bar>

    <h1>ArticleDetailView</h1>
    <h1>{{ article.title }}</h1>
    <h3>{{ article.content }}</h3>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'ArticleEdit', params: { crew_pk, article_pk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle({crew_pk, article_pk})">Delete</button>
    </div>
    

    <!-- comment ui -->
    <comment-list
      :comments="article.comments"
    ></comment-list>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import CommentList from '@/components/CommentList.vue'

import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleDetailView',
  components:{
    NavBar,
    CommentList
  },
  data(){
    return {
      article_pk: this.$route.params.article_pk,
      crew_pk: this.$route.params.crew_pk,
    }
  },
  computed:{
    ...mapGetters(['article', 'isAuthor'])
  },
  methods:{
    ...mapActions(['fetchArticle', 'fetchProfile', 'deleteArticle',])
  },
  created(){
    this.fetchArticle({crew_pk: this.crew_pk, article_pk: this.article_pk})

  },


}
</script>

<style>

</style>