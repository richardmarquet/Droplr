import React from 'react';
import './DropItem.css'
// import { ProgressBar } from 'bootstrap'

import ProgressBar from 'react-bootstrap/ProgressBar';



const dropItem = (props) => {
  const now = 60;

  return(
  <div className="dropItemContainer">
    <img src={ props.image } className="itemPicture"/>
    <p><b>Amazon Echo</b></p>
    <ProgressBar striped variant="info" now={now} label={`${now}%`} />
    <span className="strikedPrice">$450    </span><span>   $300</span>
  </div>)
}

export default dropItem;
