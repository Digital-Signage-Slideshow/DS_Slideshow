import {
    AUTH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_LOGOUT,
    AUTH_VALIDATE,
    TOKEN_GENERATED
} from '../actions/auth';

import axios from 'axios';

const getters = {
    isAuthenticated: (state) => {return state.authenticated},
};

const state = {
    token: localStorage.getItem('user-token') || '',
    authenticated: false,
    hasLoadedOnce: false,
};

const actions = {
    // Login will create a post request to the server for a new login key
    [AUTH_REQUEST]: ({ commit }, user) => {
        return new Promise((resolve, reject) => {
            commit(AUTH_REQUEST);

            axios
            .post('http://localhost:5000/user/login', {
                username: user.username, 
                password: user.password
            })
            .then((response) => {
                console.log('success');

                commit(TOKEN_GENERATED, response);
                resolve(response);
            })
            .catch(error => {
                console.log(error.response.data);

                commit(AUTH_ERROR, error);
                localStorage.removeItem('user-token');
                reject(error);
            });
        });
    },

    // Logout will invalidate the key on the server
    [AUTH_LOGOUT]: ({ commit }, user) => {
        return new Promise(resolve => {
            commit(AUTH_LOGOUT);
   
            axios
            .post('http://localhost:5000/user/logout', {data: user})
            .then(() => {
                localStorage.removeItem('user-token');
                commit(AUTH_LOGOUT);
            })

            resolve();
        });
    },

    // Validate authentication token
    [AUTH_VALIDATE]: ({commit}) => {
        return new Promise((resolve, reject) => {
            axios.
            get('http://localhost:5000/user/token_valid', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('user-token')}`
                }
            })
            .then(() => {
                console.log('token valid');
                commit(AUTH_SUCCESS);
            })
            .catch((error) => {
                console.log('token invalid: ' + error);

                commit(AUTH_ERROR, error);
                commit(AUTH_LOGOUT);

                reject();
            });
            resolve();
        })
    }
};

const mutations = {
    [AUTH_REQUEST]: state => {
        state.status = 'loading';
    },

    [AUTH_SUCCESS]: (state) => {
        state.authenticated = true;
    },

    [AUTH_ERROR]: state => {
        state.authenticated = false;
    },

    [AUTH_LOGOUT]: () => {
        localStorage.removeItem('user-token');
    },

    [TOKEN_GENERATED]: (state, response) => {
        state.authenticated = true;
        localStorage.setItem('user-token', response.data.access_token);
        state.hasLoadedOnce = true;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};