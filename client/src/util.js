import axios from 'axios'

export function queryTVMazeAPI (query) {
    // send HTTP request to the Express server, which will make a request to the TVMaze API
    return axios.get('/shows?q='+query)
    // create HTTP request to the route in parentheses
        .then(response => {
            return response.data
        })
}

export function addFavoriteMovie(movie) {
    return axios.post('/favorites', movie)
}

export function getFavorites() {
    return axios.get('/favorites')
        .then(results => results.data);
}

export function deleteFavoriteMovie(movie) {
    return axios.delete(`/favorites/${movie._id}`)
}