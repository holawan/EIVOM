<template>
  <div>

    <vue-glide
    class="glide__track m-4"
    data-glide-el="track"
    ref="slider"
    type="carousel"
    :breakpoints="{3000: {perView: 5}, 1100: {perView: 4}, 600: {perView: 3}}"
  >
  <!-- {{actors}} -->
  <vue-glide-slide 
    v-for="actor,idx in this.actors"
    :key="idx"
    :idx="idx"
  >
  <actor-list-item :actor="actor"></actor-list-item>
  <!-- {{actors}} -->
  </vue-glide-slide>
  </vue-glide>
  {{actors}}
  </div>
</template>


<script>
import ActorListItem from '@/components/ActorListItem.vue'
export default {
  name : 'ActorList',
  components : {
    ActorListItem,
  },
    props:{
    actors:Array,
  }
}
</script>

<style>

</style>