<template>
  <div>
    <img src="@/assets/waiting.png" style="width:100vw; height:100vh" alt="">
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