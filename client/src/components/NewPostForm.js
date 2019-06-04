import React, {Component} from 'react'
import './NewPostForm.css'

class NewPostForm extends Component {
    state = {
        post: {
            created_at: '',
            title: '',
            picture: '',
            content: '',
            site_url: '',
            vote_total: ''
            // user: ''
        }
    }

    handleInput = (event) => {
        const attributeName = event.target.name
        const attributeValue = event.target.value

        const newPost = { ...this.state.post }
        newPost[attributeName] = attributeValue

        this.setState({ user: newPost }, function(){
        })
    }

    handleSubmit = (event) => {
        event.preventDefault();
        // createNewPost(this.state.post)
        this.props.handleNewPost(this.state.post)
    }

    render(){
        return(
        <div >
            <form>
                <div className="form-group">
                    <label>Time of Creation: </label>
                    <input type="text" name="created_at" placeholder="Date" onChange={this.handleInput} />
                </div>
                <div className="form-group">
                    <label>Post Title: </label>
                    <input type="text" name="title" placeholder="Post Title" onChange={this.handleInput} />
                </div>
                <div className="form-group">
                    <label>Picture URL: </label>
                    <input type="text" name="picture" placeholder="url link here" onChange={this.handleInput} />
                </div>
                <div className="form-group">
                    <label>Content: </label>
                    <input type="text" name="content" placeholder="Whatcha say" onChange={this.handleInput} />
                </div>
                <div className="form-group">
                    <label>Sub-reddit: </label>
                    <input type="text" name="site_url" placeholder="subject" onChange={this.handleInput} />
                </div>
                <div className="form-group">
                    <label>Votes: </label>
                    <input type="text" name="vote_total" placeholder="vote4me" onChange={this.handleInput} />
                </div>
                <input className="post-submit-button" type="submit" value="Submit" onClick={this.handleSubmit} />
            </form>
        </div> 
        )
    }
}

export default NewPostForm;