<template>
    <div class='col mb-3'>
        <div class='card rounded-0 text-left h-100'>
            <div class='card-body'>
                <h3 class='card-title'>{{ slide.path }}</h3>
                <span class='card-subtitle badge badge-outline'>{{ slide.type }}</span>
                <small>{{ slide.rotation_speed }}</small><br>
                <small>Slide Number: {{ slide.priority }}</small>
            </div>

            <div class='card-footer'>
                <a class='btn btn-sm btn-outline-secondary'>Settings</a>
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
