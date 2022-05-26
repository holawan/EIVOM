<template>
  <div>
    <h3> article form </h3>
    <div class="container">
      
      <form @submit.prevent="onSubmit" class="form-group row-cols-8" >
        <div>
          <label for="title">제목</label>
          <input type="text" class="form-control" id="title"  v-model="newArticle.title">
        </div>
        <div class="form-group">
          <label for="content">내용</label>
          <input style="height: 150px;" type="text" class="form-control" id="content" v-model="newArticle.content">
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