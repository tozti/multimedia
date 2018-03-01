<template>
 <section class="fixed-content">
        <div class="tc-content-wrapper">
            <div class="tc-content">
                <MediaDisplay
                    :openWidget="openWidget"
                    :file="file"
                    :pages="pages"
                    :selectImage="selectImage"/>
            </div>
            <div class="tc-content">
                <Sidebar
                    :openWidget="openWidget"/>
            </div>
        </div>
    </section>
</template>

<script>
import Sidebar from './Sidebar.vue'
import MediaDisplay from './MediaDisplay.vue'

  export default {
    components: {
        Sidebar,
        MediaDisplay
    },

    data(){
        return{
             file: null,
             preview: null,
             pages: [],
        }
    },

    created() {
        let pdfUploadScript = document.createElement('script')
        pdfUploadScript.setAttribute('src', '//widget.cloudinary.com/global/all.js')
        document.head.appendChild(pdfUploadScript)
    },


    methods:{
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

<style>
.tc-content-wrapper {
    display: flex;
    flex-direction: row;
    height: 100%;
}

.tc-content {
    flex: auto;
}

.tc-sidebar {
    position: relative;
    right: -20px;
}


</style>