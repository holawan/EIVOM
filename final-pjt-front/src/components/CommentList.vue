<template>
  <div class="comment-list container">
    <h1>댓글을 작성해보세요 ~!~ </h1>
    
    <comment-form></comment-form>
    <br>
    <br>
    <div class="row">
      <comment-list-item class="col-8 offset-2" 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>        

    </div>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>