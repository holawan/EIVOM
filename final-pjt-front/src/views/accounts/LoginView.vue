<template>
  <div>
    <h1>로그인</h1>
    <account-error-list v-if="authError"></account-error-list>

    <google-vue></google-vue>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="email">userid: </label>
        <input v-model="credentials.email" type="email" id="email" required />
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
import GoogleVue from '@/components/GoogleVue.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
    GoogleVue,
  },
  data() {
    return{
      credentials: {
        email: '',
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