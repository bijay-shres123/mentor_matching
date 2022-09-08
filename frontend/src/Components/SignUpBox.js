
import React, { useState } from "react";
import styled from 'styled-components'


import { Button, Form} from "react-bootstrap"
import * as Yup from 'yup';
import { useFormik } from 'formik';
import { PostData } from "../Services/PostData";

const SignUpBox = () => {
    const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [passwordError, setpasswordError] = useState("");
  const [emailError, setemailError] = useState("");
  const [Success, setSuccess] = useState(false);
  const formik = useFormik({
    initialValues: {
      name: '',
      email: '',
      password: '',
      user_type:'',
    },
    validationSchema: Yup.object({
      name: Yup.string()
        .required('Please provide a user name!')
        .min(2, 'Seems a bit short...')
        .max(
          23,
          'A username is your identity.Keep it short .Less than 10 letters'
        ),
      
      email: Yup.string().label('Email').email().required(),
      password: Yup.string()
        .label('Password')
        .required('Required!')
        .min(7, 'Seems a bit short...'),
 
      password2: Yup.string()
        .required('Required!')
        .test('passwords-match', 'Passwords must match !', function (value) {
          return this.parent.password === value;
         
        }),
    }),
    onSubmit: (values) => {
      if (
        values.name &&
        values.email &&
        values.password
      ) { 
        PostData(values).then((result) => {
          let responseJSON:any = result;
          console.log(responseJSON);
          if (responseJSON.status===200|| responseJSON.status===201) {
            console.log('User Created');
            setSuccess(true)
             }
              else{
                alert('Error')
              }
        }
        );
      }
    
    }})

    return (

      <Wrapper>
          <div className="row" style={{boxShadow:' -1px 1px 6px 10px #c8d3d7', }}>
            <div className="col-sm" style={{backgroundImage: 'url(/assets/images/signup.jpeg)', backgroundSize:'cover',textAlign:'center',boxShadow:'inset 0 0 0 2000px rgb(0 0 0 / 10%)'}}> 
                <h1 style={{color:'#fff',padding:'3% 0%'}}>Signup</h1>
            </div>
    
    <div className="col-sm">
    <Form onSubmit={formik.handleSubmit} className="card-body cardbody-color ">
    <div className="text-center" >
              
            </div>
            <Form.Group>
        <Form.Label>Name</Form.Label>
        <Form.Control
          id="name"
         name="name"
         onChange={formik.handleChange}
         value={formik.values.name}
        placeholder="name"
        />
      </Form.Group>
      <Form.Group>
        <Form.Label>Email Address</Form.Label>
        <Form.Control
        id="email"
         name="email"
          type="email"
          onChange={formik.handleChange}
          value={formik.values.email}
          placeholder="email"
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
      <Form.Group controlId="formBasicPassword">
        <Form.Label>Confirm Password</Form.Label>
        <Form.Control
        id="password2"
         name="password2"
          type="password"
          onChange={formik.handleChange}
          value={formik.values.password2}
          placeholder="confirm password"
        />
      </Form.Group>
      <Form.Group>
      <Form.Label>Select User Type :</Form.Label><br></br>
      <div id="my-radio-group">User Type:</div>
          <div role="group" aria-labelledby="my-radio-group">
            <label style={{marginRight:'20px'}}>
              <input type="radio" name="user_type"   id="mentor" onChange={formik.handleChange}
              value="COACH"/>
              Mentor  
            </label>
            <label>
              <input type="radio" name="user_type"  id="mentee" onChange={formik.handleChange}
              value="STUDENT" />
              Mentee
            </label>
           
          </div>
      
      </Form.Group>
 
      <br></br>
      <div className="form-check d-flex justify-content-center mb-5">
                    
                    <label className="form-check-label" for="form2Example3">
                      I agree all statements in <a href="#!">Terms of service</a>
                    </label>
                  </div>
      <Button 
      className="btn btn-color px-5 mb-5 w-100"
        style={{ marginTop: 30,BackgroundColor:'#0e1c36',
            color: '#fff' }}
        variant="primary"
        size="sm"
        block
       
        type="submit"
        
      >
        Sign Up
      </Button>
      <div id="emailHelp" className="form-text text-center mb-5 text-dark">Already Registered? <a href="/login" className="text-dark fw-bold"> Sign In</a>
                </div>
    </Form>
    </div>
   </div>
    </Wrapper>);
    
  };
    
  export default SignUpBox;

  const Wrapper = styled.section`
  margin-top:-25px;
padding: 4em;
min-height:700px;

background-size:cover;
background-blend-mode: multiply;

color:#000;
`;
const Box = styled.section`
border-radius: 25px;
  padding: 4em;
  color:#000;
  background:#f0f0f0;
`;
