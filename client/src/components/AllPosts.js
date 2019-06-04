import React, {Component} from 'react'

class AllPosts extends Component {
    render(){
        return(
            <div>
            <h1>AllPosts</h1>
            <div>
                {
                    this.props.posts.map((post, index) => {
                        return(
                          <div key={index}><a href={`/post/${post.id}`}>{post.title} -- {post.content}</a></div>
                          
                        )
                      })
                }
            </div>
            </div>
        )
    }
}

export default AllPosts

