<template>
  <div>
    <h1>My Crew List</h1>
    <crew-list-item></crew-list-item>
  </div>
</template>

<script>
import CrewListItem from './CrewListItem.vue'

export default {
  name:'CrewList',
  components: {
    CrewListItem,
  }

}
</script>

<style>

</style>