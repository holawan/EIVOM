<template>
  <div>
    <h1>ReviewForm</h1>
    <input type="text" @keyup.enter="inputComment" v-model="comment">
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name:'CommentForm',
  data(){
    return {
      comment:'',
      }
  },
  props:{ 
    article_pk:null ,
    crew_pk:null 
  },
  methods:{
    ...mapActions(['commentCreate']),
    inputComment(){
      const newComment = this.comment
      if (newComment){
        this.commentCreate({article_pk:this.article_pk, crew_pk:this.crew_pk, content:newComment})
        console.log(this.article_pk)
        console.log(this.crew_pk)
        console.log(this.comment)
        this.comment = ''
      }
    }
  },

}
</script>

<style>

</style>