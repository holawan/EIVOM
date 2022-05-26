<template>
    <div class="row ">
      <div class="col-6 offset-2" style="border-style:none" align="start">
        <router-link 
          :to="{name:'MovieDetail', params:{movie_pk:this.movie.pk} }" 
          style="text-decoration:none; color:black;"
        >
          <p>
            {{ movie.title }}
          </p>
        </router-link>
        
        
  
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