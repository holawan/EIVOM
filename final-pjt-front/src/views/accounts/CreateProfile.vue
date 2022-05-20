<template>
  <div>
    <h1>프로필 초기 설정</h1>
    <div>
      
      <form @submit.prevent="signup(credentials)">
        <input multiple @change="onInputImage()" rec="image" type="file">
        <div>
          <label for="nickname">닉네임 입력: </label>
          <input  v-model="credentials.nickname" type="text" id="nickname" required/>
        </div>
        <div>
          <label for="birth">생년월일 입력: </label>
          <input v-model="credentials.birth" type="date" id="birth" required />
        </div>
        <div>
          <label for="introduction">프로필소개:</label>
          <input v-model="credentials.introduction" type="text" id="introduction" required />
        </div>
        <div>
          <button>Signup</button>
        </div>
    </form>

    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      credentials: {
        nickname: '',
        birth: '',
        introduction: '',
      }
    }
  },
  methods: {
    uploadImg(){
      console.log(',,')
    }
  }

}
</script>

<style>

</style>