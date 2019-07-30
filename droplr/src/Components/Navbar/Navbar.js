import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'
import ncr_logo from '../../assets/imgs/ncr_logo.png'
import './Navbar.css'



const NavbarMod = (props) => {
  return (
    <Navbar bg="dark" variant="dark">
      <Navbar.Brand href="#home">
        <img src={ncr_logo} className="logo" />
        <span className="header" >Droplr</span>
      </Navbar.Brand>
    </Navbar>)
}

export default NavbarMod;