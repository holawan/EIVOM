<template>
  <div>
    <div class="container">
      
      <form @submit.prevent="onSubmit" class="form-group row-cols-8" >
      <br>
      <br>
          <h4 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:60px">게시글 작성</h4>

        <div>
          <label for="title"></label>
          <input type="text" class="form-control" id="title" placeholder="제목을 입력해주세요." v-model="newArticle.title">
        </div>
        <div class="form-group">
          <label for="content"></label>
          <input style="height: 150px;" type="text" class="form-control" id="content" placeholder="내용을 입력해주세요." v-model="newArticle.content">
        </div>
        <br>
        <br>
        <button type="submit" class="btn-lg btn-info rounded-pill">{{action}}</button>
      </form>


    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {

  name:'ArticlForm',
  props:{
    article:Object,
    action: String,
    crew_pk: null,
  },
  data(){
    return{
      newArticle:{
        title: this.article.title,
        content: this.article.content,
      }
    }
  },
  methods:{
    ...mapActions(['createArticle', 'updateArticle']),
    onSubmit(){
      if (this.action === 'create'){
        this.createArticle({crew_pk:this.crew_pk, article:this.newArticle})
      } else if (this.action === 'update') {
        const payload ={
          crew_pk: this.crew_pk,
          article_pk: this.article.pk,
          ...this.newArticle
        }
        this.updateArticle(payload)
      }
    }
  }

}
</script>

<style>

</style>