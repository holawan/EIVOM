<template>
  <div>
    <input 
      type="text" 
      @input="onInputText" 
      @keyup.enter="onResetText"
    >
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
    onResetText (event) {
      event.target.value = ''
    }
  }
}
</script>

<style>

</style>