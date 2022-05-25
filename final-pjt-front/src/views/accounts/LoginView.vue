<template>
  <div style="width:100vw ; height:100vh" class="px-0 py-0">
    <account-error-list v-if="authError"></account-error-list>

    <div class="row" style="width:100vw">
      <!-- image -->
      <div class="col-8 mx-0 my-0 px-0 py-0" style="height:100vh">
        <img src="@/assets/login_back.png" alt="login background" class="img-fluid" style="height:100vh; filter:brightness(90%); opacity:90%">
      </div>

      <!-- form -->
      <div id="content" class="col-4" style="height:100%">
        <h1 class="my-5"> </h1>
        <h2 class="d-flex justify-content-start" style="font-weight:600">깊이봄, 같이봄, 오롯이봄</h2>
        <div>
          <form @submit.prevent="login(credentials)">
            <!-- email -->
            <div>
              <label for="email"></label>
              <span class="box int_id">
                <input v-model="credentials.email" class="int" type="email" id="email" placeholder="이메일 입력" required />
              </span>
            </div>

            <!-- password -->
            <div>
              <label for="password"></label>
              <span class="box int_pass">
                <input v-model="credentials.password" class="int" type="password" id="password" placeholder="비밀번호 입력" required />
              </span>
            </div>

            <!-- login button -->
            <div class="btn_area">
              <button id="btnJoin">
                  <span style="font-weight:700">로그인</span>
              </button>
            </div>
          </form>
        </div>
      </div>

    </div>
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

</style>