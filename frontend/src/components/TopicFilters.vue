<template>
  <v-container>
    <v-checkbox v-model="selectedFilter" label="Education" id="education-filter" value="education"></v-checkbox>
    <v-checkbox v-model="selectedFilter" label="Environment" id="environment-filter" value="environment"></v-checkbox>
    <v-checkbox v-model="selectedFilter" label="Healthcare" id="healthcare-filter" value="healthcare"></v-checkbox>
    <v-checkbox v-model="selectedFilter" label="Politics" id="politics-filter" value="politics"></v-checkbox>
    <v-checkbox v-model="selectedFilter" label="Technology" id="technology-filter" value="technology"></v-checkbox>
    <v-checkbox v-model="selectedFilter" label="Select All" id="select-all-filter" value="select-all"></v-checkbox>
    <v-btn depressed color="primary" @click="applyFilters">Apply</v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'TopicFilters',
  data() {
    return {
      selectedFilter: []
    }
  },
  methods: {
    applyFilters() {
      console.log(this.selectedFilter)
    }
  }
}
</script>
