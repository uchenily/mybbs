<template>
<div>
    <admin-header></admin-header>
    <admin-content></admin-content>
</div>
</template>

<script>
import axios from 'axios'
import AdminHeader from './common/Header'
import AdminContent from './common/Content'
export default {
    name: 'AdminIndex',
    components: {
        AdminHeader,
        AdminContent
    },
    data: function () {
        return {
            categories: [],
            target: "categories"
        }
    },
    mounted: function () {
        if (!this.$store.state.token) {
            this.$router.push('/admin/login')
            return
        }
        axios.get('/api/v1/categories')
        .then((response) => {
            this.categories = response.data
            let dashboard = {
                target: this.target,
                items: this.categories,
                actions: ['update', 'delete']
            }
            this.$store.dispatch('updateDashboard', dashboard)
        })
    }
}
</script>

<style scoped>
</style>
