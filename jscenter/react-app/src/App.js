import React, { Component } from 'react';
import Art from "./components/Art.js"
import Nav from "./components/Nav.js"
import Subject from "./components/Subject.js"
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(porps) { // 제일먼저 실행되어 초기화 담당 
    super(porps);
    this.state = {
      subject: { title: 'W2EB', sub: ' World' },
      contents : [
        {id : 1, title : 'HTML' , desc : 'HTML is hyperText...'},
        {id : 2, title : 'CSS' , desc : 'HTML is hyperText...'},
        {id : 3, title : 'JavaScript' , desc : 'HTML is hyperText...'}
      ]
    }
  }
  render() {
    return ( // 상위 컴포넌트의 state 값을 하위 컴포넌트의 props 값으로 전달
      <div className="App">
        <Subject title={this.state.subject.title} sub=" world Wide Web"></Subject>
        <Subject></Subject>
        <Nav data = {this.state.contents}></Nav>
        <Art></Art>
      </div>
    );
  }
}

export default App;
