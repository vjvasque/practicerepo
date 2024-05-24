import axios from 'axios'

const api = axios.create({
    baseURL: 'http://localhost:3000/api'
})

export const createUser = userData => api.post('/users', userData)
export const getUser = email => api.get(`/users/${email}`)
export const createPost = postData => api.post('/posts', postData)
export const getUserPosts = userId => api.get(`/posts/${userId}`)