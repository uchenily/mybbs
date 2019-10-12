<template>
<div>
    <common-header></common-header>
    <div class="wrapper">
        <div class="title clearfix"><span>标题</span><input type="text" v-model="title"/></div>
        <div class="category clearfix">
            <span>分类</span>
            <select  v-model="selected">
                <option v-for="category in categories.data" :value="category.id">{{ category.name }}</option>
            </select>
        </div>
        <textarea placeholder="随便写点什么吧~" v-model="content"></textarea>
        <button @click="onSubmit()">提交</button>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Header from './common/Header'
export default {
    name: "TopicNew",
    components: {
        CommonHeader: Header
    },
    data: function () {
        return {
            title: "",
            selected: 1,
            categories: [],
            content: ""
        }
    },
    methods: {
        onSubmit () {
            if (this.$store.state.token == null) {
                this.$router.push('/login') 
                return
            }
            let topic = {
                title: this.title,
                author_id: this.$store.state.token.user.id,
                category_id: this.selected,
                content: this.content
            }
            axios({
                method: "post",
                url: "/api/v1/topics",
                header: {
                    "Content-Type": "application/json"
                },
                data: {
                    topic: topic
                }
            }).then(
                (response) => {
                    if (response.data != null) {
                        this.$router.push('/')
                    }
                }
            )
        }
    },
    mounted: function () {
        axios.get('/api/v1/categories')
        .then((response) => {
            this.$set(this.categories, "data", response.data)
        })
    }
}
</script>

<style scoped>
.wrapper {
    width: 70%;
    margin: 0 auto;
}
.wrapper textarea {
    width: 100%;
    height: 500px;
    padding: 0;
    padding-left: 1px;
    font-size: 18px;
    font-weight: 500;
    font-family: Consolas, emoji, "Microsoft YaHei";
    border: 1px dotted #eee;
}
.wrapper textarea:focus {
    outline: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
}
.wrapper button {
    padding: 12px 24px;
    float: right;
}
.title span, .title input, .category span, .category select {
    display: inline-block;
    float: left;
}
.title, .category {
    margin-bottom: 12px;
}
.title span, .category span {
    font-weight: 700;
    margin-right: 20px;
    line-height: 30px;
}
.title input, .category select {
    width: 60%;
    height: 30px;
}
select {
}
</style>
