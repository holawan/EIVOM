<template>
  <div>
    <nav-bar :now="CrewCreate"></nav-bar>

    <account-error-list v-if="authError"></account-error-list>
    <div>
      
      <form @submit.prevent="sendImageToServer" enctype="multipart/form-data">
        <label for="crew_image">크루 이미지 입력: </label>
        <input multiple @change="onGetFile()" ref="crew_image" type="file" id="crew_image">
        <label for="crew_backdrop">배경사진 입력: </label>
        <input multiple @change="onGetFile2()" ref="crew_backdrop" type="file" id="crew_backdrop">
        <div>
          <label for="crewname">닉네임 입력: </label>
          <input  v-model="credentials.crewname" type="text" id="crewname" required/>
        </div>
        <div>
          <label for="crewintro">크루소개:</label>
          <input v-model="credentials.crewintro" type="text" id="crewintro" required />
        </div>
        <div>
          <label for="crew_location1">시/도:</label>
          <input v-model="credentials.crew_location1" type="text" id="crew_location1" required />
        </div>
        <div>
          <label for="crew_location2">시/군/구:</label>
          <input v-model="credentials.crew_location2" type="text" id="crew_location2" required />
        </div>
        <div>
          <button>Signup</button>
        </div>
    </form>

    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions,mapGetters } from 'vuex'
export default {
  components: {
    NavBar,
    
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
        crew_location2: '',
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
      this.credentials.crew_location2 = ''
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
        formData.append('crew_location2', this.credentials.crew_location2)
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

</style>