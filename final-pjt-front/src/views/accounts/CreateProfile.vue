<template>
  <div style="width:100vw ; height:100vh" class="px-0 py-0">
    <account-error-list v-if="authError"></account-error-list>

    <div class="row" style="width:100vw">
      <!-- image -->
      <div class="col-8 mx-0 my-0 px-0 py-0" style=" height:100vh">
        <img src="@/assets/profile_back.png" class="img-fluid" alt="signup background" style=" height:100vh; filter:brightness(90%); opacity:90%">
      </div>

      <!-- form -->
      <div id="content" class="col-4" style="height:100%">
        <h1 class="my-5"> </h1>
        <h1 class="d-flex justify-content-start" style="font-weight:600">프로필 설정</h1>
        <div>
          
          <form @submit.prevent="sendImageToServer" enctype="multipart/form-data">

            <div class="d-flex justify-content-center">
              <!-- profile image -->
              <label for="image"></label>
              <div style="border-radius:100%;" class="mx-3">
                <input multiple @change="onGetFile()" ref="image" type="file" id="image" class="profile_image">
              </div>


              <!-- back image -->
              <label for="back"></label>
              <div style="border-radius:100%;" class="mx-3">
                <input multiple @change="onGetFile2()" ref="backdrop" type="file" id="back" class="back_image">
              </div>
            </div>
            
            
            <!-- nickname -->
            <div>
              <label for="nickname"></label>
              <span class="box int_name">
                <input class="int" v-model="credentials.nickname" placeholder="닉네임 입력" type="text" id="nickname" required/>
              </span>
            </div>

            <!-- birth -->
            <div>
              <label for="birth"></label>
              <span class="box">
                <input v-model="credentials.birth" class="int" type="date" placeholder="생년월일" id="birth" required />
              </span>
              <span class="error_next_box"></span>
            </div>


            <!-- profile info -->
            <div>
              <label for="introduce"></label>
              <span class="box int_name">
                <input class="int" v-model="credentials.introduce" type="text" placeholder="프로필 소개말을 입력해주세요" id="introduce" required />
              </span>
            </div>

            <!-- gender -->
            <div>
              <label for="gender"></label>
              <!-- <input v-model="credentials.gender" type="text" id="gender" required /> -->
              <span class="box gender_code">
                <select id="gender" class="sel int" v-model="credentials.gender" type="text" required>
                  <option value="" disabled selected>성별</option>
                  <option value="남성">남자</option>
                  <option value="여성">여자</option>
                </select>
              </span>
              <span class="error_next_text"></span>
            </div>

            <!-- location -->
            <div>
              <label for="location1"></label>
              <!-- <input v-model="credentials.location1" type="text" id="location1" required /> -->
              <span class="box gender_code">
                <select id="location1" v-model="credentials.location1" class="int sel" type="text" required>
                  <option value="" disabled selected>시/도</option>
                  <option value="서울특별시">서울특별시</option>
                  <option value="부산광역시">부산광역시</option>
                  <option value="대구광역시">대구광역시</option>
                  <option value="인천광역시">인천광역시</option>
                  <option value="광주광역시">광주광역시</option>
                  <option value="대전광역시">대전광역시</option>
                  <option value="울산광역시">울산광역시</option>
                  <option value="세종특별자치시">세종특별자치시</option>
                  <option value="경기도">경기도</option>
                  <option value="강원도">강원도</option>
                  <option value="충청북도">충청북도</option>
                  <option value="충청남도">충청남도</option>
                  <option value="전라북도">전라북도</option>
                  <option value="전라남도">전라남도</option>
                  <option value="경상북도">경상북도</option>
                  <option value="경상남도">경상남도</option>
                  <option value="제주특별자치도">제주특별자치도</option>
                </select>
              </span>
              <span class="error_next_box"></span>
            </div>


            <!-- <div>
              <label for="location2">시/군/구:</label>
              <input v-model="credentials.location2" type="text" id="location2" required />
            </div> -->

            <!-- create profile button -->
            <div class="btn_area">
              <button id="btnJoin">
                  <span style="font-weight:700">프로필 설정</span>
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
import { mapActions,mapGetters } from 'vuex'
export default {
  components: {
    AccountErrorList,
  },
  data(){
    return {
      credentials: {
        image :'',
        backdrop : require('@/assets/default_back.png'),
        nickname: '',
        birth: '',
        introduce: '',
        gender: '',
        location1: '',
        location2: '',
      }
    }
  },
  methods: {
    initModal: function () {
      this.credentials.image = ''
      this.credentials.backdrop = ''
      this.credentials.nickname = ''
      this.credentials.birth = ''
      this.credentials.introduce = ''
      this.credentials.gender = ''
      this.credentials.location1 = ''
      this.credentials.location2 = ''
    },
    onGetFile() {
      this.credentials.image = this.$refs.image.files[0]
      console.log(this.credentials.image)
    },
    onGetFile2() {
      this.credentials.backdrop =this.$refs.backdrop.files[0]
    },
    sendImageToServer(){
      const formData = new FormData()
        formData.append('image', this.credentials.image)
        formData.append('backdrop', this.credentials.backdrop)
        formData.append('nickname', this.credentials.nickname)
        formData.append('birth', this.credentials.birth)
        formData.append('introduce', this.credentials.introduce)
        formData.append('gender', this.credentials.gender)
        formData.append('location1', this.credentials.location1)
        formData.append('location2', this.credentials.location2)
        this.createProfile(formData)
      },
      ...mapActions(['createProfile']),
  },
  computed: {
  ...mapGetters(['authError'])
  },
  created(){
    const backimg = 
    this.credentials.backdrop = backimg
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
    height: 5%;
    border: solid 1px #dadada;
    border-radius: 10px;
    padding: 2% 14px 2% 14px;
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

#bir_wrap {
    display: table;
    width: 100%;
}

#bir_yy {
    display: table-cell;
    width: 147px;
    
}

#bir_mm {
    display: table-cell;
    width: 147px;
    vertical-align: middle;
}

#bir_dd {
    display: table-cell;
    width: 147px;
}

#bir_mm, #bir_dd {
    padding-left: 10px;
}

select {
    width: 100%;
    height: 5%;
    font-size: 15px;
    background: #fff url(https://static.nid.naver.com/images/join/pc/sel_arr_2x.gif) 100% 50% no-repeat;
    background-size: 20px 8px;
    -webkit-appearance: none;
    display: inline-block;
    text-align: start;
    border: none;
    cursor: default;
    font-family: Dotum,'돋움',Helvetica,sans-serif;
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
    padding: 5% 0 17px;
    border: 0;
    border-radius: 10px;
    cursor: pointer;
    color: #fff;
    background-color: rgb(255, 235, 96);
    font-size: 20px;
    font-weight: 600;
    font-family: Dotum,'돋움',Helvetica,sans-serif;
}

input.profile_image{
  background-image: url("@/assets/profile_default_small_text.png");
  border:none;
  cursor: pointer;
  outline: 0;
  width: 100px;
  height: 100px;
  background-repeat:no-repeat;
  border-radius: 100%;
}

input.back_image{
  background-image: url("@/assets/back_origin_small_text.png");
  border:none;
  cursor: pointer;
  outline: 0;
  width: 100px;
  height: 100px;
  background-repeat:no-repeat;
  border-radius: 100%;
}

input::file-selector-button {
  display:none;
}



</style>