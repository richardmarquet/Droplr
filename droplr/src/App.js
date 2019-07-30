import React from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './Components/Navbar/Navbar'
import Sidebar from './Components/Sidebar/Sidebar'
import Mainbody from './Containers/Mainbody/Mainbody'

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="info">
        <Sidebar className ="left" />
        <Mainbody className ="right" />
      </div>

    </div>
  );
}

export default App;
