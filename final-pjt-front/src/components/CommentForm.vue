<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment"> </label>
    <input class="commentInput" type="text" id="comment" v-model="content" required>
    <button class="btn btn-group" >Submit!</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      crew_pk:this.$route.params.crew_pk,
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ crew_pk: this.crew_pk, article_pk: this.article.pk, content: this.content, })
      this.content = ''
      this.$router.go()
    }
  }
}
</script>

<style>
.commentInput{
   width: 500px;
  height: 32px;
  font-size: 15px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-left: 10px;
  background-color: rgb(233, 233, 233);
}
</style>