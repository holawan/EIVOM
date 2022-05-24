<template>
  <div>
    <input v-model="searchvalue"
      type="text" 
      @input="onInputText" 
      @keyup.enter="onResetText"
    >
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
    data(){
    return {searchvalue:''}
  },
  methods: {
    onInputText () {
      const searchKeyword = this.searchvalue.trim()
      if (searchKeyword) {
        this.$emit('text-input', searchKeyword)
        }
    },
    onResetText () {
      this.searchvalue=''
    }
  }
}
</script>

<style>

</style>