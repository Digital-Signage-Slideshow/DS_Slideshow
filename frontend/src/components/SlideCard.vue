<template>
    <div class='col mb-3'>
        <div class='card rounded-0 text-left h-100'>
            <div class='card-body'>
                <h3 class='card-title'>{{ slide.title }}</h3>
                <span class='card-subtitle badge badge-outline'>{{ slide.type }}</span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'SlideCard',
        props: {
            slide: Object,
        },
    }
</script>
