<template>
    <div class='home'>
        <Navbar />
        <SlideDeck v-if='slides.length' v-bind:slides='slides' />

        <div v-else class='text-center mt-5'>
            <h1>No Content to Display</h1>
            <button type="button" class="btn btn-primary ml-3" data-toggle="modal" data-target="#myModal">
                Upload Content
            </button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import SlideDeck from "@/components/SlideDeck.vue";
    import Navbar from "@/components/Navbar.vue";

    export default {
        name: 'Home',
        components: {
            SlideDeck,
            Navbar,
        },

        data() {
            return {
                slides: '',
            };
        },

        mounted() {
            axios
                .get("http://localhost:5000/slides")
                .then((slides) => {
                    this.slides = slides.data; console.log(slides)
                });
        },
    };
</script>