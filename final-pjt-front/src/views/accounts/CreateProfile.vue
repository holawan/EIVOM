<template>
  <div>
    <h1>프로필 초기 설정</h1>
    <div>
      
      <form @submit.prevent="createProfile(credentials)" enctype="multipart/form-data">
        <label for="image">프로필사진 입력: </label>
        <input multiple @change="onInputImage()" ref="image" type="file" id="image">
        <label for="backdrop">배경사진 입력: </label>
        <input multiple @change="onInputImage2()" ref="backdrop" type="file" id="backdrop">
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
import { mapActions } from 'vuex'
export default {
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
    ...mapActions(['createProfile']),
    onInputImage() {
      this.image = this.$refs.image.files

    },
    onInputImage2() {
      this.backdrop = this.$refs.backdrop.files

    }
  }

}
</script>

<style>

</style>