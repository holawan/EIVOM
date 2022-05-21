<template>
  <div>
    <h1>회원가입</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="email">아이디: </label>
        <input v-model="credentials.email" type="email" id="email"  required/>
        <!-- <span class="badge badge-danger mt-1" v-if="!availableEmail">이미 사용중인 이메일입니다.</span>
        <span class="badge badge-danger mt-1" v-if="!availableEmailForm">이메일 형식이 다릅니다.</span> -->
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
        email: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup']),
    // async checkDuplicate() {
    //   //일단은 사용가능한 이메일로 true로 초기화 한다.
    //   this.availableEmail = true;
        
    //     //이메일 유효성을 검사한다.
    //   if (!validateEmail(this.email)) {
    //     //유효성이 틀리다면 data 값을 false로 한다.
    //         this.availableEmailForm = false;
    //     return;
    //   } else {
    //     this.availableEmailForm = true;
    //   }
        
    //     //이메일 중복체크를 한다.
    //   const response = await checkDuplicateEmail(this.email);
    //   if (!response.data) {
    //     this.availableEmail = false;
    //   } else {
    //     this.availableEmail = true;
    //   }
  },
}

</script>

<style>

</style>