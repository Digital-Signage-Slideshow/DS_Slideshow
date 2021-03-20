<template>
    <div class='album pt-5'>
        <div class='container'>
            <button type='button' class='btn btn-primary ml-3'>Upload Content</button>
            <a href='/slideshow' class='btn btn-outline-secondary ml-3'>View Slideshow</a>

            <div class='album pt-4'>
                <div class='container'>
                    <h2>Content</h2>
                    <p class='text-muted'>Drag and drop slides to reorder the slideshow (not implemented yet)</p>
                    <hr>

                    <div class='card-deck'>
                        <SlideCard
                        v-for='slide in slides'
                        v-bind:slide='slide'
                        :key='slide.title'
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import SlideCard from '@/components/SlideCard.vue';

    export default {
        name: 'SlideDeck',

        data() {
            return {
                rotation_speed: 10,
            }
        },

        props: {
            slides: Object,
        },

        components: {
            SlideCard,
        },
    }
</script>