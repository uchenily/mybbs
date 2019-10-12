<template>
<div>
<!-- use form element will cause a bug here -->
  <div class="form">
    <input type='text' placeholder='用户名' v-model='username'/>
    <input type='password' placeholder='密码' v-model='password'/>
    <button @click='login()'>登录</button>
  </div>
  <div class="alert-warning clearfix" v-show="hasWarning">
    <div class="text">{{ this.alertWarning }}</div>
    <div class="close" @click="closeWarning"></div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data: function() {
    return {
      username: "",
      password: "",
      alertWarning: "用户名或密码错误!",
      hasWarning: false
    }
  },
  methods: {
    login () {
      let data = {
        username: this.username,
        password: this.password
      }
      axios({
        method: "post",
        url: "/api/v1/tokens",
        header: {
          "Content-Type": "application/json"
        },
        data: {
          data: data
        }
      }).then(
        (response) => {
          if (response.data) {
            this.$store.dispatch('updateToken', response.data)
            this.$router.push('/')
          } else {
            this.hasWarning = true
          }
        }
      )
    },
    closeWarning () {
      this.hasWarning = false
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
.alert-warning {
    position: fixed;
    top: 70px;
    right: 100px;
    background: #f8d7da;
    padding: 12px 20px;
    color: #721c24;
    border-radius: 4px;
    border: 1px solid #f5c6cb;
}
.alert-warning .text {
    float: left;
}
.alert-warning .close {
    float: right;
    padding-left: 20px;
    color: #d23142;
}
.alert-warning .close::after {
    content: "\2716"; /* close symbol */
}
.alert-warning .btn:hover {
    cursor: pointer;
}
@-webkit-keyframes fadeIn {
	0% {
        opacity: 0;
	}
	20%{
		opacity: .2;
	}
	50% {
		opacity: .5;
	}
	70%{
		opacity: .7;
	}
	100% {
		opacity: 1;
	}
}
.alert-warning {
    /*调用动画效果*/
	-webkit-animation-name: fadeIn;
	-webkit-animation-duration: .8s;
	-webkit-animation-iteration-count: 1;
	-webkit-animation-delay: 0s;
}
</style>
