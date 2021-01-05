<template>
  <div >
  <v-card class = "mx-16 my-7">
    <v-card-title>
      Products
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="products"
      :search="search"
    >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        class=" my-5"
        style="max-width:300px"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <template v-slot:activator="{on}">
          <v-btn
              color="primary"
              dark
              
              v-on="on"
            >
              New Item
            </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">{{formtitle}}</span>
          </v-card-title>
          <v-card-text>
            <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.category"
                      label="Category"
                    ></v-text-field>
                  </v-col>
                </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
        </v-card>

      </v-dialog>
      <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title >Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-toolbar>

    </template>

    <template v-slot:[`item.action`] ="{ item }">
       
        <v-icon small class="mr-3" @click="editItem(item)"> edit </v-icon>
        <v-icon small @click="deleteItem(item)"> delete </v-icon>
    </template>
    </v-data-table>
    <v-snackbar v-model="snackbar" color="dark" :top="true" :timeout="2000" >
      {{ text }}
      
      <v-btn dark text @click="snackbar = false" class="ml-3">
        Close
      </v-btn>
    </v-snackbar>
    
  </v-card>
  </div>
  
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      
      search: "",
      snackbar: false,
      text: "",
      ip: "",
      dialog: false,
      headers: [
        { text: "ID", value: "id", filterable: false },
        { text: "Name", value: "name" },
        { text: "Category", value: "category", filterable: false },
        {
          text: "Actions",
          value: "action",
          sortable: false,
          filterable: false,
        },
      ],
      products: [],
      editedIndex: -1,
      editedItem: {
        name: "",
        category: "",
      },
      defaultItem: {
        name: "",
        category: "",
      },
    };
  },
  
  methods:{
    getProducts(){
      const path = 'http://localhost:5000/getProducts';
      axios.get(path)
        .then((res=>{
          this.products = res.data;
          console.log(res.data)
          
        }))
          .catch((err)=>{
            console.error(err);
          }
        )

    },
    close() {
      this.dialog = false;
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;
    },
    closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

    editItem (item) {
        this.editedIndex = this.products.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },
      deleteItem (item) {
        this.editedIndex = this.products.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },
      deleteItemConfirm () {
        this.products.splice(this.editedIndex, 1)
        const product = this.editedItem;
        axios
          .post('http://localhost:5000/delProduct', product)
          .then((res) => {
            this.products = res.data;
            this.text = "Successfully deleted product";
            this.snackbar = true;
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsuccessfully deleted product";
            this.snackbar = true;
          });
        
        this.closeDelete()
      },
      save() {
      if (this.editedIndex > -1) {
        const product = this.editedItem;
        
        axios
          .post('http://localhost:5000/editProduct', product)
          .then((res) => {
            this.products = res.data;
            this.text = "Successfully edited product";
            this.snackbar = true;
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsuccessfully edited product";
            this.snackbar = true;
          });
      } else {
        const product = this.editedItem;
        
        axios
          .post('http://localhost:5000/addProduct', product)
          .then((res) => {
            this.products = res.data;
            this.text = "Successfully added product";
            this.snackbar = true;
          })
          .catch((err) => {
            console.log(err);
            this.text = "Unsuccessfully added product";
            this.snackbar = true;
          });
      }
      this.editedItem = Object.assign({}, this.defaultItem);
      this.dialog = false;
    },
  },
  computed: {
      formtitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },
  created(){
    this.getProducts();
      
    },
    
  };

</script>