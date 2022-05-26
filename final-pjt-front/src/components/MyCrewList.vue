<template>
  <div>
    <crew-list-item
      v-for="(crew, idx) in myCrews"
      :key="idx"
      :crew="crew"
    ></crew-list-item>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CrewListItem from './CrewListItem.vue'

export default {
  name:'CrewList',
  components: {
    CrewListItem,
  },
  props:{
    myCrews:Array,
  },
  computed:{
    ...mapGetters(['currentUser'])
  },
  methods:{
    ...mapActions(['fetchCurrentuser'])
  },

}
</script>

<style>

</style>