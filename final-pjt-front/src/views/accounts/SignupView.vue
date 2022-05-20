<template>
  <div>
    <h1>회원가입</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="userid">아이디: </label>
        <input v-model="credentials.userid" type="text" id="username" required/>
      </div>
      <div>
        <label for="password1">비밀번호: </label>
        <input v-model="credentials.password1" type="password" id="password1" required/>
      </div>
      <div>
        <label for="password2">비밀번호 확인: </label>
        <input v-model="credentials.password2" type="password" id="password2" required/>
      </div>
      <div>
        <button>회원가입</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data(){
    return{
      credentials: {
        userid: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>