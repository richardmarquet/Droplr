import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './Components/Navbar/Navbar'
import Sidebar from './Components/Sidebar/Sidebar'
import Mainbody from './Containers/Mainbody/Mainbody'
import Suggested from './Components/Suggested/Suggested'

import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios'
import * as $ from "jquery";



class App extends Component{
  state = {
    sidebarOn: true
  }

  toggleSideBar() {
    console.log("Sidebar: ", this.state.sidebarOn)
    this.setState({sidebarOn: !this.state.sidebarOn})
  }

  render() {

    return (
      <div className="App">
        <Navbar toggleSideBar = {this.toggleSideBar.bind(this)}/>
        <Mainbody sidebarOn = {this.state.sidebarOn}/>

      </div>
    );
  }

}

export default App;
