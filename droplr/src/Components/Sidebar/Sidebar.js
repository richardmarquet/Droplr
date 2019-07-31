import React from 'react';
import './Sidebar.css'
import Droplist from '../Droplist/Droplist'
import Button from 'react-bootstrap/Button'



const sidebar = (props) => {
  return(
  <div className="sidebarContainer">
    <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" className="profilePicture"/>
    <div style={{height: '10%', width: '40%'}}>&nbsp;</div>
    {(!props.userAdmin) ? <Droplist />:  <h3 className="white">Company: JBL </h3>}


  </div>)
}

export default sidebar;
