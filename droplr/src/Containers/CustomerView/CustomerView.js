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
    items: [{img: 'https://i.ya-webdesign.com/images/png-with-transparent-background.png'},
  {img: 'https://i.ya-webdesign.com/images/png-with-transparent-background.png'},
  {img: 'https://i.ya-webdesign.com/images/png-with-transparent-background.png'},
  {img: 'https://i.ya-webdesign.com/images/png-with-transparent-background.png'},
  {img: 'https://cms.qz.com/wp-content/uploads/2016/05/amazonechodotfronton-e1463797661349.jpg?quality=75&strip=all&w=410&h=240.8018471872376'},
  {img: 'https://cms.qz.com/wp-content/uploads/2016/05/amazonechodotfronton-e1463797661349.jpg?quality=75&strip=all&w=410&h=240.8018471872376'},
  {img: 'https://cms.qz.com/wp-content/uploads/2016/05/amazonechodotfronton-e1463797661349.jpg?quality=75&strip=all&w=410&h=240.8018471872376'},
  {img: 'https://cms.qz.com/wp-content/uploads/2016/05/amazonechodotfronton-e1463797661349.jpg?quality=75&strip=all&w=410&h=240.8018471872376'},
  {img: 'https://cms.qz.com/wp-content/uploads/2016/05/amazonechodotfronton-e1463797661349.jpg?quality=75&strip=all&w=410&h=240.8018471872376'}]
}

  render() {
    return (
      <div>
      <Trending />
      <Container>
        <Row>
        {this.state.items.map((item, index )=> {
          return(
            <Col xs={6} md={4}>
              <DropItem image = {item.img} />
            </Col>)
        })}
        </Row>
      </Container>
    </div>)
  }
}


export default CustomerView;
