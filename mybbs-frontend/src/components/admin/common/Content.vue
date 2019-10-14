<template>
<div class="content">
    <table v-if="items.length != 0">
        <tr>
            <th v-for="(value, key) in items[0]">{{ key }}</th>
            <th v-for="action in actions">{{ action }}</th>
        </tr>
        <tr v-for="(item, index) in items">
            <td v-for="(value, key) in item">
                <div v-if="!(value instanceof Object)">{{ value }}</div>
                <div v-else>{{ value.id }}</div>
            </td>
            <td v-for="action in actions">
                <ul class="action">
                    <button @click="doAction(action, '/api/v1/' + target + '/' + item.id, index)" :class="action">{{ action }}</button>
                </ul>
            </td>
        </tr>
    </table> 
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AdminContent',
    computed: {
        target: function () {
            return this.$store.state.dashboard.target
        },
        items: function () {
            return this.$store.state.dashboard.items
        },
        actions: function () {
            return this.$store.state.dashboard.actions
        }
    },
    methods: {
        doAction (action, url, index) {
            if (action == 'update') {
                // TODO
                return
            } else if (action == 'delete') {
                axios.delete(url)
                .then(() => {
                    this.items.splice(index, 1)
                })
            }
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
    text-align: left;
    line-height: 30px;
    overflow: hidden;
}
table tr th {
    color: #f3f3f3;
    font-weight: 700;
    background: #81ceca;
}
table tr:nth-child(odd) {
    background: #fff;
}
.action button {
    display: inline-block;
    height: 30px;
    padding: 0 20px;
    border: 1px solid #fff;
}
.delete, .update {
    border-radius: 4px;
    color: #fff;
}
.delete {
    background: #ff6363;
}
.update {
    background: #42af42;
}
table {
    table-layout:fixed;  
}
table tr td div {
    text-align: left;
    font-weight: 30px;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
