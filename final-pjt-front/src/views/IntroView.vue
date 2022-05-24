<template>
  <div>
    <h1>어서오세요 이봄입니다아~~~</h1>
  </div>
</template>

<script>
import router from '@/router'
export default {
  name:'TmpView',
  methods:{
    onTime(){
      router.push({name:'Main'})
    }
  },
  created(){
    setTimeout(this.onTime, 2000);
  }

}
</script>

<style>

</style>