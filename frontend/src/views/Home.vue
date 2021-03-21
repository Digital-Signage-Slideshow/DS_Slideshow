<template>
    <div class='home'>
        <Navbar />
        <SlideDeck v-if='slides.slides.length' />

        <div v-else class='text-center mt-5'>
            <h1>No Content to Display</h1>
            
            <button type="button" class="btn btn-primary ml-3" data-toggle="modal" data-target="#myModal">
                Upload Content
            </button>
        </div>

        <Footer />
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    import SlideDeck from "@/components/SlideDeck.vue";
    import Navbar from "@/components/Navbar.vue";
    import Footer from "@/components/Footer.vue";

    export default {
        name: 'Home',

        components: {
            SlideDeck,
            Navbar,
            Footer,
        },

        computed: mapState([
            'slides'
        ]),

        mounted() {
            this.$store.dispatch('UPDATE_SLIDES');
        },
    };
</script>