<template>
  <div id="app">
    <div class="container">
      <h3 class="text-center" style="color:#fff">PDF Viewer</h3>
      <div class="row">
        <div class="col-md-6 col-md-offset-3" v-if="file">
          <img :src="preview" alt="" class="preview">
        </div>
      </div>
      <div class="row pages">
        <div class="col-md-4" v-for="page in pages">
          <img :src="page.url" alt="" class="img-responsive" @click="selectImage(page.page)">
        </div>
      </div>
      <div class="row upload" v-if="!file">
        <div class="col-md-offset-4 col-md-4">
          <button @click="openWidget()">Upload PDF</button>
        </div>
      </div>
    </div>

   <div v-if="resource">
     {{ resource.attributes.name }}
   </div>
   <div v-else>
    <div class="loading-spinner"></div>
   </div>
 </div>
</template>

<script>
  export default {

    data() {
      return {
          file: null,
          preview: null,
          pages: [],

          resource: null,
          loading: true,
      }
    },

    created() {
        let pdfUploadScript = document.createElement('script')
        pdfUploadScript.setAttribute('src', '//widget.cloudinary.com/global/all.js')
        document.head.appendChild(pdfUploadScript)
    },

  methods: {
    selectImage(page) {
      this.preview = `http://res.cloudinary.com/christekh/image/upload/w_350,h_400,c_fill,pg_${page}/${this.file.public_id}.jpg`
    },

    openWidget(url) {
      window.cloudinary.openUploadWidget(
        {
          cloud_name: 'christekh',
          upload_preset: 'qbojwl6e',
          tags: ['pdf'],
          sources: [
            'local',
            'url',
          ]
        },
        (error, result) => {
          console.log(error, result);
          this.file = result[0];
          this.preview = `http://res.cloudinary.com/christekh/image/upload/w_350,h_400,c_fill,pg_1/${this.file.public_id}.jpg`;
          for (let i = 1; i <= this.file.pages; i++) {
            this.pages.push(
              {
                url: `http://res.cloudinary.com/christekh/image/upload/w_200,h_250,c_fill,pg_${i}/${this.file.public_id}.jpg`,
                page: i
              }
            )
          }
        }
      );
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
}

.preview {
  margin-top: 40px;
}
img {
  display: block;
  margin: auto;
  border: #E1E1E1;
  box-shadow: 0px 3px 6px 0px rgba(0,0,0,0.3);
}

.upload {
  margin-top: 30%;
  margin-left: 14%;
}

button {
  color: #687DDB;
  padding: 10px 15px;
  border: #e1e1e1;
  background: #fff;
  border-radius: 4px;
}

#app {
}

.pages {
  margin-top: 20px
}
</style>
