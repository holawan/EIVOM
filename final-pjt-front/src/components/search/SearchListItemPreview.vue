<template>
  <li >
    {{ movie.title }}
  </li>
  
</template>

<script>
export default {
  name: 'SearchListItem',
  props: {
    movie: {}
  },
  methods: {
    onClickItem () {
      this.$emit('on-click-item', this.movie)
    }
  },
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