<template>
  <div id="app">
    <el-menu router :default-active="activeIndex" mode="horizontal">
      <el-menu-item index="/" >Home</el-menu-item>
      <el-menu-item index="/about">About</el-menu-item>
      <el-menu-item index="/login">Login</el-menu-item>
      <el-menu-item index="/show">Show</el-menu-item>
    </el-menu>

    <router-view/>
  </div>

</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
  a {
    text-decoration: none;
  }
</style>
