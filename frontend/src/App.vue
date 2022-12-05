<template>
  <v-app>
    <v-app-bar app dark height="75px">
      <v-img src="../assets/ir_cb_logo.png" max-height="60px" max-width="175px"></v-img>
    </v-app-bar>
    <v-main class="ma-0">
      <Grid />
    </v-main>
  </v-app>
</template>

<script>
import Grid from './components/Grid';

export default {
  name: 'App',

  components: {
    Grid
  },

  data: () => ({
  }),
};
</script>
