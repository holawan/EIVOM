<template>
  <div>
    <h1>로그아웃</h1>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'LogoutView',
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created(){
    if (this.isLoggedIn) {
      this.logout()
    } else {
      alert('접근이 잘못되었습니다')
      this.$router.back()
    }
  }
}
</script>

<style>

</style>