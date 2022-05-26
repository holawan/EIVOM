<template>
  <div>

  <div style="width:100vw ; height:100vh" class="px-0 py-0">
    <account-error-list v-if="authError"></account-error-list>

    <div class="row" style="width:100vw">
      <!-- image -->
      <div class="col-8 mx-0 my-0 px-0 py-0" style=" height:100vh">
        <img src="@/assets/cew_create_back.png" class="img-fluid" alt="signup background" style=" height:100vh; filter:brightness(90%); opacity:90%">
      </div>

      <!-- form -->
      <div id="content" class="col-4" style="height:100%">
        <h1 class="my-5"> </h1>
        <h1 class="d-flex justify-content-start" style="font-weight:600">크루 만들기</h1>
        <div>
          
          <form @submit.prevent="sendImageToServer" enctype="multipart/form-data">

            <div class="d-flex justify-content-center">
              <!-- profile image -->
              <label for="crew_image">
                <div style="border-radius:100%;" class="mx-3 profile_image_before" ></div>
              </label>
              <!-- <label for="image" v-else>
                <div style="border-radius:100%;" class="mx-3 profile_image" ></div>
              </label> -->

              <input multiple @change="onGetFile()" ref="crew_image" 
                type="file" id="crew_image" overflow="hidden" 
                style="position:absolute; clip:rect(0, 0, 0, 0);"
              >


              <!-- back image -->
              <label for="crew_backdrop" >
                <div style="border-radius:100%;" class="mx-3 back_image"></div>
              </label>
              <input multiple @change="onGetFile2()" 
                ref="crew_backdrop" type="file" id="crew_backdrop" overflow="hidden" 
                style="position:absolute; clip:rect(0, 0, 0, 0);"
              >
            </div>
            
            
            <!-- nickname -->
            <div>
              <label for="crewname"></label>
              <span class="box int_name">
                <input class="int" v-model="credentials.crewname" placeholder="크루네임 입력" type="text" id="crewname" required/>
              </span>
            </div>


            <!-- crew info -->
            <div>
              <label for="introduce"></label>
              <span class="box int_name">
                <input class="int" v-model="credentials.crewintro" type="text" placeholder="크루 소개말을 입력해주세요." id="introduce" required />
              </span>
            </div>


            <!-- location -->
            <div>
              <label for="location1"></label>
              <!-- <input v-model="credentials.location1" type="text" id="location1" required /> -->
              <span class="box">
                <select id="location1" v-model="credentials.crew_location1" class="int" type="text" style="color:black;" required>
                  <option value="" disabled selected>시 / 도</option>
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
        crew_image :'',
        crew_backdrop :'',
        crewname: '',
        crewintro: '',
        crew_location1: '',
      }
    }
  },
  methods: {
    initModal: function () {
      this.credentials.crew_image = ''
      this.credentials.crew_backdrop = ''
      this.credentials.crewname = ''
      this.credentials.crewintro = ''
      this.credentials.crew_location1 = ''
    },
    onGetFile() {
      this.credentials.crew_image = this.$refs.crew_image.files[0]
      // console.log(this.credentials.image)
    },
    onGetFile2() {
      this.credentials.crew_backdrop =this.$refs.crew_backdrop.files[0]
    },
    sendImageToServer(){
      const formData = new FormData()
        formData.append('crew_image', this.credentials.crew_image)
        formData.append('crew_backdrop', this.credentials.crew_backdrop)
        formData.append('crewname', this.credentials.crewname)
        formData.append('crewintro', this.credentials.crewintro)
        formData.append('crew_location1', this.credentials.crew_location1)
        this.createCrew(formData)
      },
      ...mapActions(['createCrew']),
    },
    computed: {
    ...mapGetters(['authError'])
  },

}
</script>

<style>
.profile_image{
  background-image: url("@/assets/crew_test.png");
  border:none;
  cursor: pointer;
  outline: 0;
  width: 100px;
  height: 100px;
  background-repeat:no-repeat;
  border-radius: 100%;
}

</style>