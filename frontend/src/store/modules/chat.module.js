const state = {
  chat: [],
};

const mutations = {
  SET_CHAT(state, value) {
    state.chat.push(value);
  },
};

const actions = {
  updateChat({ commit }, payload) {
    commit("SET_CHAT", payload);
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
