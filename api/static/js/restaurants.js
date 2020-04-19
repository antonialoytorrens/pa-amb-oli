
//Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#starting',
    delimiters: ['${', '}'],
    data: {
        restaurants: [],
        loading: false,
        currentRestaurant: {},
        message: '',
        newRestaurant: {
            'restaurant_nom': null,
            'restaurant_telefon': null,
            'restaurant_descripcio': null,
            'restaurant_email': null,
            'restaurant_web': null
        },
    },
    mounted: function() {
        this.getRestaurants();
    },
    methods: {
        getRestaurants: function() {
            this.loading = true;
            this.$http.get('/api/restaurant/')
                .then((response) => {
                    this.restaurants = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getRestaurant: function(id) {
            this.loading = true;
            this.$http.get(`/api/restaurant/${id}/`)
                .then((response) => {
                    this.currentRestaurant = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addRestaurant: function() {
            this.loading = true;
            this.$http.post('/api/restaurant/', this.newRestaurant)
                .then((response) => {
                    this.loading = false;
                    this.getRestaurants();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        updateRestaurant: function() {
            this.loading = true;
            this.$http.put(`/api/restaurant/${this.currentRestaurant.restaurant_id}/`, this.currentRestaurant)
                .then((response) => {
                    this.loading = false;
                    this.currentRestaurant = response.data;
                    this.getRestaurants();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        deleteRestaurant: function(id) {
            this.loading = true;
            this.$http.delete(`/api/restaurant/${id}/`)
                .then((response) => {
                    this.loading = false;
                    this.getRestaurants();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        }
    }
});