import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: null,
        dashboard: {
            target: String,
            items: Array
        }
    },
    actions: {
        updateToken (ctx, token) {
            ctx.commit('updateToken', token)
        },
        clearToken (ctx) {
            ctx.commit('clearToken')
        },
        updateDashboard(ctx, dashboard) {
            ctx.commit('updateDashboard', dashboard)
        }
    },
    mutations: {
        updateToken (state, token) {
            state.token = token
        },
        clearToken (state, token) {
            state.token = null
        },
        updateDashboard(state, dashboard) {
            state.dashboard = dashboard
        }
    }
})
