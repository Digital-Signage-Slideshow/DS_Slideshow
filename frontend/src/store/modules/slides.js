import axios from 'axios';
import { UPDATE_SLIDES, UPDATE_PRIORITY } from '../actions/slides';

const getters = {
    getSlides() {return state.slides},
};

const state = {
    slides: [{dummy: 'element'}],
};

const actions = {
    [UPDATE_SLIDES]: ({commit}) => {
        axios
        .get('http://localhost:5000/slides', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('user-token')}`
            }
        })
        .then((slides) => {
            commit(UPDATE_SLIDES, slides.data);
        })
    },

    [UPDATE_PRIORITY]: ({commit}, slides) => {
        axios
        .put('http://localhost:5000/update_slide_priority', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('user-token')}`
            },
            data: slides,
        })
        .then((slides) => {
            commit(UPDATE_SLIDES, slides.data);
        })
    }
};

const mutations = {
    [UPDATE_SLIDES]: (state, slides) => {
        state.slides = slides;
    },

    [UPDATE_PRIORITY]: (state, slides) => {
        state.slides = slides;
    }
}

export default {
    state,
    actions,
    mutations,
    getters
}