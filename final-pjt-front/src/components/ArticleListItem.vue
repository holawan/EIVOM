<template>
  <div>
    <div>
      <router-link :to="{ name: 'ArticleDetail', params:{article_pk:article.pk,crew_pk:crew_pk} }">
        {{ article.title }}
      </router-link>
      <p>{{ article.content }}</p>
      <hr>
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