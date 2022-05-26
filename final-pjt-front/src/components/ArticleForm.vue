<template>
  <div>
    <h3> article form </h3>
    <div>
      <form @submit.prevent="onSubmit">
        <div>
          <label for="title">제목을 입력하세요:</label>
          <input v-model="newArticle.title" type="text" id="title" required/>
        </div>

        <div>
          <label for="content">내용을 입력하세요:</label>
          <textarea v-model="newArticle.content" type="text" id="content" required/>
        </div>

        <div>
          <button>{{action}}</button>
        </div>

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