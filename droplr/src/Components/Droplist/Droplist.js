import React from 'react';
import './Droplist.css';


const droplist = (props) => {
return (<div className ="droplistContainer">
  <h5 className="droplistHeader">Drop List:</h5>
  <div className ="droplistSubContainer">
    <p className="items">Shoes</p>
    <p className="items">TV</p>
    <p className="items">Clothes</p>
    <p className="items">Hat</p>
  </div>
</div>)



}

export default droplist;
