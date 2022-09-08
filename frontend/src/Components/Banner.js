/**
******************************************************************************************
* The following function creates a banner for a home page. It consists of a background 
* image, well-designed text at the center and an example of training session.
* Designed to be used at Home page.
******************************************************************************************
*/


import styled from 'styled-components'
import Card from "react-bootstrap/Card";

export default function Banner(){
  return(
  <Wrapper>
    <div className="jumbotron" style={{background:'none'}}>
      <div className="container text-center text-lg-left">
        <div className="row">
          <div className="col-lg-8">
            <h1 className="display-4">The Best Platform
            for Mentoring</h1>
            <p className="lead">
            It has survived not only five centuries, but also the leap into electronic typesetting,  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets.
            </p>

            {/* <!-- Button "Try it" under the text --> */}
            <span className="text-center d-inline-block">
              <a className="btn  btn-lg w-100" href="/trainingsession" role="button" style={{border:'1px solid #fff',background:'#08425a',color:'#fff'}}>Start Today</a>
              {/* <p className="text-muted">No credit card required</p> */}
            </span>
          </div>
          <div className="col-lg-4 align-items-center d-flex">
            <Card style={{ width: '18rem' ,color:"#000" }}>
              <Card.Img variant="top" src="assets/images/mentor.jpeg" />
              <Card.Body>
                <Card.Title>MENTOR XYZ</Card.Title>
                <Card.Text> 
                Hey there, I am mentor XYZ. I am here to guide you through your university journey.
                </Card.Text>
              </Card.Body>
            </Card>
          </div>
        </div>
      </div>
    </div>
  </Wrapper>)
}

// Definition of auxilliary objects

// Container of the main content which has background image
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

