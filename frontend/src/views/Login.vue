<template>
    <main class='row justify-content-center align-items-center h-100'>
        <div>
            <form class='form-signin' @submit.prevent='login'>
                <h1 class='h3 font-weight-bold'>DS Slideshow</h1>

                <small v-if='error' class='text-danger'>
                    {{ error }}
                </small>

                <input v-model='username' type='text' class='form-control mb-1' placeholder='Username' required>
                <input v-model='password' type='password' class='form-control mb' placeholder='Password' required>

                <div class='checkbox mb-3 mt-2'>
                    <input class='checkbox' type='checkbox'> <small>Remember Password</small>
                </div>

                <button class='btn btn-block btn-sm btn-secondary'>Register here</button>
                <button type='submit' class='btn btn-lg btn-primary btn-block mt-2'>Login</button>
            </form>
        </div>
    </main>
</template>

<style>
    body, html {
        height: 100%;
        overflow: hidden;
    }
</style>

<script>
    import {AUTH_REQUEST} from '@/store/actions/auth.js';

    export default {
        name: 'Login',
        
        data() {
            return {
                username: '',
                password: '',
                error: '',
                closed: false,
            }
        },

        methods: {
            login: function() {
                const {username, password} = this

                this.$store.dispatch(AUTH_REQUEST, {username, password})
                .then(() => {
                    this.$router.push('/');
                })
                .catch((error) => {
                    console.log(error);

                    this.error = error.response.data;
                    this.closed = false;
                })
            }
        },
    };
</script>