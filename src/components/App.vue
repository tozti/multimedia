<template>
 <section class="fixed-content" style="padding: 20px">
        <div class="tc-content-wrapper">
            <div class="tc-content">
                <nav class="level">
                Hello
              </nav>
            </div>
        </div>
    </section>
</template>

<script>
const SidebarStatus = Object.freeze({View: 0, Modify: 1, Create: 2})


  export default {
    data(){
        return{
            sidebar : {
                opened : false,
                type : SidebarStatus.View,
                event : {},
                titles : ['Evenement', 'Modification', 'Ajout']
            }
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