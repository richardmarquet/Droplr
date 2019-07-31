import React, { Component } from 'react';
import CustomerView from '../CustomerView/CustomerView'
import axios from 'axios'
import Sidebar from '../../Components/Sidebar/Sidebar'
import Suggested from '../../Components/Suggested/Suggested'
import Trending from '../../Components/Trending/Trending'



class Mainbody extends Component {
  state = {
    items_catalog: [],
    sidebarOn: true

  }

  //return json
  getAllItemsFromFirebase() {
    axios.get('http://127.0.0.1:5000/getAllItems').then((body) => {
     let items = body.data;
     console.log("axios: ", items)

     let new_items_catalog = []

     for (let key in items) {
        if (items.hasOwnProperty(key)) {
            new_items_catalog.push(items[key]);
        }
    }
    this.setState({items_catalog: new_items_catalog})

     return body.data;
    }).catch(err => console.log('axios Error: ', err));
  }

  componentDidMount() {
    this.getAllItemsFromFirebase();

   }

   componentWillReceiveProps(nextProps) {
     // You don't have to do this check first, but it can help prevent an unneeded render
     if (nextProps.sidebarOn !== this.state.sidebarOn) {
       this.setState({ sidebarOn: nextProps.sidebarOn});
     }

   }



  render() {
    return(
    <div className ="info">
      {(this.state.sidebarOn) ? (
        <Sidebar />
      ) : console.log("sidebar off")}


        <div className= "infoCol">
          <Trending />
          <div className ="info">
            <CustomerView items_catalog = {this.state.items_catalog} />
            {(!this.state.sidebarOn) ? <Suggested suggested_items = {this.state.items_catalog} /> : console.log("sidebar on")}
              </div>
        </div>
      </div>)

  }


}


export default Mainbody;
