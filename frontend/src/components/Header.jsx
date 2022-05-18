import React from 'react'
import { Container,Nav,Navbar,NavDropdown } from 'react-bootstrap'
import {GiHouse} from 'react-icons/gi'
import {LinkContainer} from 'react-router-bootstrap'
import { FaSignInAlt, FaSignOutAlt } from "react-icons/fa"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate } from "react-router-dom"
import { logout, reset } from "../features/auth/authSlice";



export const Header = () => {

    const navigate = useNavigate();
	const dispatch = useDispatch();

	const { user } = useSelector((state) => state.auth);

	const logoutHandler = () => {
		dispatch(logout());
		dispatch(reset());
		navigate("/");
	};

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

                    { user ? (
                         <NavDropdown title={user.first_name ? user.first_name: "welcome"} id="username">
                             <LinkContainer to="/profile">
                                <NavDropdown.Item >Profile</NavDropdown.Item>
                             </LinkContainer>
                            <NavDropdown.Divider />
                            <NavDropdown.Item onClick={logoutHandler}>Logout</NavDropdown.Item>
                        </NavDropdown>
                    ): (
                        <LinkContainer to="/login">
                            <Nav.Link>
                                <FaSignInAlt/>Login
                            </Nav.Link>
                        </LinkContainer>
                    )}
                </Nav>
            </Navbar.Collapse>
        </Container>
        </Navbar>
    </header>

  )
}
