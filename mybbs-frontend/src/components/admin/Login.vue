<template>
<div>
<!-- use form element will cause a bug here -->
  <div class="form">
    <input type='text' placeholder='用户名' v-model='username'/>
    <input type='password' placeholder='密码' v-model='password'/>
    <button @click='onSubmit()'>登录</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Admin',
  data: function() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    onSubmit () {
      // let formData = new FormData()
      // for (let key in this.formInfo) {
      //   formData.append(key, this.formInfo[key])
      // }
      // axios({
      //   method: "post",
      //   url: "/api/user.json",
      //   header: {
      //     "Content-Type": "multipart/form-data"
      //   },
      //   data: formData
      // }).then(
      //   (res) => {
      //     console.log(res)
      //   }
      // )

      // axios.get("api/user.json").then(
      //   (res) => {
      //     // console.log(res)
      //     // console.log("token:", res.data.token)
      //     // let username = res.data.username
      //     let username = this.formInfo.username
      //     console.log("username:", username)
      //     this.$store.dispatch('updateUsername', username)
      //   }
      // )

      this.$store.dispatch('updateUsername', this.username)
      // 跳转到首页
      this.$router.push('/admin/')
    }
  }
}
</script>

<style scoped>
div.form {
    position: absolute;
    width: 30%;
    left: 35%;
    top: 30%;
}
input, button {
    width: 100%;
    outline-style: none;
    margin-bottom: -1px;
    padding: 13px 14px;
    font-size: 16px;
    font-weight: 200;
    font-family: "Microsoft YaHei";
}
</style>
