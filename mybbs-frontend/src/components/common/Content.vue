<template>
<div class="content">
    <ul>
        <li v-for="item in items" :key='item.id'>
            <div class="topic">
                <router-link class="title" :to="'/topics/' + item.id">{{ item.title }}</router-link>
                <div class='info'>
                    • <router-link class="" :to="'/users/' + item.author">{{ item.author }}</router-link>
                    • <router-link class="" :to="'/categories/' + item.category">{{ item.category }}</router-link>
                    <div class="reply" v-if="item.latestReply"> • {{ item.latestReply }}</div>
                </div>
            </div>
        </li>
    </ul>
</div>
</template>

<script>
export default {
    name: 'Content',
    props: {
        items: Array
    }
}
</script>

<style scoped>
a:hover {
    text-decoration:underline;
}
.content {
    border: 1px solid #eee;
    background: #fff;
    width: 70%;
    margin: 0 auto;
}
.content ul {
    padding: 0px;
    margin: 0px;
}
.content ul li {
    display: block; 
    width: 100%;
    height: 60px;
    line-height: 30px;
}
.topic {
    width: 90%; 
    margin: 0 auto;
    border-bottom: 1px solid #dcebf5;
}
.info {
    font-size: 14px;
    font-weight: 200;
    color: #b3b3b3;
}
.reply {
    display: inline-block;
    float: right;
}
</style>
