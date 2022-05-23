<template>
  <div>
    <h1>Article Create</h1>
    
    <!-- create form -->
    <div>
      <form @submit.prevent="onSubmit">
        <div>
          <label for="title">제목을 입력하세요:</label>
          <input v-model="newArticle.title" type="text" id="title" required/>
        </div>

        <div>
          <label for="content">내용을 입력하세요:</label>
          <input v-model="newArticle.content" type="text" id="content" required/>
        </div>

        <div>
          <button>make article!!</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'ArticleCreateView',
  data(){
    return {
      crewId: this.$route.params.crewId,
      newArticle:{
        title: '',
        content: '',
      }
    }
  },
  methods: {
    ...mapActions(['createArticle']),
    onSubmit(){
      const payload = {crewId: this.crewId, article:this.newArticle}
      this.createArticle(payload)
    }
  },

}
</script>

<style>

</style>