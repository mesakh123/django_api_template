import React from 'react'
import {Col,Container,Row} from 'react-bootstrap'


export default function Footer() {
  return (
    <footer>
        <Container>
            <Row>
                <Col className="py-3">
                    Copyright &copy; Real Estate {new Date().getFullYear()}
                </Col>
            </Row>
        </Container>
    </footer>
  )
}
