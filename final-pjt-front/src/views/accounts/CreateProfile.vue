<template>
  <div>
    <h1>프로필 초기 설정</h1>
    <account-error-list v-if="authError"></account-error-list>
    <div>
      
      <form @submit.prevent="sendImageToServer" enctype="multipart/form-data">
        <label for="image">프로필사진 입력: </label>
        <input multiple @change="onGetFile()" ref="image" type="file" id="image">
        <label for="backdrop">배경사진 입력: </label>
        <input multiple @change="onGetFile2()" ref="backdrop" type="file" id="backdrop">
        <div>
          <label for="nickname">닉네임 입력: </label>
          <input  v-model="credentials.nickname" type="text" id="nickname" required/>
        </div>
        <div>
          <label for="birth">생년월일 입력: </label>
          <input v-model="credentials.birth" type="date" id="birth" required />
        </div>
        <div>
          <label for="introduce">프로필소개:</label>
          <input v-model="credentials.introduce" type="text" id="introduce" required />
        </div>
          <div>
            <label for="gender">성별:</label>
            <input v-model="credentials.gender" type="text" id="gender" required />
          </div>
          <div>
            <label for="location1">시/도:</label>
            <input v-model="credentials.location1" type="text" id="location1" required />
          </div>
          <div>
            <label for="location2">시/군/구:</label>
            <input v-model="credentials.location2" type="text" id="location2" required />
          </div>
        <div>
          <button>Signup</button>
        </div>
    </form>

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
        backdrop :'',
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
      this.credentials.backdrop =this.$refs.image.files[0]
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

}
</script>

<style>

</style>