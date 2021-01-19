<template lang="html">
<v-container fill-height fluid>
  <v-row align="center" justify="center" id="home">
    <h2>Component Buttons</h2>
    
  </v-row>
  <v-row align="center" justify="center" >
    
    <btn title="Default" >

      </btn>
      
      
    <btn title="primary" variant = "primary"   >

      </btn>
      
      
    <btn title="error" variant = "error"  >

      </btn>

      <btn title="disabled" variant = "disabled"  >

      </btn>
      
    </v-row>

  
  </v-container>
</template>

<script>
import button from "../components/button.vue";
export default {
  components: {
    btn: button,
  },
  
};
</script>

