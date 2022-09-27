import React from "react";
import styled  from "styled-components";
import {Form,Button }from  "react-bootstrap";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { useState } from "react";

const UserDetailsForm = () => {
  const[userType,setUserType]=useState('Mentee')
    
    const formik = useFormik({
        initialValues: {
          gender:'',
          age:'',
          ethnicity:'',
          language:'',
          personality:'',
          faculty:'',
          grade:'',
          discplinary_actions:'',
          teaching_experience:'',
          mentoring_experience:'',
          time_availibility:'',
          accept_discplinary_actions:''
   
        },
        validationSchema: Yup.object({}),
            onSubmit: (values) =>
            {
                console.log(values)
            }
    });
   
  
  
 return(
    <Wrapper className="container">
      <div className="form-group" style={{padding:'20px',boxShadow:'10px 10px 18px  10px #888888'}}>
        <h3>Please Complete the form below:</h3>
      </div>
        <Form onSubmit={formik.handleSubmit}>
          <div className="form-group" style={{padding:'20px',boxShadow:'10px 10px 18px  10px #888888'}}>
          <Form.Group className="mb-3">
          <Form.Label>Gender</Form.Label>
          <Form.Select name="gender" type="name"
          className="form-control"
          onChange={formik.handleChange}
          value={formik.values.username}>
            
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
            <option>Dont want to specify</option>
          </Form.Select>
        </Form.Group>
      <Form.Group className="mb-3" >
        <Form.Label>Age</Form.Label>
        
        <Form.Control name="age" type="integer"
        className="form-group"
        onChange={formik.handleChange}
        value={formik.values.username} placeholder="Enter your age" />
    
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Ethinicity</Form.Label>
        <Form.Select name="ethnicity" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username}>
          <option>British</option>
          <option>Other</option>
        </Form.Select>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Laguage</Form.Label>
        <Form.Select name="language" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username}>
          <option>English</option>
          <option>Other</option>
        </Form.Select>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Personality</Form.Label>
        <Form.Select name="personality" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username}>
          <option>Extrovert</option>
          <option>Introvert</option>
        </Form.Select>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Faculty</Form.Label>
        <Form.Select name="faculty" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username}>
          <option>Science and Technology</option>
          <option>Other</option>
        </Form.Select>
      </Form.Group>
      {userType === "Mentee" ? (
        <>
      <Form.Group className="mb-3">
        <Form.Label>Previous Grades</Form.Label>
        <Form.Control name="grade" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username} placeholder="Enter Previous Grade" />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Discplinary Actions</Form.Label>
        <Form.Control name="discplinary_actions" type="name"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username} placeholder="Enter if you have any previous discplinary action" />
      </Form.Group>
      </>
           ) :(
            <>
      <Form.Group className="mb-3">
        <Form.Label>Teaching Experience</Form.Label>
        <Form.Control name="teaching_experience" type="integer"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username} placeholder="Enter years of teaching experience" />
      </Form.Group>
      <Form.Group className="mb-3">
        
        <Form.Label>Mentoring Experience</Form.Label>
        <Form.Control name="mentoring_experience" type="integer"
        className="form-control"
        onChange={formik.handleChange}
        value={formik.values.username} placeholder="Enter years of mentoring experience" />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Time Availibility Per week</Form.Label>
        <Form.Select name="time_availibility" type="name"
        className="form-control"
        onChange={formik.handleChange}>

        <option>1-5</option>
        <option>5-10</option>
        
        </Form.Select>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Do you consider studnet having past displinary actions</Form.Label>
        <Form.Select name="accept_discplinary_actions" type="name"
        className="form-control"
        onChange={formik.handleChange}>
            <option>Yes</option>
            <option>No</option>
        </Form.Select>
     </Form.Group>
     </>
    )}
     <Button 
      className="btn btn-color px-5 mb-5 w-100"
        style={{ marginTop: 30,BackgroundColor:'#0e1c36',color: '#fff' }}
        variant="primary"
        size="sm"
        block
        type="submit">
        Submit
      </Button>
      </div>
      </Form>
    </Wrapper>

 )
}
export default UserDetailsForm

const Wrapper= styled.section`
    color: #000;
`