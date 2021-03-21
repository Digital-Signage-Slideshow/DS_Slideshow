import { createStore } from 'vuex'
import auth from './modules/auth';
import slides from './modules/slides';

export default createStore({
  modules: {
    auth,
    slides
  }
})