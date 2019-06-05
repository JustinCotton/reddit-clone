import React, {Component} from 'react'
import {getPostById} from '../util'

class SinglePost extends Component {

    state = {
        post: {},
        comments: []

    }
    componentDidMount(){
        let artistId = this.props.post.match.params.id
        getPostById(artistId)
            .then(post => {
                this.setState({post: post})
            })
      }
    render(){
        return(
            <div>
            <h1>Title: {this.state.post.title}</h1>
            <h1>Content: {this.state.post.content}</h1>
            </div>
        )
    }
}

export default SinglePost