import React, { Component } from 'react';
import CustomerView from '../CustomerView/CustomerView'
import CompanyView from '../CompanyView/CompanyView'

import axios from 'axios'
import Sidebar from '../../Components/Sidebar/Sidebar'
import Suggested from '../../Components/Suggested/Suggested'
import Trending from '../../Components/Trending/Trending'



class Mainbody extends Component {
  state = {
    items_catalog: [],
    suggested_items: [],
    sidebarOn: true,
    userAdmin: false

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

  //return json
  getSuggestedItemsFromFirebase() {
    axios.get('http://127.0.0.1:5000/getSuggestedItems').then((body) => {
     let closest = body.data['closest_items'];
     let new_suggested_items = []

     for (let i = 0; i <this.state.items_catalog.length; i++) {
        for (let j = 0; j < closest.length; j++) {
            if (this.state.items_catalog[i].name == closest[j]) {
              console.log("FOUNDD", this.state.items_catalog[i].name)
              new_suggested_items.push(this.state.items_catalog[i]);
            }
       }
    }

    this.setState({suggested_items: new_suggested_items})
    console.log("FINALL:", this.state.suggested_items.length)
     return body.data;
    }).catch(err => console.log('axios Error: ', err));


  }

  componentDidMount() {
    this.getAllItemsFromFirebase();
    this.getSuggestedItemsFromFirebase();

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
        {(!this.state.userAdmin) ? <Trending/> : console.log("okay")}
          <div className ="info">
          {(this.state.userAdmin) ? <CompanyView /> : <CustomerView items_catalog = {this.state.items_catalog}  />}
            {(!this.state.sidebarOn && !this.state.userAdmin) ? <Suggested suggested_items = { this.state.suggested_items } /> : console.log("sidebar on")}
            </div>
        </div>
      </div>)

  }


}


export default Mainbody;
