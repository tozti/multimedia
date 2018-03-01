<template>
  <div>
    <div class="sidebar">
        <div class="right-sidebar">
        <h2> DRIVE </h2>
        <nav>
        <ul>
            <h3> Informations </h3>
            <li> <a href="#" > Groupe</a> </li>
            <li> <a href="#"> Users</a> </li>
            <li> <a href="#"> Droits</a> </li>
            <li> <a href="#"> Date</a> </li>
        </ul>
        </nav>

        <nav>
            <ul>
                <h3> Gestion </h3>
                <li> <a href="#" > Partage</a> </li>
                <li> 
                <a v-on:click="openWidget()">Upload</a></li>
                <li> <a href="#"> Download</a> </li>
            </ul>
        </nav>
    </div>

  </div>
 </div>
</template>

<script>
export default {
    props: ['openWidget'],

  data(){
    return{

    }
  },

  methods: {
      

  }
}
</script>

<style scoped>
.sidebar {
  bottom: 0;
  box-sizing: border-box;
  font-weight: 300;
  background: rgba(255, 255, 255, 0.5); }

.sidebar h3 {
  color: #6a6a6a;
  margin: 35px 0 10px;
  text-transform: uppercase;
  font-size: 1em;
  font-weight: 300; }

.sidebar nav a {
  display: block;
  text-decoration: none;
  font-size: 1.1em;
  color: #6a6a6a;
  margin: 4px 0;
  padding: 7px 15px;
  border-radius: 4px; }
  .sidebar nav a i {
    vertical-align: -3px;
    margin: 0 12px 0 0;
    font-size: 1.1em; }

.sidebar nav .counter {
  float: right;
  font-size: 15px;
  padding: 0 6px;
  line-height: 1.4;
  color: #a2a2a2;
  border: 2px solid #bcbcbc;
  border-radius: 20px;
  min-width: 30px;
  text-align: center; }

.sidebar nav a.active {
  font-weight: 400;
  background: #fef4f5;
  color: #ef233c; }

.sidebar nav a.active .counter {
  color: #f2495e;
  border-color: #f57484; }

.sidebar .main-sidebar {
  position: fixed;
  left: 0;
  top: 70px;
  width: 290px;
  padding: 30px 20px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.07);
  font-family: "Renner*", sans-serif; }

.sidebar .right-sidebar {
  position: absolute;
  bottom: 0;
  right: 0;
  top: 72px;
  width: 290px;
  padding: 23px;
  border-left: 2px solid #f4f4f4;
  border-right: 2px solid #f4f4f4;
  font-family: "Renner*", sans-serif; }

</style>
