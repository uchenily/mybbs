<template>
<div>
    <common-header></common-header>
    <div class="wrapper">
        <div class="title clearfix"><span>标题</span><input type="text"/></div>
        <div class="category clearfix">
            <span>分类</span>
            <select>
                <option value="volvo">Volvo</option>
                <option value="saab">Saab</option>
                <option value="fiat">Fiat</option>
                <option value="audi">Audi</option>
            </select>
        </div>
        <textarea placeholder="随便写点什么吧~"></textarea>
        <button>提交</button>
    </div>
</div>
</template>

<script>
import Header from './common/Header'
export default {
    name: "TopicNew",
    components: {
        CommonHeader: Header
    },
    data: function () {
        return {
            username: "",
        }
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
