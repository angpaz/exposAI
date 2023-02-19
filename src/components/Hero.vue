
<template>

  <div
    class="container mx-auto pt-40 lg:pt-52 2xl:pt-64 pb-16 lg:pb-20 xl:pb-28 2xl:pb-52 flex flex-col px-5 py-24 justify-center items-center max-w-7xl"
  >
    <div class="w-full md:w-2/3 flex flex-col mb-6 text-center">
      <!-- Header text -->
      <h1
        class="title-font tracking-tight font-extrabold text-2xl xs:text-3xl lg:text-4xl 2xl:text-6xl mb-4 text-gray-800"
      >
        Immobilien Exposés V2<span style="color: #6666FF;">mit AI</span>
      </h1>

      <!-- Sub text -->
      <p
        class="mb-8 leading-relaxed text-xs sm:text-sm lg:text-lg xl:text-xl 2xl:text-2xl"
      >
        Wir automatisieren Ihr Immobilienexposé. Nie wieder nervige Texte
        schreiben.
        <br />
        <br />
      </p>


      <form class="w-full max-w-none">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full h-80 w-60 md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-s mb-2" for="grid-first-name">
        Füge die Eckdaten der Immobilie ein.
      </label>
      <textarea v-model="rawtext"
 class="break-words h-40 w-60 appearance-none block w-full  text-gray-700 border border-purple-600 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="text" placeholder="80qm, 4 Zimmer, Wohnung, mit Stellplatz">      
</textarea>

      <!--<<p class="text-red-500 text-xs italic">Fülle dies aus!</p>-->
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-italic mb-2" for="grid-first-name">
        Optional: Adresse für eine Lagebeschreibung!
      </label>

      <div class="flex flex-row"> 
        
        <vue-google-autocomplete
                    id="map"
                    ref="address"
                    class="break-words h-10 w-60 appearance-none block w-full text-gray-700 border border-purple-600 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white "
                    placeholder="Venloerstraße 31, 50677 Köln"
                    v-on:placechanged="getAddressData"
                    v-on:error="handleError"
                    country="de"
                    types="street_address"
                                    >

                                    
                </vue-google-autocomplete>
        
        <button type="button" v-on:click="$refs.address.geolocate();" class="h-10 w-20 text-sm text-purple-600 font-semibold border border-purple-200 hover:text-white hover:bg-purple-600 hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Get location</button>
</div>

                

            <!-- <div class="message is-success" v-show="address">
                <div class="message-body">{{ address }}</div>
            </div> -->

<!--  
 <section class="hero">
    <div class="hero-body">
        <div class="container" id="app">
            <h3 class="title is-4">Start typing an address and below you will see found result,
                <a v-on:click="$refs.address.geolocate()">or force current location</a>
            </h3>
            <p class="control">
                <vue-google-autocomplete
                    id="map"
                    ref="address"
                    classname="input"
                    placeholder="Start typing"
                    v-on:placechanged="getAddressData"
                    v-on:error="handleError"
                    country="de"
                >
                </vue-google-autocomplete>
            </p>

            <div class="message is-success" v-show="address">
                <div class="message-body">{{ address }}</div>
            </div>
        </div>
    </div>
</section> -->

 
 <button
            id="heroEmailSubscribe"
            @click="subscribeEmail"
            type="button"
            style="background: #6666FF;"
            class="flex-wrap relative my-auto disabled:opacity-50 text-sm xl:text-xl text-white justify-start rounded-full py-2 px-8 shadow-lg focus:outline-none focus:shadow-outline transform transition hover:shadow-xl hover:scale-105 duration-300 ease-in-out"
          >
            Erstelle das Exposé
          </button>
  
    </div>
    <div  class="break-words w-full md:w-1/2 px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-s mb-2" for="grid-last-name">
        Kopiere hier dein fertiges Expose.
        
      </label>      
      <textarea v-model="this.$store.state.responseMessage" class="break-words h-80 w-60 appearance-none block w-full text-gray-700 border border-black rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500 position-relative" id="grid-last-name" type="text" placeholder="Wohnung zur Vermietung in angesagtem kölner Viertel...">
      </textarea>

    </div>
    
  </div>
  
</form>




      <!-- Form with button -->
      <div class="my-2.5 ">
        <div class="flex w-full justify-center items-end">
          <div
            class="relative mr-4 lg:w-full xl:w-1/2 w-2/4 md:w-full text-left"
          >
            <!-- Binding a placeholder from the Vuex store, just to show how it interacts 
            <input
              v-model="email"
              type="text"
              :placeholder="exampleEmail"
              name="hero-field"
              class="w-full bg-opacity-50 rounded placeholder-gray-600 placeholder-opacity-50 focus:ring-2 focus:bg-transparent border border-gray-300 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />-->
          </div>
        
        </div>

        <div class="container bg-white my-3 p-3 rounded">
	
	<div class="position-relative mb-3">
    
  	<button  class="border-gray-300 bg-opacity-50 position-absolute" style="right:0;" onclick="copyText();" title="Copy Text">
      
      <div id="clipboardicon">
      <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>
      </div>

      <span id="copyButton">Copy</span></button>
  	
  </div>
	
</div>
        <!-- Response messages
        <p
          v-if="responseType === 'error'"
          class="text-xs text-red-500 mt-6 ml-1"
        >
          ❌ {{ this.$store.state.responseMessage }}
        </p>
        <p
          v-if="responseType === 'success'"
          class="text-xs text-green-500 mt-6 ml-1"
        >
          ✅ {{ this.$store.state.responseMessage }}
        </p> -->
      </div>
    </div>
  </div>

</template>
<script>
import { mapGetters, mapActions } from "vuex";
import Vue from 'vue';
import VueGoogleAutocomplete from '/node_modules/vue-google-autocomplete/src/VueGoogleAutocomplete.vue';

export default {

  components: { VueGoogleAutocomplete },

  data() {
    return {
      // This is the local version of the email,
      // this is mounted to the input
      oart: "",
      resultExp: "",
      address: "",

    };
  },
  mounted() {

    this.$refs.address.focus();

  },
  computed: {
    ...mapGetters({
      // This is how you rename a getter, value is accessible
      // via exampleEmail now.
      exampleEmail: "getExampleEmail",
      responseMsg: "getResponseMessage",
      responseType: "getResponseType",
    }),
  },

  methods: {
    ...mapActions(["subscribe"]),
    subscribeEmail: function() {
      this.subscribe(this.rawtext);
    },
    /**
       * When the location found
       * @param {Object} addressData Data of the found location
       * @param {Object} placeResultData PlaceResult object
       * @param {String} id Input container ID
       */
       getAddressData: function (addressData, placeResultData, id) {
        this.address = addressData;
        console.log(addressData);
      }
  },
  watch: {
    responseMsg(newVal, oldVal) {
      return newVal, oldVal;
    },
    responseType(newVal, oldVal) {
      return newVal, oldVal;
    },
  },
};
</script>
