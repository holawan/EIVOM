<template>
  <div>
    <br>
    <div >
      <router-link style="text-decoration:none ; color: black;" :to="{ name: 'ArticleDetail', params:{article_pk:article.pk,crew_pk:crew_pk} }">
        <h3>{{article.pk}} 번째 글 : {{ article.title }}</h3>
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