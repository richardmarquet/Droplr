import React from 'react';
import './TrendingItem.css'
import { ProgressBar } from 'bootstrap'



const trendingItem = (props) => {
  const now = 60;

  return(
  <div className="trendingItemContainer">
    <img src={ props.image } className="itemPicture"/>
    <p><b>Amazon Echo</b></p>
    <ProgressBar striped variant="info" now={now} label={`${now}%`} />
    <span className="strikedPrice">$450    </span><span>   $300</span>
  </div>)
}

export default trendingItem;
