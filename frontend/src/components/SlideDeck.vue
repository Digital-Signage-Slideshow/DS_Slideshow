<template>
    <div class='album pt-5'>
        <div class='container'>
            <button type='button' class='btn btn-primary ml-3'>Upload Content</button>
            <a href='/slideshow' class='btn btn-outline-secondary ml-3'>View Slideshow</a>

            <div class='album pt-4'>
                <div class='container'>
                    <h2>Content</h2>
                    <p class='text-muted'>Drag and drop slides to reorder the slideshow</p>
                    <hr>

                    {{ listSlides }}
                    <div class='mt-2'>
                        <draggable
                            class='card-deck'
                            v-model='listSlides'
                            group='slideGroup'
                            item-key='priority'
                            animation='300'
                        >

                            <template #item='{element}'>
                                <SlideCard :slide=element />
                            </template>
                        </draggable>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import draggable from 'vuedraggable';
    import SlideCard from '@/components/SlideCard.vue';
    // import { mapState } from 'vuex'


    export default {
        name: 'SlideDeck',

        components: {
            draggable,
            SlideCard,
        },

        methods: {
            reindex() {
                this.slides.slides.forEach((element, index) => {element.priority = index});
            }
        },

        computed: {
            listSlides: {
                get() {
                    return this.$store.state.slides.slides;
                },
                set() {
                    this.$store.commit('UPDATE_PRIORITY');
                }
            }
        }
    }
</script>

<style scoped>
    .ghost {
        opacity: 0.5;
        background: #c8ebfb;
    }
</style>