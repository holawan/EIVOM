<template>
  <div>
      <div class="">
        <!-- <div class="shooting-stars">
          <div class="shooting-star"></div>
          <div class="shooting-star2"></div>
          <div class="shooting-star3"></div>
          <div class="shooting-star4"></div>
          <div class="shooting-star5"></div>
          <div class="shooting-star shooting-star--mid"></div>
          <div class="shooting-star shooting-star--fast"></div>
          <div class="shooting-star shooting-star--meh"></div>
          <div class="shooting-star shooting-star--mid2"></div>
          <div class="shooting-star shooting-star--fast2"></div>
          <div class="shooting-star shooting-star--meh2"></div>
        </div> -->
        <div id="particles-js"></div>
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

body, html {
	height: 100%;
	background-repeat: no-repeat;    /*background-image: linear-gradient(rgb(12, 97, 33),rgb(104, 145, 162));*/
	background:black;
	position: relative;
}
.introBackground{
  filter: brightness(90%);
  height: 100vh;
  overflow: hidden;
  margin:0;
  background-image: url("@/assets/main_bg.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
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