<template>
<div>
    <common-header></common-header>
    <div class="left-column">
        <div class='detail'>
            <div class='title'>{{ result.topic.title }}</div>
            <div class='info'>ID: {{ result.topic.id }}</div>
            <div class='info'>author: {{ result.topic.author }}</div>
            <div v-html='result.topic.content'>{{ result.topic.content }}</div>
        </div>
        <div class="point">
            <div class="agree"><span>👍</span>{{ result.topic.agree }}</div>
            <div class="disagree"><span>👎</span>{{ result.topic.disagree }}</div>
        </div>
        <div class="comment">
            <div class="header">留下一条友善的评论吧~</div>
            <div class="wrapper clearfix">
                <textarea></textarea>
                <button v-if="$store.state.username">提交</button>
                <button v-else class="disabled">提交</button>
            </div>
        </div>
        <div class="reply">
            <div class="header">
                <div v-if="result.topic.replies">最新评论:</div>
                <div v-else>还没有评论哦~</div>
            </div>
            <ul>
                <div class="wrapper">
                    <li v-for="reply in result.topic.replies">
                        <div class="info clearfix">
                            <div class="user"><router-link :to="'/users/' + reply.user">{{ reply.user }}</router-link></div>
                            <div class="date">{{ reply.date }}</div>
                        </div>
                        <div class="content">{{ reply.content }}</div>
                    </li>
                </div>
            </ul>
        </div>
    </div>
    <div class="right-column">
        <div class="post">
            <button><router-link to="/topic/new">发起新的帖子</router-link></button>
        </div>
        <div class="recommand">
            <div class="header">推荐帖子</div>
            <ul>
                <li class="item" v-for="item in result.recommand"><router-link :to="'/topics/' + item.id">{{ item.title }}</router-link></li>
            </ul>
        </div> 
        <div></div> 
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Header from './common/Header'
export default {
    name: "Topic",
    data: function () {
        return {
            result: {
                // a bug, when data hasn't loaded yet, visit 'result.topic.title' will raise a warning in console.
                topic: {
                }
            }
        }
    },
    components: {
        CommonHeader: Header
    },
    mounted: function () {
        axios.get('/api/topic.json')
        .then((result) => {
            this.result = result.data
        })
    }
    // 解决跳转同一路由下router-link不跳转问题
    // watch: {
    // 　　'$route' (to, from) {
    //     　　this.$router.go(0);
    // 　　}
    // }
}
</script>

<style scoped>
.left-column, .right-column {
}
.left-column {
    float: left;
    width: 48%;
    margin-left: 15%;
}
.right-column {
    float: right;
    width: 20%;
    margin-right: 15%;
}
.detail, .comment, .point, .reply, .post, .recommand {
    background: #fff;
    border: 1px solid #eee;
    padding: 30px;
    font-size: 16px;
    line-height: 1.4em;
}
.detail .title {
    font-size: 2em;
    font-weight: 400;
}
.detail .info {
    margin: 10px 0;
    font-size: 12px;
    font-weight: 900;
}
.point {
    margin-top: -1px;
}
.point div {
    padding: 10px 24px;
    margin-right: 30px;
    display: inline-block;
    background: rgba(0, 189, 181, 0.24);
}
.point div span {
    margin-right: 20px;
}
.comment, .reply, .recommand {
    margin-top: 40px;
}
.comment .wrapper textarea {
    width: 100%;
    padding: 0;
    height: 100px;
    font-size: 20px;
    margin: 14px -1px;
}
.comment .wrapper button {
    float: right;
    padding: 8px 24px;
}
.comment .wrapper button.disabled {
    filter:alpha(Opacity=20);
    -moz-opacity:0.2;
    opacity: 0.2;
}
.reply .header, .comment .header {
    font-size: 18px;
    font-weight: 600;
}
.reply .wrapper li {
    border-bottom: 1px dotted #dcebf5;
    padding: 6px 0;
}
.reply .wrapper .info .user {
    float: left;
}
.reply .wrapper .info .date {
    float: right;
}
.post button {
    width: 100%;
    padding: 13px 14px;
    font-size: 16px;
    font-weight: 200;
    font-family: "Microsoft YaHei";
}
.post button:hover {
    background: #02afa7;
}
.post button a {
    color: #fff;
}
.recommand .header {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 10px;
}
.recommand .item {
    margin-left: 20px;
    list-style-type: circle;
}
.recommand .item a:hover {
    text-decoration: underline; 
}
</style>
