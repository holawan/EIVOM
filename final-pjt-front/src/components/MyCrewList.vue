<template>
  <div>
    <crew-list-item
      :v-for="movie in user.like_movies"
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
  computed:{
    ...mapGetters(['currentUser'])
  },
  methods:{
    ...mapActions(['fetchCurrentuser'])
  },
  created(){
    console.log(this.currentUser.pk.like_movies)
  }

}
</script>

<style>

</style>