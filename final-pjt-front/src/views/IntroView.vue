<template>
  <div>
      <div class="background">
  </div>
    <div class="d-flex justify-content-center">
      <p class="mainPageTitle">EIVOM</p>
      <div class="mainPageContent">
        <p>EIVOM[이;봄]</p>
          <p>깊이봄, 같이봄, 오롯이봄</p>
        
      </div>
      

    </div>
  </div>
</template>

<script>
// import router from '@/router'
export default {
  name:'IntroView',
//   methods:{
//     onTime(){
//       router.push({name:'Login'})
//     }
//   },
//   created(){
//     setTimeout(this.onTime, 2000);
//   }

}
</script>

<style>
.background{
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/main_bg.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.jb-image{
  position: absolute;
  width: 100%;
  height: auto;

  left: 0px;
  top: 0px;
}
  .mainPageTitle{
    position: absolute;
top: 200px;
font-family: 'Antic Didone';
font-style: normal;
font-weight: 400;
font-size: 128px;
line-height: 152px;
text-align: center;

color: #FFFFFF;

mix-blend-mode: normal;
  }
  .mainPageContent{
    
position: absolute;
top: 450px;
font-family: 'East Sea Dokdo';
font-style: normal;
font-weight: 400;
font-size: 64px;
line-height: 80px;
text-align: center;

color: #FFFFFF;

mix-blend-mode: normal;
text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  }
</style>