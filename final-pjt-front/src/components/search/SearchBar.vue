<template>
  <div>
    <div>
      <input 
        type="text" 
        @input="onInputText" 
        @keyup.enter="onSearchText"
        >
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputText (event) {
      const searchKeyword = event.target.value.trim()
      if (searchKeyword) {
        this.$emit('text-input', searchKeyword)
        }
    },
    onSearchText (event) {
      const search = event.target.value.trim()
      this.$emit('search-text',search)
      event.target.value=''
    },
  },
  
}
</script>

<style>

</style>