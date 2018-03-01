<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-md-6 col-md-offset-3" v-if="file">
          <img :src="preview" alt="" class="preview">
        </div>
      </div>
      <div class="previews">
        <div class="col-md-4" v-for="page in pages">
          <img :src="page.url" alt="" class="img-responsive" @click="selectImage(page.page)">
        </div>
      </div>
    </div>

 <!--   <div v-if="resource">
     {{ resource.attributes.name }}
   </div>
   <div v-else>
    <div class="loading-spinner"></div>
   </div> -->
 </div>
</template>

<script>
  export default {
    props: ['openWidget', 'selectImage', 'file', 'pages'],

    data() {
      return {
          resource: null,
          loading: true,
      }
    },
  methods: {


  
  }
}
</script>

<style scoped>
.container {
  display: flex;
  margin-left: 20px;
}


.previews {
  margin-top: 20px;
  width: 60%;
  display: flex;
  flex-wrap: wrap;
}

img {
  display: block;
  margin: auto;
  border: #E1E1E1;
  box-shadow: 0px 3px 6px 0px rgba(0,0,0,0.3);
}

.upload {
  margin-top: 30%;
}

#app {
}

.pages {
  margin-top: 20px
}
</style>
