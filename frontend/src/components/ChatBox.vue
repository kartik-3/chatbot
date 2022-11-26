<template>
  <v-container>
    <!-- <v-row>
      <v-col cols="6" align="left">
        <chat-bubble />
      </v-col>
      <v-col cols="6" align="right">
        <chat-bubble />
      </v-col>
    </v-row> -->
    <!-- <v-row>
      <v-col cols="12"> -->
        <!-- <v-container class="fill-height"> -->
          <v-row class="fill-height pb-14" align="end">
            <v-col>
              <div v-for="(item, index) in user_chat" :key="index"
                :class="['d-flex flex-row align-center my-2', item.from == 'user' ? 'justify-end' : null]">
                <span v-if="item.from == 'user'" class="blue--text mr-3">{{ item.msg }}</span>
                <v-avatar :color="item.from == 'user' ? 'indigo' : 'red'" size="36">
                  <span class="white--text">{{ item.from[0] }}</span>
                </v-avatar>
                <span v-if="item.from != 'user'" class="blue--text ml-3">{{ item.msg }}</span>
              </div>
              <!-- <div v-for="(item, index) in user_chat" :key="index"
                :class="['d-flex flex-row align-center my-2 justify-end']">
                <span class="blue--text mr-3">{{ item.msg }}</span>
                <v-avatar color='indigo' size="36">
                  <span class="white--text">u</span>
                </v-avatar>
              </div>
              <div v-for="(item, index) in bot_chat" :key="index"
                :class="['d-flex flex-row align-center my-2', item.from == 'bot' ? 'justify-start' : null]">
                <span v-if="item.from == 'bot'" class="blue--text ml-3">{{ item.msg }}</span>
                <v-avatar :color="item.from == 'user' ? 'indigo' : 'red'" size="36">
                  <span class="white--text">{{ item.from[0] }}</span>
                </v-avatar>
              </div> -->
            </v-col>
          </v-row>
        <!-- </v-container> -->
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
      <!-- </v-col>
    </v-row> -->
  </v-container>
</template>

<script>
// import ChatBubble from './ChatBubble.vue';
// import ChatWindow from './ChatWindow.vue';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'ChatBox',
  components: {
    // ChatBubble
    // ChatWindow
  },
  data() {
    return {
      selectedFilter: [],
      chat: [
      ],
      msg: null,
    }
  },
  computed: {
    ...mapState('chat', ['user_chat', 'bot_chat'])
  },
  methods: {
    ...mapActions('chat', ['updateUserChat', 'updateBotChat']),
    applyFilters() {
      console.log(this.selectedFilter)
    },
    send() {
      this.updateUserChat(this.msg)
      this.msg = null
      this.addReply()
    },
    addReply() {
      let r = Math.random()
      this.updateBotChat("hi " + r)
      // console.log(this.chat)
    }
  }
}
</script>

/**

Fix enter when blank 

*/