<template>
  <div class="row">
    <nav-bar :now="'CrewDetail'"></nav-bar>
    <br>
    <br>
    <br>
    <br>
    <!-- crew info -->
    <div class="col-8 offset-2">
    <div>
      <img :src="`http://127.0.0.1:8000${crew.crew_backdrop}`" style="width:50rem; height:25rem"  alt="">
      <h3>크루 이름 :{{ crew.crewname }}</h3>
      <h4>
         크루 리더 : {{crew.crew_leader.profile.nickname}}

      </h4>
      <h4> 활동 장소 : {{ crew.crew_location1 }}</h4>
      <h4>크루 소개 : {{ crew.crewintro }}</h4>
      <h5>크루 인원 : {{crew.crew_users.length}}</h5>
    </div>
    <hr>
    <!-- Join Crew -->

    <h3 v-if="!(crew.crew_users.includes(currentUser.pk))">
      <button class="btn-lg btn-warning rounded-pill"
        @click="joinCrew(crew_pk)"
      > 가입하기 !</button>
    </h3>
    <h3 v-else>
      <button class="btn-lg btn-danger rounded-pill"
        @click="joinCrew(crew_pk)"
      > 탈퇴하기 !</button>
    </h3>
    <!-- article 만들기 -->
    <div>
       <router-link :to="{ name: 'ArticleCreate', params:{ crew_pk: crew_pk } }">
         <button class="btn-lg btn-dark">new Article</button>
        </router-link>
        
    </div>
    <!-- CREW MOVIE LIST -->
    <movie-list-item
      v-for="movie in crew.movies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
    <!-- article list -->
    <article-list-item
      v-for="article in articles"
      :key="article.pk"
      :article="article"
      :crew_pk="crew_pk"
    ></article-list-item>
  </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'
import MovieListItem from '@/components/MovieListItem.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CrewDetailView',
  components:{
    NavBar,
    ArticleListItem,
    MovieListItem,
  },
  data(){
    return{
      crew_pk: this.$route.params.crew_pk
    }
  },
  computed:{
    ...mapGetters(['crew', 'isLeader', 'articles','currentUser']),
    joinCount(){
      return this.crew.crew_user?.length
    }
  },
  methods:{
    ...mapActions(['fetchCrew', 'fetchProfile', 'fetchArticles', 'joinCrew'])
  },
  created(){
    this.fetchCrew(this.crew_pk)
    this.fetchArticles(this.crew_pk)
    console.log(this.crew_pk)
  }

}
</script>

<style>

</style>