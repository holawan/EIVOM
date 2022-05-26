<template>
  <div class="comment-list-item d-flex justify-content-between">
    <router-link  style="text-decoration: none; color: black;" :to="{ name: 'Profile', params: { user_pk:comment.user.pk } }">
       댓글쓴이  :    {{ comment.user.profile.nickname }}
    </router-link>
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate" class="btn btn-open">Update</button> |
      <button @click="switchIsEditing" class=" btn btn-close" ></button>
    </span>

    <span v-if="currentUser.pk === comment.user.pk && !isEditing">
      <button @click="switchIsEditing" class="btn btn-open">Edit </button>
      <button @click="onDelete(payload)" class=" btn btn-open">Delete</button>
    </span>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        crew_pk : this.$route.params.crew_pk,
        article_pk: this.comment.article,
        comment_pk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser','isAuthor']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
    onDelete(payload){
      this.deleteComment(payload)
      this.$router.go()
    }
  },

}
</script>

<style>

</style>