<template>
  <v-app>
    <v-app-bar app color="primary" dark>
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
