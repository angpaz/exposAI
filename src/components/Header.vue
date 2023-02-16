<template>
  <!-- Header class depends on scroll position -->
  <nav class="fixed inset-x-0 top-0 z-50 w-full text-gray-700 bg-white" :class="{
      shadow: scrollPosition > 10
  }">
    
    <!-- Small menu -->
    <div class="md:hidden pt-2 flex">
        
        <div class="md:hidden pt-2 flex w-full">
            <!-- Logo -->
            <img class="object-scale-down ml-3 m-4 h-20 cursor-pointer" @click="$router.push('/')" src="../assets/imgs/logo_big.png" alt="" />
            
            <div class="justify-between flex-1" />
            <!-- Hamburger menu icon -->
            <button @click="isOpen = !isOpen" type="button" aria-label="openMenu" class="block justify-end m-4 float-right focus:outline-none">
            <svg class="h-10 w-10 fill-current" viewBox="0 0 24 24">
                <path v-if="isOpen" fill-rule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"/>
                <path v-if="!isOpen" fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"/>
            </svg>
            </button>
        </div>

    </div>

    <!-- Large menu -->
    <nav :class="isOpen ? 'block' : 'hidden'" class="container pt-2 md:flex">
        <!-- Logo -->
        <img class="hidden md:flex md:object-scale-down md:my-auto md:h-20 md:cursor-pointer" @click="$router.push('/')" src="../assets/imgs/logo_big.png" alt="" />

        <!-- Nav -->
        <button type="button" @click="$router.push('/')" class="mt-1 block px-5 py-4 text-xl rounded md:mt-0 md:ml-2 transform transition hover:scale-105 duration-200 ease-in-out">Home</button>
        <button type="button" @click="$router.push('/features')" class="mt-1 block px-5 py-4 text-xl rounded md:mt-0 md:ml-2 transform transition hover:scale-105 duration-200 ease-in-out">Historie</button>
        <button type="button" @click="$router.push('#')" class="mt-1 block px-5 py-4 text-xl rounded md:mt-0 md:ml-2 transform transition hover:scale-105 duration-200 ease-in-out text-indigo-700	">Login</button>
        <button type="button" @click="$router.push('/demo')" class="mt-1 block px-5 py-4 text-xl rounded md:mt-0 md:ml-2 transform transition hover:scale-105 duration-200 ease-in-out text-indigo-700	">Demo</button>

      </nav>
  </nav>





</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      scrollPosition: null
    }
  },
  methods: {
    updateScroll() {
       this.scrollPosition = window.scrollY
    }
  },
  mounted() {
    window.addEventListener('scroll', this.updateScroll);
  },
}
</script>
<style scoped>
.shadow {
  box-shadow: 0 4px 20px -2px #D3D3D3;
}
</style>
