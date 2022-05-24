<template>
  <li @click="onClickItem" class="item">
    {{ movie.title }}
  </li>
</template>

<script>
export default {
  name: 'SearchListItemPreview',
  props: {
    movie: Object
  },
  methods: {
    onClickItem () {
      this.$emit('on-click-item', this.movie)
    }
  }
}
</script>

<style>
  .item {
    cursor: pointer;
  }

  .item:hover {
    background: #eee;
  }
</style>