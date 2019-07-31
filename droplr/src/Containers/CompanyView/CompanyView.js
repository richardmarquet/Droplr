import React, { Component } from 'react';
import DropItem from '../../Components/DropItem/DropItem';
import Trending from '../../Components/Trending/Trending'
import Image from 'react-bootstrap/Image'
import Navbar from 'react-bootstrap/Navbar'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container'




class CompanyView extends Component {
  state = {
    items: this.props.items_catalog
  }

  componentWillReceiveProps(nextProps) {
    // You don't have to do this check first, but it can help prevent an unneeded render
    if (nextProps.items_catalog !== this.state.items) {
      this.setState({ items: nextProps.items_catalog});
    }

  }

  render() {
    console.log("this.state.items", this.state.items)
    return (
      <div>
      <Trending />
      <Trending />
      <Trending />
    </div>)
  }
}



export default CompanyView;
