<template>
  <div>
    <h1>CastDetailView</h1>
    {{actorInfo}}
    <filmo-graphy></filmo-graphy>
  </div>
</template>

<script>
import FilmoGraphy from '@/components/FilmoGraphy.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CastDetailView',
  components: {
    FilmoGraphy,
  },
  data(){
    return {
      castId: this.$route.params.castId
    }
  },
  computed:{
    ...mapGetters(['filmos', 'actorInfo'])
  },
  methods:{
    ...mapActions(['getActorInfo' ,'getCastDetail'])
  },
  created(){
    this.getActorInfo(this.castId)
    this.getCastDetail(this.castId)
  }
}
</script>

<style>

</style>