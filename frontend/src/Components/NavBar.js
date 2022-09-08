import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useEffect, useState } from 'react';
import 'font-awesome/css/font-awesome.min.css';



function ColorSchemesExample() {

  const [userLoginInfo, setuserLoginInfo] = useState(false);


  useEffect(() => {
    if (localStorage.getItem('token')) {
      setuserLoginInfo(true);
    }
  }, []);


  return (
    <>
      <Navbar collapseOnSelect expand="lg" style={{background:"#40798C"}} variant="dark">
        <Container>
          <Navbar.Brand href="#home">BrokesBuddy</Navbar.Brand>
          {userLoginInfo === false ? (
            <Nav className='navbar-nav ml-auto'>
            <Nav.Link href="/login" style={{color:'#fff'}}>

            <i className="fa fa-user" style={{padding: '0px 2px'}} />
             Login
            </Nav.Link> 
            <Nav.Link href="/signup" style={{color:'#fff'}}>
              Sign Up
            </Nav.Link>
            </Nav>
          ): (
            <Nav className='navbar-nav ml-auto'>
              <Nav.Link to="/my-profile" className="sign-in">
                My Profile
              </Nav.Link>
              <Nav.Link
                to="/"
                className="sign-in"
                onClick={() => {
                  setuserLoginInfo(false);
                  console.log('clicked');
                  localStorage.clear();
                }}
              >
                LOGOUT
              </Nav.Link>
            </Nav>
          )}
        </Container>
      </Navbar>
      <br />
      
    </>
  );
}

export default ColorSchemesExample;