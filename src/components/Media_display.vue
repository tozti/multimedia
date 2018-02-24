<template>
  <div>
    <div class="previsu">
       <h2> Prévisualisation </h2>
   </div>

   <div v-if="resource">
     {{ resource.attributes.name }}
   </div>
   <div v-else>
    <div class="loading-spinner"> loading... </div>
   </div>
 </div>
</template>

<script>
  export default {
    data() {
      return {
          resource: null,
          loading: true,
      }
    },

    beforeMounted() {
        tozti
          .store.get(this.$route.params.id)
          .then(resource => {
              this.resource = resource
              this.loading = false
          })
    }
  }
</script>
