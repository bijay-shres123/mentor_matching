
import React, { useState } from "react"
import styled from 'styled-components'
import {LoginPostData} from '../Services/LoginPostData'
import { useFormik } from 'formik';
import { Button, Form, Alert } from "react-bootstrap"
import * as Yup from 'yup';
import { Navigate } from 'react-router-dom';

const LoginBox = () => {
  const [ErrorLogin, setErrorLogin] = useState('');
  const [SuccessLogin, setSuccessLogin] = useState('');

  // Class with functionality to send/submit a form
  const formik = useFormik({
     initialValues: {
       email_or_username: '',
       password:'',

     },
     validationSchema: Yup.object({
      email_or_username: Yup.string().label('Email').email().required(),
      password: Yup.string()
        .label('Password')
        .required('Required!')
        .min(7, 'Seems a bit short...'),
    }),
     onSubmit: (values) => {
      if (values.email_or_username && values.password) {
        LoginPostData(values).then((result) => {
          let responseJSON:any= result;
          console.log(responseJSON);

          if (responseJSON.status===200) {
            localStorage.setItem('token', responseJSON.data.token);
            setSuccessLogin('True');
          } else {
            alert('Login Error')
            console.log(LoginPostData.Data)
            setErrorLogin(responseJSON.data.non_field_errors[0]);
            
            setTimeout(() => {
              setErrorLogin("")
            }, 10000); 
          }
        });
      }
    },
  });

  //  if (localStorage.getItem('token')) {
  //   return <Navigate to={'/'} />;
  // }
  if (SuccessLogin === 'True') {
     alert('Logged IN')
    
     return < Navigate to={'/'} /> 
  } 
  
  return (

        <Wrapper>
        <div className="jumbotron" style={{background:'none'}}>
          <div className="container text-center text-lg-left">
          <div className="row d-flex justify-content-center">
          <div className="col-md-5">
            <Box>
            <Form onSubmit={formik.handleSubmit} className="card-body cardbody-color " style={{boxShadow:' -1px 1px 6px 10px #c8d3d7'}}>
        <div className="text-center">
          <img src="assets/images/user.png" className="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"
            width="160px" alt="profile"/>
        </div>

        {/* <!-- Form to Login --> */}  
        <Form.Group>
          <Form.Label>Email Address</Form.Label>
          <Form.Control
          id="email_or_username"
          name="email_or_username"
            type="email"
            onChange={formik.handleChange}
          value={formik.values.email_or_username}
            placeholder="email_or_username"
          />
        </Form.Group>
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
          id="password"
          name="password"
            type="password"
            onChange={formik.handleChange}
          value={formik.values.password}
            placeholder="password"
          />
        </Form.Group>
          
        {/* <!-- Links to Forgot Password / Create Accout --> */}  
        <Button 
        className="btn btn-color px-5 mb-5 w-100"
          style={{ marginTop: 30,BackgroundColor:'#40798C',
              color: '#fff' }}
          variant="primary"
          size="sm"
          block
        
          type="submit"
        >
          Login
        </Button>
        <div id="forgotPassword" className="form-text text-center mb-3 text-dark">
          Forgot Password?
          <a href="/forgot-password" class="text-dark fw-bold">
            {" "}
            Reset Password
          </a>
        </div>
        <div id="emailHelp" className="form-text text-center mb-3 text-dark">
          Not Registered? 
          <a href="/signup" class="text-dark fw-bold"> 
          {" "}
          Create an Account</a>
        </div>
      </Form>
            </Box>
          </div>
         
        </div>
          </div>
        </div>
      </Wrapper>);
    
  };
    
  export default LoginBox;

  const Wrapper = styled.section`
  margin-top:-25px;
padding: 4em;
min-height:700px;
background-image: url(/assets/Images/background.jpg);
background-size:cover;
background-blend-mode: multiply;
box-shadow: inset 0 0 0 2000px rgb(0 0 0 / 50%);
color:#fff;
`;
const Box = styled.section`


  color:#000;
  background:#f0f0f0;
`;
