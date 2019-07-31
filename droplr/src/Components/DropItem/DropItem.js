import React from 'react';
import './DropItem.css'
// import { ProgressBar } from 'bootstrap'

import ProgressBar from 'react-bootstrap/ProgressBar';



const dropItem = (props) => {
  const now = 60;

  return(
  <div className="dropItemContainer">
    <img src={ props.image } className="itemPicture"/>
    <p><b>{ props.item_name }</b></p>
    <ProgressBar striped variant="info" now={now} label={`${now}%`} />
    <span className="strikedPrice">{ props.item_prevCost }    </span><span>   $300</span>
  </div>)
}

export default dropItem;
