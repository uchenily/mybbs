<template>
<div>
    <common-header></common-header>
    <div class="left-column">
        <div class='detail'>
            <div class='title'>{{ topic.title }}</div>
            <div class='info'>ID: {{ topic.id }}</div>
            <div class='info' v-if="topic.author">author: {{ topic.author.username }}</div>
            <div v-html='topic.content'></div>
        </div>
        <div class="point">
            <div class="agree" @click="doAgree()" :disabled="disabledAgree"><span>👍</span>{{ topic.agree }}</div>
            <div class="disagree" @click="doDisagree()" :disabled="disabledDisagree"><span>👎</span>{{ topic.disagree }}</div>
        </div>
        <div class="comment">
            <div class="header">留下一条友善的评论吧~</div>
            <div class="wrapper clearfix">
                <textarea v-model="content"></textarea>
                <button v-if="$store.state.token" @click="replySubmit()">提交</button>
                <button v-else class="disabled">提交</button>
            </div>
        </div>
        <div class="reply">
            <div class="header">
                <div v-if="topic.replies">最新评论:</div>
                <div v-else>还没有评论哦~</div>
            </div>
            <ul>
                <div class="wrapper">
                    <li v-for="reply in topic.replies">
                        <div class="info clearfix">
                            <div class="user"><router-link :to="'/users/' + reply.user.username">{{ reply.user.username }}</router-link></div>
                            <div class="date">{{ reply.updated_time.split('.')[0] }}</div>
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
                <li class="item" v-for="item in topic.recommand"><router-link :to="'/topics/' + item.id">{{ item.title }}</router-link></li>
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
            topic: {},
            content: "",
            disabledAgree: false,
            disabledDisagree: false
        }
    },
    components: {
        CommonHeader: Header
    },
    methods: {
        replySubmit () {
            if (this.$store.token) {
                this.$router.push('/login')
                return
            }
            let reply = {
                user_id: this.$store.state.token.user.id,
                topic_id: this.topic.id,
                content: this.content
            }
            axios({
                method: "post",
                url: "/api/v1/replies",
                header: {
                    "Content-Type": "application/json"
                },
                data: {
                    reply: reply
                }
            }).then(
                (response) => {
                    if (response.data) {
                        // unshift, add in head of array.
                        this.topic.replies.unshift(response.data)
                        this.content = ""
                    }
                }
            )
        },
        doAgree () {
            if (this.$store.state.token && !this.disabledAgree) {
                this.topic.agree += 1
                this.disabledAgree = true
                let topic = {
                    id: this.topic.id,
                    agree: this.topic.agree
                }
                axios({
                    method: "put",
                    url: "/api/v1/topics",
                    header: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        topic: topic
                    }
                })
            }
        },
        doDisagree () {
            if (this.$store.state.token && !this.disabledDisagree) {
                this.topic.disagree += 1
                this.disabledDisagree = true
            }
        }
    },
    mounted: function () {
        let id = this.$route.params.id
        axios.get('/api/v1/topics/' + id)
        .then((response) => {
            if (response.data) {
                this.topic = response.data
                // this.topic.replies is null when replySubmit()
                // it's only appear on online version(it works well in local)
                // I don't know why...
                this.$set(this.topic, "replies", [])
            }
        })
        axios.get('/api/v1/replies?topic_id=' + id)
        .then((response) => {
            if (response.data) {
                this.$set(this.topic, "replies", response.data)
            }
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
    line-height: 1.2em;
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
.agree:hover, .disagree:hover {
    cursor: pointer;
}
</style>
