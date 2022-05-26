<template>
  <div class="row">
    <nav-bar :now="'ArticleDetail'"></nav-bar>
    <div class="col-8 offset-2">
    <br>
    <br>
    <br>
    <br>
    <br>
    <h3>{{article.user.profile.nickname}} 의 글 </h3>
    <h3 style="font-weight: bold;   ">{{ article.title }}</h3>
    <p style="font-size : 20px">{{ article.content }}</p>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'ArticleEdit', params: { crew_pk, article_pk } }">
        <button  class="btn btn-primary rounded-pill" >Edit</button>
      </router-link>
      |
      <button  class="btn btn-danger rounded-pill" @click="deleteArticle({crew_pk, article_pk})">Delete</button>
    </div>
    <br>
    <hr>
    <br>
    <!-- comment ui -->
    <comment-list
      :comments="article.comments"
    ></comment-list>
  </div>
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
    ...mapGetters(['article', 'isAuthor','currentUser']) 
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