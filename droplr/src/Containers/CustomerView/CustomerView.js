import React, { Component } from 'react';
import DropItem from '../../Components/DropItem/DropItem';
import Trending from '../../Components/Trending/Trending'
// import { Image } from 'react-bootstrap'
// import { Col } from 'react-bootstrap'
// import { Row } from 'react-bootstrap'
// import { Table } from 'react-bootstrap'
// import { Container } from 'bootstrap'


import Image from 'react-bootstrap/Image'
import Navbar from 'react-bootstrap/Navbar'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container'








class CustomerView extends Component {
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
      <Container>
        <Row>
        {this.state.items.map((item, index )=> {
          console.log(item)
          return(
            <Col xs={6} md={4}>
              <DropItem image = {"https://i.ebayimg.com/images/g/UvQAAOSwB1Jasui-/s-l225.jpg"} item_name = {item.name} item_prevCost = {item.prevCost} item_reqSold= {item.reqSold}   />
            </Col>)
        })}
        </Row>
      </Container>
    </div>)
  }
}



export default CustomerView;
