import React from 'react';
// import { Navbar } from 'bootstrap'
import Navbar from 'react-bootstrap/Navbar'

// import { Nav } from 'bootstrap'
// import { NavDropdown } from 'bootstrap'


const NavbarMod = (props) => {
  return (
    <div>
    <Navbar bg="light">
    <Navbar.Brand href="#home">Brand link</Navbar.Brand>
  </Navbar>
  <br />
  <Navbar bg="light">
    <Navbar.Brand>Brand text</Navbar.Brand>
  </Navbar>
  <br />
  <Navbar bg="dark">
    <Navbar.Brand href="#home">
      <img
        src="/logo.svg"
        width="30"
        height="30"
        className="d-inline-block align-top"
        alt="React Bootstrap logo"
      />
    </Navbar.Brand>
  </Navbar>
  <br />
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="#home">
      <img
        alt=""
        src="/logo.svg"
        width="30"
        height="30"
        className="d-inline-block align-top"
      />
      {' React Bootstrap'}
    </Navbar.Brand>
  </Navbar>
</div>)
}

export default NavbarMod;
