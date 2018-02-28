<template>
 <section class="fixed-content" style="padding: 20px">
        <div class="tc-content-wrapper">
            <div class="tc-content">
                <MediaDisplay />
                <Sidebar />
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