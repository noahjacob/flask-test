
<template>
  <button :style="btnstyle" >{{ title }}</button>
</template>>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "Test",
    },
    variant: String,
    click: { type: Function },
    disabled:{type:Boolean,default:false}
  },
  computed: {
    btnstyle() {
        if (this.variant == "disabled"||this.disabled == true) {
        return {
          cursor: "not-allowed",
          "pointer-events": "none",
          color: "#c0c0c0",
          "background-color": "#ffffff",
        };
      }else if (this.variant == "primary") {
        return {
          "background-color": "#1565C0",
        };
      } else if (this.variant == "error") {
        return {
          "background-color": "#E53935",
        };
      }
       else if (this.variant == "warning") {
        return {
          "background-color": "#FB8C00",
        };
      } else if (this.variant == "success") {
        return {
          "background-color": "#2ecc71",
        };
      } else {
        return {
          "background-color": "#E0E0E0",
          color: "black",
        };
      }
    },
  },
  
};
</script>
<style scoped>
button {
  position: relative;
  color: "black";
  text-transform: uppercase;
  cursor: "";
  pointer-events: all;
  font-family: Roboto;
  font-weight: 500;
  letter-spacing: 0.0892857143em;
  font-size: 0.875rem;
  display: block;
  margin: 20px 10px;

  padding: 8px 18px;

  overflow: hidden;

  border-width: 0;
  outline: none;
  border-radius: 2px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);

  background-color: #2ecc71;
  color: #ecf0f1;

  transition: background-color 0.3s;
}

button:before {
  content: "";

  position: absolute;
  top: 50%;
  left: 50%;

  display: block;
  width: 0;
  padding-top: 0;

  border-radius: 100%;

  background-color: rgba(236, 240, 241, 0.3);

  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

button:active:before {
  width: 120%;
  padding-top: 120%;

  transition: width 0.2s ease-out, padding-top 0.2s ease-out;
}

</style>