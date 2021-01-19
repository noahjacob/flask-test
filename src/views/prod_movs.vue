<template>
  <div>
    <v-card class="mx-16 my-7">
      <v-card-title>
        <v-container>
          <v-row class="mb-4"> Report </v-row>
          <v-row class="mb-1">
            <v-text-field
              v-model="search"
              @change="check"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
              style="max-width: 250px"
            ></v-text-field>
          </v-row>
        </v-container>
      </v-card-title>
      <v-data-table :headers="headers" :items="prod_loc" :search="search">
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-container>
              <v-row>
                <v-form ref="lcheck" v-model="lcheck">
                  <v-combobox
                    v-model="location"
                    :items="locations"
                    @change="getProducts()"
                    item-text="name"
                    :rules="[(v) => !!v || ' Please select a location']"
                    label="Select a Location"
                    color="#5E64FF"
                    return-object
                    autofocus
                    style="max-width: 250px"
                  ></v-combobox>
                </v-form>
                <v-spacer></v-spacer>
                <v-dialog v-model="idialog" max-width="500px">
                  <template v-slot:activator="{ on }">
                    <v-btn color="green" dark :disabled="!lcheck" v-on="on">
                      Import
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>
                      <span>Import</span>
                    </v-card-title>
                    <v-card-text>
                      <v-form ref="imp" v-model="valid" lazy-validation>
                        <v-container>
                          <v-row>
                            <v-combobox
                              v-model="p_select"
                              :items="products"
                              ref="test"
                              item-text="name"
                              label="Select a Product"
                              :rules="[
                                (v) => !!v || ' Please select a product',
                              ]"
                              color="#5E64FF"
                              return-object
                              autofocus
                            ></v-combobox>
                          </v-row>
                          <v-row>
                            <v-text-field
                              v-model="quant"
                              label="Quantity"
                              :rules="[rules.qi]"
                              class="my-5"
                            >
                            </v-text-field>
                          </v-row>
                        </v-container>
                      </v-form>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="close">
                        Cancel
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        :disabled="!valid"
                        @click="save('imp')"
                      >
                        import
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <v-dialog v-model="edialog" max-width="500px">
                  <template v-slot:activator="{ on }">
                    <v-btn
                      color="red"
                      dark
                      class="mx-4"
                      :disabled="!lcheck"
                      v-on="on"
                    >
                      export
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>
                      <span>Export</span>
                    </v-card-title>
                    <v-card-text>
                      <v-form ref="exp" v-model="valid" lazy-validation>
                        <v-container>
                          <v-row>
                            <v-combobox
                              v-model="ep_select"
                              :items="prod_loc"
                              item-text="name"
                              label="Select a Product"
                              :rules="[
                                (v) => !!v || ' Please select a product',
                              ]"
                              color="#5E64FF"
                              return-object
                              autofocus
                            ></v-combobox>
                          </v-row>
                          <v-row>
                            <v-text-field
                              v-model="quant"
                              label="Quantity"
                              :rules="[rules.qi1]"
                              class="my-5"
                            >
                            </v-text-field>
                          </v-row>
                        </v-container>
                      </v-form>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="close">
                        Cancel
                      </v-btn>
                      <v-btn
                        :disabled="!valid"
                        color="blue darken-1"
                        text
                        @click="save('export')"
                      >
                        export
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <v-dialog v-model="mdialog" max-width="500px">
                  <template v-slot:activator="{ on }">
                    <v-btn color="#ffc400" dark v-on="on" :disabled="!lcheck">
                      Transfer
                    </v-btn>
                  </template>
                  <v-form ref="mov" v-model="valid" lazy-validation>
                    <v-card>
                      <v-card-title>
                        <span>Transfer</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-combobox
                              v-model="ep_select"
                              :items="prod_loc"
                              item-text="name"
                              label="Select a Product"
                              :rules="[
                                (v) => !!v || ' Please select a product',
                              ]"
                              color="#5E64FF"
                              return-object
                              autofocus
                            ></v-combobox>
                          </v-row>
                          <v-row>
                            <v-combobox
                              v-model="loc_select"
                              :items="loc_ops"
                              class="my-3"
                              item-text="name"
                              label="Select a location"
                              :rules="[
                                (v) => !!v || ' Please select a location',
                              ]"
                              color="#5E64FF"
                              required
                              return-object
                            ></v-combobox>
                          </v-row>
                          <v-row>
                            <v-text-field
                              v-model="quant"
                              label="Quantity"
                              :rules="[rules.qi1]"
                              class="my-5"
                            >
                            </v-text-field>
                          </v-row>
                        </v-container>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close">
                          Cancel
                        </v-btn>
                        <v-btn
                          :disabled="!valid"
                          color="blue darken-1"
                          text
                          @click="save('move')"
                        >
                          move
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-form>
                </v-dialog>
              </v-row>
            </v-container>
          </v-toolbar>
        </template>
      </v-data-table>
      <v-snackbar v-model="snackbar" color="dark" :top="true" :timeout="3000">
        {{ text }}

        <v-btn dark text @click="snackbar = false" class="ml-16"> Close </v-btn>
      </v-snackbar>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      idialog: false,
      edialog: false,
      mdialog: false,
      search: "",
      lcheck: true,
      valid: true,
      snackbar: false,
      text: "",
      location: "",
      loc_ops: [],
      p_select: "",
      loc_select: "",
      ep_select: "",
      quant: "",
      path: "",
      ip: "",
      locations: [],
      products: [],
      headers: [
        { text: "ID", value: "id", filterable: false },
        { text: "Name", value: "name" },
        { text: "Qty", value: "Qty" },
      ],
      prod_loc: [],
      rules: {
        qi: (value) => {
          return parseInt(value) > 0 || "Please enter a number greater than 0";
        },
        qi1: (value) => {
          return (
            (parseInt(value) > 0 && parseInt(value) <= this.ep_select.Qty) ||
            `Max Amount : ${this.ep_select.Qty} `
          );
        },
      },
    };
  },

  methods: {
    getProducts() {
      const location = this.location.id;

      this.loc_ops = this.locations.slice();
      for (var i = 0; i < this.loc_ops.length; i++) {
        if (this.loc_ops[i].id == this.location.id) {
          this.loc_ops.splice(i, 1);
        }
      }

      axios
        .get(`/movements/getProducts`, { params: { location: location } })
        .then((res) => {
          this.prod_loc = res.data;
          console.log(res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    save(type) {
      console.log(type);
      if (type == "imp") {
        const type = "import";
        const to_loc = this.location.id;
        const pid = this.p_select.id;
        const quant = this.quant;
        const cur_loc = this.location.id;
        axios
          .post(`/movements/import`, { type, to_loc, pid, quant, cur_loc })
          .then((res) => {
            this.prod_loc = res.data;
            this.text = "Successfully Imported";
            this.snackbar = true;
            this.idialog = false;
            this.$refs.imp.resetValidation();
            this.clear();
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsucessfully Imported";
            this.snackbar = true;
            this.$refs.imp.resetValidation();
            this.clear();
          });
        this.idialog = false;
        this.$refs.imp.resetValidation();
      } else if (type == "export") {
        const type = "export";
        const from_loc = this.location.id;
        const pid = this.ep_select.id;
        const quant = this.quant;
        const cur_loc = this.location.id;
        axios
          .post(`/movements/export`, {
            type,
            from_loc,
            pid,
            quant,
            cur_loc,
          })
          .then((res) => {
            this.prod_loc = res.data;
            this.text = "Successfully Exported";
            this.snackbar = true;
            this.$refs.exp.resetValidation();
            this.clear();
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsucessfully Imported";
            this.snackbar = true;
            this.$refs.exp.resetValidation();
            this.clear();
          });
        this.edialog = false;
        this.$refs.exp.resetValidation();
      } else {
        const type = "move";
        const from_loc = this.location.id;
        const pid = this.ep_select.id;
        const quant = this.quant;
        const to_loc = this.loc_select.id;
        const cur_loc = this.location.id;
        axios
          .post(`/movements/move`, {
            type,
            from_loc,
            to_loc,
            pid,
            quant,
            cur_loc,
          })
          .then((res) => {
            this.prod_loc = res.data;
            this.text = "Successfully Transfered";
            this.snackbar = true;
            this.$refs.mov.resetValidation();
            this.clear();
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsucessfully Transfered";
            this.snackbar = true;
          });
        this.mdialog = false;
        this.$refs.mov.resetValidation();
      }
    },

    clear() {
      this.p_select = "";
      this.ep_select = "";
      this.quant = 0;
      this.loc_select = "";
    },
    close() {
      this.text = "";
      this.p_select = "";
      this.ep_select = "";
      this.loc_select = "";
      this.idialog = false;
      this.edialog = false;
      this.mdialog = false;
      this.$refs.imp.resetValidation();
      this.$refs.mov.resetValidation();
      this.$refs.exp.resetValidation();
    },

    init() {
      axios
        .get(`/getLocations`)
        .then((res) => {
          this.locations = res.data;
          axios
            .get(`/getProducts`)
            .then((res) => {
              this.products = res.data;
            })
            .catch((err) => {
              console.error(err);
            });
        })
        .catch((err) => {
          console.error(err);
        });
    },
    check() {
      console.log(this.search);
    },
  },
  created() {
    this.init();
  },
};
</script>