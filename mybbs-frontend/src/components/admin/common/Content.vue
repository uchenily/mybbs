<template>
<div class="content">
    <table>
        <tr>
            <th v-for="(value, key) in items[0]">{{ key }}</th>
        </tr>
        <tr v-for="item in items">
            <td v-for="(value, key) in item">
                <div v-if="value instanceof Array">
                    <ul class="actions">
                        <li v-for="action in value" :class="action">
                            <router-link :to="'/admin/' + target + '/' + action">{{ action }}</router-link>
                        </li>
                    </ul>
                </div>
                <div v-else>{{ value }}</div>
            </td>
        </tr>
    </table> 
</div>
</template>

<script>
export default {
    name: 'AdminContent',
    computed: {
        target: function () {
            return this.$store.state.dashboard.target
        },
        items: function () {
            return this.$store.state.dashboard.items
        }
    }
}
</script>

<style scoped>
.content {
    width: 70%;
    margin: 0 auto;
}
table {
    border-spacing: 0;
    width: 100%;

    border: solid #ccc 1px;
    -moz-border-radius: 6px;
    -webkit-border-radius: 6px;
    border-radius: 6px;
    -webkit-box-shadow: 0 1px 1px #ccc;
    -moz-box-shadow: 0 1px 1px #ccc;
    box-shadow: 0 1px 1px #ccc;
}
table tr{
    -o-transition: all 0.1s ease-in-out;
    -webkit-transition: all 0.1s ease-in-out;
    -moz-transition: all 0.1s ease-in-out;
    -ms-transition: all 0.1s ease-in-out;
    transition: all 0.1s ease-in-out;
    text-align: center;
    line-height: 30px;
}
table tr th {
    color: #f3f3f3;
    font-weight: 700;
    background: #81ceca;
}
table tr:nth-child(odd) {
    background: #fff;
}
ul.actions {
    
}
ul.actions li {
    display: inline-block;
    padding: 0 20px;
}
.delete, .update {
    border-radius: 4px;
    margin: 2px 10px;
}
.delete a, .update a {
    display: inline-block;
    color: #fff;
}
.delete {
    background: #ff6363;
}
.update {
    background: #42af42;
}
</style>
