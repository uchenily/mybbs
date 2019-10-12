<template>
<div>
    <common-header></common-header>
    <div class="category">
        <div class="name">{{ result.name }}</div>
        <div class="desc">{{ result.description }}</div>
    </div>
    <common-content :items="result.items"></common-content>
</div>
</template>

<script>
import axios from 'axios'
import Header from './common/Header'
import Content from './common/Content'
export default {
    name: "Category",
    components: {
        CommonHeader: Header,
        CommonContent: Content
    },
    data: function () {
        return {
            result: {}
        }
    },
    mounted: function () {
        let id = this.$route.params.id
        axios.get('/api/v1/categories/' + id)
        .then((response) => {
            this.$set(this.result, "name", response.data.name)
            this.$set(this.result, "description", response.data.description)
        })
        axios.get('/api/v1/topics?category_id=' + id)
        .then((response) => {
            this.$set(this.result, "items", response.data)
        })
    }
}
</script>

<style scoped>
.category {
    width: 70%;
    margin: 0 auto;
    background: #10c1b9;
    color: #fff;
    padding: 40px;
    margin-bottom: 40px;
}
.name {
    font-size: 24px; 
    margin-bottom: 24px;
}
</style>
