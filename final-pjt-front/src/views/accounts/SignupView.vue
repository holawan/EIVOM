<template>
<div style="width:100vw ; height:100vh" class="px-0 py-0">
<account-error-list v-if="authError"></account-error-list>

<!-- <div class="container mx-0 my-0" style="width:100vw; height:100vh"> -->
  
    <div class="row" style="width:100vw">
      <div class="col-8 mx-0 my-0 px-0 py-0" style=" height:100vh">
        <img src="@/assets/signup.png" class="img-fluid" alt="signup background" style=" height:100%; filter:brightness(90%); opacity:90%">
        
      </div>
  
      <div id="content" class="col-4" style="height:100%">

        <h1 class="my-5"> </h1>
        <h1 class="d-flex justify-content-start" style="font-weight:600">회원가입</h1>
        <!-- 회원가입 폼 -->
        <div>
        <form @submit.prevent="signup(credentials)">
          
          <!-- email -->
          <div>
            <label for="email"></label>
            <span class="box int_id">
              <input @input="onInputText" class="id int" v-model="credentials.email" type="email" id="email" placeholder="아이디 입력" required/>
            </span>
          </div>

          <!-- password1 -->
          <div>
            <label for="password1"></label>
            <span class="box int_pass">
                <input @input="onInputText" class="int pw1" v-model="credentials.password1" type="password" id="password1" placeholder="비밀번호 입력" required/>
                <span id="alertTxt">사용불가</span>
            </span>
            <span class="error_next_box"></span>
          </div>

          <!-- password2 -->
          <div>
            <label for="password2"></label>
            <span class="box int_pass_check">
                <input @input="onInputText" class="int pw2" v-model="credentials.password2" type="password" id="password2" placeholder="비밀번호 입력" required/>
                <span id="alertTxt">사용불가</span>
            </span>
            <span class="error_next_box"></span>
          </div>

          <!-- join button -->
          <div class="btn_area">
            <button id="btnJoin"
            v-if="count >= 3">
                <span>회원가입</span>
            </button>
            <button disabled="disabled"
              v-else id="disbtnJoin"
            ><span style="font-weight:500">회원가입</span></button>
          </div>
        </form>
        </div>
      </div>
  </div>
  
  
</div>
<!-- </div> -->
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
      },
      count:0,
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup']),
    onInputText (event) {
      const searchKeyword = event.target.value.trim()
      if (searchKeyword) {
        this.count += 1
        }
    },
  },
}

</script>

<style>
/* .photo{
  filter: brightness(90%);
  height: 100vh;
  margin:0;
  background-image: url("@/assets/signup_back.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
} */


input:focus {
    outline: none;
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
    /* position: relative; */
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
    border-radius: 10px;
    cursor: pointer;
    color: #fff;
    background-color: rgb(255, 235, 96);
    font-size: 20px;
    font-weight: 400;
    font-family: Dotum,'돋움',Helvetica,sans-serif;
}

#disbtnJoin {
    width: 100%;
    padding: 21px 0 17px;
    border: 0;
    border-radius: 10px;
    cursor: pointer;
    color: #fff;
    background-color: rgb(255, 247, 191);
    font-size: 20px;
    font-weight: 400;
    font-family: Dotum,'돋움',Helvetica,sans-serif;
    color: rgb(63, 63, 63);
}

</style>