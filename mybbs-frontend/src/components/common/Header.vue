<template>
    <div class='header'>
        <div class='logo'><router-link to='/'>MYBBS</router-link></div>
        <ul class='menu'>
            <li><router-link to="/">主页</router-link></li> 
            <li><router-link to="/categories">分类</router-link></li> 
            <li>公告</li> 
            <li><router-link to="/topic/new">发布</router-link></li> 
            <li>发现</li> 
        </ul>
        <div class='user logout' v-if='$store.state.username'>
            <div>欢迎, {{ this.$store.state.username }}</div>
            <router-link to="/logout"> 注销 </router-link>
        </div>
        <div class='user login' v-else>
            <router-link to="/login"> 登录 </router-link>
            <router-link to="/register"> 注册 </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "Header"
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
