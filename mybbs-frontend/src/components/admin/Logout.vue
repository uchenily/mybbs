<template>
</template>

<script>
export default {
  name: 'Logout',
  mounted: function () {
    this.$store.dispatch('clearUsername')
    this.$router.push('/admin/login')
  }
}
</script>

<style scoped>
</style>
