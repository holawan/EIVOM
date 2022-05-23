<template>
  <div>
    <h1>CrewCreateForm</h1>
    <account-error-list v-if="authError"></account-error-list>

    <!-- form UI -->
    <div>
      <form @submit.prevent="sendCrewImage" enctype="multipart/form-data">
        <label for="image">크루 프로필 사진 :</label>
        <input multiple @change="onGetFile3()" ref="image" type="file" id="image">

        <label for="backdrop">배경사진 :</label>
        <input multiple @change="onGetFile4()" ref="backdrop" type="file" id="backdrop">

        <div>
          <label for="crewname">크루이름: </label>
          <input  v-model="credentials.crewname" type="text" id="crewname" required/>
        </div>

        <div>
          <label for="location1">시/도: </label>
          <input  v-model="credentials.location1" type="text" id="location1" required/>
        </div>

        <div>
          <label for="location2">시/군/구:</label>
          <input v-model="credentials.location2" type="text" id="location2" required />
        </div>

        <div>
          <label for="introduce">크루소개:</label>
          <input v-model="credentials.introduce" type="text" id="introduce" required />
        </div>

        <div>
          <button>make crew!</button>
        </div>
      </form>

    </div>


  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  components:{
    AccountErrorList,
  },
  data(){
    return {
      credentials: {
        image: '',
        backdrop: '',
        crewname: '',
        location1: '',
        location2: '',
        introduce : '',
      }
    }
  },
  methoods: {
    initModal: function () {
      this.credentials.image = ''
      this.credentials.backdrop = ''
      this.credentials.introduce = ''
      this.credentials.crewname = ''
      this.credentials.location1 = ''
      this.credentials.location2 = ''
    },
    onGetFile3() {
      this.credentials.image = this.$refs.image.files[0]
      console.log(this.credentials.image)
    },
    onGetFile4() {
      this.credentials.backdrop =this.$refs.backdrop.files[0]
    },
    sendCrewImage(){
      const formData = new FormData()
        formData.append('image', this.credentials.image)
        formData.append('backdrop', this.credentials.backdrop)
        formData.append('crewname', this.credentials.crewname)
        formData.append('introduce', this.credentials.introduce)
        formData.append('location1', this.credentials.location1)
        formData.append('location2', this.credentials.location2)
        this.createCrew(formData)
      },
      ...mapActions(['createCrew'])
  },
  computed:{
    ...mapGetters(['authError'])
  }

}
</script>

<style>

</style>