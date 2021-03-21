<template>
    <router-view/>
</template>

<script>
import axios from 'axios';
import {AUTH_LOGOUT} from './store/actions/auth';

export default {
    created: function () {
        axios.interceptors.response.use(undefined, function (err) {
            return new Promise(function () {
                if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
                    this.$store.dispatch(AUTH_LOGOUT)
                }
                throw err;
            });
        });
    }
}
</script>