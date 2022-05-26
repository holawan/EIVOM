<template>
  <div class="comment-list-item d-flex justify-content-between">
    <router-link  style="text-decoration: none; color: black;" :to="{ name: 'Profile', params: { user_pk:comment.user.pk } }">
       글쓴이  :    {{ comment.user.profile.nickname }}
    </router-link>
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="onDelete(payload)">Delete</button>
    </span>
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
    ...mapGetters(['currentUser']),
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
       this.$router.push()
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>