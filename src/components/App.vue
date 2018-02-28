<template>
 <section class="fixed-content" style="padding: 20px">
        <div class="tc-content-wrapper">
            <div class="tc-content">
                HELLO
            </div>
        </div>
    </section>
</template>

<script>

  export default {
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