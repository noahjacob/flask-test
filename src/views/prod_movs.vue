<template>
  <div >
  <v-card class = "mx-16 mt-7">
    <v-card-title>
      Report
    </v-card-title>
    <v-container>
        <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        class="mb-2 ml-1"
        style="max-width:250px"
      ></v-text-field>
        </v-container>
    <v-data-table
      :headers="headers"
      :items="prod_loc"
      :search="search"
    >
    <template v-slot:top>
        

        
      <v-toolbar flat color="white">
          <v-container>
          <v-row>
          <v-form
          ref="lcheck"
          v-model="lcheck">
        <v-combobox
              v-model="location"
              :items="locations"
              @change="getProducts()"
              item-text="name"
              :rules="[v => !!v || ' Please select a location']"
            
              label="Select a Location"
              color="#5E64FF"
              return-object
              autofocus
              style="max-width:250px"
            ></v-combobox>
          </v-form>
      <v-spacer></v-spacer>
      <v-dialog v-model="idialog" max-width="500px">
        <template v-slot:activator="{on}">
          <v-btn
              color="green"
              dark
              :disabled="!lcheck"
              v-on="on"
              
            >
              Import
            </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span >Import</span>
          </v-card-title>
          <v-card-text>
              <v-form
              ref="imp"
              v-model="valid"
              lazy-validation
              >
            <v-container>
            
                <v-row>
                <v-combobox
              v-model="p_select"
              :items="products"
              ref="test"
              item-text="name"
              label="Select a Product"
              :rules= "[rules.p]"
              
              color="#5E64FF"
              
              return-object
              autofocus
              
            ></v-combobox>
                    
                </v-row>
                <v-row>
                    <v-text-field
                    v-model="quant"
                    label="Quantity"
                    :rules= "[rules.qi]"
                    class="my-5">

                    </v-text-field>
                </v-row>
                
            </v-container>
             </v-form>
           
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="iclose"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                :disabled = "!valid"
                @click="isave"
              >
                IMPORT
              </v-btn>
            </v-card-actions>
        </v-card>

      </v-dialog>
      




      <v-dialog v-model="edialog" max-width="500px">
        <template v-slot:activator="{on}">
          <v-btn
              color="red"
              dark
              class= "mx-4"
              :disabled="!lcheck"
              v-on="on"
              
            >
              Export
            </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span >Export</span>
          </v-card-title>
          <v-card-text>
              <v-form
              ref="exp"
              v-model="valid"
              lazy-validation
              >
            <v-container>
            
                <v-row>
                <v-combobox
              v-model="ep_select"
              :items="prod_loc"
              
              item-text="name"
              label="Select a Product"
              :rules= "[rules.ep]"
              
              color="#5E64FF"
              
              return-object
              autofocus
              
            ></v-combobox>
                    
                </v-row>
                <v-row>
                    <v-text-field
                    v-model="quant"
                    label="Quantity"
                    :rules= "[rules.qi1]"
                    class="my-5">

                    </v-text-field>
                </v-row>
                
            </v-container>
             </v-form>
           
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="eclose"
              >
                Cancel
              </v-btn>
              <v-btn
                :disabled = "!valid"
                color="blue darken-1"
                text
                @click="esave"
              >
                EXPORT
              </v-btn>
            </v-card-actions>
        </v-card>

      </v-dialog>




      <v-dialog v-model="mdialog" max-width="500px">
        <template v-slot:activator="{on}">
          <v-btn
              color="#ffc400"
              dark
              
              
              v-on="on"
              :disabled="!lcheck"
              
            >
              Transfer
            </v-btn>
        </template>
         <v-form
              ref="mov"
              v-model="valid"
              lazy-validation
              >
        <v-card>
          <v-card-title>
            <span >Transfer</span>
          </v-card-title>
          <v-card-text>
             
            <v-container>
            
                <v-row>
                <v-combobox
              v-model="ep_select"
              :items="prod_loc"
              
              item-text="name"
              label="Select a Product"
              :rules= "[rules.ep]"
              
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
              
              :rules= "[rules.l_check]"
              color="#5E64FF"
              required
              return-object
              
              
            ></v-combobox>
                    
                </v-row>
                <v-row>
                    <v-text-field
                    v-model="quant"
                    label="Quantity"
                    :rules= "[rules.qi1]"
                    class="my-5">

                    </v-text-field>
                </v-row>
                
            </v-container>
             
           
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="mclose"
              >
                Cancel
              </v-btn>
              <v-btn
                :disabled ="!valid"
                color="blue darken-1"
                text
                @click="msave"
              >
                MOVE
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
    <v-snackbar v-model="snackbar" color="dark" :top="true" :timeout="3000" >
      {{ text }}
      
      <v-btn dark text @click="snackbar = false" class="ml-16">
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


      idialog:false,
      edialog:false,
      mdialog:false,
      search: "",
      lcheck:true,
      valid:true,
      snackbar: false,
      text: "",
      location: "" ,
      loc_ops: [],
      p_select:"",
      loc_select:"",
      ep_select:"",
      quant:0,
      path:"",

      locations: [],
      products: [],
      headers: [
        { text: "ID", value: "id", filterable: false },
        { text: "Name", value: "name" },
        {text:"Qty", value:"Qty"},
      ],
      prod_loc: [],
      rules: {
        qi: (value) => {
            return (
            ( parseInt(value)>0 ||
            "Please enter a number greater than 0" )
          );
        },
        qi1: (value) => {
            return (
            ( parseInt(value)>0 && parseInt(value)<=this.ep_select.Qty||
            `Max Amount : ${this.ep_select.Qty} ` )
          );
        },
         p: ()=>{
            if(this.p_select===""){
                return "Please eneter a product"
            }
        },
        ep: ()=>{
            if(this.ep_select===""){
                return "Please enter a product"
            }
        },
        l_check: ()=>{
            if(this.loc_select===""){
                return "Please enter a location"
            }
        },
      },
      
    };
  },
  
  methods:{
    getProducts(){
    //   const path = 'http://localhost:5000//movements/getProducts';
      console
      const location = this.location.id

      this.loc_ops = this.locations.slice()
      for (var i=0;i < this.loc_ops.length;i++){
          if(this.loc_ops[i].id == this.location.id ){
              this.loc_ops.splice(i,1)
          }
        


      }

      axios.post('http://localhost:5000//movements/getProducts',{location})
        .then((res=>{
            // console.log(res.data)
            this.prod_loc = res.data;
            console.log(this.location)
          
          
        }))
          .catch((err)=>{
            console.error(err);
          }
        )

    },
    isave(){
        if(this.location ===  ""){
            this.text = "Please select a location"
            this.snackbar = true
            this.clear()
            this.idialog =false
            
            this.$refs.imp.resetValidation()
            return;
            }
            if(!this.$refs.imp.validate()){
            this.text = "Some fields were invalid"
            this.snackbar = true
            this.clear()
            this.idialog =false
            
            this.$refs.imp.resetValidation()
            return
            }
            const type = "import"
            const to_loc=this.location.id
            const pid=this.p_select.id
            const quant = this.quant
            const path=this.path
            const cur_loc = this.location.id
            axios.post(`${path}/movements/import`,{type,to_loc,pid,quant,cur_loc})
                .then((res)=>{
                    this.prod_loc = res.data
                    this.text="Successfully Imported"
                    this.snackbar=true
                    
                    this.clear()
                })
                .catch((err)=>{
                    console.log(err)
                    this.text="Unsucessfully Imported"
                    this.snackbar=true
                    
                });
            this.idialog=false
            this.$refs.imp.resetValidation()
            



    },
    esave(){
        if(this.location ===  ""){
            this.text = "Please select a location"
            this.snackbar = true
            this.clear()
            this.edialog =false
            this.$refs.exp.resetValidation()
            return;
            }
            const type = "export"
            const from_loc=this.location.id
            const pid=this.ep_select.id
            const quant = this.quant
            const path=this.path
            const cur_loc = this.location.id
            axios.post(`${path}/movements/export`,{type,from_loc,pid,quant,cur_loc})
                .then((res)=>{
                    this.prod_loc = res.data
                    this.text="Successfully Exported"
                    this.snackbar=true
                    this.clear()
                })
                .catch((err)=>{
                    console.log(err)
                    this.text="Unsucessfully Imported"
                    this.snackbar=true
                    
                });
            this.edialog=false
            this.$refs.exp.resetValidation()

    },
    msave(){
        if(this.location ===  ""){
            this.text = "Please select a location"
            this.snackbar = true
            this.clear()
            this.edialog =false
            this.$refs.mov.resetValidation()
            return;}
            const type="move"
            const from_loc=this.location.id
            const pid=this.ep_select.id
            const quant = this.quant
            const to_loc = this.loc_select.id
            const path=this.path
            const cur_loc = this.location.id
            axios.post(`${path}/movements/move`,{type,from_loc,to_loc,pid,quant,cur_loc})
                .then((res)=>{
                    this.prod_loc = res.data
                    this.text="Successfully Transfered"
                    this.snackbar=true
                    
                    this.clear()
                })
                .catch((err)=>{
                    console.log(err)
                    this.text="Unsucessfully Transfered"
                    this.snackbar=true
                    
                });
            this.mdialog=false
            this.$refs.mov.resetValidation()
             
           

    },
    reset(){
        this.$refs.imp.resetValidation()
        this.$refs.mov.resetValidation()

    },
    
    clear(){
        this.p_select=""
        this.ep_select=""
        this.quant=0

    },
    iclose(){
        this.text = ""
        this.p_select=""
        this.idialog = false
        this.$refs.imp.resetValidation()
    },
    mclose(){
        this.text = ""
        this.ep_select=""
        this.loc_select=""
        this.mdialog = false
        this.$refs.mov.resetValidation()
    },
    eclose(){
        this.text = ""
        this.ep_select=""
        this.$refs.exp.resetValidation()
        this.edialog = false
        
    },

    init(){
      const path = 'http://localhost:5000/getLocations';
      const path1= 'http://localhost:5000/getProducts';
      axios.get(path)
        .then((res=>{
          this.locations = res.data;
          axios.get(path1)
        .then((res=>{
          this.products = res.data;
          
        }))
          .catch((err)=>{
            console.error(err);
          }
        )
          
        }))
          .catch((err)=>{
            console.error(err);
          }
        )

    },
    check(){
        if(this.location ===  ""){
            this.text = "Please select a location"
            this.snackbar = true
            this.clear()
            this.$refs.form.resetValidation()
           
            this.idialog =false
            return;
            }

    }
          
    },
  created(){
      
      this.path = "http://localhost:5000"
      this.init();
    //   this.getProducts();
    //   console.log(this.locations)
      
          console.log(this.p_select)
      
    },
    
  };

</script>