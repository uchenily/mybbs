import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        username: "",
        dashboard: {
            target: String,
            items: Array
        }
    },
    actions: {
        updateUsername (ctx, username) {
            ctx.commit('updateUsername', username) // mutations中的updateusername
        },
        clearUsername (ctx) {
            ctx.commit('clearUsername')
        },
        updateDashboard(ctx, dashboard) {
            ctx.commit('updateDashboard', dashboard)
        }
    },
    mutations: {
        updateUsername (state, username) {
            state.username = username
        },
        clearUsername (state, username) {
            state.username = ""
        },
        updateDashboard(state, dashboard) {
            state.dashboard = dashboard
        }
    }
})
