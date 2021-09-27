<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="12">
      <v-card class="py-4">
        <v-data-table
          :headers="headers"
          :items="tasks"
          item-key="title"
          sort-by="start_time"
          class="elevation-1"
          :search="search"
          :custom-filter="filterOnlyLowText"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-row>
                <v-col cols="12" sm="4" md="4">
                  <v-toolbar-title>All Tracked Tasks</v-toolbar-title>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-dialog
                    ref="dialogPickerDateToFilter"
                    v-model="dialogPickerDateToFilterStatus"
                    :return-value.sync="dateToFilter"
                    width="290px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="dateToFilter"
                        label="Date"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="dateToFilter" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn
                        text
                        color="primary"
                        @click="dialogPickerDateToFilterStatus = false"
                      >
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="
                          $refs.dialogPickerDateToFilter.save(dateToFilter)
                          changeDate()
                        "
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-dialog>
                </v-col>
              </v-row>

              <v-spacer></v-spacer>
              <h5>Total Duration: {{ totalDuration }}</h5>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-dialog v-model="dialog" max-width="80vw">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="primary"
                    dark
                    class="mb-2"
                    v-bind="attrs"
                    v-on="on"
                    @click="initDialog"
                  >
                    New Task
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" sm="6" md="6">
                          <v-text-field
                            v-model="editedItem.title"
                            label="Task Name"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6">
                          <v-menu
                            ref="datePicker"
                            v-model="datePicker"
                            :close-on-content-click="false"
                            :return-value.sync="editedItem.task_date"
                            transition="scale-transition"
                            offset-y
                            min-width="auto"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-text-field
                                v-model="editedItem.task_date"
                                label="Task Date"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                              ></v-text-field>
                            </template>
                            <v-date-picker
                              v-model="editedItem.task_date"
                              no-title
                              scrollable
                            >
                              <v-spacer></v-spacer>
                              <v-btn
                                text
                                color="primary"
                                @click="datePicker = false"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                text
                                color="primary"
                                @click="
                                  $refs.datePicker.save(editedItem.task_date)
                                "
                              >
                                OK
                              </v-btn>
                            </v-date-picker>
                          </v-menu>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                          style="width: 350px; flex: 0 1 auto"
                        >
                          <h3>Start Time:</h3>
                          <v-time-picker
                            v-model="editedItem.start_time"
                            :max="editedItem.end_time"
                          ></v-time-picker>
                        </v-col>
                        <v-col
                          cols="12"
                          sm="6"
                          md="4"
                          style="width: 350px; flex: 0 1 auto"
                        >
                          <h3>End Time:</h3>
                          <v-time-picker
                            v-model="editedItem.end_time"
                            :min="editedItem.start_time"
                          ></v-time-picker>
                        </v-col>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="durationCounter"
                            label="Duration (hh:mm:ss)"
                            readonly
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">
                      Cancel
                    </v-btn>
                    <v-btn color="blue darken-1" text @click="save">
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="text-h5"
                    >Are you sure you want to delete this item?</v-card-title
                  >
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDelete"
                      >Cancel</v-btn
                    >
                    <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                      >OK</v-btn
                    >
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)">
              mdi-pencil
            </v-icon>
            <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
          </template>
          <template v-slot:no-data> There is no task in this date </template>
          <template v-slot:[`body.append`]>
            <tr>
              <td>
                <v-text-field
                  v-model="search"
                  label="Search (LOWER CASE ONLY)"
                  class="mx-4"
                ></v-text-field>
              </td>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <v-text-field
                  v-model="durationFilter"
                  type="number"
                  label="Longer than"
                ></v-text-field>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from 'vue'

interface IData {
  id: number
  title: string
  task_date: string
  start_time: string
  end_time: string
  duration: number
}

export default Vue.extend({
  name: 'MainComp',
  data() {
    let tasks: IData[] = []
    return {
      durationFilter: 0,
      search: '',
      dateToFilter: '',
      dialogPickerDateToFilterStatus: false,
      totalDuration: '0',
      datePicker: false,
      dialog: false,
      dialogDelete: false,
      tasks,
      editedIndex: -1,
      editedItem: {
        id: -1,
        title: 'Default Task Name',
        task_date: new Date().toISOString().slice(0, 10),
        start_time: '',
        end_time: '',
        duration: 0,
      },
      defaultItem: {
        id: -1,
        title: 'Default Task Name',
        task_date: new Date().toISOString().slice(0, 10),
        start_time: '',
        end_time: '',
        duration: 0,
      },
    }
  },

  computed: {
    headers() {
      return [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'title',
        },
        { text: 'Date', value: 'task_date' },
        { text: 'Start', value: 'start_time' },
        { text: 'End', value: 'end_time' },
        { 
          text: 'Duration (in Sec)', 
          value: 'duration',
          filter: (value: number) => {
            if (!this.durationFilter) return true
            return value > this.durationFilter
          },
        },
        { text: 'Actions', value: 'actions', sortable: false },
      ]
    },
    formTitle(): string {
      return this.editedIndex === -1 ? 'New Task' : 'Edit Task'
    },
    durationCounter(): string {
      const diff =
        new Date(
          '1970-01-01 ' + this.editedItem.end_time.slice(0, 5)
        ).getTime() -
        new Date(
          '1970-01-01 ' + this.editedItem.start_time.slice(0, 5)
        ).getTime()
      this.updateDuration(diff)
      return new Date(new Date().getTimezoneOffset() * 60000 + diff)
        .toLocaleTimeString('en-GB')
        .slice(0, 5)
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  created() {
    this.dateToFilter = new Date().toISOString().slice(0, 10)
    this.initialize()
  },

  methods: {
    filterOnlyLowText(value: string, search: string, item: IData[]) {
      return value != null &&
        search != null &&
        typeof value === 'string' &&
        value.toString().toLocaleLowerCase().indexOf(search) !== -1
    },
    updateDuration(diff: number) {
      this.editedItem.duration = diff / 1000
    },

    async initialize() {
      const ip = await this.$axios.$get(
        '/api/v1/tasks/date/' + this.dateToFilter
      )
      this.tasks = ip

      if (typeof this.tasks === 'object') {
        const totalDurationInSec =
          this.tasks.reduce((total, val) => total + val.duration, 0) * 1000
        this.totalDuration = new Date(
          new Date().getTimezoneOffset() * 60000 + totalDurationInSec
        )
          .toLocaleTimeString('en-GB')
          .slice(0, 5)
      }
    },

    changeDate() {
      this.editedItem.task_date = this.dateToFilter
      this.defaultItem.task_date = this.dateToFilter
      this.initialize()
    },

    editItem(item: IData) {
      this.editedIndex = this.tasks.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item: IData) {
      this.editedIndex = this.tasks.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    async deleteItemConfirm() {
      await this.$axios.$delete(
        '/api/v1/tasks/' + this.editedItem.id
      )
      this.closeDelete()
    },

    initDialog() {
      if (this.editedIndex === -1) {
        this.editedItem.start_time =
          new Date().toLocaleTimeString('en-GB').slice(0, 5) + ':00'
        this.editedItem.end_time =
          new Date().toLocaleTimeString('en-GB').slice(0, 5) + ':00'
      }
    },

    close() {
      this.initialize()
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete() {
      this.initialize()
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    async save() {
      this.editedItem.start_time =
        this.editedItem.start_time.slice(0, 5) + ':00'
      this.editedItem.end_time = this.editedItem.end_time.slice(0, 5) + ':00'

      if (this.editedIndex > -1) {
        await this.$axios.$put(
          '/api/v1/tasks/' + this.editedItem.id,
          this.editedItem
        )
      } else {
        await this.$axios.$post(
          '/api/v1/tasks/',
          this.editedItem
        )
      }
      this.close()
    },
  },
})
</script>