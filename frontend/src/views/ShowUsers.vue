<template>
  <el-table :data="userData" style="width: 80%; border: 1px lightgray;">
    <el-table-column prop="name" label="姓名" width="100px"></el-table-column>
    <el-table-column prop="pws" label="密码" width="100px"></el-table-column>
  </el-table>
</template>

<script>
export default {
  name: 'ShowUsers',
  data() {
    return {
      userData: {}
    }
  }
}
</script>

<style scoped>

</style>
