import React from 'react';
import './Trending.css'
import Carousel from 'react-bootstrap/Carousel'
import DropItem from '../../Components/DropItem/DropItem';
import TrendingItem from '../../Components/TrendingItem/TrendingItem';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Jumbotron from 'react-bootstrap/Jumbotron'



const trending = (props) => {
  return(
  <div className="carouselContainer">
  <Carousel>
  <Carousel.Item>
    <Jumbotron fluid id="jumbo">
        <Container>
          <Row>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"http://www.pngmart.com/files/1/Black-Shoe-Transparent-Background.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://www.pngarts.com/files/3/Gym-Shoes-Transparent-Background-PNG.png"} />
            </Col>
          </Row>
        </Container>
        </ Jumbotron>
    </Carousel.Item>
    <Carousel.Item>
      <Jumbotron fluid id="jumbo">
          <Container>
          <Row>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://i.pinimg.com/originals/7c/38/83/7c38834c1c5c1aefadcd57524fc672e7.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
            </Col>
            <Col xs={6} md={3}>
              <TrendingItem image = {"https://cdn.pixabay.com/photo/2015/09/16/11/27/mans-hat-942573_960_720.png"} />
            </Col>
          </Row>
          </Container>
          </ Jumbotron>
      </Carousel.Item>
      <Carousel.Item>
        <Jumbotron fluid id="jumbo">
            <Container>
            <Row>
              <Col xs={6} md={3}>
                <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
              </Col>
              <Col xs={6} md={3}>
                <TrendingItem image = {"https://i.pinimg.com/originals/7c/38/83/7c38834c1c5c1aefadcd57524fc672e7.png"} />
              </Col>
              <Col xs={6} md={3}>
                <TrendingItem image = {"https://www.stickpng.com/assets/images/580b57fbd9996e24bc43bf0c.png"} />
              </Col>
              <Col xs={6} md={3}>
                <TrendingItem image = {"https://cdn.pixabay.com/photo/2015/09/16/11/27/mans-hat-942573_960_720.png"} />
              </Col>
            </Row>
            </Container>
            </ Jumbotron>
        </Carousel.Item>

</Carousel>
  </div>)
}

export default trending;
