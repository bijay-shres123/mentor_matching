
import styled from 'styled-components'
import Card from "react-bootstrap/Card";

const UserProfileBox = () => {
    return (
        <Wrapper>
        <div className="jumbotron" style={{background:'none'}}>
          <div className="container text-center text-lg-left">
            <div className="row justify-content-between">
                <div className='col-md-3'>
                    <div>
                    <Card style={{ width: '18rem' ,color:"#000" }}>
                    <Card.Img variant="top" src="assets/images/mentor.jpeg" className="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"/>
                    <Card.Body>
                        <Card.Title>Mr Mentee</Card.Title>
                        <Card.Text> 
                        <table class="table">
                        
                        <tbody>
                            <tr>
                            <td>Course:</td>
                            <td>Bachelors of Computer Science</td>
                            
                            </tr>
                            <tr>
                            <td>Year:</td>
                            <td>First</td>
                            
                            </tr>
                            </tbody>
                            </table>
                        </Card.Text>
                    </Card.Body>
                    </Card>
                    </div>
                </div>
                <div className='col-md-8'>
                <div>
                    <Card style={{ color:"#000" }}>
                    
                    <Card.Body>
                    <Card.Title style={{textAlign:"center"}}>User Details</Card.Title>
                        <Card.Text> 
                        <table class="table">
                        
                        <tbody>
                            <tr>
                            <td>Full Name:</td>
                            <td>XYZ Mentee</td>
                            
                            </tr>
                            <tr>
                            <td>Phone:</td>
                            <td>0938434324</td>
                            
                            </tr>
                            
                            <tr>
                            <td>Email:</td>
                            <td>abc@brookes.ac.uk</td>
                            
                            </tr>
                            <tr>
                            <td>Address:</td>
                            <td>0x32, Oxford</td>
                            
                            </tr>
                            </tbody>
                            </table>
                        </Card.Text>
                    </Card.Body>
                    </Card>
                    </div>
                    <div style={{marginTop:"20px"}}>
                    <Card style={{ color:"#000" }}>
                    
                    <Card.Body>
                    <Card.Title style={{textAlign:"center"}}>Allocated Mentor</Card.Title>
                        <Card.Text> 
                        <table class="table">
                        
                        <tbody>
                            <tr>
                            <td>Full Name:</td>
                            <td>XYZ Mentor</td>
                            
                            </tr>
                            <tr>
                            <td>Email:</td>
                            <td>mentor@brookesbuddy.com</td>
                            
                            </tr>
                            
                            
                            </tbody>
                            </table>
                        </Card.Text>
                    </Card.Body>
                    </Card>
                    </div>

                </div>
                </div>
                
              
            </div>
          </div>
        
      </Wrapper>)
  };
    
  export default UserProfileBox;
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
