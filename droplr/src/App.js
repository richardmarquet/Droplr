import React from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './Components/Navbar/Navbar'
import Sidebar from './Components/Sidebar/Sidebar'
 import Mainbody from './Containers/Mainbody/Mainbody'
import 'bootstrap/dist/css/bootstrap.css';



function App() {
  return (
    <div className="App">
          <Navbar />
    <div className ="info">
      <Sidebar />
      <Mainbody />
      </div>

    </div>
  );
}

export default App;
