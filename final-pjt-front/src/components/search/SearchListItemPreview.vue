<template>
    <div class="row ">
      <div class="col-6 offset-3" style="border: solid 1px;" >
        <p >
          {{ movie.title }}
        </p>
  
      </div>

    </div>
  
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