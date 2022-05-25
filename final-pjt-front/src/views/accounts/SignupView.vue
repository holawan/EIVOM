<template>
  <div id="content">
    <h1>회원가입</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      
      <!-- email -->
      <div>
        <h3>
          <label for="email"></label>
        </h3>
        <span class="box int_id">
          <input class="id" v-model="credentials.email" type="email" id="email" placeholder="아이디 입력" ng-required="true"/>
        </span>
      </div>

      <!-- password1 -->
      <div>
        <h3 class="join_title"><label for="password1">비밀번호</label></h3>
        <span class="box int_pass">
            <input class="int" v-model="credentials.password1" type="password" id="password1" placeholder="비밀번호 입력" ng-required="true"/>
            <span id="alertTxt">사용불가</span>
        </span>
        <span class="error_next_box"></span>
      </div>

      <!-- password2 -->
      <div>
        <h3 class="join_title"><label for="password2">비밀번호 확인</label></h3>
        <span class="box int_pass_check">
            <input class="int" v-model="credentials.password2" type="password" id="password2" placeholder="비밀번호 입력" ng-required="true"/>
            <span id="alertTxt">사용불가</span>
        </span>
        <span class="error_next_box"></span>
      </div>

      <!-- join button -->
      <div class="btn_area">
        <button type="submit" id="btnJoin">
            <span>회원가입</span>
        </button>
      </div>

        <!-- <label for="email">
          <input class="input" v-model="credentials.email" type="email" id="email" placeholder="아이디 입력" ng-required="true"/>
        </label>

        <b-form-group label for="password1">
          <input class="input" v-model="credentials.password1" type="password" id="password1" placeholder="비밀번호 입력" ng-required="true"/>
        </b-form-group>

        <b-form-group label for="password2">
          <b-form-input class="input" v-model="credentials.password2" type="password" id="password2" placeholder="비밀번호 확인" ng-required="true"/>
        </b-form-group>

        <b-button size="lg" variant="success" type="submit">Signup</b-button> -->

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
  },
}

</script>

<style>
#content {
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    width: 460px;
}

input:focus {
    outline: none;
}

h3 {
    margin: 19px 0 8px;
    font-size: 14px;
    font-weight: 700;
}

.box {
    display: block;
    width: 100%;
    height: 51px;
    border: solid 1px #dadada;
    border-radius: 10px;
    padding: 10px 14px 10px 14px;
    box-sizing: border-box;
    background: #fff;
    position: relative;
}

.int {
    display: block;
    position: relative;
    width: 100%;
    height: 29px;
    border: none;
    background: #fff;
    font-size: 15px;
}

input {
    font-family: Dotum,'돋움',Helvetica,sans-serif;    
}

.box.int_id {
    padding-right: 110px;
}

.box.int_pass {
    padding-right: 40px;
}

.box.int_pass_check {
    padding-right: 40px;
}

.error_next_box {
    margin-top: 9px;
    font-size: 12px;
    color: red;    
    display: none;
}

#alertTxt {
    position: absolute;
    top: 19px;
    right: 38px;
    font-size: 12px;
    color: red;
    display: none;
}

.btn_area {
    margin: 30px 0 91px;
}

#btnJoin {
    width: 100%;
    padding: 21px 0 17px;
    border: 0;
    cursor: pointer;
    color: #fff;
    background-color: #fdfdb1;
    font-size: 20px;
    font-weight: 400;
    font-family: Dotum,'돋움',Helvetica,sans-serif;
}

</style>