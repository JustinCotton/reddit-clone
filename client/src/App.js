import React, {Component} from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import logo from './logo.svg';
import './App.css';

import {getPosts} from './util'

class App extends Component {

  state = {
    posts: []
  }

  componentDidMount(){
    getPosts() 
      .then(posts => {
        this.setState({posts: posts})
      })
  }
  render(){
  return (
    <Router>
      <div className="App">
        <h1>Hello World</h1>
        <button onClick={getPosts}>get posts</button>
        <div>
        {
          this.state.posts.map((post, index) => {
            return(
              <div key={index}>{post.title} -- {post.content}</div>
              
            )
          })
        }
        </div>
      </div>
    </Router>
  );
  }
}

export default App;
