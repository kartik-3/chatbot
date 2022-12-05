<template>
  <v-container>
    <div class="chat">
      <div v-for="(item, index) in chat" :key="index" class="mt-64 mb-5">
        <v-row class="mb-11">
          <v-col cols="6" align="left">
            <v-avatar v-if="item.from == 'bot'" color="red" size="36">
              <div class="white--text">{{ item.from }}</div>
            </v-avatar>
            <div v-if="item.from == 'bot'" class="red--text ml-3" style="word-break: break-word;">{{ item.msg }}</div>
          </v-col>
          <v-col cols="6" align="right">
            <v-avatar v-if="item.from == 'user'" color="blue" size="36">
              <div class="white--text">{{ item.from }}</div>
            </v-avatar>
            <div v-if="item.from == 'user'" class="blue--text mr-3" style="word-break: break-word;">{{ item.msg }}</div>
          </v-col>
        </v-row>
      </div>
    </div>
    <v-footer fixed>
      <v-container class="ma-0 pa-0">
        <v-row no-gutters>
          <v-col>
            <div class="d-flex flex-row align-center">
              <v-text-field v-model="msg" placeholder="Type Something" @keypress.enter="send"></v-text-field>
              <v-btn icon class="ml-4" @click="send">
                <v-icon>mdi-send</v-icon>
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { getQueryResponse } from "../utils/api";

export default {
  name: 'ChatBox',
  components: {
  },
  data() {
    return {
      msg: "",
      botResponse: ""
    }
  },
  computed: {
    ...mapState('chat', ['chat'])
  },
  methods: {
    ...mapActions('chat', ['updateChat']),
    async send() {
      if (!this.msg) {
        return
      }
      this.updateChat({
        from: "user",
        msg: this.msg,
      })
      const queryResponse = await getQueryResponse({ "text": this.msg })
      this.msg = ""
      this.botResponse = queryResponse.data.response
      this.addReply()
    },
    addReply() {
      this.updateChat({
        from: "bot",
        msg: this.botResponse,
      })
      this.scrollToElement()
    },
    scrollToElement() {
      window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
    }
  }
}
</script>

<style>
.chat {
  margin-bottom: 176px;
}
</style>