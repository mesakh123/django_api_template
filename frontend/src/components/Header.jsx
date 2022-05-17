import React from 'react'
import { Container,Nav,Navbar,NavDropdown } from 'react-bootstrap'
import {GiHouse} from 'react-icons/gi'
import {LinkContainer} from 'react-router-bootstrap'


export const Header = () => {
  return (
    <header>
        <Navbar fixed="top" bg="dark" expand="lg" variant="dark" collapseOnSelect>
        <Container>

            <LinkContainer to="/">
                <Navbar.Brand>
                    <GiHouse className='nav-icon'/>Real estate
                </Navbar.Brand>
            </LinkContainer>

            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
                <Nav className="ml-auto">
                    <LinkContainer to="/">
                        <Nav.Link >Home</Nav.Link>
                    </LinkContainer>

                    <LinkContainer to="/properties">
                        <Nav.Link >Properties</Nav.Link>
                    </LinkContainer>

                    <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Container>
        </Navbar>
    </header>

  )
}
