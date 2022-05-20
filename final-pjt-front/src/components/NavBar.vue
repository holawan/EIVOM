<template>
<div>
  <router-link :to="{ name: 'Search' }">Search</router-link> |
  <router-link :to="{ name: 'Main' }">Main</router-link> |
  <router-link :to="{ name: 'Crew' }">Crew</router-link> |
  <router-link :to="{ name: 'Profile' }">Profile</router-link>

</div>
</template>

<script>

export default {
  name:'NavBar',


}
</script>

<style>

</style>