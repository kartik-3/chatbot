<template>
  <v-container class="ma-0" fluid>
    <v-row class="text-center">
      <!-- <v-col cols="2">
        1
      </v-col> -->
      <v-col cols="10">
        <ChatBox />
      </v-col>
      <v-col cols="2">
        <TopicFilters />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TopicFilters from './TopicFilters';
import ChatBox from './ChatBox';
export default {
  name: 'Grid',
  components: {
    TopicFilters,
    ChatBox
  },
}
</script>
