<template>
  <v-app>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      flat
      color="white"
      app
      hide-on-scroll
      dense
      style="padding-left: 10vw;padding-right: 10vw"
    >
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn plain text to="/">
        All Tasks
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang='ts'>
import Vue from 'vue'
export default Vue.extend({
  data () {
    return {
      clipped: true,
      drawer: false,
      fixed: false,
      right: true,
      rightDrawer: false,
      title: 'Time Tracking App'
    }
  }
})
</script>
