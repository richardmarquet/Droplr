import React from 'react';
import './Suggested.css'
import SuggestedItem from '../SuggestedItem/SuggestedItem'


const suggested = (props) => {
  return (
  <div className="suggestedContainer">
    {props.suggested_items.map((item, index) => {
      return (<SuggestedItem image = {"https://www.pngarts.com/files/3/Gym-Shoes-Transparent-Background-PNG.png"} />)
    })}
  </div>)
}

export default suggested;
