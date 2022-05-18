import React from 'react'
import {Col,Container,Row} from 'react-bootstrap';
import {FaHeartBroken,FaSadTear} from 'react-icons/fa'


export default function NotFound() {
  return (
      <Container>
          <Row>
              <Col className="text-center">
                  <h1 className='notfound'>404 Not found</h1>
                  <FaHeartBroken className="broken-heart"/>
                  <FaSadTear className='sad-tear'/>
              </Col>
          </Row>
      </Container>
  )
}
