<template>
  <v-container class="d-flex flex-column">
    <v-checkbox v-model="educationFilter" label="Education" id="education-filter" :false-value="false"
      :true-value="true" @change="checkboxChanged"></v-checkbox>
    <v-checkbox v-model="environmentFilter" label="Environment" id="environment-filter" :false-value="false"
      :true-value="true" @change="checkboxChanged"></v-checkbox>
    <v-checkbox v-model="healthcareFilter" label="Healthcare" id="healthcare-filter" :false-value="false"
      :true-value="true" @change="checkboxChanged"></v-checkbox>
    <v-checkbox v-model="politicFilter" label="Politics" id="politics-filter" :false-value="false" :true-value="true"
      @change="checkboxChanged"></v-checkbox>
    <v-checkbox v-model="technologyFilter" label="Technology" id="technology-filter" :false-value="false"
      :true-value="true" @change="checkboxChanged"></v-checkbox>
    <v-checkbox v-model="selectAllFilter" label="Select All" id="select-all-filter" :false-value="false"
      :true-value="true" @click="selectAllChanged" :disabled="readOnlySelectAll"></v-checkbox>
    <v-btn depressed class="card-actions" color="primary" @click="applyFilters" :disabled="readOnlyApplyBtn">Apply
    </v-btn>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { updateFilters } from "../utils/api";

export default {
  name: 'TopicFilters',
  data() {
    return {
      totalSelected: 0,
      educationFilter: true,
      environmentFilter: true,
      healthcareFilter: true,
      politicFilter: true,
      technologyFilter: true,
      selectAllFilter: true,
      readOnlyApplyBtn: true,
      readOnlySelectAll: true,
      currentState: {}
    }
  },
  mounted() {
    this.educationFilter = this.filters.educationFilter
    this.environmentFilter = this.filters.environmentFilter
    this.healthcareFilter = this.filters.healthcareFilter
    this.politicFilter = this.filters.politicFilter
    this.technologyFilter = this.filters.technologyFilter
    this.selectAllFilter = this.filters.selectAllFilter
    this.totalSelected = 5

    this.changeCurrentState()
  },
  computed: {
    ...mapState('chat', ['filters'])
  },
  methods: {
    ...mapActions('chat', ['updateFilters']),
    async applyFilters() {
      this.updateFilters({
        educationFilter: this.educationFilter,
        environmentFilter: this.environmentFilter,
        healthcareFilter: this.healthcareFilter,
        politicFilter: this.politicFilter,
        technologyFilter: this.technologyFilter,
        selectAllFilter: this.selectAllFilter,
      })

      await updateFilters({
        "topics": {
          "education": this.filters.educationFilter,
          "environment": this.filters.environmentFilter,
          "healthcare": this.filters.healthcareFilter,
          "politics": this.filters.politicFilter,
          "technology": this.filters.technologyFilter,
          "all": this.filters.selectAllFilter
        }
      })

      this.readOnlyApplyBtn = true
      this.changeCurrentState()
    },
    checkboxChanged(e) {
      this.totalSelected += (e == false ? -1 : 1)
      if ((this.educationFilter && this.environmentFilter && this.healthcareFilter && this.politicFilter && this.technologyFilter)) {
        this.selectAllFilter = true
        this.readOnlySelectAll = true
      } else {
        this.selectAllFilter = false
        this.readOnlySelectAll = false
      }

      this.changeApplyBtnState()
    },
    selectAllChanged() {
      this.educationFilter = true
      this.environmentFilter = true
      this.healthcareFilter = true
      this.politicFilter = true
      this.technologyFilter = true
      this.readOnlySelectAll = true
      this.totalSelected = 5
      this.changeApplyBtnState()
    },
    changeApplyBtnState() {
      if (this.totalSelected > 0 &&
      (this.currentState.educationFilter != this.educationFilter ||
        this.currentState.environmentFilter != this.environmentFilter ||
        this.currentState.healthcareFilter != this.healthcareFilter ||
        this.currentState.politicFilter != this.politicFilter ||
        this.currentState.technologyFilter != this.technologyFilter ||
        this.currentState.selectAllFilter != this.selectAllFilter)
        ) {
        this.readOnlyApplyBtn = false
      } else {
        this.readOnlyApplyBtn = true
      }
    },
    changeCurrentState() {
      this.currentState = {
        educationFilter: this.educationFilter,
        environmentFilter: this.environmentFilter,
        healthcareFilter: this.healthcareFilter,
        politicFilter: this.politicFilter,
        technologyFilter: this.technologyFilter,
        selectAllFilter: this.selectAllFilter,
      }
    }
  }
}
</script>

<style scoped>
.card-actions {
  /* position: absolute; */
  top: 400px;
}
</style>