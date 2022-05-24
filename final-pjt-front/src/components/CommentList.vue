<template>
  <div>
    <h1>CommentList</h1>
    
    <comment-list-item
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk"  
    ></comment-list-item>

    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentForm from './CommentForm.vue'
import CommentListItem from './CommentListItem.vue'

export default {
  name:'CommentList',
  components: {
    CommentForm,
    CommentListItem,
  },
  props:{ comments:Array }
}
</script>

<style>

</style>