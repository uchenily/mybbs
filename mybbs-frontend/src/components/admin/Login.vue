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
      axios({
        method: "post",
        url: "/api/v1/tokens",
        header: {
          "Content-Type": "application/json"
        },
        data: {
          data: {
            username: this.username,
            password: this.password
          }
        }
      }).then(
        (response) => {
          console.log(response)
          if (response.data != null) {
            this.$store.dispatch('updateToken', response.token)
            this.$store.dispatch('updateUsername', this.username)
            this.$router.push('/admin/')
          }
        }
      )
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
