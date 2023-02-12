import { createStore } from 'vuex'
const axios = require('axios');

export default createStore({
    state: {
        exampleEmail: "name@example.com",
        responseMessage: "",
        responseType: ""
    },

    // getters are functions.
    getters: {
        getExampleEmail (state) {
            return state.exampleEmail
        },

        getResponseMessage (state) {
            return state.responseMessage
        },

        getResponseType (state) {
            return state.responseType
        },
    },

    // actions are functions that cause side effects and can involve
    // asynchronous operations.
    actions: {
        async subscribe (_, input) {
            await axios({
                //  Post request as defined by api/subscribe/function.json
                method: 'post',
                // This is how we handle CORS. It gets the value from the 
                // .env file
                // headers: {'Content-Type':'text/event-stream'},
                url: `${process.env.VUE_APP_API || 'api'}/subscribe`,
                withCredentials: false,
                
                // Additional params
                params: {
                    inputprompt: input,
                },
            }).then(res => { console.log(res)
                // Set response message & type when API call successful
                this.commit('SET_RESPONSEMESSAGE', res.data)
                this.commit('SET_RESPONSETYPE', 'success')
            }).catch(err => {
                // Set response message & type when API call unsuccessful
                this.commit('SET_RESPONSEMESSAGE', 'Whoops, looks like something went wrong. Please try again later!')
                this.commit('SET_RESPONSETYPE', 'error')
                // Console log for debugging
                console.log(err)
            });
        },
    },

    // mutations are operations that actually mutate the state.
    // each mutation handler gets the entire state tree as the
    // first argument, followed by additional payload arguments.
    // mutations must be synchronous and can be recorded by plugins
    // for debugging purposes.
    mutations: {
        SET_RESPONSEMESSAGE (state, value) {
            state.responseMessage = value
        },

        SET_RESPONSETYPE (state, value) {
            state.responseType = value
        }
    }
})