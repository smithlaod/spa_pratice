<template>
<!--  登录界面-->
  <div class="container">
<!--    <div class="logo-box"><img src="../back.png"/></div>-->
    <div class="login-box">

      <div class="login-text"> 登录 <br> 欢迎使用AcersTech</div>
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules">
        <el-form-item prop="username">
          <el-input
            v-model="loginForm.username"
            prefix-icon="el-icon-s-custom"
            placeholder="请输入用户名"
            @input="change($event)"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            prefix-icon="el-icon-unlock"
            placeholder="请输入密码"
            @input="change($event)"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="primary" @click="submitForm">登录</el-button>
          <el-button type="primary" @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login.vue',
  data () {
    return {
      // 登录表单对象
      loginForm: {
        username: '',
        password: ''
      },
      // 登录表单检验内容
      loginFormRules: {
        username: [
          { required: true, message: '请输入用户名', triiger: blur() },
          { min: 3, max: 20, message: '长度在6到20半角字符之间', triiger: blur() }
        ],
        password: [
          { required: true, message: '请输入密码', triiger: blur() },
          { min: 6, max: 20, message: '长度在6到20半角字符之间', triiger: blur() }
        ]
      }
    }
  },
  methods: {
    // 多层嵌套无效解决方案
    change (e) {
      this.$forceUpdate()
    },
    // 表单重置方法
    resetForm () {
      this.$refs.loginFormRef.resetFields()
    },
    // 登录表单
    submitForm () {
      const netUrl = 'http://localhost:5000/login/laod'
      console.log('点击了登录！')

      this.$http.post(netUrl, {
        name: this.loginForm.username,
        pwd: this.loginForm.password
      }).then(
        response => {
          if (response.data != null) {
            console.log(response.data)
          }
        }
      )
    }
  }
}
</script>

<style scoped>
  .container {
    width: 100%;
    height: 100%;
    background: url('../back.png');
    background-size: 100% 100%;
  }
  .logo-box {
    position: absolute;
    top: 60px;
    left: 30px;
  }
  .login-box {
    position: absolute;
    top: 50%;
    left: 25%;
    width: 400px;
    height: 400px;
    transform: translate(-50%, -50%);
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .login-text {
    width: 100%;
    font-size: 24px;
    text-align: center;
    color: #2f82fe;
    margin-bottom: 50px;
    box-sizing: border-box;
    padding: 20px;
  }
  .el-form-item {
    width: 90%;
    margin: 20px auto;
  }
  .login-text span {
    line-height: 30px;
    font-size: 18px;
    color: #666666;
  }
  .btns {
    width: 100%;
    text-align: center;
    margin-top: 50px;
  }
</style>
