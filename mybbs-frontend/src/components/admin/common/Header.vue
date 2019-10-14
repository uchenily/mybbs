<template>
    <div class='header'>
        <div class='logo'><router-link to='/'>MYBBS</router-link></div>
        <ul class='menu'>
            <li><a @click="management('categories')">分类管理</a></li> 
            <li><a @click="management('users')">用户管理</a></li> 
            <li><a @click="management('topics')">帖子管理</a></li> 
            <li><a @click="management('replies')">评论管理</a></li> 
        </ul>
        <div class='user logout' v-if="this.$store.state.token">
            <div>欢迎, {{ this.$store.state.token.user.username }}</div>
            <router-link to="/admin/logout"> 注销 </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "AdminHeader",
    methods: {
        management (target) {
            axios.get('/api/v1/' + target)
            .then((response) => {
                if (response.data) {
                    let dashboard = {
                        target: target,
                        items: response.data,
                        actions: ['update', 'delete']
                    }
                    this.$store.dispatch('updateDashboard', dashboard)
                }
            })
        }
    }
}
</script>

<style scoped>
.user a, user a:visited {
    color: rgb(124, 124, 125);
}
a:hover {
    color: #000;
}
.header {
    margin: 0 auto;
    border-color: #e7e7e7;
    border-top: 4px solid #00b5ad;
    height: 60px;
    border-bottom: #e8e8e8;
    box-shadow: 0px 1px 11px 2px rgba(42, 42, 42, 0.1);
    margin-bottom: 40px;
    padding: 0 30px;
}
.header .logo {
    display: inline-block;
    font-size: 1.4em;
    font-weight: 900;
    text-align: center;
    line-height: 60px;
    margin-right: 30px;
}
.header .menu, .header .menu li {
    display: inline-block;
}
.header .menu li {
    margin: 0 10px;
}
.header .user {
    display: inline-block;
    float: right;
    text-align: center;
    line-height: 60px;
}
.header .user div {
    float: left;
    margin-right: 16px;
}
.logout a {
    color: #f18080;
}
</style>
