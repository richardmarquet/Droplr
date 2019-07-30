import React from 'react';
import './Sidebar.css'
import Droplist from '../Droplist/Droplist'


const sidebar = (props) => {
  return(
  <div className="sidebarContainer">
    <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" className="profilePicture"/>

    <Droplist />
  </div>)
}

export default sidebar;
