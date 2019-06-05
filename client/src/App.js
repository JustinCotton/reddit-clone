import React, {Component} from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import logo from './logo.svg';
import './App.css';
import AllPosts from './components/AllPosts'
import SinglePost from './components/SinglePost'
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

  const Posts = () => (<AllPosts
    posts = {this.state.posts}
    />)
  const Post = () => (<SinglePost
    
    />)

  return (
    <Router>
      <div className="App">
        <h1>Hello World</h1>
        <div>
          <Switch>
            <Route exact path="/" render={Posts}/>
            <Route exact path="/post/:id" render={Post}/>
          </Switch> 
        </div>
      </div>
    </Router>
  );
  }
}

export default App;
