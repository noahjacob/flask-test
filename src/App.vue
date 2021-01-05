<template>
  <div  id="app">
    <head>
      <link
        href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons"
        rel="stylesheet"
      />
    </head>
    <v-app >
      <div>
        <v-toolbar color="#FF4081">
          <router-link :to="{ path: '/' }"
            ><v-toolbar-title class="white--text ml-16"
              >Inventory Tracking System</v-toolbar-title
            ></router-link
          >

          <v-spacer></v-spacer>

          <v-toolbar-items class="mx-16">
            <v-btn class="white--text" :to="{ path: '/products'}" text>Products</v-btn>
            <v-btn class="white--text" :to="{path: '/locations'}" text>Locations</v-btn>
            <v-btn class="white--text" :to="{path:'/prod_movs'}" text
              >Product Movements</v-btn
            >
          </v-toolbar-items>
        </v-toolbar>
        <router-view />
      </div>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  }),
};
</script>
<style>
a {
  
  text-decoration: none;
}
</style>