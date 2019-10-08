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
            result: {}
        }
    },
    mounted: function () {
        if (!this.$store.state.username) {
            this.$router.push('/admin/login')
            return;
        }
        axios.get('/api/admin_category.json')
        .then((result) => {
            this.result = result.data
            let dashboard = {
                target: this.result.target,
                items: this.result.items
            }
            this.$store.dispatch('updateDashboard', dashboard)
        })
    }
}
</script>

<style scoped>
</style>
