import React, {Component} from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import logo from './logo.svg';
import './App.css';

class App extends Component {

  state = {
    posts: []
  }
  render(){
  return (
    <Router>
      <div className="App">
        <h1>Hello World</h1>
      </div>
    </Router>
  );
  }
}

export default App;
