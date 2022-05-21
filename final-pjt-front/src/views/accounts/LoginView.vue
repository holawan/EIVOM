<template>
  <div>
    <h1>로그인</h1>
    <account-error-list v-if="authError"></account-error-list>


    <form @submit.prevent="login(credentials)">
      <div>
        <label for="userid">userid: </label>
        <input v-model="credentials.userid" type="text" id="userid" required />
      </div>

      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>Login</button>
    </form>

  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return{
      credentials: {
        userid: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  }

}
</script>

<style>

</style>