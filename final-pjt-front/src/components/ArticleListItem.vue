<template>
  <div>
    <br>
    <div >
      <router-link style="text-decoration:none ; color: black;" :to="{ name: 'ArticleDetail', params:{crew_pk:crew_pk, article_pk:article.pk} }">
        <h3>{{article.user.profile.nickname}} | {{ article.title }}</h3>
      </router-link>
      <br>
    </div>
  </div>
</template>

<script>
export default {
  name:'ArticleListItem',
  props:{
    article:Object,
    crew_pk : String
  }
}
</script>

<style>

</style>