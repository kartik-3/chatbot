const state = {
  chat: [],
  filters: {
    educationFilter: true,
    environmentFilter: true,
    healthcareFilter: true,
    politicFilter: true,
    technologyFilter: true,
    selectAllFilter: true,
  }
};

const mutations = {
  SET_CHAT(state, value) {
    state.chat.push(value);
  },
  SET_FILTER(state, value) {
    state.filters = value;
  },
};

const actions = {
  updateChat({ commit }, payload) {
    commit("SET_CHAT", payload);
  },
  updateFilters({ commit }, payload) {
    commit("SET_FILTER", payload);
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
