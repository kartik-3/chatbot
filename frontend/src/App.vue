<template>
  <v-app>
    <v-app-bar app dark height="75px">
      <v-img src="../assets/ir_cb_logo.png" max-height="60px" max-width="175px" style="margin-right: 50px"></v-img>
      <v-btn-toggle>
        <a style="text-decoration: none; margin-right: 20px;"
          href="https://app.powerbi.com/view?r=eyJrIjoiNDBjYTM0MGUtMmQ4Zi00MTczLWJlNjYtYTE4MjkyMTMzMGVmIiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9&pageName=ReportSection"
          target="_blank">
          <v-btn depressed color="green lighten-2">Comments Data Visualization
          </v-btn>
        </a>
        <a style="text-decoration: none;"
          href="https://app.powerbi.com/view?r=eyJrIjoiNDk5NTljNGYtZTc0Yi00ODFlLTgzOTgtMWRhNzUwMTNiZGRlIiwidCI6Ijk2NDY0YThhLWY4ZWQtNDBiMS05OWUyLTVmNmI1MGEyMDI1MCIsImMiOjN9&pageName=ReportSection"
          target="_blank">
          <v-btn depressed color="blue lighten-2">Submissions Data Visualization
          </v-btn>
        </a>
      </v-btn-toggle>
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
