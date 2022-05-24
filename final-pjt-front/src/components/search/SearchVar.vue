<template>
  <div>
    <div>
      <input :value="searchValue"
        type="text" 
        @input="onInputText" 
        @keyup.enter="onResetText"
        >
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
    data(){
    return {searchvalue:''}
  },
  methods: {
    onInputText (event) {
      const searchKeyword = event.target.value.trim()
      if (searchKeyword) {
        this.$emit('text-input', searchKeyword)
        }
    },
    onResetText (event) {
      event.target.value=''
    }
  }
}
</script>

<style>

</style>