import Vue from 'vue'
import Vuex from 'vuex'
import shared from './Shared'
import user from './User'


Vue.use(Vuex)

export const store = new Vuex.Store({
  modules:{
    shared: shared,
    user: user
  }
})
