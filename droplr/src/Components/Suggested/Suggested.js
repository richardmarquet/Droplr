import React, { Component } from 'react';
import './Suggested.css'
import SuggestedItem from '../SuggestedItem/SuggestedItem'


class suggested extends Component {
  state = {
    suggested_items: this.props.suggested_items
  }

  componentWillReceiveProps(nextProps) {
    // You don't have to do this check first, but it can help prevent an unneeded render
    if (nextProps.suggested_items !== this.state.suggested_items) {
      this.setState({ suggested_items: nextProps.suggested_items});
    }
    console.log("suggested_items", this.state.suggested_items.length)

  }


    render(){
      console.log("suggested_items", this.state.suggested_items.length)
      return (
      <div className="suggestedContainer">
        {this.state.suggested_items.map((item, index) => {
          return (<SuggestedItem image = {item.picture} per_sold = {100 - (Math.floor((item.reqSold - item.totalSold) * 100/ item.reqSold))} item_name = {item.name} item_prevCost = {item.prevCost} item_cost = {item.cost}  item_reqSold= {item.reqSold}  />)
        })}
      </div>)
  }
}

export default suggested;
