<template>
  <div>
    <h1>영화가 아직 준비중입니다.</h1>
    <h3>곧 메인페이지로 돌아갑니다.</h3>
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