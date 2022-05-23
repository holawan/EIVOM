<template>
  <div>
    <div>
      <router-link :to="{ name: 'ArticleDetail', params:{articleId:article.pk} }">
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
  }
}
</script>

<style>

</style>